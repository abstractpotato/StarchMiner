import pygame
from modules.ui.images import get_font
from modules.ui.images import get_green_button, get_gray_button, get_red_button

class Window:

    def __init__(self, config):
        self.size = (8 * 80, 16 * 25)
        if config:
            size = (config["width"] * 8, config["height"] * 16)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("StarchMiner")
        self.elements = []
        self.processes = []

        self.button = get_gray_button()
        self.green_button = get_green_button()
        self.red_button = get_red_button()
        self.font = get_font()

        pygame.mouse.set_visible(False)
        self.running = True

    def add_element(self, button):
        self.elements.append(button)

    def add_process(self, process):
        self.processes.append(process)

    def clear(self):
        self.elements = []

    def draw(self):
        self.screen.fill((255, 255, 255))

        # draw elements
        for element in self.elements:
            element.draw(self)

        # draw mouse
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(self.screen, "black", mouse_pos, 2)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for process in self.processes:
                process(event)
            for element in self.elements:
                element.click(event)

    def run(self):
        while self.running:
            self.draw()
            self.events()
        pygame.quit()

class Text:
    def __init__(self, text, position):
        self.text = text.upper()
        self.position = position

    def draw(self, window):
        for i in range(len(self.text)):
            char = window.font[self.text[i]]
            x = self.position[0] + (i * 8)
            y = self.position[1]
            window.screen.blit(char, (x, y))

    def click(self, event):
        pass

class Button:

    def __init__(self, text, position, func, color="grey"):
        text_position = (position[0] + 8, position[1] + 16)
        self.text = text
        self.position = position
        self.func = func
        self.color = color
        self.hidden = False

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = True

    def draw(self, window):
        if self.hidden:
            return

        width = len(self.text)
        x = self.position[0]
        y = self.position[1]

        button = window.button
        if self.color == "red":
            button = window.red_button
        if self.color == "green":
            button = window.green_button

        ax = x + ((width + 1) * 8)
        self.box = (x + 5, y + 13, ((width + 1) * 8) - 1, y - 9)
        # rect = pygame.draw.rect(window.screen, "red", self.box)

        window.screen.blit(button["top_left"], (x, y))
        window.screen.blit(button["top_right"], (ax, y))
        window.screen.blit(button["center_left"], (x, y + 16))
        window.screen.blit(button["center_right"], (ax, y + 16))
        window.screen.blit(button["bottom_left"], (x, y + 32))
        window.screen.blit(button["bottom_right"], (ax, y + 32))

        for i in range(width):
            window.screen.blit(button["top"], (x + (8 * (i + 1)), y))
            window.screen.blit(button["center"], (x + (8 * (i + 1)), y + 16))
            window.screen.blit(button["bottom"], (x + (8 * (i + 1)), y + 32))

        text_position = (x + 8, y + 16)
        text_obj = Text(self.text, text_position)
        text_obj.draw(window)

    def click(self, event):
        if self.hidden:
            return
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        x, y = pygame.mouse.get_pos()
        xin = x > self.box[0] and x < self.box[2] + self.box[0]
        yin = y > self.box[1] and y < self.box[3] + self.box[1]

        if not xin and not yin:
            return

        self.func(self, event)
