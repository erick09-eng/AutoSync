class Product:
    
    #create the object vehicle 
    class Product:
        def __init__(self, name, description, price, on_offer, offer_price, category_id, current_stock, min_stock, is_active, created_at, updated_at):
            self.product_id = product_id
            self.sku = sku
            self.name = name
            self.description = description
            self.category_id = category_id
            self.unit_price = unit_price
            self.cost_price = cost_price
            self.current_stock = current_stock
            self.min_stock = min_stock
            self.is_active = is_active
            self.created_at = created_at
            self.updated_at = updated_at


            
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
    def description(self, newdescription):
        self._description = newdescription
        
    @property
    def price (self):
        return self._price
        
    @price.setter
    def price (self, newprice):
        self._price = newprice
        
    @property
    def on_offer(self):
        return self._on_offer
        
    @onOffer.setter
    def on_offer(self, newonoffer):
        serf._on_offer = newonoffer
        
    @property
    def offer_price(self):
        return self._offer_price

    @offer_price.setter
    def offer_price(self, newofferprice):
        self._offer_price = newofferprice

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, newcategoryid):
        self._category_id = newcategoryid

    @property
    def current_stock(self):
        return self._current_stock

    @current_stock.setter
    def current_stock(self, newcurrentstock):
        self._current_stock = newcurrentstock

    @property
    def min_stock(self):
        return self._min_stock

    @min_stock.setter
    def min_stock(self, newminstock):
        self._min_stock = newminstock

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, newisactive):
        self._is_active = newisactive

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, newcreatedat):
        self._created_at = newcreatedat

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, newupdatedat):
        self._updated_at = newupdatedat