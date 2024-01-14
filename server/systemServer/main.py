import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
import numpy as np
import pickle
from datetime import datetime

load_dotenv()

app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

CREATE_ADMIN = (
    "CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);"
)

INSERT_ADMIN = ("INSERT INTO users (username, password) VALUES ('admin', 'admin123');")

SELECT_USER = ("SELECT id, username FROM users WHERE username = %s AND password = %s;")

INSERT_CASE = ("INSERT INTO cases (status,customer_id,transaction_id) VALUES ('open', %s, %s);")

CLOSE_CASE = ("UPDATE cases SET status = 'close' WHERE case_id = %s;")

SELECT_ACC = ("SELECT * FROM system_account WHERE customer_id = %s;")

INSERT_ACC = ("INSERT INTO system_account (customer_id,first_name,last_name,account_balance,age,address,mobileno,addharno,lastlogin,branchid,account_type,emailid,upi_id,account_number,pancard_number,city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")

FREQUENCY_INDICATOR_QUERY = """SELECT COUNT(*) FROM system_transaction WHERE receiver_account = %s;"""

INSERT_TRANSACTION = """
    INSERT INTO system_transaction (transactiontype, oldbalanceorg,newbalanceorig, oldbalancedest, newbalancedest, transaction_date,sender_account,receiver_account,ip_address_sender,fraud_transaction,amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)
    RETURNING transactionid;
"""

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Admin Apis

@app.post('/api/admin/createAdmin')
def createAdmin():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ADMIN)
            cursor.execute(INSERT_ADMIN)
    return("Admin created"), 201

@app.post('/api/admin/login')
def adminLogin():
    data = request.get_json()
    username = data['username']
    password = data['password']

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_USER, (username, password))
                user_data = cursor.fetchone()

        if user_data:
            user_id, user_username = user_data
            return {"id": user_id, "username": user_username, "message": "Login successful."}, 200
        else:
            return {"error": "Invalid username or password."}, 401

    except Exception as e:
        return {"error": str(e)}, 500

#calculating diff function
def balance_diff(data):
    #Sender's balance
    orig_change=data['newbalanceorig']-data['oldbalanceorg']
    # orig_change=orig_change.astype(int)
    data['orig_txn_diff']=round(data['amount']+orig_change,2)
    data['orig_txn_diff']=round(data['amount']-orig_change,2)
    # data['orig_txn_diff']=data['orig_txn_diff'].astype(int)
    data['orig_diff'] = 1 if data['orig_txn_diff'] !=0 else 0
    
    #Receiver's balance
    dest_change=data['newbalancedest']-data['oldbalancedest']
    # dest_change=dest_change.astype(int)
    data['dest_txn_diff']=round(data['amount']+dest_change,2)
    data['dest_txn_diff']=round(data['amount']-dest_change,2)
    # data['dest_txn_diff']=data['dest_txn_diff'].astype(int)
    data['dest_diff'] = 1 if data['dest_txn_diff'] !=0 else 0

    # data = data.pop("orig_txn_diff")
    del data["orig_txn_diff"]
    del data["dest_txn_diff"]
    
    return(data)

#Surge indicator
def surge_indicator(data):
    data['surge']=1 if data['amount']>450000 else 0 
    return(data)

#Save transaction to system database
@app.route('/api/insertSystemTransactions', methods=['POST'])
def saveTransaction():
    data = request.get_json()
    data["transaction_date"] = datetime.now().date()

    transaction_fraud_detection = pickle.load(open('transaction_fraud_detection.pkl','rb'))
    # [step, amount,	oldbalanceOrg,	newbalanceOrig,	oldbalanceDest,	newbalanceDest,	orig_diff,	dest_diff,	surge,	freq_dest,	type__CASH_IN,	type__CASH_OUT,	type__DEBIT,	type__PAYMENT,	type__TRANSFER,	customers_org,	customers_des]
    model_data = [1]
    model_data.append(data['amount'])
    model_data.append(data['oldbalanceorg'])
    model_data.append(data['newbalanceorig'])
    model_data.append(data['oldbalancedest'])
    model_data.append(data['newbalancedest'])
    M_data = balance_diff(data)
    model_data.append(M_data['orig_diff'])
    model_data.append(M_data['dest_diff'])
    M_data = surge_indicator(M_data)
    model_data.append(M_data['surge'])
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(FREQUENCY_INDICATOR_QUERY,(data['receiver_account'],))
                f_count = cursor.fetchone()[0]
                model_data.append(f_count)
                if(data['tansactiontype']=="Cash In"):
                    model_data.append(1)
                else:
                    model_data.append(0)
                if(data['tansactiontype']=="Cash Out"):
                    model_data.append(1)
                else:
                    model_data.append(0)
                if(data['tansactiontype']=="Debit"):
                    model_data.append(1)
                else:
                    model_data.append(0)
                if(data['tansactiontype']=="Payment"):
                    model_data.append(1)
                else:
                    model_data.append(0)
                if(data['tansactiontype']=="Transfer"):
                    model_data.append(1)
                else:
                    model_data.append(0)
                model_data.append(int(data["sender_account"]))
                model_data.append(int(data["receiver_account"]))
                array_data_2d = np.array(model_data).reshape(1, -1)
                prediction = transaction_fraud_detection.predict_proba(array_data_2d)
                output = '{0:.{1}f}'.format(prediction[0][1],2)
                print("output:",output)
                if float(output) >= 0.5:
                    data['fraud_transaction'] = True
                else:
                    data['fraud_transaction'] = False
                
                values = (data['tansactiontype'],data['oldbalanceorg'], data['newbalanceorig'],data['oldbalancedest'],data['newbalancedest'], data['transaction_date'], data['sender_account'], data['receiver_account'], data['ip_address_sender'],data['fraud_transaction'],data['amount'])

                cursor.execute(INSERT_TRANSACTION,values)
                trans_id = cursor.fetchone()[0]
                print("trans_id = ",trans_id)

                if float(output) <= 0.5:
                    #Database notification
                    cursor.execute("""SELECT * FROM system_account WHERE account_number = %s;""",(data['sender_account'],))
                    Customer_id = cursor.fetchone()[0]
                    message = "Fraud Transaction Detected!"
                    noti_values = (message, 'Fraud_Transaction', trans_id, Customer_id)
                    print(noti_values)
                    cursor.execute("""INSERT INTO notifications (Message, Type, Transaction_id , Customer_id ) VALUES (%s, %s, %s, %s) RETURNING notification_id;""",noti_values)
                    notification_id = cursor.fetchone()[0]

                    #User sms notification


                    return {'transaction_id': trans_id,"Output":output,"notification_id":notification_id}, 201
                else :
                    return {'transaction_id': trans_id,"Output":output}, 201
                
        # if notification_id :
        #     #check if the transaction is fraud
        #     return jsonify({'transaction_id': trans_id,"Output":output,"notification_id":notification_id}), 201
        
    except Exception as e:
        return {"transaction_data": data, "model_data": model_data ,"error": str(e)}, 500




