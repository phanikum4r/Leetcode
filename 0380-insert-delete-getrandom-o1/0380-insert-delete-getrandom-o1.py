import random
class RandomizedSet:

    def __init__(self):
        self.s=[]
        

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        try:
            self.s.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return self.s[random.randint(0,len(self.s)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()