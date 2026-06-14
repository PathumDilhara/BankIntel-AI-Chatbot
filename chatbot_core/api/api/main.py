from fastapi import FastAPI
from api.routes import chat_routes, health_routes


# Create FastAPI app
app = FastAPI(
    title="BankIntel AI Chatbot",
    description="RAG + BERT + LLaMA based banking chatbot",
    version="1.0.0"
)

# Register routes, with prefix we need to use that before access any routes registered here
# eg : http://127.0.0.1:8000/health/REST_PATH
app.include_router(chat_routes.router, prefix="/chat", tags=["Chat"])
app.include_router(health_routes.router, prefix="/health", tags=["Health"])

# Root endpoint (http://127.0.0.1:8000/)
@app.get('/')
def root():
    return {
        "message": "BankIntel AI Chatbot is running"
    }


# NOTE : Run project always on root otherwise defined paths may be wrong



# # run the app : uvicorn main:app --reload
# # pip install fastapi uvicorn
# # Select interpreter in VS Code > Ctrl + Shift + P > Python: Select Interpreter > TFenv
