from fastapi import APIRouter
from models.schema import EmailRequest
from services.ai_service import classify_email, generate_reply
from services.db_service import save_email, get_emails

router = APIRouter()

@router.post("/process-email")
def process_email(request: EmailRequest):
    category = classify_email(request.email_text)
    reply = generate_reply(request.email_text)

    data = {
        "email_text": request.email_text,
        "category": category,
        "ai_reply": reply,
        "status": "pending"
    }

    save_email(data)

    return {
        "category": category,
        "ai_reply": reply
    }

@router.get("/emails")
def fetch_emails():
    return get_emails().data