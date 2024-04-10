from re import Pattern, compile
from typing import Tuple
from conversor.calc_notation import CalcNotation
from conversor.register_in_core import register_in_core
from conversor.stack_conversion import StackConversor


@register_in_core
class ToPrefix(CalcNotation):
    def from_prefix(self) -> None: pass

    def from_infix(self) -> None:
        parenthesis_compiled: Pattern = compile(r'(\()(.+?)(\))')
        expression: str | tuple
        expression = ' '.join(self._stacks.initial)
        while parenthesis_compiled.search(expression):
            expression = parenthesis_compiled.sub(r'\3\2\1', expression)
        self._stacks._initial_stack = tuple(reversed(expression.split()))
        super().from_infix(True)

    def from_postfix(self) -> None: pass
