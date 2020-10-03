"""
    wBuilder Tuts
    (c) 2020 Rodney Maniego Jr.
"""

import wbuilder.wbuilder as wb
from wbuilder.wbuilder import WebBuilder
from wbuilder.wbuilder import title, link, form, Input, button, span


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
email = (Input()
         .Type("email")
         .Class("custom-input")
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
button = button().html("<span>Next</span>").Type("submit").build()
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
                         .Id("custom-form")
                         .action("ip-address/process")
                         .method("get")
                         .build())
html.find("#custom-form").append(header).append(message).append(email).append(button)
print(html.build())

## generate full html
print("\n#6a: Create and save full html document, set html.build() to return HTML string")
def templater(page, show_html=False):
    # initialize web builder
    html = wb.WebBuilder() 
    
    ## prepare head contents
    html.find("head").append(wb.title().text(page).build())
    html.find("head").append(wb.meta().charset("UTF-8").build())
    html.find("head").append(wb.meta()
                             .name("viewport")
                             .content("width=device-width, initial-scale=1, shrink-to-fit=no")
                             .build())
    html.find("head").append(wb.link()
                             .rel("icon")
                             .href("icon.png")
                             .Type("image/png")
                             .sizes("96x96")
                             .build(), static=True)
    html.find("head").append(wb.link()
                             .rel("stylesheet")
                             .href("reset.css")
                             .build(), static=True)
    html.find("head").append(wb.link()
                             .rel("stylesheet")
                             .href("custom.css")
                             .build(), static=True)
    
    ## load body contents
    html.find("body").append(wb.div(Id="progress", Class="progress").data("progress", "-1").build())
    html.find("body").append(wb.div(Id="body-loader", Class="loader loader-bg spin postload")
                             .data("tk", "modal,nav,feed,footer").build())
    
    ## load scripts after body contents
    html.find("body").append(wb.script()
                             .src("jquery-3.5.1.min.js", True)
                             .build(), static=True)
    html.find("body").append(wb.script()
                             .src("custom.js")
                             .build(), static=True)
    
    html.save(f"{page}.html")

## generate snippets / for ajax updates
print("\n#6b: Create html snippet")
def snippet():
    html = WebBuilder(wb.div(Id="loader-msg", Class="feed-contents content-center hide").build())
    html.find("#loader-msg").append(wb.div(Class="feed-content content-center").build())
    html.find(".feed-content").append(wb.span(Class="loader-msg-label")
                             .text("Busy, please wait...")
                             .build())
    return html.build()
print(snippet())
