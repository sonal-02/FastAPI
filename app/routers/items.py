from fastapi import APIRouter, Depends, HTTPException
from models.items import items_db
from dependencies import get_token_header
from utils.permissions.get_permissions import check_permission

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/all")
async def get_items():
    check_permission(router)
    return items_db

@router.get("/{item_id}")
async def get_item(item_id: int):
    check_permission(router)
    item_dict = items_db.get(item_id)
    if not item_dict:
        raise HTTPException(status_code=400, detail="Item not found")
    return item_dict