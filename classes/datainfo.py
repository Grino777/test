from typing import Optional

from pydantic import BaseModel

from classes.adressinfo import AdressInfo
from classes.contactsinfo import ContactsInfo
from classes.coordinatesinfo import CoordinatesInfo
from classes.salaryinfo import SalaryInfo
from classes.scheduleinfo import ScheduleInfo


class DataInfo(BaseModel):
    address: AdressInfo
    allow_messages: Optional[bool]# = None
    billing_type: Optional[str]# = "packageOrSingle"
    business_area: Optional[int]# = 1
    contacts: ContactsInfo
    coordinates: Optional[CoordinatesInfo]
    description: str
    experience: Optional[str]
    html_tags: Optional[bool]
    image_url: Optional[str]
    employment: str
    name: str
    salary: SalaryInfo
    schedule: Optional[ScheduleInfo]

    # def validate(cls: type['Data'], value: any) -> 'Data':
    #     for name, field in Data.__fields__.items():
    #         value = value.get(name)
