from typing import Optional

from pydantic import BaseModel, Field, validator, ValidationError

from classes.phoneinfo import PhoneInfo


class ContactsInfo(BaseModel):
    email: Optional[str]
    fullName: str
    phone: str #Field(alias='number')

    @validator('phone')
    def check_number(cls, v):
        try:
            if len(v) == 11 and all([i in '0123456789' for i in v]) :
                return v
        except ValidationError as e:
            print(e)

    # class Config:
    #     allow_population_by_field_name = True
