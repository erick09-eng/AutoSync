class Sale:
    def __init__(self, sale_id, document_type_id, serial_number, customer_id, user_id,
                 subtotal, tax_amount, discount_amount=0.0, total_amount=0.0,
                 payment_method='cash', status='completed',
                 created_at=None, updated_at=None):
        self.sale_id = sale_id
        self.document_type_id = document_type_id
        self.serial_number = serial_number
        self.customer_id = customer_id
        self.user_id = user_id
        self.subtotal = subtotal
        self.tax_amount = tax_amount
        self.discount_amount = discount_amount
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        
    @property
    def sale_id(self):
        return self._sale_id

    @sale_id.setter
    def sale_id(self, _sale_id):
        self._sale_id = _sale_id

    @property
    def document_type_id(self):
        return self._document_type_id

    @document_type_id.setter
    def document_type_id(self, _document_type_id):
        self._document_type_id = _document_type_id

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, _serial_number):
        self._serial_number = _serial_number

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, _customer_id):
        self._customer_id = _customer_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, _user_id):
        self._user_id = _user_id

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, _subtotal):
        self._subtotal = _subtotal

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, _tax_amount):
        self._tax_amount = _tax_amount

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, _discount_amount):
        self._discount_amount = _discount_amount

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, _total_amount):
        self._total_amount = _total_amount

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, _payment_method):
        self._payment_method = _payment_method

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, _status):
        self._status = _status

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, _created_at):
        self._created_at = _created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, _updated_at):
        self._updated_at = _updated_at
        
        
