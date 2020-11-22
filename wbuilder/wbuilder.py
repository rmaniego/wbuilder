"""
    wBuilder v1.2
    (c) 2020 Rodney Maniego Jr.
    https://github.com/rmaniego/wbuilder
    MIT License
"""

import os
import html5lib
from bs4 import BeautifulSoup as bs
from arkivist import Arkivist


class ElemBuilder:
    # 2020-03-04
    def __init__(self, Id="", Class=""):
        self.tag_ = "div"
        self.attributes = {}
        self.attributes.update({"id": Id})
        self.attributes.update({"class": Class})
        self.Content = ""
        self.html_escape = True

    def tag(self, value):
        self.Tag = verify(value)
        return self
       
    def text(self, value):
        self.html_escape = True
        self.Content = value
        return self
       
    def html(self, value):
        self.html_escape = False
        self.Content = value
        return self
   
    ### attributes
    def attr(self, key, val):
        self.attributes.update({key: val})
        return self
   
    def action(self, val):
        self.attributes.update({"action": val})
        return self
   
    def accesskey(self, val):
        self.attributes.update({"accesskey": val})
        return self
   
    def align(self, val):
        if val in ["right", "left", "center"]:
            self.attributes.update({"align": val})
        return self
   
    def alt(self, val):
        self.attributes.update({"alt": val})
        return self
   
    def aria(self, key, val):
        self.attributes.update({concat(["aria-", key]): val})
        return self
   
    def Async(self):
        self.attributes.update({"async": ""})
        return self
   
    def autocomplete(self, val):
        if val in ["on", "off"]:
            self.attributes.update({"autocomplete": val})
        return self
   
    def autofocus(self):
        self.attributes.update({"autofocus": ""})
        return self
   
    def background(self, val):
        self.attributes.update({"background": val})
        return self
   
    def bgcolor(self, val):
        self.attributes.update({"bgcolor": val})
        return self
   
    def charset(self, val):
        self.attributes.update({"charset": val})
        return self
   
    def checked(self):
        self.attributes.update({"checked": "true"})
        return self
   
    def Class(self, val):
        self.attributes.update({"class": val})
        return self

    def content(self, val):
        self.attributes.update({"content": val})
        return self
   
    def contenteditable(self, val):
        if val in ["true", "false"]:
            self.attributes.update({"contenteditable": val})
        return self

    def contextmenu(self, val):
        self.attributes.update({"contextmenu": val})
        return self
   
    def crossorigin(self, val):
        self.attributes.update({"crossorigin": val})
        return self
   
    def data(self, key, val):
        data_key = "data"
        if key != "":
            data_key = concat(["data-", key])
        self.attributes.update({data_key: val})
        return self
   
    def defer(self):
        ## 2020-09-06
        self.attributes.update({"defer": ""})
        return self
   
    def For(self, val):
        self.attributes.update({"for": val})
        return self
   
    def disabled(self):
        self.attributes.update({"disabled": ""})
        return self

    def draggable(self, val):
        if val in ["true", "false", "auto"]:
            self.attributes.update({"draggable": val})
        return self
   
    def height(self, val):
        self.attributes.update({"height": val})
        return self
   
    def hidden(self):
        self.attributes.update({"hidden": ""})
        return self
   
    def href(self, val, cache=False):
        if not cache: val = concat([val, "?t=", str(timestamp())])
        self.attributes.update({"href": val})
        return self
   
    def Id(self, val):
        self.attributes.update({"id": val})
        return self
   
    def icon(self, val):
        self.attributes.update({"icon": val})
        return self
   
    def integrity(self, val):
        self.attributes.update({"integrity": val})
        return self

    def item(self, val):
        self.attributes.update({"item": val})
        return self

    def itmprop(self, val):
        self.attributes.update({"itmprop": val})
        return self

    def maxlength(self, val):
        self.attributes.update({"maxlength": val})
        return self

    def method(self, val):
        if val in ["post", "get"]:
            self.attributes.update({"method": val})
        return self

    def minlength(self, val):
        self.attributes.update({"minlength": val})
        return self

    def name(self, val):
        self.attributes.update({"name": val})
        return self
   
    def onclick(self, val):
        self.attributes.update({"onclick": val})
        return self

    def placeholder(self, val):
        self.attributes.update({"placeholder": val})
        return self
   
    def readonly(self):
        self.attributes.update({"readonly": ""})
        return self
   
    def rel(self, val):
        self.attributes.update({"rel": val})
        return self
   
    def required(self):
        self.attributes.update({"required": ""})
        return self
   
    def role(self, val):
        self.attributes.update({"role": val})
        return self

    def sizes(self, val):
        self.attributes.update({"sizes": val})
        return self

    def spellcheck(self, val):
        if val in ["true", "false"]:
            self.attributes.update({"spellcheck": val})
        return self

    def src(self, val, cached=False):
        if not cached: val = concat([val, "?t=", str(timestamp())])
        self.attributes.update({"src": val})
        return self
   
    def style(self, val):
        self.attributes.update({"style": val})
        return self
   
    def subject(self, val):
        self.attributes.update({"subject": val})
        return self
   
    def tabindex(self, val):
        self.attributes.update({"tabindex": val})
        return self
   
    def target(self, val):
        ## 2020-09-07
        self.attributes.update({"target": val})
        return self
   
    def title(self, val):
        self.attributes.update({"title": val})
        return self
   
    def Type(self, val):
        self.attributes.update({"type": val})
        return self
   
    def valign(self, val):
        if val in ["top", "middle", "bottom"]:
            self.attributes.update({"valign": val})
        return self
   
    def value(self, val):
        self.attributes.update({"value": val})
        return self
   
    def width(self, val):
        self.attributes.update({"width": val})
        return self

    ### utils
    def build(self, clear=True):
        html = mkTag(self.Tag,
                     compile_attribs(self.attributes),
                     self.Content,
                     self.html_escape)
        if clear:
            self.Tag = "div"
            self.attributes = {}
            self.Content = ""
            self.html_escape = True
        return html


