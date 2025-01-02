from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # flask-security specific fields
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
    active = db.Column(db.Boolean(), default=True)   
    
    roles = db.relationship('Role', backref='bearers', secondary='user_roles')

    def __repr__(self):
        return f'<User {self.email}>'


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)  
    description = db.Column(db.String(255)) 
    
    def __repr__(self):
        return f'<Role {self.name}>'



class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
    
    def __repr__(self):
        return f'<UserRoles {self.user_id} -> {self.role_id}>'
