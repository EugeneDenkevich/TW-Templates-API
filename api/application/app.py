from typing import Union
from typing import final

from fastapi import APIRouter
from fastapi import FastAPI


@final
class App(FastAPI):
    def add_routers(
        self, *routers: Union[APIRouter, tuple[APIRouter]]
    ) -> None:
        for router_group in routers:
            if isinstance(router_group, tuple):
                for router in router_group:
                    self.include_router(router)
            else:
                self.include_router(router_group)


__all__ = ("App",)