class WebBuilder:
    def __init__(self, html="<!DOCTYPE html>"):
        self.html = parse(html)
        self.stylesheet = {}
        self.parent = None

    def find(self, selector):
        self.parent = None
        insert_at = self.html.select(selector)
        if len(insert_at) >= 1:
            self.parent = insert_at[0]
        return self

    def append(self, html, static=False):
        parsed = parse(html)
        if static:
            tag = "link"
            attr = "href"
            if "<script" in html:
                tag = "script"
                attr = "src"
            elif "<img" in html:
                tag = "img"
                attr = "src"
            for item in parsed.find_all(tag):
                source = item.attrs[attr]
                item.attrs[attr] = concat([
                    "{{ url_for('static', filename='", source, "') }}"])
        self.parent.append(parsed)
        return self
   
    def build(self):
        return self.html.prettify()
   
    def save(self, filepath):
        if filepath[-5:] != ".html": filepath = f"{filepath}.html"
        make_dirs(filepath)
        file_write(filepath, self.html.prettify())
        return self


class Css:
    def __init__(self, stylesheet={}, strict=False, sort=False):
        """
            Update selector with a dictionary of property-value pairs
            ...
            Parameters
            ---
            filepath: string
                custom directory to save the stylesheet
            strict: boolean
                only add properties found in allowlist
            sort: boolean
                sort the selectors and its properties
        """
        self.stylesheet = stylesheet
        self.strict = strict
        self.sort = sort
        self.allowlist = ["align-content", "align-items", "align-self", "animation", "animation-delay", "animation-direction", "animation-duration", "animation-fill-mode", "animation-iteration-count", "animation-name", "animation-play-state", "animation-timing-function", "backface-visibility", "background", "background-attachment", "background-clip", "background-color", "background-image", "background-origin", "background-position", "background-repeat", "background-size", "border", "border-bottom", "border-bottom-color", "border-bottom-left-radius", "border-bottom-right-radius", "border-bottom-style", "border-bottom-width", "border-collapse", "border-color", "border-image", "border-image-outset", "border-image-repeat", "border-image-slice", "border-image-source", "border-image-width", "border-left", "border-left-color", "border-left-style", "border-left-width", "border-radius", "border-right", "border-right-color", "border-right-style", "border-right-width", "border-spacing", "border-style", "border-top", "border-top-color", "border-top-left-radius", "border-top-right-radius", "border-top-style", "border-top-width", "border-width", "bottom", "box-shadow", "box-sizing", "caption-side", "clear", "clip", "color", "column-count", "column-fill", "column-gap", "column-rule", "column-rule-color", "column-rule-style", "column-rule-width", "column-span", "column-width", "columns", "content", "counter-increment", "counter-reset", "cursor", "direction", "display", "empty-cells", "flex", "flex-basis", "flex-direction", "flex-flow", "flex-grow", "flex-shrink", "flex-wrap", "float", "font", "font-family", "font-size", "font-size-adjust", "font-stretch", "font-style", "font-variant", "font-weight", "height", "justify-content", "left", "letter-spacing", "line-height", "list-style", "list-style-image", "list-style-position", "list-style-type", "margin", "margin-bottom", "margin-left", "margin-right", "margin-top", "max-height", "max-width", "min-height", "min-width", "opacity", "order", "outline", "outline-color", "outline-offset", "outline-style", "outline-width", "overflow", "overflow-x", "overflow-y", "padding", "padding-bottom", "padding-left", "padding-right", "padding-top", "page-break-after", "page-break-before", "page-break-inside", "perspective", "perspective-origin", "position", "quotes", "resize", "right", "tab-size", "table-layout", "text-align", "text-align-last", "text-decoration", "text-decoration-color", "text-decoration-line", "text-decoration-style", "text-indent", "text-justify", "text-overflow", "text-shadow", "text-transform", "top", "transform", "transform-origin", "transform-style", "transition", "transition-delay", "transition-duration", "transition-property", "transition-timing-function", "vertical-align", "visibility", "white-space", "width", "word-break", "word-spacing", "word-wrap", "z-index"]
    
    def add(self, selector, data):
        """
            Update selector with a dictionary of property-value pairs
            ...
            Parameters
            ---
            selector: string
                CSS selector
            data: dictionary
                property-value pairs
        """
        if type(data) == dict:
            if self.strict:
                for property in data:
                    if property not in self.allowlist:
                        data.pop(property)
            temp = self.stylesheet.get(selector, {})
            temp.update(data)
            self.stylesheet.update({selector: temp})
        return self
    
    def add_from_string(self, selector, properties):
        """
            Update selector with a dictionary of property-value pairs
            ...
            Parameters
            ---
            selector: string
                CSS selector
            properties: string
                property-value pairs as string
        """
        if type(properties) == str:
            for item in properties.split(";"):
                if item.strip() != "":
                    property, value = item.split(":")
                    self.update(selector, property.strip(), value.strip())
        return self
    
    def update(self, selector, property, value):
        if not self.strict or property in self.allowlist:
            data = self.stylesheet.get(selector, {})
            data.update({property: value})
            self.stylesheet.update({selector: data})
        return self
    
    def get(self, selector):
        """
            Returns the property-value pairs of the selector
            ...
            Parameters
            ---
            selector: string
                CSS selector
        """
        return self.stylesheet.get(selector, {})
    
    def remove(self, selector):
        """
            Removes the selector from the stylesheet
            ...
            Parameters
            ---
            selector: string
                CSS selector
        """
        self.stylesheet.pop(selector, None)
        return self
    
    def build(self):
        """
            Returns a parsed, plain-text version of the stylesheet
        """
        stylesheet = []
        for selector, data in self.stylesheet.items():
            attributes = []
            if self.sort:
                data = dict(sorted(data.items()))
            for attr, value in data.items():
                attributes.append(f"{attr}: {value};")
            cleaned = " ".join(attributes)
            stylesheet.append(f"{selector} {{ {cleaned} }} ")
        if self.sort:
            stylesheet.sort()
        return "\n".join(stylesheet)
    
    def save(self, filepath, filename):
        """
            Save the
            ...
            Parameters
            ---
            filepath: string
                directory of the stylesheet
            filename: string
                filename of the stylesheet
        """
        make_dirs(filepath)
        if filename[-4:] != ".css": filename = f"{filename}.css"
        file_write(f"{filepath}/{filename}", self.build())
        return self
        

