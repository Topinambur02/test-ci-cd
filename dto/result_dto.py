from pydantic import BaseModel


class ResultDto(BaseModel):
    message: str
    result: int
