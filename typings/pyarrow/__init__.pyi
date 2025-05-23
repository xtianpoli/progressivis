from typing import Optional, List, Any, Iterator


class ArrowInvalid(Exception):
    ...


class ArrowNotImplementedError(Exception):
    ...


class Schema:

    names: List[str]
    types: List[Any]
    ...

class Scalar:
    def as_py(self) -> Any: ...
    def cast(self, typ: Any) -> Any: ...

class DataType: ...
class BooleanArray: ...

class Array:
    null_count: int
    type: DataType
    def is_null(self, x: Any = None) -> BooleanArray: ...
    def cast(self, typ: Any) -> Array: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Scalar]: ...

class RecordBatch:

    num_rows: int
    schema: Schema
    columns: Any
    type: DataType

    def from_pandas(self, schema: Optional[Schema] = None) -> RecordBatch: ...
    def __len__(self) -> int: ...

    @staticmethod
    def from_arrays(v: Any, names: List[str]) -> RecordBatch:
        ...

    def __iter__(self) -> Iterator[Array]: ...

    def filter(self, filt: Array) -> RecordBatch: ...

    def __getitem__(self, col: str) -> Array: ...

class Table:
    @staticmethod
    def from_batches(v: List[RecordBatch]) -> "Table": ...


class compute:
    @staticmethod
    def sum(v: Any) -> Any:
        ...

    @staticmethod
    def invert(v: Any) -> Any:
        ...

    @staticmethod
    def or_(v1: Any, v2: Any) -> Any:
        ...

def array(v: Any, type: Any) -> Any:
    ...

class TimestampArray:
    ...

class lib:
    class RecordBatchReader:
        def read_next_batch(self) -> RecordBatch: ...


__all__ = ["lib"]
