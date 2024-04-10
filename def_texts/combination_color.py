def black_white(msg: str) -> str:
    color: str = '{bg_black}{fg_lightwhite_ex}'
    colors_len: int = len('{bg_black}{fg_lightcyan_ex}')
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset


def black_yellow(msg: str) -> str:
    color: str = '{bg_black}{fg_lightyellow_ex}'
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset


def black_cyan(msg: str) -> str:
    color: str = '{bg_black}{fg_lightcyan_ex}'
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset
def cyan_black(msg: str) -> str:
    color: str = '{bg_cyan}{fg_black}'
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset

def blue_yellow(msg: str) -> str:
    color: str = '{bg_blue}{fg_lightyellow_ex}'
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset


def red_white(msg: str) -> str:
    color: str = '{bg_red}{fg_lightwhite_ex}'
    colors_len: int = len('{bg_black}{fg_lightcyan_ex}')
    reset: str = '{bg_reset}{fg_reset}'
    return color+msg+reset
