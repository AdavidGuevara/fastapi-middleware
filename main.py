from fastapi import FastAPI, Request
from starlette.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Login API",
    description="a login REST API using python and mysql",
    version="0.0.1",
)


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def verify_user_agent(request: Request, call_next):
    if request.headers["User-Agent"].find("Mobile") == -1:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(
            content={"message": "no permitimos mobiles"}, status_code=401
        )


@app.get("/")
def index(request: Request, response: Response):
    response.set_cookie(key="mykey", value="Hola")
    return {"message": "ok"}
