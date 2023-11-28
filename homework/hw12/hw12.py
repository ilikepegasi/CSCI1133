class Item():
    def __init__(self, csv_string: str, store: str) -> None:
        self.store = store
        csv_string = csv_string.split(",")
        self.name = csv_string[0]
        self.price = csv_string[1]
        self.category = csv_string[2]
    def __str__(self) -> str:
        return 	f"{self.name} ({self.category}): ${self.price}"
    def __lt__(self, other) -> bool:
        if self.price < other.price:
            return True
        return False
    
class Store():
    def __init__(self, name, filename):
        self.name = name
        self.items = []
        with open(filename, "r", encoding="utf-8") as fp:
            data = fp.read()
        data = data.split("\n")
        data.pop(0)
        for line in data:
            self.items.append(Item(line, self.name))
    def __str__(self) -> str:
        value = f"{self.name}\n"
        for item in self.items:
            value += f"{str(item)}\n"
        return value

if __name__ == "__main__":
    s = Store("blacksmith", "testFiles/blacksmith.csv")
    print(str(s))