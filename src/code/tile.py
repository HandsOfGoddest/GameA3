import pygame 
from settings import *
from support import import_folder

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		if sprite_type != 'coin':
			y_offset = HITBOX_OFFSET[sprite_type]
		self.image = surface[0] if isinstance(surface, list) else surface
		if sprite_type == 'object':
			self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
		else:
			self.rect = self.image.get_rect(topleft = pos)
		if sprite_type != 'coin':
			self.hitbox = self.rect.inflate(0,y_offset)

class Coin(Tile):
	def __init__(self,pos,groups,sprite_type,surface):
		super().__init__(pos,groups,sprite_type,surface)
		self.frames = surface
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		center_x = pos[0] + int(TILESIZE / 2)
		center_y = pos[1] + int(TILESIZE / 2)
		self.rect = self.image.get_rect(center = (center_x,center_y))
	
	def animate(self):
		self.frame_index += 0.05
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self):
		self.animate()