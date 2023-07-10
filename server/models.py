from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)


class Activity(db.Model, SerializerMixin):
    __tablename__ = 'activities'

    # -relationship.backref
    serialize_rules = ('-campers.activity', )
    # serialize_rules = ('-signups.activity', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    difficulty = db.Column(db.Integer)

    campers = db.relationship("Signup", backref = "activity")
    # signups = db.relationships("Signup", backref = "activity")
    # signups = db.relationships("Signup", cascade = "all, delete", backref = "activity")
    
    def __repr__(self):
        return f'<Activity {self.id}: {self.name}>'


class Camper(db.Model, SerializerMixin):
    __tablename__ = 'campers'

    # -relationship.backref
    serialize_rules = ('-activities.camper', )
    # serialize_rules = ('-signups.camper', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    activities = db.relationship("Signup", backref = "camper")
    # signups = db.relationship("Signup", backref = "camper")

    # validation caught by try... except block
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Camper must have a name!")
        else:
            return name
        
    @validates('age')
    def validate_age(self, key, age):
        if age < 8 or age > 18:
            raise ValueError("Camper must be between 8 and 18, inclusive!")
        else:
            return age
    
    def __repr__(self):
        return f'<Camper {self.id}: {self.name}>'


class Signup(db.Model, SerializerMixin):
    __tablename__ = 'signups'

    # -backref.relationship, -backref.relationship
    serialize_rules = ('-activity.campers', '-camper.actitivies')
    # serialize_rules = ('-activity.signups', '-camper.signups')

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)

    camper_id = db.Column(db.Integer, db.ForeignKey('campers.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'))

    @validates('time')
    def validate_time(self, key, time):
        if time < 0 or time > 23:
            raise ValueError("Signup time must be between 0 and 23, inclusive!")
        else:
            return time
    
    def __repr__(self):
        return f'<Signup {self.id}>'