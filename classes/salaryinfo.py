from pydantic import BaseModel, Field


class SalaryInfo(BaseModel):
    from_: int = Field(alias='from')
    to: int
    # currency: str
    # gross: bool
