class Human:

    HUMAN = -1
    piece = None
    first = False

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def set_first(self, first):
        self.first = first

    def is_first(self):
        return self.first
