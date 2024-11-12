from io import BytesIO
from typing import IO, Optional, List, Any, Generator
from .encoder import Encoder
from .decoder import Decoder

# ! Encoding Methods
def dump(
    data: List[List[Optional[str]]],
    io: IO[bytes],
    encoding: str='utf-8',
    errors: str='strict'
) -> None:
    Encoder(io).dump(data, encoding, errors)

def dumps(
    data: List[List[Optional[str]]],
    encoding: str='utf-8',
    errors: str='strict'
) -> bytes:
    bio = BytesIO()
    Encoder(bio).dump(data, encoding, errors)
    bio.seek(0)
    return bio.read()

# ! Decoding Methods
def load(
    io: IO[bytes],
    encoding: str='utf-8',
    errors: str='strict'
) -> List[List[Optional[str]]]:
    return Decoder(io).load(encoding, errors)

def load_split(
    io: IO[bytes],
    size: int=-1,
    encoding: str='utf-8',
    errors: str='strict'
) -> List[List[Optional[str]]]:
    return Decoder(io).load_split(size, encoding, errors)

def load_generator(
    io: IO[bytes],
    encoding: str='utf-8',
    errors: str='strict'
) -> Generator[List[Optional[str]], Any, None]:
    return Decoder(io).load_generator(encoding, errors)

def loads(
    data: bytes,
    encoding: str='utf-8',
    errors: str='strict'
) -> List[List[Optional[str]]]:
    return Decoder(BytesIO(data)).load(encoding, errors)

def loads_split(
    data: bytes,
    encoding: str='utf-8',
    errors: str='strict'
) -> List[List[Optional[str]]]:
    return Decoder(BytesIO(data)).load_split(-1, encoding, errors)
