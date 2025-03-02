import pygame
import sys
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Draw by github/Balivan-src")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Настройки кисти
brush_color = BLACK
brush_size = 5
drawing = False

# Функция для отрисовки текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Основной цикл игры
def main():
    global brush_color, brush_size, drawing

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    # Создаем поверхность для рисования
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(WHITE)

    while True:
        screen.fill(WHITE)
        screen.blit(canvas, (0, 0))

        # Отрисовка интерфейса
        draw_text("ЛКМ: Рисовать | ПКМ: Ластик | C: Очистить | S: Сохранить | Q: Выйти", font, BLACK, screen, 10, 10)
        draw_text("Цвета: 1-Чёрный, 2-Красный, 3-Зелёный, 4-Синий, 5-Жёлтый, 6-Фиолетовый, 7-Оранжевый, 8-Голубой", font, BLACK, screen, 10, 50)
        draw_text(f"Текущий цвет: {brush_color} | Размер кисти: {brush_size}", font, BLACK, screen, 10, 90)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатий клавиш
            if event.type == KEYDOWN:
                if event.key == K_c:  # Очистить экран
                    canvas.fill(WHITE)
                if event.key == K_s:  # Сохранить рисунок
                    pygame.image.save(canvas, "drawing.png")
                    print("Рисунок сохранен как drawing.png")
                if event.key == K_q:  # Выйти
                    pygame.quit()
                    sys.exit()

                # Выбор цвета
                if event.key == K_1:  # Чёрный
                    brush_color = BLACK
                if event.key == K_2:  # Красный
                    brush_color = RED
                if event.key == K_3:  # Зелёный
                    brush_color = GREEN
                if event.key == K_4:  # Синий
                    brush_color = BLUE
                if event.key == K_5:  # Жёлтый
                    brush_color = YELLOW
                if event.key == K_6:  # Фиолетовый
                    brush_color = PURPLE
                if event.key == K_7:  # Оранжевый
                    brush_color = ORANGE
                if event.key == K_8:  # Голубой
                    brush_color = CYAN

            # Обработка нажатий мыши
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    drawing = True
                if event.button == 3:  # ПКМ
                    drawing = True
                    brush_color = WHITE  # Ластик

            if event.type == MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    drawing = False

            # Обработка движения мыши
            if event.type == MOUSEMOTION and drawing:
                mouse_pos = pygame.mouse.get_pos()
                pygame.draw.circle(canvas, brush_color, mouse_pos, brush_size)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()