import pygame as pg
import sys

from event.event_handlers import EventHandler


class InputEventHandler(EventHandler):
	def handle_event(self, event: pg.event) -> None:
		self.__handle_quit_event(event)

	def __handle_quit_event(self, event: pg.event) -> None:
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
