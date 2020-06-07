import pygame

class State:
    def __init__(self):
        self.done     = False # состояние завершилось
        self.next     = None  # следубщее состояние
        self.prev     = None  # предудущее состояние

    # запускается при создании
    def on_create(self):
        pass

    # запускается @fps раз в секунду для обновления
    def on_update(self, keys):
        pass

    # запускается для отлова ивентов
    def get_event(self, event):
        pass

    # задаем соседние состояния
    def set_prenex(self, pre, nex):
        self.next = nex;
        self.prev = pre;
