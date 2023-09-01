import pygame as pg

from event.event_manager import EventManager
from event.handlers.input import InputEventHandler
from event.handlers.window import WindowEventHandler
from window.window_manager import WindowManager

if __name__ == '__main__':
	pg.init()

	window_manager = WindowManager(800, 600, 800, 600, 'Two Birds, One Stone!')

	event_manager = EventManager()
	event_manager.add_handler(InputEventHandler())
	event_manager.add_handler(WindowEventHandler(window_manager))

	while True:
		event_manager.handle_event()
		window_manager.update()
