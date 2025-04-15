class Vehicle:
    
    #create the object vehicle 
    def __init__(self, name, description, price, onOffer):
        self._name = name
        self._description = description
        self._price = price
        self._onOffer = onOffer

            
    #getter and setters of class vehicle
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, _nameNew):
        self._name = _nameNew
        
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, newDescription):
        self._description = newDescription
        
    @property
    def price (self):
        return self._price
        
    @price.setter
    def price (self, newPrice):
        self._price = newPrice
        
    @property
    def onOffer(self):
        return self._onOffer
        
    @onOffer.setter
    def onOffer(self, newOnOffer):
        serf._onOffer = newOnOffer