
from abc import ABC, abstractmethod
from typing import Generator, Tuple

from conversor.stack_conversion import StackConversor


class CalcNotation(ABC):
    _initial_notation: int
    _initial_calculation: tuple
    _target_calculation: tuple
    _stacks: StackConversor
    PRECEDEMCE: dict = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '^^': 3
    }

    def __init__(self, original_clcltn: tuple, initial_notation: int) -> None:
        self._initial_notation = initial_notation
        self._initial_calculation = original_clcltn
        self._stacks = StackConversor(original_clcltn)

    def convert(self) -> tuple:
        possible_conversions_from: tuple = (
            self.from_prefix,
            self.from_infix,
            self.from_postfix
        )
        # Call convert from original notation
        possible_conversions_from[self._initial_notation]()
        return self._target_calculation

    def compare_precedence(self, char_current: str, char_top_stack: str) -> bool:
        return self.PRECEDEMCE[char_current] <= self.PRECEDEMCE[char_top_stack]

    @abstractmethod
    def from_prefix(self) -> None: pass

    @abstractmethod
    def from_infix(self, rev: bool = False) -> None:
        operations = self.PRECEDEMCE.keys()
        for char in self._stacks.initial:
            if char == '(':
                self._stacks.push_operator_stack(char)
            elif char == ')':
                while self._stacks.last_operator != '(':
                    self._stacks.push_final_stack(
                        self._stacks.pop_operator_stack()
                    )
                self._stacks.pop_operator_stack()
            elif char in operations:
                while not self._stacks.is_operators_empty and self.compare_precedence(char, self._stacks.last_operator):
                    self._stacks.push_final_stack(
                        self._stacks.pop_operator_stack()
                    )
                self._stacks.push_operator_stack(char)
            else:
                self._stacks.push_final_stack(char)
        while not self._stacks.is_operators_empty:
            self._stacks.push_final_stack(
                self._stacks.pop_operator_stack()
            )
        if rev:
            self._target_calculation = tuple(reversed(
                self._stacks._final_stack
            ))
        else:
            self._target_calculation = tuple(self._stacks._final_stack)

    @abstractmethod
    def from_postfix(self) -> None: pass
