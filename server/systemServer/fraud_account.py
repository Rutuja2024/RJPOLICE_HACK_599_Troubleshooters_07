from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS 
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG2
from app import app


CORS(app)



def connect_to_database():
    connection = psycopg2.connect(**DB_CONFIG2)
    return connection, connection.cursor(cursor_factory=RealDictCursor)

def execute_query(query, values=None, fetch_one=False):
    connection, cursor = connect_to_database()
    cursor.execute(query, values)
    connection.commit()
    result = cursor.fetchone() if fetch_one else cursor.fetchall()
    connection.close()
    return result




# Get all fraud accounts
@app.route('/fraud_accounts', methods=['GET'])
def get_fraud_accounts():
    query = "SELECT * FROM FraudAccounts"
    fraud_accounts = execute_query(query)
    return jsonify(fraud_accounts)

# Get a single fraud account by ID
@app.route('/fraud_accounts/<int:fraud_account_id>', methods=['GET'])
def get_fraud_account(fraud_account_id):
    query = "SELECT * FROM FraudAccounts WHERE FraudAccount_id = %s"
    fraud_account = execute_query(query, (fraud_account_id,), fetch_one=True)
    if fraud_account:
        return jsonify(fraud_account)
    return jsonify({'message': 'Fraud account not found'}), 404

# Create a new fraud account
@app.route('/fraud_accounts', methods=['POST'])
def create_fraud_account():
    data = request.get_json()
    query = """
        INSERT INTO FraudAccounts (
            customer_id, First_name, Last_name, Account_Balance, Age,
            Address, MobileNo, AddharNo, Lastlogin, BranchId, Account_type,
            Emailid, UPI_id, Account_number, Pancard_number, City
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING FraudAccount_id;
    """
    values = (
        data['customer_id'], data['First_name'], data['Last_name'],
        data['Account_Balance'], data['Age'], data['Address'],
        data['MobileNo'], data['AddharNo'], data['Lastlogin'],
        data['BranchId'], data['Account_type'], data['Emailid'],
        data['UPI_id'], data['Account_number'], data['Pancard_number'],
        data['City']
    )
    fraud_account_id = execute_query(query, values, fetch_one=True)['fraudaccount_id']
    return jsonify({'fraud_account_id': fraud_account_id}), 201

# Update an existing fraud account
@app.route('/fraud_accounts/<int:fraud_account_id>', methods=['PUT'])
def update_fraud_account(fraud_account_id):
    data = request.get_json()
    query = """
        UPDATE FraudAccounts SET
            customer_id = %s,
            First_name = %s,
            Last_name = %s,
            Account_Balance = %s,
            Age = %s,
            Address = %s,
            MobileNo = %s,
            AddharNo = %s,
            Lastlogin = %s,
            BranchId = %s,
            Account_type = %s,
            Emailid = %s,
            UPI_id = %s,
            Account_number = %s,
            Pancard_number = %s,
            City = %s
        WHERE FraudAccount_id = %s;
    """
    values = (
        data['customer_id'], data['First_name'], data['Last_name'],
        data['Account_Balance'], data['Age'], data['Address'],
        data['MobileNo'], data['AddharNo'], data['Lastlogin'],
        data['BranchId'], data['Account_type'], data['Emailid'],
        data['UPI_id'], data['Account_number'], data['Pancard_number'],
        data['City'], fraud_account_id
    )
    execute_query(query, values)
    return jsonify({'message': 'Fraud account updated successfully'})

# Delete a fraud account
@app.route('/fraud_accounts/<int:fraud_account_id>', methods=['DELETE'])
def delete_fraud_account(fraud_account_id):
    query = "DELETE FROM FraudAccounts WHERE FraudAccount_id = %s"
    execute_query(query, (fraud_account_id,))
    return jsonify({'message': 'Fraud account deleted successfully'})


