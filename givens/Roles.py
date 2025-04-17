class Roles:
    def __init__(self, role_id, role_name, role_description=None):
        self.role_id = role_id
        self.role_name = role_name
        self.role_description = role_description
        
    @property
    def role_id(self):
        return self._role_id

    @role_id.setter
    def role_id(self, _role_id):
        self._role_id = _role_id

    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, _role_name):
        self._role_name = _role_name

    @property
    def role_description(self):
        return self._role_description

    @role_description.setter
    def role_description(self, _role_description):
        self._role_description = _role_description
        
