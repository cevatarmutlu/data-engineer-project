from random import randint
from src.model.movie import Movie
from datetime import datetime
from src.enums.PersonStatusEnum import PersonStatus

class PersonActivity:
    def __init__(self, user_id, session) -> None:
        self.user_id = user_id

        self.db_session = session

        self.movie = None

        self.status = PersonStatus.OFFLINE
        self.movie_watching = False
        self.all_film_watching = 'yes'
        
        self.time = 0

    
    def online_decision(self):
        if randint(1, 10) > 6:
            self.status = PersonStatus.ONLINE
        
    def movie_watching_decision(self):
        if randint(1, 10) > 6:
            self.movie_watching = True
            self.movie = self.get_movie_info(self.select_film())
            self.film_end_desicion()
            self.time += 10

    def select_film(self):
        return randint(1, 10)
    
    def get_movie_info(self, movie_row):
        return self.db_session.query(Movie).limit(1).offset(movie_row).all()[0]
    
    def film_end_desicion(self):
        if randint(1, 10) > 7:
            self.all_film_watching = 'no'
        
    def is_film_end_desicion(self):
        self.time += 10
        if (self.all_film_watching == 'no' and self.time > (self.movie.duration / 2)) \
                or (self.all_film_watching == 'yes' and self.time > self.movie.duration):
            
            self.movie_watching = False
            self.status = PersonStatus.OFFLINE if randint(1, 10) > 9 else PersonStatus.ONLINE
            self.movie = None
            return True
        else:
            return False
    
    def decide(self):
        if self.status == PersonStatus.OFFLINE:
            self.online_decision()
        

        if self.status == PersonStatus.ONLINE:
            if self.movie_watching == False:
                self.movie_watching_decision()
            else:
                self.is_film_end_desicion()
        
    
    def get_activity(self):
        return {
            'user_id': self.user_id,
            'film_watch': self.movie_watching,
            'movie': self.movie.as_json_activity() if self.movie != None else self.movie,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    

