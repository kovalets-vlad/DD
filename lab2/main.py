from plat import Platform
from genre import Genre
from publisher import Publisher
import game as Game

def main():
    platform_pc = Platform(1, "PC")
    platform_ps5 = Platform(2, "PlayStation 5")
    genre_action = Genre(101, "Action")
    genre_rpg = Genre(102, "RPG")
    publisher_ubisoft = Publisher(201, "Ubisoft")
    publisher_ea = Publisher(202, "Electronic Arts")


    digital_game = Game.DigitalGame(1, "Cyber Adventure", genre_action, platform_pc, "2023-05-20", 59.99, publisher_ubisoft, 301, 70)
    physical_game = Game.PhysicalGame(2, "Fantasy World", genre_rpg, platform_ps5, "2022-11-15", 79.99, publisher_ea, 302, 0.1, "70/40")

    print("Digital Game Information:")
    digital_game.display_info()

    print("\nPhysical Game Information:")
    physical_game.display_info()

    digital_game.update_price(1000)

    print(f"New price for digital game = {digital_game.primary_price}")

    convert_price = Game.Game.convert_price(digital_game.primary_price, 42)

    print(f"Price conversion in hryvnias {convert_price}")

if __name__ == "__main__":
    main()
