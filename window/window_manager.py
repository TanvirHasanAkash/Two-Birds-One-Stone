import pygame as pg


class WindowManager:
	def __init__(self, width: int, height: int, min_width: int, min_height: int, title: str) -> None:
		pg.init()
		self.width = width
		self.height = height

		self.min_width = min_width
		self.min_height = min_height

		self.title = title

		self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
		pg.display.set_caption(self.title)

	def update(self) -> None:
		pg.display.update()
