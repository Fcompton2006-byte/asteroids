import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        # All of the data that you need to establish the player
        self.rotation = 0
        self.cooldown_timer = 0
        self.blast_timer = 0
        self.shotgun_timer = 0
        self.boost = 1
        
    def draw(self, screen: pygame.Surface) -> None:
        #Print the player to the screen
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def triangle(self) -> list[pygame.Vector2]:
        # Makes the player a triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt, boost=1):
        # Move along the axis your looking
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed = rotated_vector * PLAYER_SPEED * boost * dt
        self.position += rotated_with_speed


    def rotate(self, dt):
        # Rotate the player 
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt: float) -> None:
        # Adds controlls to the player
        keys = pygame.key.get_pressed()
        self.cooldown_timer -= dt
        self.blast_timer -= dt
        self.shotgun_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if keys[pygame.K_KP5]:
            self.blast()
        
        if keys[pygame.K_KP8]:
            self.shotgun()

        if keys[pygame.K_LSHIFT] and keys[pygame.K_w]:
            self.move(dt, 1.5)
            

    def shoot(self):
        if self.cooldown_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown_timer = PLAYER_SHOT_COOLDOWNN_SECONDS       
    
    

    def blast(self):
        if self.blast_timer > 0:
            return
        
        for i in range(0, 18):
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(20 * (i + 1)) * PLAYER_SHOOT_SPEED
        
        self.blast_timer = PLAYER_SHOT_COOLDOWNN_SECONDS * 10

    def shotgun(self):
        if self.shotgun_timer > 0:
            return
        shotgun_radius = self.rotation - 60
        for i in range(0, 5):
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(shotgun_radius + ((i + 1) * 20)) * PLAYER_SHOOT_SPEED
        self.shotgun_timer = PLAYER_SHOT_COOLDOWNN_SECONDS * 5
