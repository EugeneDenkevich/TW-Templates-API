import pathlib as pt
import sys

sys.path.append(str(pt.Path(__file__).parent.parent.resolve()))


from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from api.apps.menu import models
from api.settings import settings


class DBSession:
    engine = create_engine(url=settings.ALEMBIC_DB_URL, echo=True)

    def get_session(self):
        with Session(self.engine) as session:
            return session


class DBInit:
    session: Session = DBSession().get_session()
    admin_menu = [
        "Home",
        "About",
        "Houses",
        "Kitchen",
        "Entertainments",
        "Nearests",
        "Special",
        "Rules",
        "Gallery",
        "Contacts",
    ]

    def create_menu(self):
        try:
            for record in self.admin_menu:
                self._create_record(record)

        except Exception as e:
            raise f"DBInierror: {e}"

    def _create_record(self, record):
        _class = getattr(models, record)  # Get class implicitly

        query = select(_class)
        rec = self.session.execute(query).fetchone()

        if not rec:
            rec = _class(title=record, display=True)
            self.session.add(rec)
            self.session.commit()
            return

        print(f"Already exists: {record}")


db_init = DBInit()
db_init.create_menu()
