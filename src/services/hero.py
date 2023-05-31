import grpc

from models import hero

from generated.comicbook.hero_pb2_grpc import (HeroServicer)
from generated.comicbook.hero_pb2 import (HeroResponse)
from google.protobuf.empty_pb2 import Empty


class Hero(HeroServicer):
    async def GetAll(
            self, request: Empty,
            context: grpc.aio.ServicerContext) -> HeroResponse:
        for h in hero.all():
            yield HeroResponse(**h)
