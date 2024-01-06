from typing import IO, Optional, List

# ! Main Encoder Class
class Encoder:
    def __init__(self, io: IO[bytes]) -> None:
        assert io.writable()
        self.io = io
    
    def dump(
        self,
        data: List[List[Optional[str]]],
        encoding: str='utf-8',
        errors: str='strict'
    ) -> None:
        for row in data:
            for value in row:
                if value is None:
                    self.io.write(b"\xFE")
                elif len(value) > 0:
                    self.io.write(value.encode(encoding, errors))
                self.io.write(b"\xFF")
            self.io.write(b'\xFD')
