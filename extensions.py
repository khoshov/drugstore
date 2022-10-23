from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

admin = Admin()
db = SQLAlchemy()
migrate = Migrate()
