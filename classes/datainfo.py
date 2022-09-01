from typing import Optional

from pydantic import BaseModel, Field, validator

from classes.adressinfo import AdressInfo
from classes.contactsinfo import ContactsInfo
from classes.coordinatesinfo import CoordinatesInfo
from classes.experienceinfo import ExperienceInfo
from classes.salaryinfo import SalaryInfo
from classes.scheduleinfo import ScheduleInfo


class DataInfo(BaseModel):
    address: AdressInfo
    allow_messages: Optional[bool] = True
    billing_type: Optional[str] = "packageOrSingle"
    business_area: Optional[int] = 1
    contacts: ContactsInfo
    coordinates: Optional[CoordinatesInfo]
    description: str
    experience: Optional[ExperienceInfo]
    html_tags: Optional[bool] = True
    image_url: Optional[str] = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    name: str
    salary: SalaryInfo
    employment: Optional[str] = Field(alias="schedule")

    # @validator('coordinates')
    # def check_address(cls, v):
    #     print(v)

    # class Config:
    #     allow_population_by_field_name = True

    # def validate(cls: type['Data'], value: any) -> 'Data':
    #     for name, field in Data.__fields__.items():
    #         value = value.get(name)
