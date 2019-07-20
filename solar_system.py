class System: 
    def __init__(self, bodies): 
        self.bodies = bodies 
    def __str__(self): 
        return f'{self.bodies}'





solar = System(4) 
print(solar)

