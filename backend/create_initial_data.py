from flask import current_app as app
from backend.models import db
from flask_security import SQLAlchemyUserDatastore, hash_password


with app.app_context():
    db.create_all()

    userdatastore : SQLAlchemyUserDatastore  = app.security.datastore

    userdatastore.find_or_create_role(name='admin', description='Administrator')
    userdatastore.find_or_create_role(name='user', description='User')
    

    if (not userdatastore.find_user(email = 'admin@study.ac.in')):
        userdatastore.create_user(email = 'admin@study.ac.in', password = hash_password('admin'), roles = ['admin'])

    if (not userdatastore.find_user(email = 'user01@study.ac.in')):
        userdatastore.create_user(email = 'user01@study.ac.in', password = hash_password('user01'), roles = ['user'])
 

    db.session.commit()

    