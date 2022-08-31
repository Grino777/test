from pydantic import BaseModel, Field
from pyparsing import Optional

from classes.phoneinfo import PhoneInfo


class ContactsInfo(BaseModel):
    email: Optional = str
    fullName: str = Field(alias='name')
    phone: dict[PhoneInfo]

    class Config:
        allow_population_by_field_name = True