from fastapi import APIRouter, Depends, HTTPException, status
from models.items import items_db
from dependencies import get_token_header
from utils.permissions.get_permissions import Permission

router = APIRouter(
    prefix="/items",
    tags=["Items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/all")
async def get_items():
    """
    This api is used to return all items if user have access
    """
    permission = Permission(router)
    permission.check_permission()
    return items_db


@router.get("/{item_id}")
async def get_item(item_id: int):
    """
    This api is used to return specific item if user have access
    """
    permission = Permission(router)
    permission.check_permission()
    item_dict = items_db.get(item_id)
    if not item_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item_dict
