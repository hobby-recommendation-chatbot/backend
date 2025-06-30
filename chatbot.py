from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="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")  # 직접 넣거나 환경변수로 불러오기

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "당신은 친절하고 유쾌한 챗봇입니다."},
                {"role": "user", "content": req.message},
            ],
            max_tokens=150,
            temperature=0.8,
        )
        answer = response.choices[0].message.content
        return {"response": answer.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
