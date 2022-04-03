# wBuilder
```
    wBuilder
    (c) 2020 Rodney Maniego Jr.
    MIT License
```

HTML template generator for Python.

Read: [Introducing wBuilder: An HTML5 Generator for Python](https://peakd.com/hive-102677/@oniemaniego/introducing-wbuilder-an-html5-generator-for-python)

*Requirements:*
- Arkivist, BS4, Namari

*Future Features*
- Simple JQuery generator

## WebBuilder Usage
**Import**
```python
from wbuilder import WebBuilder
```

**Initialize**
```python
html = WebBuilder()
html = WebBuilder("web.html")
html = WebBuilder(html="<span id='label'></span>")
```

**HTML head**
```python
html.prop("html", "lang", "en")
html.at("head").append("title", text="WebBuilder")
html.at("head").append("meta", charset="UTF-8")
html.at("head").append("meta", name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
html.at("head").append("link", rel="icon", href="icon.png", type_="image/png", sizes="96x96", static=True)
html.at("head").append("link", rel="stylesheet", href="reset.css", static=True)
html.at("head").append("link", rel="stylesheet", href="design.css")

```

**Basic usage**
```python
html.at("body").append("div", id="#popup .popup")
html.at("#popup").append("header3", id=".header", text="Welcome!")
```

**CSS selectors**
```python
html.at("#popup").append("span", id="#popup-txt .popup-txt", text="Hello, user!")
html.at("#popup").append("button", id="#ok .blue", text="OK")

# CSS as a string
html.inlineCss("div", {"color": "#000"})
html.inlineCss("div", "font-size:12px;", reset=True))

# CSS as a dictionary
design = { "font-size": "12px", "color": "#222", "background-color": "#f0f0f0" }
html.at("#popup").append("div", id=".message", text="Lorem ipsum...", style=design)
```

**Update element properties**
```python
html.prop("html", "lang", "en")
html.prop("#popup", "data-name", "container")
html.prop("#popup", "data-title", "message")
html.prop("div", "style", "font-size:12px;")
```

**Preview HTML**
```python
content = html.build()
print(content)
```

**Save to HTML file**
```python
html.save()
html.save("saveAsNewFile.html")
```

**Save to/Read from JSON file**
```python
html.toJson("test.json")
html.fromJson("test.json")
```
