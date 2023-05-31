
from generated.comicbook import (company_pb2, hero_pb2)
from generated.comicbook import (company_pb2_grpc, hero_pb2_grpc)

from grpc_reflection.v1alpha import reflection

from services.company import Company
from services.hero import Hero


def add_service_to_server(server):
    company_pb2_grpc.add_CompanyServicer_to_server(Company(), server)
    hero_pb2_grpc.add_HeroServicer_to_server(Hero(), server)

    SERVICE_NAMES = (
        company_pb2.DESCRIPTOR.services_by_name['Company'].full_name,
        hero_pb2.DESCRIPTOR.services_by_name['Hero'].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)
