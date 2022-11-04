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
		pygame.display.set_caption('')
		self.clock = pygame.time.Clock()

		self.BG = pygame.image.load("../graphics/main-menu/Background.png")

		self.score = 0

		# sound 
		self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
		self.main_sound.set_volume(0.5)
		self.main_sound.play(loops = -1)
		self.isSoundPlayed= True
		self.enableCoinSound= True
		self.enablePlayerSound= True

	def get_font(self, size): # Returns Press-Start-2P in the desired size
		return pygame.font.Font("../graphics/font/joystix.ttf", size)
	
	def play(self):
		self.level = Level(self.enableCoinSound, self.enablePlayerSound)
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
			elif game_score[0] == "Winning":
				self.score = game_score[1]
				self.wining()
			pygame.display.update()
			self.clock.tick(FPS)

	def options(self):
		self.screen.blit(self.BG, (0, 0))
     
		while True:
			
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

			OPTIONS_TEXT = self.get_font(45).render("BACK GROUND MUSIC SOUND: ", True, 'White')
			OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(540, 260))
			self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

			OPTIONS_BACK = Button(image=None, pos=(640, 600), 
								text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")
			bgsoundImg= pygame.transform.scale(pygame.image.load("../graphics/soundIcon/sound_icon.png"), (150, 150)) if self.isSoundPlayed else pygame.transform.scale(pygame.image.load("../graphics/soundIcon/noSound_icon.png"), (150, 150))
			gsoundImg= pygame.transform.scale(pygame.image.load("../graphics/soundIcon/sound_icon.png"), (150, 150)) if self.enableCoinSound else pygame.transform.scale(pygame.image.load("../graphics/soundIcon/noSound_icon.png"), (150, 150))
			BGSOUND_BACK = Button(image=bgsoundImg, pos=(1050, 260), 
				text_input="", font=self.get_font(75), base_color="White", hovering_color="Green")
			GAMESOUND_TEXT = self.get_font(45).render("GAME MUSIC SOUND: ", True, 'White')
			GAMESOUND_RECT = OPTIONS_TEXT.get_rect(center=(540, 460))
			self.screen.blit(GAMESOUND_TEXT, GAMESOUND_RECT)
			GAMESOUNDBTN= Button(image=gsoundImg, pos=(780, 460), 
				text_input="", font=self.get_font(75), base_color="White", hovering_color="Green")

			OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
			BGSOUND_BACK.changeColor(OPTIONS_MOUSE_POS)
			GAMESOUNDBTN.changeColor(OPTIONS_MOUSE_POS)
			OPTIONS_BACK.update(self.screen)
			BGSOUND_BACK.update(self.screen)
			GAMESOUNDBTN.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
						self.main_menu()
				if BGSOUND_BACK.checkForInput(OPTIONS_MOUSE_POS) and event.type == pygame.MOUSEBUTTONUP:
					if self.isSoundPlayed:
						self.main_sound.set_volume(0)
						self.isSoundPlayed= False
					else:
						self.main_sound.set_volume(0.5)
						self.isSoundPlayed = True
				if GAMESOUNDBTN.checkForInput(OPTIONS_MOUSE_POS) and event.type == pygame.MOUSEBUTTONUP:
					if self.enableCoinSound:
						self.enableCoinSound= False
						self.enablePlayerSound= False
					else:
						self.enableCoinSound= True
						self.enablePlayerSound= True

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
			DucImg= pygame.transform.scale(pygame.image.load("../graphics/ava/Duc.png"), (120, 120))
			DucText = self.get_font(45).render("HOÀNG KIM ANH ĐỨC - 1811958", True, "Black")
			DucRect = ABOUT_TEXT.get_rect(center=(400, 630))

			self.screen.blit(HieuImg,(20, 100))
			self.screen.blit(HieuText, HieuRect)
			self.screen.blit(CuongImg,(20, 250))
			self.screen.blit(CuongText, CuongRect)
			self.screen.blit(ToanImg,(20, 400))
			self.screen.blit(ToanText, ToanRect)
			self.screen.blit(DucImg,(20, 550))
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
		gobg= pygame.transform.scale(pygame.image.load("../graphics/background/gobg_1.png"), (1280, 720))
		while True:
			self.screen.blit(gobg, (0,0))
			GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

			GAME_OVER_TEXT = self.get_font(150).render("GAME OVER", True, "Red")
			HIGH_SCORE_TEXT = self.get_font(60).render("YOUR SCORE IS " + str(self.score), True, "Yellow")

			GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 210))
			HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(640, 360))

			self.screen.blit(GAME_OVER_TEXT, GAME_OVER_RECT)
			self.screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)

			GAME_OVER_BACK = Button(image=None, pos=(640, 560), 
								text_input="BACK TO MENU", font=self.get_font(40), base_color="White", hovering_color="Red")

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
   
	def wining(self):
		gobg= pygame.transform.scale(pygame.image.load("../graphics/background/gobg_1.png"), (1280, 720))
		while True:
			self.screen.blit(gobg, (0,0))
			GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

			GAME_OVER_TEXT = self.get_font(70).render("CONGRATULATION", True, "Red")
			HIGH_SCORE_TEXT = self.get_font(60).render("YOUR SCORE IS " + str(self.score), True, "Yellow")

			GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 210))
			HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(640, 360))

			self.screen.blit(GAME_OVER_TEXT, GAME_OVER_RECT)
			self.screen.blit(HIGH_SCORE_TEXT, HIGH_SCORE_RECT)

			PLAY_AGAIN_BTN= Button(image=None, pos=(640, 460), 
								text_input="PLAY AGAIN ?", font=self.get_font(40), base_color="White", hovering_color="Red")
			BTN_BACK = Button(image=None, pos=(640, 560), 
								text_input="BACK TO MENU", font=self.get_font(40), base_color="White", hovering_color="Red")

			BTN_BACK.changeColor(GAME_OVER_MOUSE_POS)
			BTN_BACK.update(self.screen)
			PLAY_AGAIN_BTN.changeColor(GAME_OVER_MOUSE_POS)
			PLAY_AGAIN_BTN.update(self.screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if BTN_BACK.checkForInput(GAME_OVER_MOUSE_POS):
						self.main_menu()
					if PLAY_AGAIN_BTN.checkForInput(GAME_OVER_MOUSE_POS):
						self.play()

			pygame.display.update()

	def main_menu(self):
		bg= pygame.image.load("../graphics/background/bg.jpg")
		while True:
			self.screen.blit(bg, (0, 0))

			MENU_MOUSE_POS = pygame.mouse.get_pos()

			MENU_TEXT = self.get_font(100).render("HOME", True, "#b68f40")
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