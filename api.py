from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os

load_dotenv()

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}


app = FastAPI()

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid or expired API key, or no credits remaining.")
    
    return x_api_key

@app.post("/generate")
async def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="gpt-oss:20b-cloud", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}



    