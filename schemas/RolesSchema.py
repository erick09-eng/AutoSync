from pydantic import BaseModel
from typing import Optional

class RoleBase(BaseModel):
    role_name: str
    role_description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleResponse(RoleBase):
    role_id: int

    class Config:
        orm_mode = True
