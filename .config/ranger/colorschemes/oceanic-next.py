# This file is part of ranger, the console file manager.
# License: GNU GPL version 3, see the file "AUTHORS" for details.
# Author: Joseph Tannhuber <sepp.tannhuber@yahoo.de>, 2013
# Solarized like colorscheme, similar to solarized-dircolors
# from https://github.com/seebi/dircolors-solarized.
# This is a modification of Roman Zimbelmann's default colorscheme.

from __future__ import (absolute_import, division, print_function)

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    cyan, magenta, red, white, default,
    normal, bold, reverse,
    default_colors,
)


class Solarized(ColorScheme):
    progress_bar_color = 74

    def use(self, context):  # pylint: disable=too-many-branches,too-many-statements
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg = 244
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = 240
                bg = 221
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = 136
                else:
                    fg = 172
            if context.container:
                fg = 73
            if context.directory:
                fg = 74
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                fg = 94
                attr |= bold
            if context.socket:
                fg = 136
                bg = 230
                attr |= bold
            if context.fifo:
                fg = 136
                bg = 230
                attr |= bold
            if context.device:
                fg = 244
                bg = 230
                attr |= bold
            if context.link:
                fg = 94 if context.good else 221
                attr |= bold
                if context.bad:
                    bg = 240
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                fg = 244
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    bg = 242
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

            if context.inactive_pane:
                fg = 241

        elif context.in_titlebar:
            attr |= bold
            if context.hostname:
                fg = 16 if context.bad else 255
                if context.bad:
                    bg = 172
            elif context.directory:
                fg = 74
            elif context.tab:
                fg = 47 if context.good else 74
                bg = 244
            elif context.link:
                fg = cyan

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = 73
                elif context.bad:
                    fg = 221
                    bg = 240
            if context.marked:
                attr |= bold | reverse
                fg = 242
                bg = 47
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 221
                    bg = 240
            if context.loaded:
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 73

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        return fg, bg, attr
