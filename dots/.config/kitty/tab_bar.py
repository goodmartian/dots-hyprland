from kitty.fast_data_types import Screen
from kitty.tab_bar import DrawData, ExtraData, TabBarData, as_rgb


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_tab_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    orig_fg = screen.cursor.fg
    orig_bg = screen.cursor.bg

    active_fg = as_rgb(0xFFFFFF)
    active_accent = as_rgb(0x5F8787)
    inactive_fg = as_rgb(0x666666)
    inactive_accent = as_rgb(0x333333)
    bg = as_rgb(0x000000)

    screen.cursor.bg = bg

    title = tab.title
    if ":" in title:
        title = title.split(":", 1)[-1]
    title = title.rsplit("/", 1)[-1] or "~"
    if len(title) > 15:
        title = title[:15] + "…"

    if tab.is_active:
        screen.cursor.fg = active_accent
        screen.draw(" ● ")
        screen.cursor.fg = active_fg
        screen.cursor.bold = True
    else:
        screen.cursor.fg = inactive_accent
        screen.draw(" ○ ")
        screen.cursor.fg = inactive_fg
        screen.cursor.bold = False

    screen.draw(title)
    screen.cursor.bold = False
    screen.draw(" ")

    screen.cursor.fg = orig_fg
    screen.cursor.bg = orig_bg

    return screen.cursor.x
