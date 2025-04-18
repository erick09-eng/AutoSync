class Category:
    def __init__(self, category_id, name, description=None, parent_category_id=None):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.parent_category_id = parent_category_id

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, _category_id):
        self._category_id = _category_id

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

    @property
    def parent_category_id(self):
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, _parent_category_id):
        self._parent_category_id = _parent_category_id
    