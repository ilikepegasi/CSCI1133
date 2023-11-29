import copy

CATEGORIES = ['Head', 'Torso', 'Legs', 'Feet']

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

def cheap_outfit(stores: list[Store]) -> dict:
    all_clothes = []
    for i, store in enumerate(stores):
        for j, item in enumerate(store.items):
            all_clothes.append(item)
    cheap_outfit_dict = {}
    for target_category in CATEGORIES:
        print(target_category)
        cheap_outfit_dict[target_category] = cheap_item(all_clothes, target_category)
    return cheap_outfit_dict


def cheap_item(items: list[Item], target_category: str) -> Item:
    relevant_items = []
    for i, item in enumerate(items):
        if item.category == target_category:
            relevant_items.append(item)
    return min(relevant_items)

if __name__ == "__main__":
    s = Store("blacksmith", "/workspaces/CSCI1133/homework/hw12/testFiles/blacksmith.csv")
    print(str(s))


if __name__ == '__main__':
    print()
    path1 = "/workspaces/CSCI1133/homework/hw12/testFiles/blacksmith.csv"
    path2 = "/workspaces/CSCI1133/homework/hw12/testFiles/sparkles.csv"
    outfit1 = cheap_outfit([Store('Blacksmith', path1), Store("Sparkles", path2)])
    print(outfit1) #{'Head': <__main__.Item object at 0x03407310>, 'Torso': <__main__.Item object at 0x03407340>, 'Legs': <__main__.Item object at 0x03407250>, 'Feet': <__main__.Item object at 0x034071F0>}
    print()
    for key in outfit1:
        print(key,' - ',outfit1[key])
