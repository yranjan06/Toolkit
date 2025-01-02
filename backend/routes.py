from flask import current_app as app, request, jsonify, render_template
from flask_security import auth_required, verify_password, hash_password

datastore = app.security.datastore

@app.get('/')
def hello():
    return render_template('index.html')


@app.get('/protected')
@auth_required()
def protected():
    return '<h1>Protected, and only accessible by authenticated users</h1>'



@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'email and password are required'}), 400

    user = datastore.find_user(email=email)
    if not user:
        return jsonify({'message': 'user not found'}), 404

    if verify_password(password, user.password):
        return jsonify({'token': user.get_auth_token(), 'email': user.email, 'role': user.roles[0].name, 'id': user.id}), 200
     
    return jsonify({'message': 'invalid password'}), 401




@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    if not email or not password or not role in ['admin', 'user']:
        return jsonify({'message': 'invalid inputs'}), 404

    user = datastore.find_user(email=email)

    if user:
        return jsonify({'message': 'user already exists'}), 404

    try:
        datastore.create_user(email=email, password=hash_password(password), roles=[role], active=True)
        db.session.commit()
        return jsonify({'message': 'user created'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'error creating user'}), 400
    

   

