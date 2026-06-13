from fastapi import APIRouter

from api.schemas.request import ChatRequest
from api.schemas.response import ChatResponse
 
router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat(request:ChatRequest):
    user_message = request.message

    # Test response
    bot_response = f"Response from bot fro q : {user_message}"

    return ChatResponse(response=bot_response)
