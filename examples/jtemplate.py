#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder as wb


block = wb.Blocks()
block.for_("book in books")
block.set_var("id", "{{ book.id }}")
block.set_var("author", "{{ book.author }}")
block.if_("'children' in book.genre")
block.set_var("genre", "children")
block.if_("book.pages >= 300")
block.set_var("pages", "300")
block.elif_("book.pages >= 200")
block.set_var("pages", "200")
block.else_()
block.set_var("pages", "100")
block.endif()
block.endif()
block.else_()
block.set_var("id", "-1")
block.set_var("pages", "0")
block.set_var("author", "-1")
block.endfor()
print(block.build())