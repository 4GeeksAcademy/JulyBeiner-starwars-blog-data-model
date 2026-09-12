from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorite_characters: Mapped[list["FavoriteCharacter"]] = relationship(
        back_populates="user"
    )

    favorite_planets: Mapped[list["FavoritePlanet"]] = relationship(
        back_populates="user"
    )

    favorite_vehicles: Mapped[list["FavoriteVehicle"]] = relationship(
        back_populates="user"
    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    gender: Mapped[str] = mapped_column(String(50))
    birth_year: Mapped[str] = mapped_column(String(50))
    height: Mapped[str] = mapped_column(String(50))
    mass: Mapped[str] = mapped_column(String(50))

    favorited_by: Mapped[list["FavoriteCharacter"]] = relationship(
        back_populates="character"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "mass": self.mass
        }


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(120))
    climate: Mapped[str] = mapped_column(String(120))
    terrain: Mapped[str] = mapped_column(String(120))
    diameter: Mapped[str] = mapped_column(String(120))

    favorited_by: Mapped[list["FavoritePlanet"]] = relationship(
        back_populates="planet"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "diameter": self.diameter
        }


class Vehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    model: Mapped[str] = mapped_column(String(120))
    manufacturer: Mapped[str] = mapped_column(String(120))
    vehicle_class: Mapped[str] = mapped_column(String(120))
    cost_in_credits: Mapped[str] = mapped_column(String(120))

    favorited_by: Mapped[list["FavoriteVehicle"]] = relationship(
        back_populates="vehicle"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "vehicle_class": self.vehicle_class,
            "cost_in_credits": self.cost_in_credits
        }


class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    character_id: Mapped[int] = mapped_column(
        ForeignKey("character.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="favorite_characters"
    )

    character: Mapped["Character"] = relationship(
        back_populates="favorited_by"
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    planet_id: Mapped[int] = mapped_column(
        ForeignKey("planet.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="favorite_planets"
    )

    planet: Mapped["Planet"] = relationship(
        back_populates="favorited_by"
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }


class FavoriteVehicle(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey("vehicle.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="favorite_vehicles"
    )

    vehicle: Mapped["Vehicle"] = relationship(
        back_populates="favorited_by"
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }
