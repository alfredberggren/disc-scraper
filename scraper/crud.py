"""
Module supporting functions for any interaction with the database.
"""

import models
from html_parser import fetch_price, UnparseableHTMLException
import datetime
from disc import Disc

from database import SessionLocal, engine
from sqlalchemy import and_

models.Base.metadata.create_all(bind=engine)


def insert_discs(discs: set[Disc]):
    """
    Inserts set of found discs into database.
    """
    db = SessionLocal()
    db_disc: models.Disc = None

    for d in discs:
        exists: models.Disc = (
            db.query(models.Disc)
            .filter(
                and_(
                    models.Disc.plastic == d.plastic,
                    models.Disc.mold_name == d.mold_name,
                )
            )
            .first()
        )
        if exists:
            if d.price < exists.price:
                exists.price = d.price
                exists.url = d.url
                exists.last_updated = datetime.datetime.now().isoformat()
                db.add(exists)
            else:
                time_since_last_update = (
                    datetime.datetime.now()
                    - datetime.datetime.fromisoformat(exists.last_updated)
                )
                if (
                    time_since_last_update > datetime.timedelta(days=7)
                ):  # If time since last update is greater than 7 days, disc is updated to prevent out-of-date prices persisting in database
                    try:
                        exists.price = fetch_price(d.url)
                        exists.last_updated = datetime.datetime.now().isoformat()
                        db.add(exists)
                    except UnparseableHTMLException:
                        # Disc has probably been removed
                        exists.price = d.price
                        exists.url = d.url
                        exists.last_updated = datetime.datetime.now().isoformat()
                        db.add(exists)
        else:
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
