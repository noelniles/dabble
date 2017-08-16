class Packet:
    def __init__(self, data, T):
        self.data = data
        self.type = T
        self.size = self.getSize()

