from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, nullable=False)
    computer_choice = db.Column(db.String, nullable=False)
    result = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return  f"{self.id} 회 경기"
