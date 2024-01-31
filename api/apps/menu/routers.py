from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.apps.menu import responses
from api.apps.menu import schemas
from api.apps.menu.db_interface import db_interface
from api.database import get_async_session

menu_router = APIRouter(prefix="/menu", tags=["Menu"])
menuadmin_router = APIRouter(prefix="/menuadmin", tags=["Menu Admin"])


@menu_router.get(
    "/",
    summary="Get menu client",
    description="Get menu client",
    responses={200: responses.resp_200},
)
async def get_menu(session: AsyncSession = Depends(get_async_session)):
    data = await db_interface.get_menu(session)
    return data


@menuadmin_router.get(
    "/",
    summary="Get menu for admin",
    description="Get menu for admin",
    responses={200: responses.resp_200},
)
async def get_menuadmin(session: AsyncSession = Depends(get_async_session)):
    data = await db_interface.get_menuadmin(session)
    return data


@menuadmin_router.patch(
    "/",
    summary="Part update menu for admin",
    description="Part update menu for admin",
    responses={200: responses.resp_200},
)
async def update_menuadmin(
    data: schemas.MenuAdmin, session: AsyncSession = Depends(get_async_session)
):
    response = {}
    for item in data:
        manu_name = item[0]
        menu_item = item[1]
        if menu_item is None:
            continue
        response[manu_name] = {
            "title": menu_item.title,
            "display": menu_item.display
        }
        await db_interface.update_record(session, item)

    return response


routers = (menu_router, menuadmin_router)


__all__ = ("routers",)
