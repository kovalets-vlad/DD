class Genre:
    def __init__(self, genre_id, genre_name):
        self.__genre_id = genre_id  
        self.__genre_name = genre_name  

    @property
    def genre_id(self):
        return self.__genre_id

    @property
    def genre_name(self):
        return self.__genre_name

    def display_info(self):
        print(f"Жанр: {self.__genre_name}")