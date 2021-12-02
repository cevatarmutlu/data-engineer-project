from random import randint
from src.model.movie import Movie

class PersonActivity:
    def __init__(self, user_id, session) -> None:
        self.user_id = user_id
        self.db_session = session
        self.movie = None
        self.film_watching = 'no'
        self.all_film_watching = 'yes'
        self.status = 'offline'
        self.time = 0

    
    def online_decision(self):
        if randint(1, 100) < 20:
            self.status = 'online'
        
    def movie_watching_decision(self):
        if randint(1, 100) < 20:
            self.film_watching = 'yes'
            self.movie = self.get_movie_info(self.select_film())
            self.film_end_desicion()
            self.time += 10

    def select_film(self):
        return randint(1, 126)
    
    def get_movie_info(self, movie_id):
        return self.db_session.query(Movie).filter(Movie.show_id == movie_id).all()[0]
    
    def film_end_desicion(self):
        if randint(1, 100) > 7:
            self.all_film_watching = 'no'
        
    def is_film_end_desicion(self):
        self.time += 10
        if (self.all_film_watching == 'no' and self.time > (self.movie.duration / 2)) \
                or (self.all_film_watching == 'yes' and self.time > self.movie.duration):
            
            self.film_watching = 'no'
            self.status = 'offline' if randint(1, 10) > 9 else 'online'
            return True
        else:
            return False
    
    def get_activity(self):
        if self.status == 'offline':
            self.online_decision()
        else:
            if self.film_watching == 'no':
                self.movie_watching_decision()
            else:
                self.is_film_end_desicion()
        
        return {
            'user_id': self.user_id,
            'status': self.status,
            'film_watch': self.film_watching,
            'movie': self.movie.as_json_activity() if self.movie != None else self.movie
        }
    

