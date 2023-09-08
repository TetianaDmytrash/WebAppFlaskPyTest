from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "C:\\prj_dmytrash\\first_proj\\flaskWebApp\\website\\database.db"
#DB_NAME = "database.db" #есть ли возможность избежать полного пути

def create_app():
	app = Flask(__name__) #initialization
	app.config['SECRET_KEY'] = 'hello flask' #secret key (cookie)
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Note
	with app.app_context():
		db.create_all()
	#create_database(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	#как загрузить юзера
	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
	if not path.exists('website/' + DB_NAME):
		db.create_all(app=app)
		print('Created Database')