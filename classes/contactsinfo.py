from typing import Optional

from pydantic import BaseModel, Field


from classes.phoneinfo import PhoneInfo


class ContactsInfo(BaseModel):
    email: Optional[str]
    fullName: str
    phone: Optional[PhoneInfo] = Field(alias='number')

    class Config:
        allow_population_by_field_name = True
