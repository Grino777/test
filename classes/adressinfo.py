from typing import Optional

from pydantic import BaseModel


class AdressInfo(BaseModel):
    region: str
    city: str
    street_type: Optional[str]
    street: Optional[str]
    house_type: Optional[str]
    house: Optional[str]
    value: str
    lat: float
    lng: float