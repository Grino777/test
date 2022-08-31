from typing import Optional

from pydantic import BaseModel


class CoordinatesInfo(BaseModel):
    latitude: Optional[str]
    longitude: Optional[str]
