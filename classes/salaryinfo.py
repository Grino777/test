from pydantic import BaseModel, Field


class SalaryInfo(BaseModel):
    _from: int = Field(alias='from')
    to: int
    currency: str
    gross: bool