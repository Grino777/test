from pydantic import BaseModel


class CoordinatesInfo(BaseModel):
    latitude: float
    longitude: float
