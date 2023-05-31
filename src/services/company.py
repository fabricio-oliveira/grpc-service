import grpc

from models import company

from generated.comicbook.company_pb2_grpc import (CompanyServicer)
from generated.comicbook.company_pb2 import (CompanyResponse)
from google.protobuf.empty_pb2 import Empty


class Company(CompanyServicer):
    async def GetAll(
            self, request: Empty,
            context: grpc.aio.ServicerContext) -> CompanyResponse:
        for c in company.all():
            yield CompanyResponse(**c)