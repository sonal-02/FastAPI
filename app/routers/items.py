from fastapi import APIRouter, Depends, HTTPException
from models.items import items_db
from dependencies import get_item_token

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_item_token)],
    responses={404: {"description": "Not found"}},
)

@router.get("/all")
async def get_items():
    return items_db

@router.get("/{item_id}")
async def get_item(item_id: int):
    item_dict = items_db.get(item_id)
    if not item_dict:
        raise HTTPException(status_code=400, detail="Incorrect item")
    return item_dict