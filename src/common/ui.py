class Menu:
    def __init__(self, display, items):
        self.display = display
        self.items = items
        self.index = 0

    def draw(self):
        self.display.fill(0)
        self.display.text("--- PICO TERMINAL ---", 0, 0)
        for i, item in enumerate(self.items):
            prefix = "> " if i == self.index else "  "
            self.display.text(prefix + item, 0, 15 + (i * 10))
        self.display.show()

    def move_down(self):
        self.index = (self.index + 1) % len(self.items)
        self.draw()

    def move_up(self):
        self.index = (self.index - 1) % len(self.items)
        self.draw()
