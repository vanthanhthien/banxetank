import pygame
from sprites import *


class TankWar:
    NUM_CHANNELS = 2  # Đặt số kênh âm thanh

    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None
        self.failed_sound_played = False


    @staticmethod
    def __init_game():
        """
        Khởi tạo các cài đặt của trò chơi
        """
        pygame.init()   # Khởi tạo pygame
        pygame.display.set_caption(Settings.GAME_NAME)  # Đặt tiêu đề cửa sổ
        pygame.mixer.init()

        # Cài đặt âm lượng cho các kênh âm thanh
        for _ in range(TankWar.NUM_CHANNELS):
            pygame.mixer.Channel(_).set_volume(0.5)  # Sử dụng chỉ số kênh để tạo kênh mới

        # Phát nhạc nền
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(Settings.BACKGROUND_MUSIC))

    def __create_sprite(self):
        self.hero = Hero(Settings.HERO_IMAGE_NAME, self.screen)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for i in range(Settings.ENEMY_COUNT):
            direction = random.randint(0, 3)
            enemy = Enemy(Settings.ENEMY_IMAGES[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)
        self.__draw_map()

    def __draw_map(self):
        """
        Vẽ bản đồ
        """
        for y in range(len(Settings.MAP_ONE)):
            for x in range(len(Settings.MAP_ONE[y])):
                if Settings.MAP_ONE[y][x] == 0:
                    continue
                wall = Wall(Settings.WALLS[Settings.MAP_ONE[y][x]], self.screen)
                wall.rect.x = x*Settings.BOX_SIZE
                wall.rect.y = y*Settings.BOX_SIZE
                if Settings.MAP_ONE[y][x] == Settings.RED_WALL:
                    wall.type = Settings.RED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.IRON_WALL:
                    wall.type = Settings.IRON_WALL
                elif Settings.MAP_ONE[y][x] == Settings.WEED_WALL:
                    wall.type = Settings.WEED_WALL
                elif Settings.MAP_ONE[y][x] == Settings.BOSS_WALL:
                    wall.type = Settings.BOSS_WALL
                    wall.life = 1
                self.walls.add(wall)

    def __check_keydown(self, event):
        """Kiểm tra sự kiện khi nhấn phím"""
        if event.key == pygame.K_LEFT:
            # Nhấn phím mũi tên trái
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_RIGHT:
            # Nhấn phím mũi tên phải
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_UP:
            # Nhấn phím mũi tên lên
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_DOWN:
            # Nhấn phím mũi tên xuống
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_SPACE:
            # Bắn đạn
            self.hero.shot()

    def __check_keyup(self, event):
        """Kiểm tra sự kiện khi nhả phím"""
        if event.key == pygame.K_LEFT:
            # Nhả phím mũi tên trái
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_RIGHT:
            # Nhả phím mũi tên phải
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_UP:
            # Nhả phím mũi tên lên
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_DOWN:
            # Nhả phím mũi tên xuống
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False

    def __event_handler(self):
        for event in pygame.event.get():
            # Kiểm tra sự kiện thoát game
            if event.type == pygame.QUIT:
                TankWar.__game_over()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup(event)

    def __check_collide(self):
        # Đảm bảo xe tăng không di chuyển ra khỏi màn hình
        self.hero.hit_wall()
        for enemy in self.enemies:
            enemy.hit_wall_turn()

        # Đạn trúng tường
        for wall in self.walls:
            # Đạn của nhân vật chính trúng tường
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()
            # Đạn của kẻ địch trúng tường
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if pygame.sprite.collide_rect(wall, bullet):
                        if wall.type == Settings.RED_WALL:
                            wall.kill()
                            bullet.kill()
                        elif wall.type == Settings.BOSS_WALL:
                            self.game_still = False
                        elif wall.type == Settings.IRON_WALL:
                            bullet.kill()

            # Xe tăng chính của chúng ta va chạm vào tường
            if pygame.sprite.collide_rect(self.hero, wall):
                # Không thể xuyên qua tường
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # Di chuyển ra khỏi tường
                    self.hero.move_out_wall(wall)

            # Xe tăng của kẻ địch va chạm vào tường
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # Đạn trúng, xe tăng kẻ địch va chạm, va chạm giữa xe tăng của địch và của chúng ta
        pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        # Đạn của kẻ địch trúng vào chúng ta
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(bullet, self.hero):
                    bullet.kill()
                    self.hero.kill()

    def __update_sprites(self):
        if self.hero.is_moving:
            self.hero.update()
        self.walls.update()
        self.hero.bullets.update()
        self.enemies.update()
        for enemy in self.enemies:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)
        self.enemies.draw(self.screen)
        self.hero.bullets.draw(self.screen)
        self.screen.blit(self.hero.image, self.hero.rect)
        self.walls.draw(self.screen)

    def check_mission_completed(self):
        """
        Kiểm tra xem tất cả kẻ địch đã bị tiêu diệt chưa.
        Nếu đã tiêu diệt hết, hiển thị thông báo "Mission Completed" và thoát chương trình.
        """
        # Phát nhạc nền
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(Settings.COMPLETED_MUSIC))

        if len(self.enemies) == 0:
            font = pygame.font.Font('freesansbold.ttf', 60)
            text = font.render('MISSION COMPLETED', True, (0, 255, 0))
            text_rect = text.get_rect(center=(Settings.SCREEN_RECT.width // 2, Settings.SCREEN_RECT.height // 2))
            self.screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(5600)
            self.game_still = False



    def check_mission_failed(self):
        """
        Hiển thị thông báo "MISSION FAILED" khi trò chơi kết thúc với thất bại.
        """
        if not self.failed_sound_played:
            # Phát âm thanh failed nếu chưa phát
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Settings.FAILED_MUSIC))
            self.failed_sound_played = True

        # Hiển thị thông báo "MISSION FAILED"
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render('MISSION FAILED', True, (255, 0, 0))
        text_rect = text.get_rect(center=(Settings.SCREEN_RECT.width // 2, Settings.SCREEN_RECT.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(5300)

    def run_game(self):
        self.__init_game()
        self.__create_sprite()

        mission_completed = False  # Thêm biến cờ để đánh dấu nhiệm vụ đã hoàn thành

        while True and self.hero.is_alive and self.game_still:

            self.screen.fill(Settings.SCREEN_COLOR)
            # 1、Thiết lập tốc độ khung hình
            self.clock.tick(Settings.FPS)
            # 2、Xử lý sự kiện
            self.__event_handler()
            # 3、Kiểm tra va chạm
            self.__check_collide()
            # 4、Kiểm tra điều kiện hoàn thành nhiệm vụ
            if not mission_completed:
                self.check_mission_completed()
                if len(self.enemies) == 0:
                    mission_completed = True

            # 5、Cập nhật/vẽ các đối tượng/đối tượng quản lý
            self.__update_sprites()
            # 6、Cập nhật hiển thị
            pygame.display.update()

        if not mission_completed:
            self.check_mission_failed()

        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
