from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

app=FastAPI()

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

class Prompt(BaseModel):
    prompt: str

@app.get('/', tags=["root"])
async def read_root()->dict:
    return {"message":"Completions API"}

@app.post('/complete-text')
async def completions(request: Prompt)->dict:
    content=request.prompt
    print(content)
    chat_completion = client.chat.completions.create(
        messages=[
             {
            "role": "system",
            "content": "you complete the provided sentences."
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama-3.1-70b-versatile",
        )
    return{"completion":f"{content} {chat_completion.choices[0].message.content}"}