from sqlalchemy.orm import Session
from sqlalchemy import asc
import models

def get_discs(db_session: Session):
    return db_session.query(models.Disc).order_by(asc(models.Disc.price)).all()
