class Game:
    def __init__(self, game_id, title, genre, platform, release_date, primary_price, publisher, discount_id):
        self.__game_id = game_id
        self.__title = title
        self.__genre = genre 
        self.__platform = platform 
        self.__release_date = release_date
        self.__primary_price = primary_price
        self.__publisher = publisher  
        self.__discount_id = discount_id

    # Гетери для доступу до приватних властивостей
    @property
    def game_id(self):
        return self.__game_id

    @property
    def title(self):
        return self.__title

    @property
    def genre(self):
        return self.__genre

    @property
    def platform(self):
        return self.__platform

    @property
    def release_date(self):
        return self.__release_date

    @property
    def primary_price(self):
        return self.__primary_price

    @property
    def publisher(self):
        return self.__publisher

    @property
    def discount_id(self):
        return self.__discount_id

    # Метод для оновлення ціни
    def update_price(self, new_price):
        if new_price > 0:
            self.__primary_price = new_price
        else:
            print("Ціна має бути більше нуля.")

    def display_info(self):
        print(f"Гра: {self.__title}")
        print(f"Жанр: {self.__genre.genre_name}")  
        print(f"Платформа: {self.__platform.platform_name}") 
        print(f"Ціна: {self.__primary_price}")
        print(f"Видавець: {self.__publisher.publisher_name}") 

    @staticmethod
    def convert_price(price, rate):
        return price * rate

class DigitalGame(Game):
    def __init__(self, game_id, title, genre_id, platform_id, release_date, primary_price, publisher_id, discount_id, download_size):
        super().__init__(game_id, title, genre_id, platform_id, release_date, primary_price, publisher_id, discount_id)
        self.__download_size = download_size  

    @property
    def download_size(self):
        return self.__download_size

    def display_info(self):
        super().display_info()
        print(f"Розмір завантаження: {self.__download_size} ГБ")


class PhysicalProduct:
    def __init__(self, weight, dimensions):
        self.__weight = weight  
        self.__dimensions = dimensions  

    @property
    def weight(self):
        return self.__weight

    @property
    def dimensions(self):
        return self.__dimensions

    def display_shipping_info(self):
        print(f"Вага: {self.__weight} кг, Розміри: {self.__dimensions}")


class PhysicalGame(Game, PhysicalProduct):
    def __init__(self, game_id, title, genre_id, platform_id, release_date, primary_price, publisher_id, discount_id, weight, dimensions):
        Game.__init__(self, game_id, title, genre_id, platform_id, release_date, primary_price, publisher_id, discount_id)
        PhysicalProduct.__init__(self, weight, dimensions)

    def display_info(self):
        super().display_info()
        self.display_shipping_info()

