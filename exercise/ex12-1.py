class Corn:
    def __init__(self, variety, ears):
        self.vari = variety
        self.ears = ears
        self.cooked = False
    def cook_corn(self):
        self.cooked = True

if __name__ == '__main__':
    harvest = Corn('Standard', 10)
    extra = Corn('Bicolor', 5)
    harvest.cook_corn()
    print(harvest.cooked) # Should be True
    print(extra.cooked) # Should be False
