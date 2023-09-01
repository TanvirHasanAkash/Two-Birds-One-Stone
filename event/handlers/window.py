import pygame as pg
import sys

from event.event_handlers import EventHandler
from window.window_manager import WindowManager


class WindowEventHandler(EventHandler):
    def __init__(self, window: WindowManager) -> None:
        self.window = window

    def handle_event(self, event: pg.event) -> None:
        self.__handle_resize_event(event)

    def __handle_resize_event(self, event: pg.event) -> None:
        if event.type == pg.VIDEORESIZE:
            if event.w < self.window.min_width:
                event.w = self.window.min_width
            if event.h < self.window.min_height:
                event.h = self.window.min_height

            # Uncomment to check for maximum width or height
            # if self.window.max_width is not None and event.w > self.window.max_width:
            #     event.w = self.window.max_width
            # if self.window.max_height is not None and event.h > self.window.max_height:
            #     event.h = self.window.max_height

            self.window.width, self.window.height = event.w, event.h
            self.window.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
