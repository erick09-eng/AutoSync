# schemas/sale_details.py
from pydantic import BaseModel
from typing import Optional

#SaleDetailsBase, son los campos que se envial al cliente a crear por ejemplo un post, no mandamos el pk de la tabla 
class SaleDetailBase(BaseModel):
    
    sale_id : int
    product_id : int
    quantity : int
    unit_price : float
    discount_percentage : float
    subtotal : Optional[float] = 0


class SaleDetailCreate(SaleDetailBase):
    pass  # Mismo que el base para crear


# cuando se crea el detalle de la venta la base de datos genera el id, y lo responde 
class SaleDetailResponse(SaleDetailBase):
    sale_detail_id : int

    class Config:
        orm_mode : True
