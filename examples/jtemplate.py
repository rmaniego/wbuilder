#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder as wb


block = wb.Blocks()
block.for_("book in books")
block.setv("id", "{{ book.id }}")
block.setv("author", "{{ book.author }}")
block.if_("'children' in book.genre")
block.setv("genre", "children")
block.if_("book.pages >= 300")
block.setv("pages", "300")
block.elif_("book.pages >= 200")
block.setv("pages", "200")
block.else_()
block.setv("pages", "100")
block.endif()
block.endif()
block.else_()
block.setv("id", "-1")
block.setv("pages", "0")
block.setv("author", "-1")
block.endfor()
print(block.build())