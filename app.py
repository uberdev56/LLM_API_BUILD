from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/generate")
def generate_response(prompt: str):
    response = ollama.chat(model="gpt-oss:20b-cloud", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}