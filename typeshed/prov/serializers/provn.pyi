from prov.serializers import Serializer as Serializer

class ProvNSerializer(Serializer):
    def serialize(self, stream, **kwargs) -> None: ...
    def deserialize(self, stream, **kwargs) -> None: ...
