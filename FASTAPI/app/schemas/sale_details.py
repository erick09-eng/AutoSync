# app/schemas/sale_details.py
"""SaleDetail schemas module.
This module contains Pydantic schemas for sale details.
Classes:
    SaleDetailBase: Base schema for sale details.
    SaleDetailCreate: Schema for creating sale details.
    SaleDetailResponse: Schema for response of sale details.
"""
# pylint: disable=too-few-public-methods
from typing import Optional
from pydantic import BaseModel


class SaleDetailBase(BaseModel):
    """
        Base model for sale details.
    """
    sale_id : int
    product_id : int
    quantity : int
    unit_price : float
    discount_percentage : float
    subtotal : Optional[float] = 0

class SaleDetailCreate(SaleDetailBase):
    """
        Model for creating sale details.
    """

class SaleDetailResponse(SaleDetailBase):
    """
        Model for response of sale details.
    """
    sale_detail_id : int

    class Config:
        """"
            Configurations for the SaleDetailResponse model.
        """
        from_attributes = True
