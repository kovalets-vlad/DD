class Publisher:
    def __init__(self, publisher_id, publisher_name):
        self.__publisher_id = publisher_id  
        self.__publisher_name = publisher_name 

    @property
    def publisher_id(self):
        return self.__publisher_id

    @property
    def publisher_name(self):
        return self.__publisher_name

    def display_info(self):
        print(f"Видавець: {self.__publisher_name}")