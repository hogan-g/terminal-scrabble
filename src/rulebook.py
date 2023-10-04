# https://python-patterns.guide/gang-of-four/singleton/

class Rulebook():
    _instance = None
    rules = []

    def __new__(self): # singleton patter implementation
        if self._instance is None:
            self._instance = super(Rulebook, self).__new__(self)
            with open('rules.txt') as f:
                self.rules = f.read().split("#")
        
        return self._instance

    def __str__(self): # print the rules
        return "".join(self.rules)
    
    def retrieve(self, num): # retrieve a specific rule
        print(self.rules[num-1].strip())