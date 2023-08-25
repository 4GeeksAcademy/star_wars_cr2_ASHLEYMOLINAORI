from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FavoritePeople(db.Model):
    __tablename__ = "favoritepeople"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "email":  User.query.get(self.user_id).serialize()["email"],
            "people_name": People.query.get(self.people_id).serialize()["name"]
        }
    
class FavoritesPlanets(db.Model):
   __tablename__ = 'favoritesplanets'
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

   def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "email":  User.query.get(self.user_id).serialize()["email"],
            #revisar
            "planets_name": Planets.query.get(self.planets_id).serialize()["name"]
        }



class FavoritesVehicles(db.Model):
    __tablename__ = 'favoritesvehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicles_id": self.vehicles_id,
            "email":  User.query.get(self.user_id).serialize()["email"],
            #revisar
            "vehicles_name": Vehicles.query.get(self.vehicles_id).serialize()["name"]
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_people = db.relationship(FavoritePeople, backref = 'user', lazy=True)
    favorites_planets = db.relationship(FavoritesPlanets, backref='user', lazy=True)
    favorites_vehicles = db.relationship(FavoritesVehicles, backref='user', lazy=True)



    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(30), unique=True, nullable=False)
    eye_color = db.Column(db.String(30), unique=False, nullable=True)
    hair_color = db.Column(db.String(30), unique=False, nullable=True)
    height = db.Column(db.Float, unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(30), unique=False, nullable=True, default="N/A")
    favorite_people = db.relationship(FavoritePeople, backref = 'people')

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "eye_color":self.eye_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "age": self.age,
            "gender": self.gender
        }
    

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    rotation_period = db.Column(db.String(200), nullable = True)
    orbital_period = db.Column(db.String(200), nullable = True)
    population = db.Column(db.Integer, nullable = False)
    terrain = db.Column(db.Integer, nullable = False)
    climate = db.Column(db.String(250), nullable = False)
    favorites_planets = db.relationship(FavoritesPlanets, backref = 'planets')  

    def serialize(self):
        return{
            "id":self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate
                        
        }




class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    model = db.Column(db.String(250), nullable = False)
    length = db.Column(db.String(250), nullable = True)
    cargo_capacity = db.Column(db.String(250), nullable = True)
    favorites_vehicles = db.relationship(FavoritesVehicles, backref='vehicles', lazy=True)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "model":self.model,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity
        }



