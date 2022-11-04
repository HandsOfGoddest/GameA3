import pygame, sys
from settings import *
from button import Button
from level import Level
from player import Player

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.BG = pygame.image.load("../graphics/main-menu/Background.png")

		self.score = 0

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def get_font(self, size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("../graphics/font/joystix.ttf", size)
	
	def play(self):
		self.level = Level()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			game_score = self.level.run()
			if game_score[0] == "Over":
				self.score = game_score[1]
				self.game_over()
			pygame.display.update()
			self.clock.tick(FPS)

	def options(self):
		while True:
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
			
			self.screen.fill("white")

			OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			OPTIONS_BACK = Button(image=None, pos=(640, 460), 
								text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

			OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
			OPTIONS_BACK.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
						self.main_menu()

			pygame.display.update()
   
	def about(self):
		while True:
			ABOUT_MOUSE_POS = pygame.mouse.get_pos()
			
			self.screen.fill("white")

			ABOUT_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
			ABOUT_RECT = ABOUT_TEXT.get_rect(center=(640, 260))
			self.screen.blit(ABOUT_TEXT, ABOUT_RECT)

			ABOUT_BACK = Button(image=None, pos=(640, 460), 
								text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

			ABOUT_BACK.changeColor(ABOUT_MOUSE_POS)
			ABOUT_BACK.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
						self.main_menu()

			pygame.display.update()

	def game_over(self):
		while True:
			GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()
			
			self.screen.fill("white")

			GAME_OVER_TEXT = self.get_font(100).render("Game Over !!!", True, "Black")
			HIGH_SCORE_TEXT = self.get_font(45).render("Your score is " + str(self.score), True, "Black")

			GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 160))
			HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(640, 260))

			self.screen.blit(GAME_OVER_TEXT, GAME_OVER_RECT)
			self.screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)

			GAME_OVER_BACK = Button(image=None, pos=(640, 660), 
								text_input="BACK TO MAIN MENU", font=self.get_font(30), base_color="Black", hovering_color="Green")

			GAME_OVER_BACK.changeColor(GAME_OVER_MOUSE_POS)
			GAME_OVER_BACK.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if GAME_OVER_BACK.checkForInput(GAME_OVER_MOUSE_POS):
						self.main_menu()

			pygame.display.update()

	def main_menu(self):
		while True:
			self.screen.blit(self.BG, (0, 0))

			MENU_MOUSE_POS = pygame.mouse.get_pos()

			MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

			PLAY_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 250), 
								text_input="NEW GAME", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			OPTIONS_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 400), 
								text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			ABOUT_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 400), 
								text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			QUIT_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Quit Rect.png"), pos=(640, 550), 
								text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

			self.screen.blit(MENU_TEXT, MENU_RECT)

			for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
				button.changeColor(MENU_MOUSE_POS)
				button.update(self.screen)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.play()
					if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.options()
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.main_menu()