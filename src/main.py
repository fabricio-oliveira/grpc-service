import asyncio
import logging
import grpc

from grpc_reflection.v1alpha import reflection


from generated.comicbook.company_pb2 import (CompanyResponse, Empty, DESCRIPTOR)
from generated.comicbook.company_pb2_grpc import (CompanyServicer, add_CompanyServicer_to_server)

from model import company


class Company(CompanyServicer):
    async def GetAll(
            self, request: Empty,
            context: grpc.aio.ServicerContext) -> CompanyResponse:
        for c in company.all():
            yield CompanyResponse(**c)


async def serve() -> None:
    server = grpc.aio.server()
    add_CompanyServicer_to_server(Company(), server)

    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['Company'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    print("🚀 Server starting. localhost:50051")
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(serve())
