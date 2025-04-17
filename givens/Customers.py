class Customers:
    def __init__(self, customer_id, tax_id, full_name, email=None, phone=None,
                 address=None, is_active=True, created_at=None, updated_at=None):
        self.customer_id = customer_id
        self.tax_id = tax_id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.address = address
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, _customer_id):
        self._customer_id = _customer_id

    @property
    def tax_id(self):
        return self._tax_id

    @tax_id.setter
    def tax_id(self, _tax_id):
        self._tax_id = _tax_id

    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, _full_name):
        self._full_name = _full_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, _email):
        self._email = _email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, _phone):
        self._phone = _phone

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, _address):
        self._address = _address

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, _is_active):
        self._is_active = _is_active

    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, _created_at):
        self._created_at = _created_at

    @property
    def updated_at(self):
        return self._updated_at
