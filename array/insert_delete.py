import random
class RandomizedSet(object):
    def __init__(self):
        self.mapa = {}
        self.data = []

    def insert(self, val):
        if val not in self.mapa:
            self.data.append(val)
            self.mapa[val] = len(self.data) - 1
            return True
        else:
            return False


    def remove(self, val):
        if val in self.mapa:
            self.data.pop(self.mapa[val])
            return True
        else:
            return False


    def getRandom(self):
        random_element = random.choice(self.data)
        return random_element
    
arr = []
obj = RandomizedSet()
arr.append(None)
arr.append(obj.insert(2))
arr.append(obj.insert(1))
arr.append(obj.remove(3))
arr.append(obj.insert(3))
arr.append(obj.getRandom())
print(arr)
