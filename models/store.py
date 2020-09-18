from db import db

class StoreModel(db.Model):
  # we tell SQLAlchemy where to store data
  __tablename__ = 'stores'

  # then the columns we will have
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40))

  # there are two approaches we can take here:
  # 1 - add "lazy = 'dynamic'" to the next line of code. 
  #   This means that it creates it dynamically as it needs. 
  #   The table is created faster, by everytime we call for example json function, 
  #   it has to go over all the items
  # 2 - don't add it
  #   This means it might take time to create the table at first, 
  #   but then the rest is very easy and fast
  items = db.relationship('ItemModel', lazy='dynamic')

  def __init__(self, name):
    self.name = name
  
  def json(self):
    return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
  
  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
  
  @classmethod
  def find_by_name(cls, name):
    # SELECT * FROM users WHERE name=name LIMIT 1
    return cls.query.filter_by(name=name).first()
