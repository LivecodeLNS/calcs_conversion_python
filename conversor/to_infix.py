from typing import Tuple
from conversor.calc_notation import CalcNotation
from conversor.register_in_core import register_in_core
from conversor.stack_conversion import StackConversor


@register_in_core
class ToInfix(CalcNotation):
    def from_prefix(self) -> None: pass
    def from_infix(self) -> None: pass
    def from_postfix(self) -> None: pass
