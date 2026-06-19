from fastapi import FastAPI
from src.routes import routes

app = FastAPI()


# if __name__ == "__main__":
print("running the fastapi server")
app.include_router(routes.router)
