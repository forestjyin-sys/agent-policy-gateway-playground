from fastapi import FastAPI
from pydantic import BaseModel
from app.policy import decide_policy
app = FastAPI(title="AI Gateway Simulation")
class ChatRequest(BaseModel):
    userId: str
    roleId: str
    message: str
class ChatResponse(BaseModel):
    allowed: bool
    model: str
    policy: str
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest) -> ChatResponse:
    model, policy = decide_policy(role_id=req.roleId)
    return ChatResponse(allowed=True, model=model, policy=policy)