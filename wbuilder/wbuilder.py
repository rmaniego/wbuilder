#!/usr/bin/env python3
"""
    web builder
    (c) 2020 Rodney Maniego Jr.
"""

from bs4 import BeautifulSoup as bs


class ElemBuilder:
    # 2020-03-04
    def __init__(self):
        self.tag_ = "div"
        self.attributes = {}
        self.content_ = ""
        self.html_escape = True

    def tag(self, value):
        self.tag_ = verify(value)
        return self
        
    def text(self, value):
        self.html_escape = True
        self.content_ = value
        return self
        
    def html(self, value):
        self.html_escape = False
        self.content_ = value
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
    
    def async_(self):
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
    
    def class_(self, val):
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
    
    def for_(self, val):
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
        if not cache:
            val = concat([val, "?v=", str(timestamp())])
        self.attributes.update({"href": val})
        return self
    
    def id_(self, val):
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

    def itemprop(self, val):
        self.attributes.update({"itemprop": val})
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

    def src(self, val):
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
    
    def type_(self, val):
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
        html = mkTag(self.tag_,
                     compile_attribs(self.attributes),
                     self.content_,
                     self.html_escape)
        if clear:
            self.tag_ = "div"
            self.attributes = {}
            self.content_ = ""
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

    def append(self, html):
        self.parent.append(parse(html))
        return self

    def update(self, tag, old_value, new_value):
        for item in self.html.find_all(tag):
            if tag == "link":
                if item.attrs['href'] == old_value:
                    item.attrs['href'] = new_value
            elif tag == "script":
                if item.attrs['src'] == old_value:
                    item.attrs['src'] = new_value
    
    def build(self):
        return self.html.prettify()

class Blocks:
    def __init__(self):
        self.depth = 0
        self.statements = []
    
    def if_(self, statement):
        self.depth = depth(self.depth, 1)
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- if ", statement, " -%}"]))
        return self
    
    def elif_(self, statement):
        tabs = ("\t" * (self.depth))
        self.statements.append(concat([
            tabs, "{%- elif ", statement, " -%}"]))
        return self
    
    def else_(self):
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
    
    def for_(self, statement):
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
    
    def set_var(self, key, value):
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
def a():
    return ElemBuilder().tag("a")

def audio():
    return ElemBuilder().tag("audio")

def body():
    return ElemBuilder().tag("body")

def br():
    return ElemBuilder().tag("br")

def button():
    return ElemBuilder().tag("button")

def canvas():
    return ElemBuilder().tag("canvas")

def caption():
    return ElemBuilder().tag("caption")

def div():
    return ElemBuilder().tag("div")

def footer():
    return ElemBuilder().tag("footer")

def form():
    return ElemBuilder().tag("form")

def h1():
    return ElemBuilder().tag("h1")

def h2():
    return ElemBuilder().tag("h2")

def h3():
    return ElemBuilder().tag("h3")

def h4():
    return ElemBuilder().tag("h4")

def h5():
    return ElemBuilder().tag("h5")

def h6():
    return ElemBuilder().tag("h6")

def head():
    return ElemBuilder().tag("head")

def html():
    return ElemBuilder().tag("html")

def img():
    return ElemBuilder().tag("img")

def input_():
    return ElemBuilder().tag("input")

def label():
    return ElemBuilder().tag("label")

def li():
    return ElemBuilder().tag("li")

def link():
    return ElemBuilder().tag("link")

def meta():
    return ElemBuilder().tag("meta")

def nav():
    return ElemBuilder().tag("nav")

def noscript():
    return ElemBuilder().tag("noscript")

def ol():
    return ElemBuilder().tag("ol")

def option():
    return ElemBuilder().tag("option")

def p():
    return ElemBuilder().tag("p")

def script():
    return ElemBuilder().tag("script")

def select():
    return ElemBuilder().tag("select")

def span():
    return ElemBuilder().tag("span")

def style():
    return ElemBuilder().tag("style")

def table():
    return ElemBuilder().tag("table")

def td():
    return ElemBuilder().tag("td")

def textarea():
    return ElemBuilder().tag("textarea")

def title():
    return ElemBuilder().tag("title")

def tr():
    return ElemBuilder().tag("tr")

def ul():
    return ElemBuilder().tag("ul")

def video():
    return ElemBuilder().tag("video")

### utils
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
            if key not in ["async", "disabled", "hidden", "readonly", "required"]:
                formatted.append(concat([key, "='", value, "'"]))
            else:
                formatted.append(key)
    return " ".join(formatted)
        
    
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