from sqlalchemy.orm import Session
from database import get_db, logger
import models, schemas, database
from schemas import ProcessedDetectionResultCreate

logger = database.logger

def create_data(db: Session, data: schemas.ProcessedDetectionResultCreate):
    db_data = models.ProcessedDetectionResult(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    logger.info(f"Created entry ID: {db_data.id}")
    return db_data

def get_data(db: Session, skip: int = 0, limit: int = 10):
    result = db.query(models.ProcessedDetectionResult).offset(skip).limit(limit).all()
    logger.info("Fetched data entries")
    return result

from datetime import datetime

def get_data_by_id(db: Session, data_id: int):
    result = db.query(models.ProcessedDetectionResult).filter(
        models.ProcessedDetectionResult.id == data_id
    ).first()
    
    if result:
        # ✅ Convert `datetime` to `date` before returning response
        result.date = result.date.date() if isinstance(result.date, datetime) else result.date

    return result

def update_data(db: Session, data_id: int, data: schemas.ProcessedDetectionResultUpdate):
    db_data = db.query(models.ProcessedDetectionResult).filter(models.ProcessedDetectionResult.id == data_id).first()
    if db_data:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_data, key, value)
        db.commit()
        db.refresh(db_data)
        logger.info(f"Updated data ID: {data_id}")
    else:
        logger.warning(f"Failed to update - Data ID: {data_id} not found")
    return db_data

def delete_data(db: Session, data_id: int):
    db_data = db.query(models.ProcessedDetectionResult).filter(models.ProcessedDetectionResult.id == data_id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
        logger.info(f"Deleted data ID: {data_id}")
    else:
        logger.warning(f"Failed to delete - Data ID: {data_id} not found")
    return db_data
