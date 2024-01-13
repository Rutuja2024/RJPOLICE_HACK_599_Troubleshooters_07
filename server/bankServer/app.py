from flask import Flask, jsonify, request
import psycopg2
from config import DB_CONFIG

app = Flask(__name__)

# Root URL
@app.route('/')
def hello():
    return 'Hello, this is the root URL of Bank System!'

# Read operation
@app.route('/api/transaction/<int:transaction_id>', methods=['GET'])
def get_transaction_info(transaction_id):
    conn = None  # Initialize conn outside the try block

    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Fetch transaction information from the transactiontable
        cursor.execute("""
            SELECT * FROM transactiontable WHERE transactionid = %s;
        """, (transaction_id,))

        transaction_data = cursor.fetchone()

        if transaction_data:
            # Convert data to a dictionary for JSON response
            transaction_info = {
                'transaction_id': transaction_data[0],
                'transaction_type': transaction_data[1],
                'amount_before_transaction': float(transaction_data[2]),
                'amount_after_transaction': float(transaction_data[3]),
                'transaction_date': str(transaction_data[4]),
                'from_account_id': transaction_data[5],
                'to_account_id': transaction_data[6],
            }

            return jsonify(transaction_info)
        else:
            return jsonify({'error': 'Transaction not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()

# Create operation
@app.route('/api/transaction/create', methods=['POST'])
def create_transaction():
    conn = None  # Initialize conn outside the try block

    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        data = request.get_json()
        # Extract data from the request payload
        transaction_type = data.get('transaction_type')
        amount_before_transaction = data.get('amount_before_transaction')
        amount_after_transaction = data.get('amount_after_transaction')
        transaction_date = data.get('transaction_date')
        from_account_id = data.get('from_account_id')
        to_account_id = data.get('to_account_id')

        # Insert new transaction into the transactiontable
        cursor.execute("""
            INSERT INTO transactiontable (
                transactiontype, amount_before_transaction, amount_after_transaction,
                transaction_date, from_account_id, to_account_id
            )
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            transaction_type, amount_before_transaction, amount_after_transaction,
            transaction_date, from_account_id, to_account_id
        ))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'Transaction created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()

# Update operation
@app.route('/api/transaction/update/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    conn = None  # Initialize conn outside the try block

    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        data = request.get_json()
        # Extract data from the request payload
        transaction_type = data.get('transaction_type')
        amount_before_transaction = data.get('amount_before_transaction')
        amount_after_transaction = data.get('amount_after_transaction')
        transaction_date = data.get('transaction_date')
        from_account_id = data.get('from_account_id')
        to_account_id = data.get('to_account_id')

        # Update transaction in the transactiontable
        cursor.execute("""
            UPDATE transactiontable
            SET transactiontype = %s,
                amount_before_transaction = %s,
                amount_after_transaction = %s,
                transaction_date = %s,
                from_account_id = %s,
                to_account_id = %s
            WHERE transactionid = %s;
        """, (
            transaction_type, amount_before_transaction, amount_after_transaction,
            transaction_date, from_account_id, to_account_id, transaction_id
        ))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'Transaction updated successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()

# ... Other route handlers ...

# Delete operation
@app.route('/api/transaction/delete/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    conn = None  # Initialize conn outside the try block

    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Delete transaction from the transactiontable
        cursor.execute("""
            DELETE FROM transactiontable WHERE transactionid = %s;
        """, (transaction_id,))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'Transaction deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
