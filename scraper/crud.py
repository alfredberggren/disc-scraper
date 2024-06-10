import models
from disc import Disc

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def insert_discs(discs: set[Disc]):
    db = SessionLocal()
    db_disc: models.Disc = None

    for d in discs:
        exists = (
            db.query(models.Disc)
            .filter(
                models.Disc.plastic == d.plastic, models.Disc.mold_name == d.mold_name
            )
            .first()
        )
        if exists:
           db.delete(exists) 

        db_disc = models.Disc(
            mold_name=d.mold_name,
            plastic=d.plastic,
            manufacturer=d.manufacturer,
            price=d.price,
            url=d.url,
        )
        db.add(db_disc)

    db.commit()
    db.refresh(db_disc)

    db.close()

def get_discs():
    db = SessionLocal()
    discs = db.query(models.Disc).all()
    db.close()

    return discs
