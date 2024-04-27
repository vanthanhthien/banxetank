import pygame
from sprites import *


class TankWar:

    def __init__(self):
        self.screen = pygame.display.set_mode(Settings.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None

    @staticmethod
    def __init_game():
        """
Khởi tạo một số cài đặt trò chơi
        :return:
        """
        pygame.init()   # Khởi tạo mô-đun pygame
        pygame.display.set_caption(Settings.GAME_NAME)  # Đặt tiêu đề cửa sổ
        pygame.mixer.init()    # Khởi tạo mô-đun âm thanh

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
        :return:
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
        """Kiểm tra sự kiện nhấn nút"""
        if event.key == pygame.K_LEFT:
            # Nhấn nút trái
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_RIGHT:
            # nhấn nút phải
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_UP:
            # nhân nút lên
            self.hero.direction = Settings.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_DOWN:
            # nhấn nút down
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_SPACE:
            # bắn đặn
            self.hero.shot()

    def __check_keyup(self, event):
        """Kiểm tra sự kiện nhả nút"""
        if event.key == pygame.K_LEFT:
            # Nhả nút trái
            self.hero.direction = Settings.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_RIGHT:
            # nhả nút phải
            self.hero.direction = Settings.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_UP:
            # nhả nút lên
            self.hero.direction = Settings.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_DOWN:
            # nhả nút xuống
            self.hero.direction = Settings.DOWN
            self.hero.is_moving = False

    def __event_handler(self):
        for event in pygame.event.get():
            # thoát game
            if event.type == pygame.QUIT:
                TankWar.__game_over()
            elif event.type == pygame.KEYDOWN:
                TankWar.__check_keydown(self, event)
            elif event.type == pygame.KEYUP:
                TankWar.__check_keyup(self, event)

    def __check_collide(self):
        # tan ko out khỏi màn hình
        self.hero.hit_wall()
        for enemy in self.enemies:
            enemy.hit_wall_turn()

        # đạn trúng tường
        for wall in self.walls:
            # đạn của tank vàng trúng tường
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Settings.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Settings.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Settings.IRON_WALL:
                        bullet.kill()
            # đạn tank xanh trúng tường
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

            # Xe tăng của chúng tôi đâm vào tường
            if pygame.sprite.collide_rect(self.hero, wall):
                # bức tường không thể xuyên thủng
                if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # Di chuyển ra khỏi bức tường
                    self.hero.move_out_wall(wall)

            # Xe tăng địch đâm vào tường
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Settings.RED_WALL or wall.type == Settings.IRON_WALL or wall.type == Settings.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        #Đạn trúng, va chạm xe tăng địch, va chạm xe tăng địch và bạn
        pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        # Đạn địch bắn trúng tank vàng
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

    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        while True and self.hero.is_alive and self.game_still:
            self.screen.fill(Settings.SCREEN_COLOR)
            # 1. Đặt tốc độ khung hình làm mới
            self.clock.tick(Settings.FPS)
            #2. Giám sát sự kiện
            self.__event_handler()
            #3. Giám sát va chạm
            self.__check_collide()
            # 4. Cập nhật/vẽ sprite/nhóm quản lý
            self.__update_sprites()
            # 5. Hiển thị cập nhật
            pygame.display.update()
        self.__game_over()

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
