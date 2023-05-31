
from generated.comicbook.company_pb2 import (DESCRIPTOR)
from generated.comicbook.company_pb2_grpc import (add_CompanyServicer_to_server)

from grpc_reflection.v1alpha import reflection
from services.company import Company


def add_service_to_server(server):
    add_CompanyServicer_to_server(Company(), server)
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['Company'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
