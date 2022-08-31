from typing import Dict, Optional
from pydantic import BaseModel

from classes.adressinfo import AdressInfo
from classes.contactsinfo import ContactsInfo
from classes.salaryinfo import SalaryInfo
from classes.scheduleinfo import ScheduleInfo



class DataInfo(BaseModel):
    address: AdressInfo
    # allow_messages: Optional[bool]
    # billing_type: Optional[str] = "packageOrSingle"
    # business_area: Optional[int] = 1
    # contacts: dict[ContactsInfo]
    # coordinates: dict
    # description: str
    # experience: dict
    # html_tags: bool
    # image_url: str
    # employment: str
    # name: str
    # salary: SalaryInfo
    # schedule: ScheduleInfo


    # def validate(cls: type['Data'], value: any) -> 'Data':
    #     for name, field in Data.__fields__.items():
    #         value = value.get(name)
