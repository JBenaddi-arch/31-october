class Computer:
    
    
    def __init__(self):
        self.__maxiprice = 900
        
        
    def sell(self):
        print("Selling Price: {}".format(self.__maxiprice))
        
        
        def setMaxPrice(self, price):
            self.__maxiprice = price
            
        
c = Computer()
c.sell()

c.setMaxPrice(1000)
c.sell()