# wBuilder
```
    wBuilder
    (c) 2020 Rodney Maniego Jr.
    MIT License
```

HTML template generator module for Python.

Read: [Introducing wBuilder: An HTML5 Generator for Python](https://peakd.com/hive-102677/@oniemaniego/introducing-wbuilder-an-html5-generator-for-python)

*Requirements:*
- BS4

Go to `examples/pagebuilder.py` for basic usage.
Returned value is in string and can be saved into file.

*Future Features*
- Basic JQuery generator

## Usage
### hardcoding
```python
print("\n#1a: Use mkTag to create custom elements")
header = mkTag("h1",
                         {"id": "title",
                          "class": "custom-title"},
                         "Contact Information")
print(header)
```

### using element builder
```python
print("\n#1b: Use ElemBuilder to create custom elements")
box = ElemBuilder().tag("div").attr("lang", "en-PH").build()
print(box)
```

### create element
```python
print("\n#2: Use shortcut methods to create elements")
message = span().text("Complete all required fields.").build()
print(message)
```

### create element and add attributes
```python
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
```

### create element and add attributes
```python
print("\n#3b: Create element and add attributes")
stylesheet = (link()
         .rel("stylesheet")
         .href("https://example.com/resources/design.css")
         .integrity("ABCDE")
         .build())
print(stylesheet)
```

### create element with inner html
```python
print("\n#4: Create element with HTML content")
button = button().html("<span>Next</span>").Type("submit").build()
print(button)
```

### create basic html
```python
print("\n#5: Create basic HTML")
html = WebBuilder()
print(html.build())
```

### create html and append children
```python
print("\n#6: Create HTML and append children")
html = WebBuilder()
```

### USAGE: html.find("selector").append("html/string")
```python
html.find("head").append(title().text("Form").build())
html.find("body").append(form()
                         .Id("custom-form")
                         .action("ip-address/process")
                         .method("get")
                         .build())
html.find("#custom-form").append(header).append(message).append(email).append(button)
print(html.build())
```

### generate full html
```python
print("\n#7a: Create and save full html document, set html.build() to return HTML string")
def templater(page, show_html=False):
    # initialize web builder
    html = WebBuilder() 
    
    ## prepare head contents
    html.find("head").append(title().text(page).build())
    html.find("head").append(meta().charset("UTF-8").build())
    html.find("head").append(meta()
                             .name("viewport")
                             .content("width=device-width, initial-scale=1, shrink-to-fit=no")
                             .build())
    html.find("head").append(link()
                             .rel("icon")
                             .href("icon.png")
                             .Type("image/png")
                             .sizes("96x96")
                             .build(), static=True)
    html.find("head").append(link()
                             .rel("stylesheet")
                             .href("reset.css")
                             .build(), static=True)
    html.find("head").append(link()
                             .rel("stylesheet")
                             .href("custom.css")
                             .build(), static=True)
    
    ## load body contents
    html.find("body").append(div(Id="progress", Class="progress").data("progress", "-1").build())
    html.find("body").append(div(Id="body-loader", Class="loader loader-bg spin postload")
                             .data("tk", "modal,nav,feed,footer").build())
    
    ## load scripts after body contents
    html.find("body").append(script()
                             .src("jquery-3.5.1.min.js", True)
                             .build(), static=True)
    html.find("body").append(script()
                             .src("custom.js")
                             .build(), static=True)
    
    html.save(f"{page}.html")
```

### generate snippets / for ajax updates
```python
print("\n#7b: Create html snippet")
def snippet():
    html = WebBuilder(div(Id="loader-msg", Class="feed-contents content-center hide").build())
    html.find("#loader-msg").append(div(Class="feed-content content-center").build())
    html.find(".feed-content").append(span(Class="loader-msg-label")
                             .text("Busy, please wait...")
                             .build())
    return html.build()
print(snippet())
```

## Usage Css
**Initialize**
```python
print("\n# Initialize...")
css = Css(sort=True)
```

**Show all selectors**
```python
print("\n# Bulk add dfrom string...")
css.add_from_string(".box", "width: 200px; height: 100px")
```

**Show all selectors**
```python
print("\n# Bulk add dictionary...")
css.add(".btn", { "font-size": "16px",
                  "background-color": "#f0f0f0",
                  "color": "#c0c0c0"})
```

**Show all selectors**
```python
print("\n# Add by property...")
css.update("body", "font-size", "12px")
css.update(".nav", "position", "fixed")
css.update(".nav", "font-size", "14px")
```

**Show all selectors**
```python
print("\n# Show all selectors...")
print(css.build())
```

**Save to file**
```python
print("\n# Save to file...")
css.save("static", "design.css")
```

**Remove selector data**
```python
print("\n# Remove selector data..")
css.remove(".nav")
print(css.build())
```
