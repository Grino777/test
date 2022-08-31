from pydantic import BaseModel, Field
from pyparsing import Optional


class PhoneInfo(BaseModel):
    city: Optional = str
    country: Optional = int
    number: str

