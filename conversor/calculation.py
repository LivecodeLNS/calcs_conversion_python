from re import Match, Pattern, search, compile, sub
from conversor.conversor import Conversor
from conversor.register_in_core import register_in_core


@register_in_core
class Calculation:
    __OPERATORS: tuple[str, str, str, str, str] = ('+', '-', '*', '/', '^')
    __initial_calculation: tuple
    __initial_notation: int
    __target_calculation: tuple
    __target_notation: int

    def __init__(self, clcltn: str, target_notation: int) -> None:
        self.__validate(clcltn, target_notation)
        self.__initial_calculation = self.__normalize(clcltn)
        self.__detect_initial_notation()
        self.__target_notation = target_notation-1
        self.__target_calculation = ()

    def __detect_initial_notation(self) -> None:
        if self.__initial_calculation[0] in self.__OPERATORS:
            self.__initial_notation = 0
        elif self.__initial_calculation[-1] not in self.__OPERATORS:
            self.__initial_notation = 1
        else:
            self.__initial_notation = 2

    @property
    def state(self) -> dict:
        notation: tuple[str, str, str] = ('PREFIX', 'INFIX', 'POSTFIX')
        orgc:str = ' '.join(self.__initial_calculation)
        return {
            'len_initial_calculation': len(orgc),
            'initial_calculation': orgc,
            'initial_notation': notation[self.__initial_notation],
            'target_notation': notation[self.__target_notation],
            'target_calculation': ' '.join(self.__target_calculation)
        }

    def convert(self) -> None:
        conversor: Conversor = Conversor(
            self.__initial_calculation, self.__initial_notation, self.__target_notation)
        self.__target_calculation = conversor.convert()

    def raise_e(self, reason: str) -> None:
        raise ValueError(reason)

    def __validate(self, clcltn: str, objn: int) -> None:
        has_valid_objective: bool = 0 <= objn <= 3
        has_min_len: bool = len(clcltn) >= 3
        has_chars: Match | None = search(
            r'.{,2}([^\d\s\.\,\+\-\*\/\^\(\)]).{,2}',
            clcltn
        )
        has_invalid_operation: Match | None = search(
            r'[\.\+\-\*\/\^]\s*[\}\]\)]|[\{\[\(]\s*[\.\+\-\*\/\^]', clcltn
        )
        if has_valid_objective and has_min_len and not has_chars and not has_invalid_operation:
            return
        if not has_valid_objective:
            self.raise_e(
                'It hasn\'t valid objective notation to do the conversion'
            )
        elif not has_min_len:
            self.raise_e(
                'It hasn\'t minimun length to do the conversion'
            )
        elif has_chars:
            self.raise_e(
                f'It has unsupported characters: {has_chars[1]}'
            )
        elif has_invalid_operation:
            self.raise_e(
                f'It has bad syntax in position {
                    has_invalid_operation.pos+1}: {has_invalid_operation[0]}'
            )

    def __normalize(self, clcltn: str) -> tuple:
        clcltn = sub(
            r'\ {2,}',
            r' ',
            clcltn.strip()
        )
        clcltn = sub(
            r'\,{2,}',
            r',',
            clcltn
        )
        clcltn = sub(
            r'(\d+)\.{2,}(\d+)',
            r'\1.\2',
            clcltn
        )
        clcltn = sub(
            r'(\d)([\,\-\+\*\/\^\(\)])',
            r'\1 \2',
            clcltn
        )
        clcltn = sub(
            r'([\,\-\+\*\/\^\(\)])(\d)',
            r'\1 \2',
            clcltn
        )
        regex_compiled_overflow = compile(
            r'([\,\-\+\*\/\^\(\)])([\,\-\+\*\/\^\(\)])'
        )
        while regex_compiled_overflow.search(clcltn):
            clcltn = regex_compiled_overflow.sub(
                r'\1 \2',
                clcltn
            )
        return tuple(
            clcltn.split()
        )
