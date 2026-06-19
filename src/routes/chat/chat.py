from fastapi import APIRouter

router = APIRouter()


@router.get("/chat")
def chat_endpoint():
	print("request to chat endpoint appeared")
	return "This is the chat router v2"
