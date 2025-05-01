from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import LocalDevelopmentConfig
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from backend.models import db,User,Role
from backend.api import api
from flask_cors import CORS
def createApp():
    app = Flask(__name__)

    app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    api.init_app(app)
    
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    CORS(app)
    app.security = Security(app, datastore=datastore)
    app.app_context().push()

    return app

app = createApp()

import backend.initialdata 
if __name__ == "__main__":
    app.run(debug=True)
