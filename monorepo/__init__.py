from fastapi import FastAPI
from healthai.src.api.ledgers import router as healthai

# from travelai.src.api.ledgers import router as travelai

app = FastAPI()

# routing
app.include_router(healthai.router)
# app.include_router(travelai.router)
