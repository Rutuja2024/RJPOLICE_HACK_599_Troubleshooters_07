
from flask import Flask, jsonify, request
from flask_cors import CORS 
import psycopg2
from psycopg2 import connect, extras
from psycopg2.extras import DictCursor
from config import DB_CONFIG2
from config import DB_CONFIG
from config import DB_CONFIG3
import json


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, this is the root URL of all '



@app.route('/api/transactions/sender/<sender_account>', methods=['GET'])
def get_transactions_by_sender(sender_account):
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor(cursor_factory=DictCursor)

        # Assuming your table is named 'system_transaction'
        columns = ["transactionid", "transactiontype", "oldbalanceorg", "newbalanceorig", "oldbalancedest", "newbalancedest", "transaction_date", "sender_account", "receiver_account", "ip_address_sender", "fraud_transaction"]
        column_names = ', '.join(columns)

        query = f"""
            SELECT {column_names}
            FROM system_transaction
            WHERE sender_account = %s;
        """
        cursor.execute(query, (sender_account,))
        transactions_data = cursor.fetchall()

        transactions = []
        for row in transactions_data:
            transaction_info = {columns[i]: row[i] for i in range(len(columns))}
            transactions.append(transaction_info)

        return jsonify(transactions)

    except Exception as e:
        return jsonify({'error': f"Error retrieving transactions: {str(e)}"}), 500
    finally:
        if conn:
            conn.close()
        


        
@app.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM system_account;")
        users_data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        users_list = []

        for system_account_row in users_data :
            user_dict = {column_names[i]: system_account_row[i] for i in range(len(column_names))}
            users_list.append(user_dict)


        if users_data:
            return jsonify(users_list)
        else:
            return jsonify({'error': 'User not found'}), 404    
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            conn.close()


@app.route('/api/users/<int:customer_id>', methods=['GET'])
def get_user_by_id(customer_id):
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM system_account WHERE customer_id = %s;", (customer_id,))
        user_data = cursor.fetchone()

        if user_data:
            column_names = [desc[0] for desc in cursor.description]
            user_dict = {column_names[i]: user_data[i] for i in range(len(column_names))}
            return jsonify(user_dict)
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn:
            conn.close()




@app.route('/api/notifications/all', methods=['GET'])
def get_notifications_all():
    try:
     
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Notifications;")
        notifications = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        notifications_list = []
        for notification in notifications:
            notification_dict = {column_names[i]: notification[i] for i in range(len(column_names))}
            notifications_list.append(notification_dict)

        return jsonify(notifications_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        try:
            if conn:
                conn.close()
        except UnboundLocalError:
            pass


#Cases part 
def get_fraud_transaction_details(transaction_id):
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                Transactionid,
                Transactiontype,
                oldbalanceOrg,
                newbalanceOrig,
                oldbalanceDest,
                newbalanceDest,
                Transaction_date,
                Sender_account,
                Receiver_account,
                IP_address_sender,
                Fraud_Transaction
            FROM System_Transaction
            WHERE Transactionid = %s;
        """, (transaction_id,))

        transaction_data = cursor.fetchone()

        if transaction_data:
            column_names = [desc[0] for desc in cursor.description]
            transaction_details = {column_names[i]: transaction_data[i] for i in range(len(column_names))}
            return transaction_details
        else:
            return None 

    except Exception as e:
        raise e

    finally:
        if conn:
            conn.close()




def get_fraud_account_details(account_id):
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                FraudAccount_id,
                first_name,
                last_name,
                account_balance,
                age,
                address,
                mobileno,
                addharno,
                lastlogin,
                branched,
                account_type,
                emailid,
                upi_id,
                account_number,
                pancard_number,
                city,
                credit_card_number,
                flag_KYC,
                flag_Phone_verified,
                current_address_month_count,
                account_creation_date,
                intended_bank_account,
                zip_count_4w,
                velocity_6h,
                velocity_24h,
                has_other_cards_count,
                proposed_credit_limit,
                employment_status_encoded,
                housing_status_encoded,
                Fraud_Account
            FROM FraudAccounts
            WHERE FraudAccount_id = %s;
        """, (account_id,))

        account_data = cursor.fetchone()

        if account_data:
            column_names = [desc[0] for desc in cursor.description]
            account_details = {column_names[i]: account_data[i] for i in range(len(column_names))}

            return account_details
        else:
            return None 

    except Exception as e:
        raise e

    finally:
        if conn:
            conn.close()


# Define the route to get all cases
@app.route('/api/cases/all', methods=['GET'])
def get_all_cases():
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                Case_id,
                Transaction_id,
                Customer_id,
                Status
            FROM Cases;
        """)

        cases_data = cursor.fetchall()
        cases_info = []
        for case_data in cases_data:
            fraud_account_details = get_fraud_account_details(case_data['fraudaccount_id'])

            case_info = {
                'open_case_id': case_data['Case_id'],
                'status': case_data['Status'],
                'fraudaccount_id': case_data['Customer_id'],  
                'fraudtransaction_id': case_data['Transaction_id'],
                'fraud_transaction_details': get_fraud_transaction_details(case_data['Transaction_id']),
                'fraud_account_details': fraud_account_details,
                'first_name': fraud_account_details['first_name'],  
                'last_name': fraud_account_details['last_name'],   
            }
            cases_info.append(case_info)

        return jsonify({'cases': cases_info})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if conn:
            conn.close()


def update_case_status(case_id, new_status):
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE cases SET status = %s WHERE open_case_id = %s;
        """, (new_status, case_id))
        conn.commit()

        return True  

    except Exception as e:
        raise e

    finally:
        if conn:
            conn.close()


@app.route('/api/cases/update', methods=['PUT'])
def update_case():
    try:
        data = request.get_json()
        case_id = data.get('case_id')
        new_status = data.get('new_status')

        if not case_id or not new_status:
            return jsonify({'error': 'Both case_id and new_status are required'}), 400
        if new_status.lower() not in ['open', 'close']:
            return jsonify({'error': 'Invalid value for new_status. Must be "open" or "close"'}), 400

        if update_case_status(case_id, new_status):
            return jsonify({'message': f'Case {case_id} updated successfully to {new_status}'})

        return jsonify({'error': f'Failed to update case {case_id} status'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
   


# Define the route to delete a case by ID
@app.route('/api/cases/delete/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM cases WHERE open_case_id = %s;
        """, (case_id,))
        conn.commit()

        return jsonify({'message': f'Case {case_id} deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        try:
            if conn:
                conn.close()
        except UnboundLocalError:
            pass



@app.route('/api/cases/create', methods=['POST'])
def create_case():
    try:
        conn = psycopg2.connect(**DB_CONFIG3)
        cursor = conn.cursor()
        data = request.get_json()
        transaction_id = data.get('transaction_id')
        customer_id = data.get('customer_id')
        status = data.get('status')
        cursor.execute("""
            INSERT INTO cases (transaction_id, customer_id, status)
            VALUES (%s, %s, %s)
            RETURNING case_id;
        """, (transaction_id, customer_id, status))
        case_id = cursor.fetchone()[0]
        conn.commit()

        return jsonify({'message': f'Case {case_id} created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if conn:
            conn.close()
        
if __name__ == '__main__':
    app.run(debug=True)
