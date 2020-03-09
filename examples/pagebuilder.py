#!/usr/bin/env python3
"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

from wbuilder import wbuilder
from wbuilder.wbuilder import head, title, link, body, form, a, input_, button, span


# hardcoding
print("\n#1: Use mkTag to create custom elements")
header = wbuilder.mkTag("h1",
                         {"id": "title",
                          "class": "custom-title"},
                         "Contact Information")
print(header)

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
html = wbuilder.WebBuilder()
print(html.build())

# create html and append children
print("\n#6: Create HTML and append children")
html = wbuilder.WebBuilder()
# USAGE: html.find("selector").append("html/string")
html.find("head").append(title().text("Form").build())
html.find("body").append(form()
                         .id_("custom-form")
                         .action("ip-address/process")
                         .method("get")
                         .build())
html.find("#custom-form").append(header).append(message).append(email).append(button)
print(html.build())
