from typing import Optional

from pydantic import BaseModel



class ExperienceInfo(BaseModel):
    id: Optional[str] = 'noMatter'