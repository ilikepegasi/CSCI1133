class GoFishList(list):
    def remove(self, x):
        if x in self:
            list.remove(self, x)
        else:
            print("Go Fish!")       

if __name__ == '__main__':
    hand = GoFishList(['7S', '7D', '8C', 'KH'])
    hand.remove('7D')
    print(hand) #Prints ['7S', '8C', KH']
    hand.remove('QS') #Prints Go Fish!
    print(hand) #Prints ['7S', '8C', KH']
    
class Uno:                         #1
    def __init__(self, tree):      #2
        self.acorn = tree % 5      #3
        self.leaf = tree           #4
        self.branch = 53           #5
    def compute(self):             #6
        return self.acorn + 56     #7

class Dos(Uno):                    #8
    def __init__(self, leaf):      #9
        Uno.__init__(self, leaf)   #10
        self.acorn = leaf % 5      #11
        self.branch = leaf         #12
    def get_leaf(self):            #13
        return self.leaf           #14
    def get_branch(self):          #15
        return self.branch         #16

obj1 = Uno(9)                      #17
obj2 = Dos(12)                     #18
print(obj2.compute())                          #19