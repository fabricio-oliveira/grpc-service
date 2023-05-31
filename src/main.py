import asyncio
import logging
import grpc

from services import add_service_to_server


async def serve() -> None:
    server = grpc.aio.server()
    add_service_to_server(server)

    server.add_insecure_port('[::]:50051')
    print("🚀 Server starting. localhost:50051")

    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(serve())
