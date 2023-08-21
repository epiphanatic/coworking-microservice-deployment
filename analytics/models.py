from datetime import datetime

from config import db


class Token(db.Model):
    __tablename__ = "tokens"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, unique=False, nullable=False)
    token = db.Column(db.String(6), index=True, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, index=False,
                           unique=False, nullable=False, default=datetime.now())
    used_at = db.Column(db.DateTime, index=True, unique=False, nullable=True)
