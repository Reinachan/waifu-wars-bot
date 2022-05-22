import time
from dotenv import dotenv_values

from src.create_battle_image import create_battle_image  # type: ignore
from src.post import post  # type: ignore
from src.get_battle import get_current_battle  # type: ignore
from src.database import save_battle, has_posted_today  # type: ignore


# TODO: Write the psudeo-code into actual code that functions correctly

def main():
    # while True:
    #     if not has_posted_today():
    #         get_current_battle()
    #         create_battle_image()
    #         post()
    #         save_battle()

    #     time.sleep(60)
    return 1


main()
