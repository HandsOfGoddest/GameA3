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
		self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
		self.main_sound.set_volume(0.5)
		self.main_sound.play(loops = -1)
		self.isSoundPlayed= True

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
		self.screen.blit(self.BG, (0, 0))
     
		while True:
			
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

			OPTIONS_TEXT = self.get_font(45).render("SOUND: ", True, 'White')
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(540, 260))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			OPTIONS_BACK = Button(image=None, pos=(640, 460), 
								text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")
			soundImg= pygame.transform.scale(pygame.image.load("../graphics/soundIcon/sound_icon.png"), (150, 150)) if self.isSoundPlayed else pygame.transform.scale(pygame.image.load("../graphics/soundIcon/noSound_icon.png"), (150, 150))
			SOUND_BACK = Button(image=soundImg, pos=(740, 260), 
				text_input="", font=self.get_font(75), base_color="White", hovering_color="Green")


			OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
			SOUND_BACK.changeColor(OPTIONS_MOUSE_POS)
			OPTIONS_BACK.update(self.screen)
			SOUND_BACK.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
						self.main_menu()
				if SOUND_BACK.checkForInput(OPTIONS_MOUSE_POS) and event.type == pygame.MOUSEBUTTONUP:
					if self.isSoundPlayed:
						self.main_sound.set_volume(0)
						self.isSoundPlayed= False
					else:
						self.main_sound.set_volume(0.5)
						self.isSoundPlayed = True

			pygame.display.update()
			self.screen.blit(self.BG, [0,0])
   
	def about(self):
     
		while True:
			ABOUT_MOUSE_POS = pygame.mouse.get_pos()
			
			self.screen.fill("white")

			ABOUT_TEXT = self.get_font(45).render("ABOUT US", True, "Black")
			ABOUT_RECT = ABOUT_TEXT.get_rect(center=(200, 50))
			self.screen.blit(ABOUT_TEXT, ABOUT_RECT)

			HieuImg= pygame.transform.scale(pygame.image.load("../graphics/ava/Hieu.png"), (150, 150))
			HieuText = self.get_font(45).render("NGUYỄN ĐÌNH HIẾU - 1913341", True, "Black")
			HieuRect = ABOUT_TEXT.get_rect(center=(400, 180))
			CuongImg= pygame.transform.scale(pygame.image.load("../graphics/ava/Cuong.png"), (150, 150))
			CuongText = self.get_font(45).render("ĐẶNG HÙNG CƯỜNG - 1912817", True, "Black")
			CuongRect = ABOUT_TEXT.get_rect(center=(400, 330))
			ToanImg= pygame.transform.scale(pygame.image.load("../graphics/ava/Toan.png"), (150, 150))
			ToanText = self.get_font(45).render("VÕ MINH TOÀN - 1915570", True, "Black")
			ToanRect = ABOUT_TEXT.get_rect(center=(400, 480))
			DucText = self.get_font(45).render("HOÀNG KIM ANH ĐỨC - 1811958", True, "Black")
			DucRect = ABOUT_TEXT.get_rect(center=(400, 630))

			self.screen.blit(HieuImg,(20, 100))
			self.screen.blit(HieuText, HieuRect)
			self.screen.blit(CuongImg,(20, 250))
			self.screen.blit(CuongText, CuongRect)
			self.screen.blit(ToanImg,(20, 400))
			self.screen.blit(ToanText, ToanRect)
			self.screen.blit(ToanImg,(20, 550))
			self.screen.blit(DucText, DucRect)

   

			ABOUT_BACK = Button(image=None, pos=(1100, 50), 
								text_input="BACK", font=self.get_font(50), base_color="Black", hovering_color="Green")

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
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 50))

			PLAY_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 180), 
								text_input="NEW GAME", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			OPTIONS_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 330), 
								text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			ABOUT_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Options Rect.png"), pos=(640, 480), 
								text_input="ABOUT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
			QUIT_BUTTON = Button(image=pygame.image.load("../graphics/main-menu/Quit Rect.png"), pos=(640, 630), 
								text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

			self.screen.blit(MENU_TEXT, MENU_RECT)

			for button in [PLAY_BUTTON, OPTIONS_BUTTON, ABOUT_BUTTON, QUIT_BUTTON]:
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
					if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
						self.about()
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			pygame.display.update()


if __name__ == '__main__':
	game = Game()
	game.main_menu()