class User:
    def __init__(self, user_id, username, password_hash, full_name, email,
                 role_id, is_active=True, created_at=None, updated_at=None):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.full_name = full_name
        self.email = email
        self.role_id = role_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

@property
def user_id(self):
    return self.user_id

@user_id.setter
def user_id(self, user_id):
    self.user_id = user_id

@property
def username(self):
    return self.username

@username.setter
def username(self, username):
    self.username = username
    
@property
def password_hash(self):
    return self.password_hash

@password_hash.setter
def password_hash(self, password_hash):
    self.password_hash = password_hash

@property
def full_name(self):
    return self.full_name

@full_name.setter
def full_name(self, full_name):
    self.full_name = full_name

@property
def email(self):
    return self.email

@email.setter
def email(self, email):
    self.email = email

@property
def role_id(self):
    return self.role_id

@role_id.setter 
def role_id(self, role_id):
    self.role_id = role_id

@property
def is_active(self):
    return self.is_active

@is_active.setter
def is_active(self, is_active):
    self.is_active = is_active

@property
def created_at(self):
    return self.created_at

@created_at.setter
def created_at(self, created_at):
    self.created_at = created_at

@property
def updated_at(self):
    return self.updated_at

@updated_at.setter
def updated_at(self, updated_at):
    self.updated_at = updated_at