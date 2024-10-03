# platform.py

class Platform:
    def __init__(self, platform_id, platform_name):
        self.__platform_id = platform_id  
        self.__platform_name = platform_name  

    @property
    def platform_id(self):
        return self.__platform_id

    @property
    def platform_name(self):
        return self.__platform_name

    def display_info(self):
        print(f"Платформа: {self.__platform_name}")
