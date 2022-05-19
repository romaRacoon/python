class main:
    def __init__(self):
        self.condition = 'A'

    def cut(self):
        if self.condition == 'A':
            self.condition = 'A'
            return 2
        elif self.condition == 'C':
            self.condition = 'D'
            return 5
        elif self.condition == 'D':
            self.condition = 'F'
            return 7
        else:
            raise KeyError

    def zoom(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 4
        elif self.condition == 'D':
            self.condition = 'E'
            return 6
        else:
            raise KeyError

    def type(self):
        if self.condition == 'A':
            self.condition = 'D'
            return 1
        elif self.condition == 'E':
            self.condition = 'F'
            return 8
        else:
            raise KeyError

    def log(self):
        if self.condition == 'A':
            self.condition = 'F'
            return 3
        else:
            raise KeyError
