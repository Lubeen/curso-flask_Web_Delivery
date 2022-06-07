import os
from werkzeug.security import generate_password_hash
from delivery.ext.auth.models import User
from delivery.ext.db import db
from werkzeug.utils import secure_filename
from flask import current_app as app

ALG = 'pbkdf2:sha256'

def create_user(email, password, admin: bool = False) -> User:
    user = User(
        email=email,
         passwd= generate_password_hash(password, ALG) , admin=admin)
    db.session.add(user)
    #todo tratar exception caso user ja exista
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    """
    saves user foto in ./uploads/user/<filename>
    """
    filename = os.path.join(
        app.config['UPLOAD_FOLDER'],
        secure_filename(
            filename
            )
    )
    #todo: verifica se a pasta existe se nao criar
    filestorage.save(filename)