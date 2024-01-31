from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.apps.menu import enums
from api.apps.menu import models
from api.apps.menu.schemas import MenuItem


class DBInterface:
    async def get_menuadmin(self, session: AsyncSession):
        data = {}
        for m in enums.Menu.list():
            query = select(getattr(models, m))
            selection = await session.execute(query)
            record = selection.fetchone()[0]
            title = record.title
            display = record.display
            obj = {
                "title": title,
                "display": display,
            }
            data[m.lower()] = obj
        return data

    async def get_menu(self, session: AsyncSession):
        data = {}
        for m in enums.Menu.list():
            query = select(getattr(models, m))
            selection = await session.execute(query)
            record = selection.fetchone()[0]
            title = record.title
            display = record.display
            if display:
                obj = {
                    "title": title,
                    "display": display,
                }
                data[m.lower()] = obj
        return data

    async def update_record(
        self, session: AsyncSession, item: tuple[str, MenuItem]
    ):

        table = getattr(models, item[0].capitalize())
        title = item[1].title
        display = item[1].display
        
        stmt = update(table).values(title=title, display=display).where(table.id == 1)
        await session.execute(stmt)
        await session.commit()


db_interface = DBInterface()
