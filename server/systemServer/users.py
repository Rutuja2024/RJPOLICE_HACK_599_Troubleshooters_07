# app.py

from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS 
from config import DB_CONFIG  # Import the DB_CONFIG from config.py

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def hello():
#     return 'Hello, this is the root URL of Bank System!'

# API endpoint to fetch all user information
@app.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Fetch all user information from the CustomerProfile table
        cursor.execute("""
            SELECT * FROM CustomerProfile;
        """)

        user_data = cursor.fetchall()

        if user_data:
            # Convert data to a list of dictionaries for JSON response
            users_info = []
            for user in user_data:
                user_info = {
                    'customer_id': user[0],
                    'first_name': user[1],
                    'last_name': user[2],
                    'account_balance': float(user[3]),
                    'age': user[4],
                    'address': user[5],
                    'mobile_no': user[6],
                    'addhar_no': user[7],
                    'last_login': str(user[8]),
                    'branch_id': user[9],
                    'account_type': user[10],
                    'email_id': user[11],
                    'upi_id': user[12],
                    'account_number': user[13],
                    'pancard_number': user[14],
                    'city': user[15]
                }
                users_info.append(user_info)

            return jsonify(users_info)
        else:
            return jsonify({'error': 'No users found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()


# API endpoint to fetch user information
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Fetch user information from the CustomerProfile table
        cursor.execute("""
            SELECT * FROM CustomerProfile WHERE customer_id = %s;
        """, (user_id,))

        user_data = cursor.fetchone()

        if user_data:
            # Convert data to a dictionary for JSON response
            user_info = {
                'customer_id': user_data[0],
                'first_name': user_data[1],
                'last_name': user_data[2],
                'account_balance': float(user_data[3]),
                'age': user_data[4],
                'address': user_data[5],
                'mobile_no': user_data[6],
                'addhar_no': user_data[7],
                'last_login': str(user_data[8]),
                'branch_id': user_data[9],
                'account_type': user_data[10],
                'email_id': user_data[11],
                'upi_id': user_data[12],
                'account_number': user_data[13],
                'pancard_number': user_data[14],
                'city': user_data[15]
            }

            return jsonify(user_info)
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close database connection
        if conn:
            conn.close()


# API endpoint to create a new customer profile
@app.route('/api/user/create', methods=['POST'])
def create_user():
    try:
        # Connect to the PostgreSQL database using credentials from DB_CONFIG
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        account_balance = data.get('account_balance')
        age = data.get('age')
        address = data.get('address')
        mobile_no = data.get('mobile_no')
        addhar_no = data.get('addhar_no')
        last_login = data.get('last_login')
        branch_id = data.get('branch_id')
        account_type = data.get('account_type')
        email_id = data.get('email_id')
        upi_id = data.get('upi_id')
        account_number = data.get('account_number')
        pancard_number = data.get('pancard_number')
        city = data.get('city')

        # Insert new user profile into the CustomerProfile table
        cursor.execute("""
            INSERT INTO CustomerProfile (
                First_name, Last_name, Account_Balance, Age, Address, MobileNo,
                AddharNo, Lastlogin, BranchId, Account_type, Emailid, UPI_id,
                Account_number, Pancard_number, City
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            first_name, last_name, account_balance, age, address, mobile_no,
            addhar_no, last_login, branch_id, account_type, email_id, upi_id,
            account_number, pancard_number, city
        ))

        # Commit the transaction
        conn.commit()

        return jsonify({'message': 'User profile created successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


    finally:
        # Close database connection
        if conn:
            conn.close()



if __name__ == '__main__':
    app.run(debug=True)
