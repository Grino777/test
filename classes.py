from pydantic import BaseModel, ValidationError, Field, validator

class ScheduleInfo(BaseModel):
    id = 'fullDay'

class PhoneInfo(BaseModel):
    city: int = 953
    country: int = 7
    number: str = '676-23-99'

class DataContacts(BaseModel):
    email: str
    fullName: str = Field(alias='name')
    phone: dict#[PhoneInfo]

class DataSalary(BaseModel):
    _from: int = Field(alias='from')
    to: int
    currency: str
    gross: bool

class DataAdress(BaseModel):
    region: str
    city: str
    street_type: str
    street: str
    house_type: str
    house: str
    value: str
    lat: float
    lng: float

class Data(BaseModel):
    address: dict#[DataAdress]
    allow_messages: str = True
    billing_type: str = "packageOrSingle"
    business_area: int = 1
    contacts: dict#[DataContacts]
    coordinates: dict = {}
    description: str
    experience: dict = {"id": "noMatter"}
    html_tags: bool = True
    image_url: str = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    employment: str
    name: str
    salary: DataSalary
    schedule: ScheduleInfo

    def validate(cls: type['Data'], value: any) -> 'Data':
        for name, field in Data.__fields__.items():
            value = value.get(name)
