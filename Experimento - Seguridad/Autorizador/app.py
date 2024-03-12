from flask import Flask, jsonify, request
import random
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

correct_password_hash = 'password123'
generated_otp = None
token_secret = 'your_secret_key'

def generate_otp():
    return str(random.randint(1000, 9999))

def generate_token():
    access_date = datetime.utcnow()
    payload = {'access_date': access_date.isoformat()}
    token = jwt.encode(payload, token_secret, algorithm='HS256')
    return token

@app.route('/login', methods=['POST'])
def login():
    global generated_otp

    data = request.get_json()
    provided_password = data.get('password')

    if not provided_password or provided_password != correct_password_hash:
        return jsonify({'error': 'Invalid password'}), 401 
    else:
        generated_otp = generate_otp()
        print(f'Generated OTP: {generated_otp}')
        return jsonify({'message': 'OTP generated successfully'}), 200

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    global generated_otp

    data = request.get_json()
    provided_otp = data.get('otp')

    if generated_otp is not None:
        if provided_otp == generated_otp:
            token = generate_token()
            generated_otp = None
            return jsonify({'verified': True, 'token': token}), 200
        else:
            return jsonify({'verified': False}), 401  
    else:
        return jsonify({'error': 'OTP not generated yet'}), 400  

@app.route('/verify_token', methods=['POST'])
def verify_token():
    data = request.get_json()
    provided_token = data.get('token')

    try:
        decoded_payload = jwt.decode(provided_token, token_secret, algorithms=['HS256'])
        return jsonify({'verified': True, 'decoded_payload': decoded_payload}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401 
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401  

if __name__ == '__main__':
    app.run(debug=True)
