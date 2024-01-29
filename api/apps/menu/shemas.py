from typing import final

from pydantic import BaseModel


class Base(BaseModel):
    id: int
    display: bool
    title: str


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
