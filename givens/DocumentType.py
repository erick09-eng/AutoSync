class DocumentType:
    def __init__(self, document_type_id, code, name, description=None):
        self.document_type_id = document_type_id
        self.code = code
        self.name = name
        self.description = description
        
    @property
    def document_type_id(self):
        return self._document_type_id

    @document_type_id.setter
    def document_type_id(self, _document_type_id):
        self._document_type_id = _document_type_id

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, _code):
        self._code = _code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        self._name = _name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, _description):
        self._description = _description
    
    
