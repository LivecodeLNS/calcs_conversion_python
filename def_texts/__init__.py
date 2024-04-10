from typing import Callable
from def_texts.combination_color import *
from shutil import get_terminal_size


class TextStylist:
    _columns_availible, _ = get_terminal_size()
    _columns: int
    echo: Callable

    def __init__(self, echo: Callable, max_len_clcltn: int) -> None:
        self.echo = echo
        if max_len_clcltn <= 39:
            max_len_clcltn = 39
        else:
            while (max_len_clcltn % 3 != 0) or (max_len_clcltn % 5 != 0):
                max_len_clcltn += 1
        self._columns = max_len_clcltn

    def center_text(self, msg: str, *ext) -> str:
        msg = msg.center(self._columns-2)
        if len(ext) == 2:
            ext = black_white(f' {ext[0]}'), black_white(f'{ext[1]} ')
        else:
            ext = black_white(' ║'), black_white('║ ')
        return ext[0] + msg + ext[1]

    @property
    def _line(self) -> str:
        return black_white('═'*(self._columns-2))

    def line_open(self) -> None:
        line = self.center_text(self._line, '╔', '╗')
        self.echo(line)

    def line_close(self) -> None:
        line = self.center_text(self._line, '╚', '╝')
        self.echo(line)

    def line_sep(self) -> None:
        line = self.center_text(self._line, '╠', '╣')
        self.echo(line)

    def line_empty(self) -> None:
        line: str = black_yellow(" "*(self._columns-2))
        line = self.center_text(line)
        self.echo(line)

    def title(self, text: str) -> None:
        text = text.center(self._columns-2)
        text = black_yellow(text)
        text = self.center_text(text)
        text = black_white(text)
        self.line_sep()
        self.line_empty()
        self.echo(text)
        self.line_empty()

    def info(self, text: str) -> None:
        text_centered: str = text.center(self._columns-2)
        text_colored = black_white(text_centered)
        text = self.center_text(text)
        text = text.replace(text_centered, text_colored)
        self.echo(text)
        self.line_empty()

    def calc(self, text: str) -> None:
        text_pad: str = f' {text} '
        text_colored: str = cyan_black(text_pad)
        text_centered: str | tuple[str, str, str]
        text_centered = text.center(self._columns-2)
        text_centered = text_centered.partition(text_pad)
        text_centered = (
            black_white(text_centered[0]),
            cyan_black(text_centered[1]),
            black_white(text_centered[2])
        )
        text = self.center_text(''.join(text_centered))
        self.echo(text)
        self.line_empty()

    # Here in advance, it's about exceptions

    def error_center_text(self, msg: str, *ext) -> str:
        msg = msg.center(self._columns-2)
        if len(ext) == 2:
            ext = red_white(f' {ext[0]}'), red_white(f'{ext[1]} ')
        else:
            ext = red_white(' ║'), red_white('║ ')
        return ext[0] + msg + ext[1]

    @property
    def _error_line(self) -> str:
        return red_white('═'*(self._columns-2))

    def error_line_open(self) -> None:
        line = self.error_center_text(self._error_line, '╔', '╗')
        self.echo(line)

    def error_line_close(self) -> None:
        line = self.error_center_text(self._error_line, '╚', '╝')
        self.echo(line)

    def error_line_sep(self) -> None:
        line = self.error_center_text(self._error_line, '╠', '╣')
        self.echo(line)

    def error_line_empty(self) -> None:
        line: str = red_white(" "*(self._columns-2))
        line = self.error_center_text(line)
        self.echo(line)

    def error_title(self, text: str) -> None:
        text = text.center(self._columns-2)
        text = red_white(text)
        text = self.error_center_text(text)
        self.error_line_sep()
        self.error_line_empty()
        self.echo(text)
        self.error_line_empty()

    def error_info(self, text: str) -> None:
        text_centered: str = text.center(self._columns-2)
        text_colored = red_white(text_centered)
        text = self.error_center_text(text)
        text = text.replace(text_centered, text_colored)
        self.echo(text)
        self.error_line_empty()
