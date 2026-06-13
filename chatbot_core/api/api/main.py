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



# import uvicorn

# from contextlib import asynccontextmanager
# import json

# from transformers  import AutoModelForSequenceClassification, AutoTokenizer
# import torch
# import torch.nn.functional as F

# from schemas import ChatRequest
# from utils.intent_categories import intent_category
# from utils.reasponse_templates import response_templates


# global variable : load once used in several functions
# MODEL = None
# TOKENIZER = None

# # When FastAPI starts > It pauses API startup, Runs this code, Loads model from disk, 
# # Stores it in global variable MODEL, 
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global MODEL
#     global TOKENIZER

#     MODEL =  AutoModelForSequenceClassification.from_pretrained(
#         "../saved_models/model_v1",
#         low_cpu_mem_usage=True # Reduces RAM spikes during loading
#         )

#     TOKENIZER = AutoTokenizer.from_pretrained("../saved_models/tokenizer")

#     print("Model & Tokenizer loaded successfully")

#     # When app shutdown this anything bwelow this 'yield' will excute,
#     # above things are running when app starts
#     # we can use this for : close database connection, free resources after app shutdowns
#     yield
#     print("Shutting down...")


# Loading label map from saved json file
# with open('utils/label_map.json', 'r') as f:
#     label_map = json.load(f)



# ===================== API =====================

# @app.get("/ping")
# async def ping():
#     return 'hello fastapi running'

# @app.get("/labels")
# async def labels():
#     return label_map

# @app.post("/chat")
# async def chat(request : ChatRequest):
#     user_message = request.message

#     dic = await predict_intent(user_message)
#     print(dic)

#     return {
#         "intent": dic["intent"],
#         "confidence": dic["conf"],
#         "response": get_response(dic["intent"])
#     }

# # ===================== HELPERS =====================

# async def predict_intent(msg):
#     inputs = TOKENIZER(msg, return_tensors='pt', truncation=True, padding=True)

#     with torch.no_grad():
#         outputs = MODEL(**inputs)

#     logits = outputs.logits
#     #print(f"1### {logits}")

#     probs  = F.softmax(logits, dim=1)
#     #print(f"2### {probs}")
    
#     # torch.argmax(...) return as tensor ( tensor([42]) ) 
#     # item() -> converts that tensor into a normal Python integer
#     predicted_class = torch.argmax(probs, dim=1).item()
#     # print(f"3### {torch.argmax(probs, dim=1)}")

#     confidence = torch.max(probs).item()

#     return {
#         "intent" : label_map[str(predicted_class)],
#         "conf" : confidence
#     }

# def get_response(intent):
#     # Dictionary lookup using .get(), intent does NOT exist -> "default"
#     category = intent_category.get(intent,"default")
    
#     return response_templates.get(category, response_templates["default"])

# # ===================== MAIN =====================

# if __name__ == "__main__" :
#     uvicorn.run(app=app, host='localhost', port=8000)


# # run the app : uvicorn main:app --reload
# # pip install fastapi uvicorn
# # Select interpreter in VS Code > Ctrl + Shift + P > Python: Select Interpreter > TFenv
