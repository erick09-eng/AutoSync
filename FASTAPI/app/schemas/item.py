from pydantic import BaseModel

class ItemBase(BaseModel):
    """
    Base schema for an item.

    Attributes:
        name (str): The name of the item.
        description (str): A description of the item.
        price (int): The price of the item.
        on_offer (bool): Indicates if the item is on offer. Defaults to True.
    """
    name: str
    description: str
    price: int
    on_offer: bool = True

class ItemCreate(ItemBase):
    """
    Schema for creating a new item.

    Inherits all fields from ItemBase.
    """
    pass

class ItemResponse(ItemBase):
    """
    Schema for returning an item with its ID.

    Attributes:
        id (int): The unique identifier of the item.
    """
    id: int

    class Config:
        orm_mode = True