class Blocks:
    def __init__(self):
        self.depth = 0
        self.statements = []
   
    def If(self, statement):
        self.depth = depth(self.depth, 1)
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- if ", statement, " -%}"]))
        return self
   
    def Elif(self, statement):
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- elif ", statement, " -%}"]))
        return self
   
    def Else(self):
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- else -%}"]))
        return self
   
    def endif(self):
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- endif -%}"]))
        self.depth = depth(self.depth, -1)
        return self
   
    def For(self, statement):
        self.depth = depth(self.depth, 1)
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- for ", statement, " -%}"]))
        return self
   
    def endfor(self):
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- endfor -%}"]))
        self.depth = depth(self.depth, -1)
        return self
   
    def setv(self, key, value):
        tabs = ("\t" * (self.depth + 1))
        self.statements.append(concat([tabs, "{%- set ", key, " = '", value, "' -%}"]))
        return self
   
    def put(self, value):
        tabs = ("\t" * (self.depth + 1))
        if type(value) == str:
            self.statements.append(concat([tabs, value]))
        return self

    # utils
    def build(self, clear=True):
        return "\n".join(self.statements)
        if clear:
            self.depth = 0
            self.statements = []

### shortcuts
def a(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("a")

def audio(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("audio")

def body(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("body")

def br(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("br")

def button(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("button")

def canvas(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("canvas")

def caption(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("caption")

def div(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("div")

def embed(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("embed") 

def footer(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("footer")

def form(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("form")

def h1(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h1")

def h2(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h2")

def h3(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h3")

def h4(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h4")

def h5(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h5")

def h6(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("h6")

def head(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("head")

def html(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("html")

def img(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("img")

def Input(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("input")

def label(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("label")

def li(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("li")

def link(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("link")

def meta(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("meta")

def nav(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("nav")

def noscript(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("noscript")

def object(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("object") 

def ol(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("ol")

def option(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("option")

def p(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("p")

def script(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("script")

def select(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("select")

def span(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("span")

def style(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("style")

def table(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("table")

def td(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("td")

def textarea(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("textarea")

def title(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("title")

def tr(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("tr")

def ul(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("ul")

def video(Id="", Class=""):
    return ElemBuilder(Id, Class).tag("video")

### html utils
def parse(html):
    if "!DOCTYPE" not in html:
        return bs(html, 'html.parser')
    return bs(html, "html5lib")

def mkTag(tag, attribs="", content="", html_escape=True):
    tag = verify(tag)
    data = attribs
    if type(attribs) == dict:
        data = compile_attribs(attribs)
    if data != "":
        data = concat([" ", data.strip()])
    if html_escape:
        content = escape(content)
    if tag not in ["meta", "link", "br", "input", "img"]:
        return concat(["<", tag, str(data), ">", str(content), "</", tag, ">"])
    else:
        return concat(["<", tag, str(data), "/>"])

def verify(tag):
    if tag not in [
            "a", "abbr", "address", "area", "article", "aside", "audio",
            "b", "base", "blockquote", "body", "br", "button", "canvas",
            "caption", "cite", "code", "col", "colgroup", "command",
            "datalist", "dd", "del", "details", "dfn", "div", "dl", "dt",
            "em", "embed", "fieldset", "figcaption", "figure", "footer",
            "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header",
            "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins",
            "kbd", "keygen", "label", "legend", "li", "link", "map", "mark",
            "menu", "meta", "meter", "nav", "noscript", "object", "ol",
            "optgroup", "option", "output", "p", "param", "pre", "progress",
            "q", "rp", "rt", "ruby", "s", "samp", "script", "section",
            "select", "small", "source", "span", "strong", "style", "sub",
            "summary", "sup", "table", "tbody", "td", "textarea", "time",
            "title", "tr", "track", "u", "ul", "var", "video"]:
        return "div"
    return tag

def compile_attribs(attributes):
    formatted = []
    if type(attributes) == dict:
        for key, value in attributes.items():
            if value != "":
                if key not in ["async", "defer", "disabled", "hidden", "readonly", "required"]:
                    formatted.append(concat([key, "='", value, "'"]))
                else:
                    formatted.append(key)
    return " ".join(formatted)
       
## utils
def escape(text):
    """ Escape HTML characters """
    # https://stackoverflow.com/a/2077321/4943299
    html_escape_table = {
         "&": "&amp;",
         '"': "&quot;",
         "'": "&apos;",
         ">": "&gt;",
         "<": "&lt;" }
    return "".join(html_escape_table.get(c, c) for c in text)

def timestamp():
    import time
    return int(time.time())

def concat(collection):
    if type(collection) == list:
        return "".join(collection)
    return ""

def depth(value, increment=1):
    value = value + increment
    if value < 0:
        return 0
    return value

## file utils
def make_dirs(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def file_write(filepath, content, flag="w+"):
    try:
        with open(filepath, flag) as file:
            return file.write(content)
    except:
        return ""