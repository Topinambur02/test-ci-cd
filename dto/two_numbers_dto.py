from pydantic import BaseModel


class TwoNumbersDto(BaseModel):
    a: int
    b: int
    