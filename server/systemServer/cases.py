from flask import Flask, jsonify, request
import psycopg2
from config import DB_CONFIG2
from app import app




# Placeholder function to get fraud transaction details by ID
def get_fraud_transaction_details(transaction_id):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch details from FraudTransactions table by transaction ID
        cursor.execute("""
            SELECT * FROM FraudTransactions WHERE FraudTransaction_id = %s;
        """, (transaction_id,))

        transaction_data = cursor.fetchone()

        if transaction_data:
            # Convert data to a dictionary for JSON response
            transaction_details = {
                'FraudTransaction_id': transaction_data[0],
                'other_details': transaction_data[1],
                # Add more fields as needed
            }

            return transaction_details
        else:
            return None  # Return None if transaction not found

    except Exception as e:
        raise e

    finally:
        # Close database connection
        if conn:
            conn.close()

# Placeholder function to get fraud account details by ID
def get_fraud_account_details(account_id):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch details from FraudAccounts table by account ID
        cursor.execute("""
            SELECT * FROM FraudAccounts WHERE FraudAccount_id = %s;
        """, (account_id,))

        account_data = cursor.fetchone()

        if account_data:
            # Convert data to a dictionary for JSON response
            account_details = {
                'FraudAccount_id': account_data[0],
                'other_details': account_data[1],
                # Add more fields as needed
            }

            return account_details
        else:
            return None  # Return None if account not found

    except Exception as e:
        raise e

    finally:
        # Close database connection
        if conn:
            conn.close()

def get_fraud_transaction_details(transaction_id):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch details from FraudTransactions table by transaction ID
        cursor.execute("""
            SELECT * FROM FraudTransactions WHERE FraudTransaction_id = %s;
        """, (transaction_id,))

        transaction_data = cursor.fetchone()

        if transaction_data:
            # Convert data to a dictionary for JSON response
            transaction_details = {
                'FraudTransaction_id': transaction_data[0],
                'other_details': transaction_data[1],
                # Add more fields as needed
            }

            return transaction_details
        else:
            return None  # Return None if transaction not found

    except Exception as e:
        raise e

    finally:
        # Close database connection
        if conn:
            conn.close()


def get_fraud_account_details(account_id):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch details from FraudAccounts table by account ID
        cursor.execute("""
            SELECT * FROM FraudAccounts WHERE FraudAccount_id = %s;
        """, (account_id,))

        account_data = cursor.fetchone()

        if account_data:
            # Convert data to a dictionary for JSON response
            account_details = {
                'FraudAccount_id': account_data[0],
                'first_name': account_data[1],
                'last_name': account_data[2],
                'other_details': account_data[3],
                # Add more fields as needed
            }

            return account_details
        else:
            return None  # Return None if account not found

    except Exception as e:
        raise e

    finally:
        # Close database connection
        if conn:
            conn.close()



# Define the route to get all cases
@app.route('/api/cases', methods=['GET'])
def get_all_cases():
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Fetch all cases from the Cases table
        cursor.execute("""
            SELECT * FROM Cases;
        """)

        cases_data = cursor.fetchall()

        # Convert data to a list of dictionaries for JSON response
        cases_info = []
        for case_data in cases_data:
            # Fetch fraud account details for each case
            fraud_account_details = get_fraud_account_details(case_data[2])

            case_info = {
                'open_case_id': case_data[0],
                'status': case_data[1],
                'fraudaccount_id': case_data[2],
                'fraudtransaction_id': case_data[3],
                'fraud_transaction_details': get_fraud_transaction_details(case_data[3]),
                'fraud_account_details': fraud_account_details,
                'first_name': fraud_account_details['first_name'],  # Include first name in the response
                'last_name': fraud_account_details['last_name'],    # Include last name in the response
            }
            cases_info.append(case_info)

        return jsonify({'cases': cases_info})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()


def update_case_status(case_id, new_status):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Update the status of the case in the Cases table
        cursor.execute("""
            UPDATE Cases SET status = %s WHERE open_case_id = %s;
        """, (new_status, case_id))

        # Commit the transaction
        conn.commit()

        return True  # Successful update

    except Exception as e:
        raise e

    finally:
        # Close database connection
        if conn:
            conn.close()

# Define the route to update the status of a case
# Define the route to update the status of a case
@app.route('/api/cases/update', methods=['PUT'])
def update_case():
    try:
        data = request.get_json()
        case_id = data.get('case_id')
        new_status = data.get('new_status')

        if not case_id or not new_status:
            return jsonify({'error': 'Both case_id and new_status are required'}), 400

        # Adjust the condition to check for "open" or "close" case-insensitively
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
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Delete the case from the Cases table
        cursor.execute("""
            DELETE FROM Cases WHERE open_case_id = %s;
        """, (case_id,))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': f'Case {case_id} deleted successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        try:
            if conn:
                conn.close()
        except UnboundLocalError:
            pass




# ... (existing code)

# API endpoint to create a new case
@app.route('/api/cases/create', methods=['POST'])
def create_case():
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG2)
        cursor = conn.cursor()

        # Get data from the request JSON
        data = request.get_json()
        status = data.get('status')
        fraudaccount_id = data.get('fraudaccount_id')
        fraudtransaction_id = data.get('fraudtransaction_id')

        # Insert new case into the Cases table
        cursor.execute("""
    INSERT INTO cases (status, fraudaccount_id, fraudtransaction_id)
    VALUES (%s, %s, %s);
""", (status, fraudaccount_id, fraudtransaction_id))

        # Fetch the ID of the newly created case
        case_id = cursor.fetchone()[0]

        # Commit the transaction
        conn.commit()

        return jsonify({'message': f'Case {case_id} created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        try:
            if conn:
                conn.close()
        except UnboundLocalError:
            pass
