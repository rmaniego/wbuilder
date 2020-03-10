#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder as wb


block = wb.Blocks()
block.for_("book in books")
block.set_("id", "{{ book.id }}")
block.set_("author", "{{ book.author }}")
block.if_("'children' in book.genre")
block.set_("genre", "children")
block.if_("book.pages >= 300")
block.set_("pages", "300")
block.elif_("book.pages >= 200")
block.set_("pages", "200")
block.else_()
block.set_("pages", "100")
block.endif()
block.endif()
block.else_()
block.set_("id", "-1")
block.set_("pages", "0")
block.set_("author", "-1")
block.endfor()
print(block.build())