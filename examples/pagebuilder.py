#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

import wbuilder as wb
wbuilder import title, link, form, input_, button, span


# hardcoding
print("\n#1a: Use mkTag to create custom elements")
header = wb.mkTag("h1",
                         {"id": "title",
                          "class": "custom-title"},
                         "Contact Information")
print(header)
# using element builder
print("\n#1b: Use ElemBuilder to create custom elements")
box = wb.ElemBuilder().tag("div").attr("lang", "en-PH").build()
print(box)

# create element
print("\n#2: Use shortcut methods to create elements")
message = span().text("Complete all required fields.").build()
print(message)

# create element and add attributes
print("\n#3a: Create element and add attributes")
email = (input_()
         .type_("email")
         .class_("custom-input")
         .value("example@domain.com")
         .placeholder("example@domain.com")
         .maxlength("256")
         .required()
         .build())
print(email)

# create element and add attributes
print("\n#3b: Create element and add attributes")
stylesheet = (link()
         .rel("stylesheet")
         .href("https://google.com")
         .integrity("ABCDE")
         .build())
print(stylesheet)

# create element with inner html
print("\n#4: Create element with HTML content")
button = button().html("<span>Next</span>").type_("submit").build()
print(button)

# create basic html
print("\n#5: Create basic HTML")
html = wb.WebBuilder()
print(html.build())

# create html and append children
print("\n#6: Create HTML and append children")
html = wb.WebBuilder()
# USAGE: html.find("selector").append("html/string")
html.find("head").append(title().text("Form").build())
html.find("body").append(form()
                         .id_("custom-form")
                         .action("ip-address/process")
                         .method("get")
                         .build())
html.find("#custom-form").append(header).append(message).append(email).append(button)
print(html.build())
