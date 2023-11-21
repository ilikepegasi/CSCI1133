class County:
    def __init__(self, csv_string):
        entries = csv_string.strip().split(',')
        self.state = entries[0]
        self.county = entries[1]
        self.pop = int(entries[2])
    def get_state(self):
        return self.state
    def get_county(self):
        return self.county
    def get_pop(self):
        return self.pop
    def set_state(self, state):
        self.state = state
    def set_county(self, county):
        self.county = county
    def set_pop(self, pop):
        self.pop = pop
