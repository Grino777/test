from pydantic import BaseModel


class AdressInfo(BaseModel):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float
    lng: float