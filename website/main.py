from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, JSONResponse
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

@app.get("/discs", response_class=HTMLResponse)
def read_discs():
    return 
    """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get("/data.json", response_class=JSONResponse)
def get_disc_data(db_session: DbSession):
    return schemas.DiscList(data=crud.get_discs(db_session=db_session))
