from pydantic import BaseModel,Field

class TicketCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=5, max_length=1000)

class Ticket(TicketCreate):
    id: int
    ai_reply: str | None = None