from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db, logger
import crud, schemas


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.post("/data/", response_model=schemas.ProcessedDetectionResultResponse)
def create_data(data: schemas.ProcessedDetectionResultCreate, db: Session = Depends(get_db)):
    return crud.create_data(db, data)

@app.get("/data/", response_model=list[schemas.ProcessedDetectionResultResponse])
def read_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_data(db, skip, limit)

@app.get("/data/{data_id}", response_model=schemas.ProcessedDetectionResultResponse)
def read_data_by_id(data_id: int, db: Session = Depends(get_db)):
    db_data = crud.get_data_by_id(db, data_id)
    if db_data is None:
        logger.error(f"Data ID {data_id} not found")
        raise HTTPException(status_code=404, detail="Data not found")
    return db_data

@app.put("/data/{data_id}", response_model=schemas.ProcessedDetectionResultResponse)
def update_data(data_id: int, data: schemas.ProcessedDetectionResultUpdate, db: Session = Depends(get_db)):
    updated_data = crud.update_data(db, data_id, data)
    if updated_data is None:
        logger.error(f"Failed to update - Data ID {data_id} not found")
        raise HTTPException(status_code=404, detail="Data not found")
    return updated_data

@app.delete("/data/{data_id}")
def delete_data(data_id: int, db: Session = Depends(get_db)):
    deleted_data = crud.delete_data(db, data_id)
    if deleted_data is None:
        logger.error(f"Failed to delete - Data ID {data_id} not found")
        raise HTTPException(status_code=404, detail="Data not found")
    return {"message": "Data deleted successfully"}
