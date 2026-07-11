from fastapi import APIRouter
from backend.schemas import GenerateRequest
from backend.services import generate_conversation

router = APIRouter()

@router.post("/generate")
def generate(request: GenerateRequest):
    return generate_conversation(
        request.event,
        request.interest
    )