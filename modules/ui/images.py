import pygame

def get_font_image(sheet, width, height, frame=0, scale=1, color=(0, 0, 0)):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

def get_font(scale=1):
    spritesheet = pygame.image.load("src/font.png").convert_alpha()
    availible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.;:"=[]_+-*/>$ '
    font = {}
    for x in range(len(availible)):
        image = get_font_image(spritesheet, 8, 16, x, scale)
        font[availible[x]] = image
    return font

def get_button_image(sheet, width, height, x, y, scale=1, color=(0, 0, 0)):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (width * x, height * y, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

def get_button(spritesheet):

    button = {}
    button["top_left"] = get_button_image(spritesheet, 8, 16, 0, 0)
    button["top"] = get_button_image(spritesheet, 8, 16, 1, 0)
    button["top_right"] = get_button_image(spritesheet, 8, 16, 2, 0)

    button["center_left"] = get_button_image(spritesheet, 8, 16, 0, 1)
    button["center"] = get_button_image(spritesheet, 8, 16, 1, 1)
    button["center_right"] = get_button_image(spritesheet, 8, 16, 2, 1)

    button["bottom_left"] = get_button_image(spritesheet, 8, 16, 0, 2)
    button["bottom"] = get_button_image(spritesheet, 8, 16, 1, 2)
    button["bottom_right"] = get_button_image(spritesheet, 8, 16, 2, 2)
    return button

def get_gray_button():
    spritesheet = pygame.image.load("src/gray_button.png").convert_alpha()
    return get_button(spritesheet)

def get_green_button():
    spritesheet = pygame.image.load("src/green_button.png").convert_alpha()
    return get_button(spritesheet)

def get_red_button():
    spritesheet = pygame.image.load("src/red_button.png").convert_alpha()
    return get_button(spritesheet)
