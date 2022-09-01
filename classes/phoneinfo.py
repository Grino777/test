from typing import Optional

from pydantic import BaseModel, Field


class PhoneInfo(BaseModel):
    city: Optional[str]
    country: Optional[str]
    phone: Optional[str]
