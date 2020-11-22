# wBuilder
```
    wBuilder
    (c) 2020 Rodney Maniego Jr.
    MIT License
```

HTML template generator for Python.

Read: [Introducing wBuilder: An HTML5 Generator for Python](https://peakd.com/hive-102677/@oniemaniego/introducing-wbuilder-an-html5-generator-for-python)

*Requirements:*
- BS4

Go to `examples/*.py` for basic usage.
Returned value is in string and can be saved into file.

*Future Features*
- Basic JQuery generator

## WebBuilder Usage
**Import**
```python
from wbuilder.wbuilder import WebBuilder
```

**Initialize**
```python
html = WebBuilder()
```

**Basic usage**
```python
html.at("body").button().text("OK").done()
```

**HTML head**
```python
html.at("head").title().text("WebBuilder").done()
html.at("head").meta().charset("UTF-8").done()
html.at("head").meta().name("viewport").content("width=device-width, initial-scale=1, shrink-to-fit=no").done()
html.at("head").link().rel("icon").href("icon.png").Type("image/png").sizes("96x96").done(static=True)
html.at("head").link().rel("stylesheet").href("reset.css").done(static=True)
html.at("head").link().rel("stylesheet").href("design.css").done()
```

**CSS options**
```python
# No CSS
html.at("body").div("prompt-msg", "popup").done()

# CSS as a string
html.at("#prompt-msg").div(Class="header").text("Welcome!").css(".header", "font-size: 14px; font-weight: bold;").done()

# CSS as a dictionary
design = { "font-size": "12px",
           "color": "#222",
           "background-color": "#f0f0f0" }
html.at("#prompt-msg").div(Class="message").text("Lorem ipsum...").css(".message", design).done()
```

**Preview HTML**
```python
print(html.build())
```

**Save to file**
```python
# defaults
html.save_to_html()
html.save_stylesheet()

# custom filepaths
html.save_to_html("templates", "home.html")
html.save_stylesheet("static", "custom.css")
```

## Css class
**Initialize**
```python
from wbuilder.wbuilder import Css


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
