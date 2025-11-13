# Guillermo Montiel
# 11-13-2025
# Lab #10 - chimpRefactor
# Refactored version of the pygame chimp example using an Entity base class.

import os
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, image_name, data_dir, colorkey=None, scale=1):
        super().__init__()
        fullname = os.path.join(data_dir, image_name)
        image = pygame.image.load(fullname)
        image = image.convert()

        if scale != 1:
            image = pygame.transform.scale_by(image, scale)

        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        self.image = image
        self.rect = image.get_rect()


def load_sound(name, data_dir):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except (pygame.error, FileNotFoundError):
        print(f"Warning: unable to load sound '{name}'")
        return NoneSound()
    return sound


class Fist(Entity):
    def __init__(self, image_name, data_dir, colorkey, scale, fist_offset):
        super().__init__(image_name, data_dir, colorkey, scale)
        self.fist_offset = fist_offset
        self.punching = False

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punching = False


class Chimp(Entity):
    def __init__(self, image_name, data_dir, colorkey, scale, start_pos, move_amount):
        super().__init__(image_name, data_dir, colorkey, scale)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = start_pos
        self.move = move_amount
        self.dizzy = False

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.dizzy += 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            self.image = pygame.transform.rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)

    if not pygame.font:
        print("Warning: fonts disabled")
    if not pygame.mixer:
        print("Warning: sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    font = pygame.Font(None, 64)
    text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
    textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    whiff_sound = load_sound("whiff.wav", data_dir)
    punch_sound = load_sound("punch.wav", data_dir)

    chimp = Chimp("chimp.png", data_dir, -1, 4, (10, 90), 18)
    fist = Fist("fist.png", data_dir, -1, 1, (-235, -80))

    all_sprites = pygame.sprite.Group(chimp, fist)
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()
                    chimp.punched()
                else:
                    whiff_sound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
