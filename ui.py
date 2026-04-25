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

class Slider:
    def __init__(self,x,y,w,h,val=0.5):
        self.rect = pygame.Rect(x,y,w,h)
        self.circle_x = x +int(w + val)
        self.val = val
        self.dragging = False

    def draw(self,surfase):
        pygame.draw.line(surfase,(0,0,0),
                         (self.rect.x,self.rect.centery),
                         (self.rect.right,self.rect.centery),4)
        pygame.draw.circle(surfase,(100,149,237),(self.circle_x,self.rect.centery),10)

    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and (
                (event.pos[0] - self.circle_x) ** 2 + (
                event.pos[1] - self.rect.centery) ** 2
        ) ** 0.5 < 15:
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if self.dragging and event.type == pygame.MOUSEMOTION:
            self.circle_x = max(self.rect.left,
                                min(event.pos[0],self.rect.right))
            self.val = (self.circle_x - self.rect.x
                        ) / self.rect.width

            return True
        return False