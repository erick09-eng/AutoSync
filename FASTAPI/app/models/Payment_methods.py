"""Payment_methods model module.
This module contains the SQLAlchemy ORM model for payment methods.

Classes:
    PaymentMethod: Represents a payment method.

"""

from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

# pylint: disable=too-few-public-methods
class PaymentMethod(Base):
    """Represents a payment method.

    Attributes:
        payment_method_id (int): Primary key for the payment method.
        name (str): Name of the payment method.
        description (str): Description of the payment method.
        requires_authorization (bool): Indicates if authorization is required.
    """

    __tablename__ = "payment_methods"

    payment_method_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
    requires_authorization = Column(Boolean, default=False)

