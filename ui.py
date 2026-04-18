import pygame

class Button:
    def __init__(self,x,y,width,height,sound_path,color=(255,255,255)):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.original_color = color
        self.sound = pygame.mixer.Sound(sound_path)

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self.rect,border_radius=15)
        pygame.draw.rect(surface,(0,0,0),self.rect,2,border_radius=15)

    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.sound.play()
            self.color = (220,220,220)
            return True

        if event.type == pygame.MOUSEBUTTONUP:
            self.color = self.original_color

        return False