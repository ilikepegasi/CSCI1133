class Lake:
    def __init__(self, name, area, depth):
        self.name = name
        self.area = area
        self.depth = depth
    def __str__(self):
        return f"{self.name} - Area: {self.area}, Depth: {self.depth}"
    def __lt__(self, other):
        if self.area < other.area:
            return True
        return False
