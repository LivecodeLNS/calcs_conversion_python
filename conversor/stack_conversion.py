from typing import List
from conversor.register_in_core import register_in_core


@register_in_core
class StackConversor:
    _initial_stack: tuple[str, ...] = ()
    _operator_stack: List[str] = []
    _final_stack: List[str] = []

    def __init__(self, initial_calculation: tuple) -> None:
        self._initial_stack = initial_calculation

    @property
    def last_operator(self) -> str:
        return self._operator_stack[-1]

    @property
    def is_operators_empty(self) -> bool:
        return len(self._operator_stack) == 0

    @property
    def initial(self) -> tuple:
        return self._initial_stack

    def push_final_stack(self, operand: str) -> None:
        self._final_stack.append(operand)

    def push_operator_stack(self, operator: str) -> None:
        self._operator_stack.append(operator)

    def pop_operator_stack(self) -> str:
        return self._operator_stack.pop()
