import pygame as pg

from event.event_handlers import EventHandler


class EventManager:
	def __init__(self) -> None:
		self.handlers: list[EventHandler] = []

	def add_handler(self, handler: EventHandler) -> None:
		self.handlers.append(handler)

	def remove_handler(self, handler: EventHandler) -> None:
		self.handlers.remove(handler)

	def handle_event(self) -> None:
		for event in pg.event.get():
			for handler in self.handlers:
				handler.handle_event(event)
