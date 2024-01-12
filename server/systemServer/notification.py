from flask import Flask, jsonify, request
from flask_cors import CORS 
import psycopg2
from config import DB_CONFIG2  
from app import app

CORS(app)


def connect_to_database():
    try:
        conn = psycopg2.connect(**DB_CONFIG2)
        return conn
    except Exception as e:
        print(f"Error: Unable to connect to the database. {e}")
        return None

# API endpoint to create a new notification
@app.route('/api/notification/create', methods=['POST'])
def create_notification():
    try:
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        data = request.get_json()

        if 'fraud_transaction_id' in data:
            fraud_transaction_id = data['fraud_transaction_id']

            # Check if fraud_transaction_id exists in FraudTransactions table
            cursor.execute("SELECT 1 FROM FraudTransactions WHERE FraudTransaction_id = %s;", (fraud_transaction_id,))
            if not cursor.fetchone():
                return jsonify({'error': 'Invalid fraud_transaction_id. Not found in FraudTransactions table'}), 400

            message = "Fraud transaction detected"
            fraud_account_id = None  

        elif 'fraud_account_id' in data:  
           fraud_account_id = data['fraud_account_id']

    # Check if fraud_account_id exists in FraudAccounts table
           cursor.execute("SELECT 1 FROM FraudAccounts WHERE fraudaccount_id = %s;", (fraud_account_id,))
           if not cursor.fetchone():
               return jsonify({'error': 'Invalid fraud_account_id. Not found in FraudAccounts table'}), 400

           message = "Fraud account detected"
           fraud_transaction_id = None 

        else:
            return jsonify({'error': 'Invalid request. Specify either fraud_transaction_id or fraud_account_id'}), 400

        # Insert new notification into the Notifications table
        cursor.execute("""
            INSERT INTO Notifications (Message, Type, FraudTransaction_id, FraudAccount_id)
            VALUES (%s, %s, %s, %s);
        """, (message, data.get('type'), fraud_transaction_id, fraud_account_id))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'Notification created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        try:
          if conn:
            conn.close()
        except UnboundLocalError:
          pass





@app.route('/api/notifications/all', methods=['GET'])
def get_notifications_all():
    try:
     
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch all notifications from the Notifications table
        cursor.execute("SELECT * FROM Notifications;")
        notifications = cursor.fetchall()

        # Get the column names from the cursor description
        column_names = [desc[0] for desc in cursor.description]

        # Convert the result into a list of dictionaries for JSON serialization
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

