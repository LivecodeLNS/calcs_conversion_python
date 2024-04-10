from typing import Tuple, Union
from conversor.register_in_core import register_in_core
from conversor.to_infix import ToInfix
from conversor.to_postfix import ToPostfix
from conversor.to_prefix import ToPrefix


@register_in_core
class Conversor:
    __initial_notation: int = -1
    __possible_conversion: list = [ToPrefix, ToInfix, ToPostfix]
    __strategy: Union[ToPrefix, ToInfix, ToPostfix]

    def __init__(self, original_clcltn: tuple[str, ...], initial_notation: int, target_notation: int) -> None:
        self.__strategy = self.__possible_conversion[target_notation](
            original_clcltn, initial_notation
        )

    def convert(self) -> Tuple[str, ...]:
        return self.__strategy.convert()
