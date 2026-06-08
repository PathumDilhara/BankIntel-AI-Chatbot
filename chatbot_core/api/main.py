from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager
import json

from transformers  import AutoModelForSequenceClassification

from schemas import ChatRequest

# global variable : load once used in several functions
MODEL = None

# When FastAPI starts > It pauses API startup, Runs this code, Loads model from disk, 
# Stores it in global variable MODEL, 
@asynccontextmanager
async def lifespan(app: FastAPI):
    global MODEL
    MODEL =  AutoModelForSequenceClassification.from_pretrained(
        "../saved_models/model_v1",
        low_cpu_mem_usage=True # Reduces RAM spikes during loading
        )
    print("Model loaded successfully")

    # When app shutdown this anything bwelow this 'yield' will excute,
    # above things are running when app starts
    # we can use this for : close database connection, free resources after app shutdowns
    yield
    print("Shutting down...")


# Use this lifespan system to manage startup/shutdown
app = FastAPI(lifespan=lifespan)


# Loading label map from saved json file
with open('utils/label_map.json', 'r') as f:
    label_map = json.load(f)

@app.get("/ping")
async def ping():
    return 'hello fastapi running'

@app.post("/chat")
async def chat(request : ChatRequest):
    user_message = request.message

    # test
    return {
        "intent": "receiving_money",
        "confidence": 0.95,
        "response": "You can receive your salary into your account."
    }


if __name__ == "__main__" :
    uvicorn.run(app=app, host='localhost', port=8000)


# run the app : uvicorn main:app --reload
# pip install fastapi uvicorn
# Select interpreter in VS Code > Ctrl + Shift + P > Python: Select Interpreter > TFenv
