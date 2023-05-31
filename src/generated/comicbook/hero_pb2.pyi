from google.protobuf import empty_pb2 as _empty_pb2
from comicbook import company_pb2 as _company_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroResponse(_message.Message):
    __slots__ = ["company", "id", "name"]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    company: _company_pb2.CompanyResponse
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., company: _Optional[_Union[_company_pb2.CompanyResponse, _Mapping]] = ...) -> None: ...
