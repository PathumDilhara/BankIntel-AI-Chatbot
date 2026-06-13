from fastapi import APIRouter

# router obj
router = APIRouter()

# endpoint
@router.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "BankIntel AI Chatbot API is running"
    }