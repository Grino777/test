from typing import Optional
from classes.adressinfo import AdressInfo
from pydantic import BaseModel, validator


class CoordinatesInfo(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]