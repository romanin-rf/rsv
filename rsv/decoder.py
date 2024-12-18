from typing import IO, Optional, List, Any, Generator

# ! Main Encoder Class
class Decoder:
    def __init__(self, io: IO[bytes]) -> None:
        assert io.readable()
        assert io.seekable()
        self.io = io
    
    def load_generator(
        self,
        encoding: str='utf-8',
        errors: str='strict'
    ) -> Generator[List[Optional[str]], Any, None]:
        yield from []
        row: List[Optional[str]] = []
        value_start_index = self.io.tell()
        while len(data:=self.io.read(1)) > 0:
            if data == b"\xFF":
                value_length = self.io.tell() - value_start_index - 1
                self.io.seek(value_start_index)
                value_data = self.io.read(value_length)
                if value_data == b"\xFE":
                    row.append(None)
                else:
                    row.append(value_data.decode(encoding, errors))
                value_start_index = self.io.tell() + 1
                self.io.seek(value_start_index)
            elif data == b"\xFD":
                yield row.copy()
                row.clear()
                value_start_index = self.io.tell()
    
    def load(
        self,
        encoding: str='utf-8',
        errors: str='strict'
    ) -> List[List[Optional[str]]]:
        return [row for row in self.load_generator(encoding, errors)]
    
    def load_split(
        self,
        size: int=-1,
        encoding: str='utf-8',
        errors: str='strict'
    ) -> List[List[Optional[str]]]:
        return [
            [
                None if vd == b'\xFE' else vd.decode(encoding, errors) for vd in rd.split(b'\xFF')[:-1]
            ] for rd in self.io.read(size).split(b'\xFD')[:-1]
        ]
