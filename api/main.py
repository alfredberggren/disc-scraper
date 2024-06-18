from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import crud
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


DbSession = Annotated[Session, Depends(get_db_session)]


@app.get("/data.json", response_class=JSONResponse)
def get_disc_data(db_session: DbSession):
    disc_list = jsonable_encoder(schemas.DiscList(data=crud.get_discs(db_session=db_session)))
    return JSONResponse(
        headers={"Access-Control-Allow-Origin": "*"},
        content=disc_list,
    )
