from typing import Optional

from pydantic import BaseModel, validator


class AdressInfo(BaseModel):
    value: Optional[str]
