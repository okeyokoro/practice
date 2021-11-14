
"""
let’s write a Python program that interpolates points
"""

from typing import Tuple, List, Union

Number = Union[int, float]

def interpolate(points: List[Tuple[Number, Number]]) -> str:
    degree = len(points)-1
    for i in range(len(points)):
        prod = 1
        for j in range(len(points)):
            if j != i:
                coef = """\
                    (x - xj)
                    --------
                    (xi - xj)
                """
                prod *= coef

