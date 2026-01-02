from fastapi import FastAPI
import os
from dotenv import load_dotenv

from models import TicketCreate, Ticket
from services import AIService

load_dotenv()

# if os.getenv()



aisercive = AIService()

tickets_db=[]
app = FastAPI(title="AI app")

@app.get("/health")
def health():
    return {"Message":"Backend is running"}

@app.post("/tickets")
def tickets(ticket: TicketCreate):
    tickets_id = len(tickets_db) + 1

    prompt = f"""
    you are a support agent, given a problem by user you should answer it 
    politely, clearly and consisely.

    user query:
    title: {ticket.title}
    description : {ticket.description}

    """

    response=aisercive.generate_reply(prompt)

    new_ticket=Ticket(
        title = ticket.title,
        description = ticket.description,
        id=tickets_id,
        ai_reply = response)
    
    tickets_db.append(new_ticket)

    return{
        "msg":"Ticket created successfully",
        "ticket":new_ticket
    }

@app.get("/tickets")
def tickets():
    return tickets_db