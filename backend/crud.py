from backend.database import SessionLocal
from backend.models import Conversation


def save_conversation(event, interest, keywords, conversation):
    db = SessionLocal()

    try:
        record = Conversation(
            event=event,
            interest=interest,
            keywords=", ".join(keywords),
            conversation=conversation,
            feedback=""
        )

        db.add(record)
        db.commit()

    finally:
        db.close()


def get_all_conversations():
    db = SessionLocal()

    try:
        return db.query(Conversation).all()

    finally:
        db.close()


def update_feedback(conversation_id, feedback):
    db = SessionLocal()

    try:
        record = (
            db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

        if record is None:
            return False

        record.feedback = feedback
        db.commit()
        db.refresh(record)

        return True

    finally:
        db.close()