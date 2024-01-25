from typing import final

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import registry

Base: registry = declarative_base()


class BaseMenu:
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    display = Column(Boolean, default=True, nullable=False)


@final
class Home(Base, BaseMenu):
    __tablename__ = "home"

    title = Column(String, nullable=False, unique=True)


@final
class About(Base, BaseMenu):
    __tablename__ = "about"

    title = Column(String, nullable=False, unique=True)


@final
class Houses(Base, BaseMenu):
    __tablename__ = "menu"

    title = Column(String, nullable=False, unique=True)


@final
class Kitchen(Base, BaseMenu):
    __tablename__ = "houses"

    title = Column(String, nullable=False, unique=True)


@final
class Entertainments(Base, BaseMenu):
    __tablename__ = "entertainments"

    title = Column(String, nullable=False, unique=True)


@final
class Nearests(Base, BaseMenu):
    __tablename__ = "nearests"

    title = Column(String, nullable=False, unique=True)


@final
class Special(Base, BaseMenu):
    __tablename__ = "special"

    title = Column(String, nullable=False, unique=True)


@final
class Rules(Base, BaseMenu):
    __tablename__ = "rules"

    title = Column(String, nullable=False, unique=True)


@final
class Gallery(Base, BaseMenu):
    __tablename__ = "gallery"

    title = Column(String, nullable=False, unique=True)


@final
class Contacts(Base, BaseMenu):
    __tablename__ = "contacts"

    title = Column(String, nullable=False, unique=True)


menu_metadata = Base.metadata
