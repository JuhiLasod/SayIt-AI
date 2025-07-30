from pydantic import BaseModel
from datetime import datetime

class CommandLog(BaseModel):
    command: str
    confidence: float
    timestamp: datetime
