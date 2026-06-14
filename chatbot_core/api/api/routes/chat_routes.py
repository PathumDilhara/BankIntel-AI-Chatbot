from fastapi import APIRouter

from api.schemas.request import ChatRequest
from api.schemas.response import ChatResponse
from core.orchestrator import ChatOrchestrator

from core.rag.retriever import Retriever

r = Retriever()

router = APIRouter()

orchestrator = ChatOrchestrator()

@router.post("/", response_model=ChatResponse)
def chat(request:ChatRequest):
    user_message = request.message

    # get response str from orchestrator
    bot_response = orchestrator.get_response(user_message=user_message)

    return ChatResponse(response=bot_response)

# TODO : delete in production
@router.post("/r", response_model=ChatResponse)
def retriever_test(request: ChatRequest):
    #print("getting relevant docs")
    
    response = r.get_relevant_docs(query=request.message)
                                   
    return ChatResponse(response=str(response))