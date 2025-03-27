from fastapi import APIRouter, Body, Response, Header


router = APIRouter()


@router.get("/hello")  # простой URL
def greet():
    return "Hello? World?"


@router.get("/hey/{who}")  # параметр в пути URL
def greet1(who):
    return f"Hello? {who}?"


@router.get("/hi")  # в качестве параметра запроса после символа ? в URL
def greet2(who):
    return f"Hello? {who}?"


@router.post("/data")
def data(who: str = Body(
    embed=True)):  # Выражение Body(embed=True) мы получаем значение who из тела запроса в формате JSON
    return f"Hello {who}"


@router.post("/header")
def header(user_agent: str = Header()):  # передать аргумент в качестве HTTP-заголовка
    return f"{user_agent}"


@router.get("/happy")
def happy(status_code=200):
    return ":)"


@router.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"
