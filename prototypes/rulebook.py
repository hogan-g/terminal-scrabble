# https://python-patterns.guide/gang-of-four/singleton/

class Rulebook():
    _instance = None
    rules = []

    def __new__(self):
        if self._instance is None:
            self._instance = super(Rulebook, self).__new__(self)
            with open('rules.txt') as f:
                self.rules = f.read().split("#")
        
        return self._instance

    def __str__(self):
        #return str(self.rules)
        return "".join(self.rules)
    
    def retrieve(self, num):
        print(self.rules[num-1].strip())