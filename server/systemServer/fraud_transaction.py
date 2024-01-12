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

@app.route('/api/fraud_transactions', methods=['GET'])
def get_fraud_transactions():
    query = "SELECT * FROM FraudTransactions"
    fraud_transactions = execute_query(query)
    return jsonify(fraud_transactions)



@app.route('/fraud_transactions/<int:fraud_transaction_id>', methods=['GET'])
def get_fraud_transaction(fraud_transaction_id):
    query = "SELECT * FROM FraudTransactions WHERE FraudTransaction_id = %s"
    fraud_transaction = execute_query(query, (fraud_transaction_id,), fetch_one=True)
    if fraud_transaction:
        return jsonify(fraud_transaction)
    return jsonify({'message': 'Fraud transaction not found'}), 404

@app.route('/api/fraud_transactions', methods=['POST'])
def create_fraud_transaction():
    data = request.get_json()
    query = """
        INSERT INTO FraudTransactions (
            Transactionid, Transactiontype, Amount_before_transaction,
            Amount_after_transaction, Transaction_date, From_account_id, To_account_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING FraudTransaction_id;
    """
    values = (
        data['Transactionid'], data['Transactiontype'],
        data['Amount_before_transaction'], data['Amount_after_transaction'],
        data['Transaction_date'], data['From_account_id'], data['To_account_id']
    )
    fraud_transaction_id = execute_query(query, values, fetch_one=True)['fraudtransaction_id']
    return jsonify({'fraud_transaction_id': fraud_transaction_id}), 201




@app.route('/fraud_transactions/<int:fraud_transaction_id>', methods=['PUT'])
def update_fraud_transaction(fraud_transaction_id):
    data = request.get_json()
    query = """
        UPDATE FraudTransactions SET
            Transactionid = %s,
            Transactiontype = %s,
            Amount_before_transaction = %s,
            Amount_after_transaction = %s,
            Transaction_date = %s,
            From_account_id = %s,
            To_account_id = %s
        WHERE FraudTransaction_id = %s;
    """
    values = (
        data['Transactionid'], data['Transactiontype'],
        data['Amount_before_transaction'], data['Amount_after_transaction'],
        data['Transaction_date'], data['From_account_id'], data['To_account_id'],
        fraud_transaction_id
    )
    execute_query(query, values)
    return jsonify({'message': 'Fraud transaction updated successfully'})

@app.route('/fraud_transactions/<int:fraud_transaction_id>', methods=['DELETE'])
def delete_fraud_transaction(fraud_transaction_id):
    query = "DELETE FROM FraudTransactions WHERE FraudTransaction_id = %s"
    execute_query(query, (fraud_transaction_id,))
    return jsonify({'message': 'Fraud transaction deleted successfully'})


