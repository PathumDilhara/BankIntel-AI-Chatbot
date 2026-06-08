from fastapi import FastAPI
import uvicorn

app = FastAPI()

# run the app : uvicorn main:app --reload
# pip install fastapi uvicorn
# Select interpreter in VS Code > Ctrl + Shift + P > Python: Select Interpreter > TFenv

@app.get("/ping")
async def ping():
    return "hello fastapi running"



if __name__ == "__main__" :
    uvicorn.run(app=app, host='localhost', port=8000)