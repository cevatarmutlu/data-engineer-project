from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from dataclasses import dataclass

Base = declarative_base()

# Movie verilerinde duration' u düzelt
@dataclass
class Movie(Base):
    __tablename__ = 'movies'

    show_id = Column(Integer, primary_key=True)
    type = Column(String)
    title = Column(String)
    director = Column(String)
    cast = Column(String)
    country = Column(String)
    date_added = Column(DateTime)
    release_year = Column(Integer)
    rating = Column(String)
    duration = Column(Integer)
    listed_in = Column(String)
    description = Column(String)

    def as_json_activity(self):
        return {
            "show_id": self.show_id,
            "title": self.title,
            "listed_in": self.listed_in,
        }

    def __repr__(self):
        return "<User(show_id='%s', type='%s', title='%s', director='%s', cast='%s', country='%s', date_added='%s', release_year='%s', rating='%s', duration='%s', listed_in='%s', description='%s')>" % (
                                self.show_id, self.type, self.title, self.director, self.cast, self.country, self.date_added, self.release_year, self.rating, self.duration, self.listed_in, self.description)
