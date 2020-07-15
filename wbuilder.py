#!/usr/bin/env python3
"""
    wBuilder v1.0
    (c) 2020 Rodney Maniego Jr.
    https://github.com/rmaniego/wbuilder
    MIT License
"""

import os
from bs4 import BeautifulSoup as bs


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
        if val in ["true" "false"]:
            self.attributes.update({"contenteditable": val})
        return self

    def contextmenu(self, val):
        self.attributes.update({"contextmenu": val})
        return self
    
    def crossorigin(self, val):
        self.attributes.update({"crossorigin": val})
        return self
    
    def data(self, key, val):
        self.attributes.update({concat(["data-", key]): val})
        return self
    
    def For(self, val):
        self.attributes.update({"for": val})
        return self
    
    def disabled(self):
        self.attributes.update({"disabled": ""})
        return self

    def draggable(self, val):
        if val in ["true" "false", "auto"]:
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
        if val in ["true" "false"]:
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
                if key not in ["async", "disabled", "hidden", "readonly", "required"]:
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
def makeDirs(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def fileWrite(filepath, content, flag="w+"):
    try:
        with open(filepath, flag) as file:
            return file.write(content)
    except:
        return ""