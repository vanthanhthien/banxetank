import os
from pygame import Rect

class Settings:

    # Cài đặt trò chơi
    FPS = 60    # Tần số khung hình của trò chơi
    GAME_NAME = "Đại chiến xe tăng"  # Tiêu đề của trò chơi
    BOX_SIZE = 50   # Kích thước của một ô trên màn hình
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)   # Hình chữ nhật của một ô trên màn hình
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 19, BOX_SIZE * 13)  # Hình chữ nhật của màn hình
    SCREEN_COLOR = (0, 0, 0)    # Màu nền của màn hình

    # Biến chung
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    # Bản đồ
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

    # Âm thanh
    BOOM_MUSIC = "resources/musics/boom.wav"
    FIRE_MUSIC = "resources/musics/fire.wav"
    HIT_MUSIC = "resources/musics/hit.wav"

    # Loại xe tăng
    HERO = 0
    ENEMY = 1

    # Xe tăng của mình
    HERO_IMAGE_NAME = "./resources/images/hero/hero1U.gif"
    HERO_IMAGES = {
        LEFT: "./resources/images/hero/hero1L.gif",
        RIGHT: "./resources/images/hero/hero1R.gif",
        UP: "./resources/images/hero/hero1U.gif",
        DOWN: "./resources/images/hero/hero1D.gif"
    }
    HERO_SPEED = 2
    BOSS_IMAGE = "./resources/images/5.png"

    # Xe tăng địch
    ENEMY_IMAGES = {
        LEFT: "./resources/images/enemy/enemy2L.gif",
        RIGHT: "./resources/images/enemy/enemy2R.gif",
        UP: "./resources/images/enemy/enemy2U.gif",
        DOWN: "./resources/images/enemy/enemy2D.gif"
    }
    ENEMY_COUNT = 5
    ENEMY_SPEED = 1

    # Đạn
    BULLET_IMAGE_NAME = "./resources/images/bullet/bullet.png"
    BULLET_RECT = Rect(0, 0, 5, 5)
    BULLET_SPEED = 5

    # 0 đại diện cho ô trống, 1 đại diện cho tường đỏ, 2 đại diện cho tường sắt, 3 đại diện cho cỏ, 4 đại diện cho biển, 5 đại diện cho chim
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    BOSS_WALL = 5
    WALLS = [
        f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls/")
    ]

    # Hình ảnh nổ
    BOOMS = [
        "resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]
