from sqlalchemy import Column, Integer, String, Text

from backend.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String)
    interest = Column(String)
    keywords = Column(Text)
    conversation = Column(Text)
    feedback = Column(String, default="")