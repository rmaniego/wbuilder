#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder as wb

block = wb.Block()
block.for_("book in books")
block.if_("book.id == 1")

block.elif_("book.id == 2")
block.else_()
block.endfor()
block.else_()
block.endfor()