from typing import Optional

from pydantic import BaseModel, Field


class PhoneInfo(BaseModel):
    city: Optional[str]
    country: Optional[str]
    number: Optional[str] = Field(alias='number')

    class Config:
        allow_population_by_field_name = True
