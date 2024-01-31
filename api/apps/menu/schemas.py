from typing import final

from pydantic import BaseModel
from pydantic import StrictBool
from pydantic import StrictStr
from pydantic import constr


class Base(BaseModel):
    id: int
    display: bool
    title: str


class MenuItem(BaseModel):
    title: StrictStr = constr(min_length=1, strip_whitespace=True)
    display: StrictBool


@final
class MenuAdmin(BaseModel):
    home: MenuItem = None
    about: MenuItem = None
    houses: MenuItem = None
    kitchen: MenuItem = None
    entertainments: MenuItem = None
    nearests: MenuItem = None
    special: MenuItem = None
    rules: MenuItem = None
    gallery: MenuItem = None
    contacts: MenuItem = None


@final
class Home(Base):
    pass


@final
class About(Base):
    pass


@final
class Houses(Base):
    pass


@final
class Kitchen(Base):
    pass


@final
class Entertainments(Base):
    pass


@final
class Nearests(Base):
    pass


@final
class Special(Base):
    pass


@final
class Rules(Base):
    pass


@final
class Gallery(Base):
    pass


@final
class Contacts(Base):
    pass
