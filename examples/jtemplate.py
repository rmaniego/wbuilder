#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder as wb


block = wb.Blocks()
block.for_("book in books")
block.set("id", "{{ book.id }}")
block.set("author", "{{ book.author }}")
block.if_("'children' in book.genre")
block.set("genre", "children")
block.if_("book.pages >= 300")
block.set("pages", "300")
block.elif_("book.pages >= 200")
block.set("pages", "200")
block.else_()
block.set("pages", "100")
block.endif()
block.endif()
block.else_()
block.set("id", "-1")
block.set("pages", "0")
block.set("author", "-1")
block.endfor()
print(block.build())