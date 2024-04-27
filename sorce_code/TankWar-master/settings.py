import os
from pygame import Rect


class Settings:

    # cài đặt trò chơi
    FPS = 60    # tốc độ khung hình trò chơi
    GAME_NAME = "bắn xe tank"  # tựa đề trò chơi
    BOX_SIZE = 50   #Kích thước màn hình đơn vị 
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)   # box size
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 19, BOX_SIZE * 13)  # màn hình
    SCREEN_COLOR = (0, 0, 0)    # màu screen

    # Biến phổ quát
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    # bản đồ
    MAP_ONE = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
        [0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    # âm thanh
    BOOM_MUSIC = "resources/musics/boom.wav"
    FIRE_MUSIC = "resources/musics/fire.wav"
    HIT_MUSIC = "resources/musics/hit.wav"

    # Loại xe tăng
    HERO = 0
    ENEMY = 9

    # xe tank màu vàng
    HERO_IMAGE_NAME = "./resources/images/hero/hero1U.png"
    HERO_IMAGES = {
        LEFT: "./resources/images/hero/hero1L.png",
        RIGHT: "./resources/images/hero/hero1R.png",
        UP: "./resources/images/hero/hero1U.png",
        DOWN: "./resources/images/hero/hero1D.png"
    }
    HERO_SPEED = 2
    BOSS_IMAGE = "./resources/images/5.png"
    # 

    # xr tank xanh
    ENEMY_IMAGES = {
        LEFT: "./resources/images/enemy/enemy2L.gif",
        RIGHT: "./resources/images/enemy/enemy2R.gif",
        UP: "./resources/images/enemy/enemy2U.gif",
        DOWN: "./resources/images/enemy/enemy2D.gif"
    }
    ENEMY_COUNT = 5
    ENEMY_SPEED = 1

    # bullet
    BULLET_IMAGE_NAME = "./resources/images/bullet/bullet.png"
    BULLET_RECT = Rect(0, 0, 5, 5)
    BULLET_SPEED = 5

    #0 nghĩa là trống, 1 nghĩa là tường đỏ, 2 nghĩa là tường sắt, 3 nghĩa là cỏ, 4 nghĩa là biển và 5 nghĩa là .
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    BOSS_WALL = 5
    WALLS = [
        f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls/")
    ]

    # hình ảnh vụ nổ
    BOOMS = [
        "resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]
