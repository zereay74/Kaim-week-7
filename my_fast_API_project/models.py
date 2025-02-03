from sqlalchemy import Column, Integer, Text, TIMESTAMP
from database import Base

class ProcessedDetectionResult(Base):
    __tablename__ = "processed_detection_result_table"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(TIMESTAMP)  # Match "timestamp without time zone"
    message = Column(Text)
    media_path = Column(Text)
    youtube_links = Column(Text)
    bbox = Column(Text)
    confidence = Column(Text)  # ⚠️ Fix: Store as TEXT, not FLOAT
    channel_title = Column(Text)
    class_label = Column(Text)
    channel_username = Column(Text)
