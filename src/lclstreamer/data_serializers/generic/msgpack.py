from collections.abc import Iterator

import msgpack
import msgpack_numpy  # type: ignore[import-untyped]

from ...models.parameters import MsgpackBinarySerializerParameters
from ...utils.logging import log_error_and_exit
from ...utils.protocols import DataSerializerProtocol
from ...utils.typing import StrFloatIntNDArray

msgpack_numpy.patch()


class MsgpackBinarySerializer(DataSerializerProtocol):
    """
    See documentation of the `__init__` function.
    """

    def __init__(self, parameters: MsgpackBinarySerializerParameters) -> None:
        """
        Initializes an MsgPack data serializer

        This serializers turns a dictionary of numpy arrays into a MsgPack binary blob

        Arguments:

            parameters: The configuration parameters
        """
        if parameters.type != "MsgpackBinarySerializer":
            log_error_and_exit(
                "Data serializer parameters do not match the expected type"
            )

    def __call__(
        self, stream: Iterator[dict[str, StrFloatIntNDArray | None]]
    ) -> Iterator[bytes]:
        """
        Serializes data to a MsgPack binary blob

        Arguments:

            data: A dictionary storing numpy arrays

        Returns

            byte_block: A binary blob (a bytes object)
        """
        for data in stream:
            yield msgpack.packb(data)
