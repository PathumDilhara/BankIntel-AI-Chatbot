from fastapi import APIRouter

from api.schemas.request import ChatRequest
from api.schemas.response import ChatResponse
from core.orchestrator import ChatOrchestrator

from core.rag.retriever import Retriever
from utils.intent_categories import intent_category
from utils.reasponse_templates import response_templates


router = APIRouter()

orchestrator = ChatOrchestrator()

@router.post("", response_model=ChatResponse)
def chat(request:ChatRequest):
    user_message = request.message

    # get response dic from orchestrator
    bot_response = orchestrator.get_response(user_message=user_message)
    # bot_response = orchestrator.get_response_test(user_message=user_message)

    # get options to provide to user based on confidence vlaue
    category = intent_category.get(bot_response["intent"], "unknown")
    options = response_templates.get(category, response_templates["unknown"])
    
    return ChatResponse(response=bot_response["response"], options=options)
