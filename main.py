from dto.two_numbers_dto import TwoNumbersDto
from dto.result_dto import ResultDto
from service.adding_two_numbers import adding_two_numbers

from fastapi import FastAPI

import uvicorn


app = FastAPI()


@app.post('/')
async def calculate_two_numbers(dto: TwoNumbersDto) -> ResultDto:
    message = "The program added two numbers"
    result = adding_two_numbers(a=dto.a, b=dto.b)
    return ResultDto(message=message, result=result)


def main():
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
