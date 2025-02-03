from pydantic import BaseModel
from datetime import date
from typing import Optional
from datetime import datetime

class ProcessedDetectionResultBase(BaseModel):
    id: int
    date: datetime  # ✅ Change from `date` to `datetime`
    message: str
    media_path: str
    youtube_links: str
    bbox: str
    confidence: str
    channel_title: str
    class_label: str
    channel_username: str

    class Config:
        from_attributes = True

class ProcessedDetectionResultCreate(ProcessedDetectionResultBase):
    pass  # No extra fields needed for creation

class ProcessedDetectionResultUpdate(ProcessedDetectionResultBase):
    pass  # Used for updating records

class ProcessedDetectionResultResponse(ProcessedDetectionResultBase):
    id: int  # Response includes ID

    class Config:
        from_attributes = True  # Allows ORM mode
