# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from comicbook import company_pb2 as comicbook_dot_company__pb2


class CompanyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAll = channel.unary_stream(
                '/commicbook.Company/GetAll',
                request_serializer=comicbook_dot_company__pb2.Empty.SerializeToString,
                response_deserializer=comicbook_dot_company__pb2.CompanyResponse.FromString,
                )


class CompanyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompanyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAll': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=comicbook_dot_company__pb2.Empty.FromString,
                    response_serializer=comicbook_dot_company__pb2.CompanyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'commicbook.Company', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Company(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/commicbook.Company/GetAll',
            comicbook_dot_company__pb2.Empty.SerializeToString,
            comicbook_dot_company__pb2.CompanyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)