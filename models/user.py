from db import db

class UserModel(db.Model):
  # we tell SQLAlchemy where to store data
  __tablename__ = 'users'

  # then the columns we will have
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40))
  password = db.Column(db.String(40))

  def __init__(self, username, password):
    self.username = username
    self.password = password
  
  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()
  
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()