# #Fraud transaction detection api
# transaction_fraud_detection = pickle.load(open('transaction_fraud_detection.pkl','rb'))
# @app.route('/api/model/fraudTransactionPrediction',methods=['POST','GET'])
# def transactionPrediction():
#     data = request.get_json()
#     array_data = data.get('array_data', [])
#     array_data_2d = np.array(array_data).reshape(1, -1)
#     # [step	amount,	oldbalanceOrg,	newbalanceOrig,	oldbalanceDest,	newbalanceDest,	orig_diff,	dest_diff,	surge,	freq_dest,	type__CASH_IN,	type__CASH_OUT,	type__DEBIT,	type__PAYMENT,	type__TRANSFER,	customers_org,	customers_des]
#     prediction = transaction_fraud_detection.predict_proba(array_data_2d)
#     output = '{0:.{1}f}'.format(prediction[0][1],2)
#     if output == 0:
        
#         return("Not Fraud")
#     else:
#         return("Fraud")

#Case CRUD

@app.route("/api/case/openCase", methods=["POST"])
def openCase():
    data = request.get_json()
    customer_id = data['customer_id']
    transaction_id = data['transaction_id']
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_CASE,(customer_id,transaction_id))
        return("Case opened"), 200
    except Exception as e:
        return {"error": str(e)},500

@app.route("/api/case/closeCase", methods=["POST"])
def closeCase():
    data = request.get_json()
    case_id = data['case_id']
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(CLOSE_CASE,(case_id))
        return("Case closed"), 200
    except Exception as e:
        return {"error": str(e)},500

#Add confirmed fraud account 
@app.route("/api/addFraudAccount", methods=["POST"])
def addFraudAccount():
    data = request.get_json()
    customer_id = data['customer_id']
    first_name = data['first_name']
    last_name = data['last_name']
    account_balance = data['account_balance']
    age = data['age']
    address = data['address']
    mobileno = data['mobileno']
    addharno = data['lastlogin']
    lastlogin = data['lastlogin']
    branchid = data['branchid']
    account_type = data['account_type']
    emailid = data['emailid']
    upi_id = data['upi_id']
    account_number = data['account_number']
    pancard_number = data['pancard_number']
    city = data['city']
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_ACC,(customer_id))
                result = cursor.fetchone()
                if result:
                    return ("Account already in the list"), 200
                else:
                    cursor.execute(INSERT_ACC, (customer_id,first_name,last_name,account_balance,age,address,mobileno,addharno,lastlogin,branchid,account_type,emailid,upi_id,account_number,pancard_number,city))
                    return("Account added"), 200

    except Exception as e:
        return {"error": str(e)},500

# Model apis 


Fraud_account_detection = pickle.load(open('Fraud_account_detection.pkl','rb'))
@app.route('/api/model/fraudAccountPrediction',methods=['POST','GET'])
def accountPrediction():
    data = request.get_json()
    array_data = data.get('array_data', [])
    array_data_2d = np.array(array_data).reshape(1, -1)
    # ['current_address_months_count', 'customer_age', 'days_since_request',
    #    'intended_balcon_amount', 'zip_count_4w', 'velocity_6h', 'velocity_24h',
    #    'velocity_4w', 'bank_branch_count_8w',
    #    'date_of_birth_distinct_emails_4w', 'credit_risk_score',
    #    'email_is_free', 'phone_home_valid', 'has_other_cards',
    #    'proposed_credit_limit', 'month', 'payment_type_encoded',
    #    'employment_status_encoded', 'housing_status_encoded',
    #    'application_velocity']
    prediction = Fraud_account_detection.predict_proba(array_data_2d)
    output = '{0:.{1}f}'.format(prediction[0][1],2)
    if output == 0:
        return("Not Fraud")
    else:
        return("Fraud")


if __name__ == "__main__":

    app.run(debug=True, port=8000)