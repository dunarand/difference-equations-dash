from functools import lru_cache
from typing import Optional, Dict, List
import pandas as pd

class DifferenceModel:

    def __init__(self, a0: float=0, r: float=0, b: float=0):
        self.a0 = a0 if a0 is not None else 0
        self.r = r if r is not None else 0
        self.b = b if b is not None else 0

    def equilibrium(self) -> float|None:
        if self.r != 1:
            return self.b / (1 - self.r)
        elif self.r == 1 and self.b == 0:
            return self.a0
        else:
            return None

    def eval(self, n: int) -> float:
        if n < 0:
            raise ValueError("n must be greater than or equal to 0")
        if n == 0:
            return self.a0
        result = self.a0
        for _ in range(n):
            result = self.r * result + self.b
        return result

    @lru_cache(maxsize=None)
    def generate_data(self, start: Optional[int] = None, stop: int = 0) -> pd.DataFrame:
        if start is not None and stop == 0:
            stop = start
            start = 0
        elif start is None and stop == 0:
            return pd.DataFrame({'n': [0], 'a_n': [self.a0]})
        if start is None:
            start = 0
        if start < 0:
            raise ValueError("start must be greater than or equal to 0")
        if stop < start:
            raise ValueError("stop must be greater than start")
        if stop == start:
            return pd.DataFrame({'n': [start], 'a_n': [self.eval(start)]})
        results = [self.eval(start)]
        for n in range(start + 1, stop + 1):
            results.append(results[-1] * self.r + self.b)
        return pd.DataFrame({'n': list(range(start, stop + 1)), 'a_n': results})
