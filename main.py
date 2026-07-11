from fastapi import FastAPI
from pydantic import BaseModel

from backend.services import generate_conversation
from backend.wikipedia_service import get_fact
from backend.crud import get_all_conversations, update_feedback

app = FastAPI()


class UserInput(BaseModel):
    event: str
    interest: str


class FeedbackInput(BaseModel):
    conversation_id: int
    feedback: str


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }


@app.post("/generate")
def generate(user: UserInput):
    return generate_conversation(
        user.event,
        user.interest
    )


@app.get("/fact-check/{topic}")
def fact_check(topic: str):
    return {
        "topic": topic,
        "summary": get_fact(topic)
    }


@app.get("/history")
def history():
    records = get_all_conversations()

    return [
        {
            "id": record.id,
            "event": record.event,
            "interest": record.interest,
            "keywords": record.keywords,
            "conversation": record.conversation,
            "feedback": record.feedback
        }
        for record in records
    ]


@app.post("/feedback")
def feedback(data: FeedbackInput):
    success = update_feedback(
        data.conversation_id,
        data.feedback
    )

    if success:
        return {
            "message": "Feedback saved successfully!"
        }

    return {
        "message": "Conversation not found!"
    }