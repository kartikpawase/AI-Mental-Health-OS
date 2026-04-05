from pydantic import BaseModel
from typing import Optional, List

class BiometricData(BaseModel):
    age: int
    gender: str
    sleep_hours: float
    physical_activity: float
    social_interactions: float
    stress_level: float
    history_mental_illness: str

class JournalEntry(BaseModel):
    text: str

class ChatMessage(BaseModel):
    message: str
