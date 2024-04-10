from re import Pattern, compile
from conversor.calc_notation import CalcNotation
from conversor.register_in_core import register_in_core


@register_in_core
class ToPostfix(CalcNotation):
    def from_prefix(self) -> None: pass

    def from_infix(self) -> None:
        super().from_infix(False)

    def from_postfix(self) -> None: pass
