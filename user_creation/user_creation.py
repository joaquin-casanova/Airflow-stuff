import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser
from flask_bcrypt import generate_password_hash
user = PasswordUser(models.User())
user.username = 'some'
user.email = 'some@email.com'
user._password = generate_password_hash("password_here", 12).decode('utf-8')
session = settings.Session()
session.add(user)
session.commit()
session.close()
exit()