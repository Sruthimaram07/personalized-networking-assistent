from models.distilbert import tokenizer
from models.gpt2 import generate_text
from backend.crud import save_conversation

STOP_WORDS = {
    "for", "the", "a", "an", "of", "to", "in", "on", "and", "is"
}


def generate_conversation(event, interest):
    tokens = tokenizer.tokenize(event)

    keywords = [
        token for token in tokens
        if token not in STOP_WORDS
    ]

    prompt = (
        f"Event: {event}\n"
        f"Interest: {interest}\n\n"
        "Conversation Starter:\n"
    )

    conversation = generate_text(prompt)

    save_conversation(event, interest, keywords, conversation)

    return {
        "event": event,
        "interest": interest,
        "keywords": keywords,
        "conversation_starter": conversation
    }