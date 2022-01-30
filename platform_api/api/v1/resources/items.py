from fastapi import APIRouter
from typing import Any, List

from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


router = APIRouter()

@router.get("/", response_model=List[Item])
def read_items() -> Any:
    data = [
        {
            "title": "string",
            "description": "string",
            "id": 0,
            "owner_id": 0
        }
    ]
    return data