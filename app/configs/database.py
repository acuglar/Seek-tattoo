from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models import (
                                UserModel, 
                                AddressModel, 
                                DescriptionModel, 
                                CommentModel, 
                                StyleModel, 
                                ImageModel, 
                                ImageStyleModel
                            )
