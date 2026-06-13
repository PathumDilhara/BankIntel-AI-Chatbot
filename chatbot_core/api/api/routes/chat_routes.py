from fastapi import APIRouter

from api.schemas.request import ChatRequest
from api.schemas.response import ChatResponse
from core.orchestrator import ChatOrchestrator

router = APIRouter()

orchestrator = ChatOrchestrator()

@router.post("/", response_model=ChatResponse)
def chat(request:ChatRequest):
    user_message = request.message

    # get response str from orchestrator
    bot_response = orchestrator.get_response(user_message=user_message)

    return ChatResponse(response=bot_response)
