from pydantic import BaseModel


class ScheduleInfo(BaseModel):
    id: str = 'fullDay'
