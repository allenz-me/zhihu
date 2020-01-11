from abc import abstractmethod
from collections.abc import Iterable, Sequence
from typing import _T_co, overload


class SLList(Sequence):

    @overload
    def __getitem__(self, i: int) -> _T_co: ...

    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[_T_co]: ...

    def __getitem__(self, i: int) -> _T_co:
        pass

    def __len__(self) -> int:
        pass

    def __init__(self):
        pass
