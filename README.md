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

**HTML head**
```python
html.at("head").title().text("WebBuilder").done()
html.at("head").meta().charset("UTF-8").done()
html.at("head").meta().name("viewport").content("width=device-width, initial-scale=1, shrink-to-fit=no").done()
html.at("head").link().rel("icon").href("icon.png").Type("image/png").sizes("96x96").done(static=True)
html.at("head").link().rel("stylesheet").href("reset.css").done(static=True)
html.at("head").link().rel("stylesheet").href("design.css").done()
```

**Basic usage**
```python
html.at("body").button().text("OK").done()
html.at("body").href(Id="link").href("#", cached=False).text("OK").done()
html.at("body").script(Id="script").src("/path/to/js", cached=False).done()
```

**CSS selectors**
```python
html.at("body").div("prompt-msg", "popup").done()
html.at("#prompt-msg").div(Class="header").text("Welcome!").done()
html.at("#prompt-msg").div(Class="message").text("Lorem ipsum...").done()

# CSS as a string
html.css(".header", "font-size: 14px; font-weight: bold;")

# CSS as a dictionary
design = { "font-size": "12px",
           "color": "#222",
           "background-color": "#f0f0f0" }
html.css(".message", design)
html.css(".message", { "font-size": "12px",
                       "color": "#222",
                       "background-color": "#f0f0f0" })
```

**Update element attribute**
```python
html.attrs("head", "lang", "en", 0)
html.attrs("div", "style", "display: block;")
html.attrs("div", "style", "display: none;", attrs={"class": "popup"})
```

**CSS fonts**
```python
html.font("funfont", "funfont.ttf")
html.at("body").div(Class="fun").text("Fun message...").done()
    html.css(".fun", "font-family: funfont;")
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
print(css.build())
```

**Save to file**
```python
css.save("static", "design.css")
```

**Remove selector data**
```python
css.remove(".nav")
print(css.build())
```

**JSON to HTML**
```python
from wbuilder import FromJSONBuild

tags = {
    "0": {
		"selector": "head",
		"tag": "meta",
		"charset": "UTF-8"
	}
}
html = FromJSONBuild(tags).build()
print(html)
```
