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
    def attr(self, attribute, value):
        return self.attributes.get(attribute, value)
        return self
    
    def action(self, value):
        self.attributes.update({"action": value})
        return self
    
    def accesskey(self, value):
        self.attributes.update({"accesskey": value})
        return self
    
    def align(self, value):
        if value in ["right", "left", "center"]:
            self.attributes.update({"align": value})
        return self
    
    def alt(self, name, value):
        self.attributes.update({"alt": ""})
        return self
    
    def aria(self, name, value):
        self.attributes.update({concat(["aria-", name]): value})
        return self
    
    def async_(self):
        self.attributes.update({"async": ""})
        return self
    
    def autocomplete(self, value):
        if value in ["on", "off"]:
            self.attributes.update({"autocomplete": value})
        return self
    
    def autofocus(self):
        self.attributes.update({"autofocus": ""})
        return self
    
    def background(self, value):
        self.attributes.update({"background": value})
        return self
    
    def bgcolor(self, value):
        self.attributes.update({"bgcolor": value})
        return self
    
    def charset(self, value):
        self.attributes.update({"charset": value})
        return self
    
    def checked(self):
        self.attributes.update({"checked": "true"})
        return self
    
    def class_(self, value):
        self.attributes.update({"class": value})
        return self

    def content(self, value):
        self.attributes.update({"content": value})
        return self
    
    def contenteditable(self, value):
        if value in ["true" "false"]:
            self.attributes.update({"contenteditable": value})
        return self

    def contextmenu(self, name, value):
        self.attributes.update({"contextmenu": value})
        return self
    
    def crossorigin(self, value):
        self.attributes.update({"crossorigin": value})
        return self
    
    def data(self, name, value):
        self.attributes.update({concat(["data-", name]): value})
        return self
    
    def for_(self, value):
        self.attributes.update({"for": value})
        return self
    
    def disabled(self):
        self.attributes.update({"disabled": ""})
        return self

    def draggable(self, value):
        if value in ["true" "false", "auto"]:
            self.attributes.update({"draggable": value})
        return self
    
    def height(self, value):
        self.attributes.update({"height": value})
        return self
    
    def hidden(self):
        self.attributes.update({"hidden": ""})
        return self
    
    def href(self, value, cache=False):
        if not cache:
            value = concat([value, "?v=", str(timestamp())])
        self.attributes.update({"href": value})
        return self
    
    def id_(self, value):
        self.attributes.update({"id": value})
        return self
    
    def icon(self, value):
        self.attributes.update({"icon": value})
        return self
    
    def integrity(self, value):
        self.attributes.update({"integrity": value})
        return self

    def item(self, value):
        self.attributes.update({"item": value})
        return self

    def itemprop(self, value):
        self.attributes.update({"itemprop": value})
        return self

    def maxlength(self, value):
        self.attributes.update({"maxlength": value})
        return self

    def method(self, value):
        if value in ["post", "get"]:
            self.attributes.update({"method": value})
        return self

    def minlength(self, value):
        self.attributes.update({"minlength": value})
        return self

    def name(self, value):
        self.attributes.update({"name": value})
        return self

    def placeholder(self, value):
        self.attributes.update({"placeholder": value})
        return self
    
    def readonly(self):
        self.attributes.update({"readonly": ""})
        return self
    
    def rel(self, value):
        self.attributes.update({"rel": value})
        return self
    
    def required(self):
        self.attributes.update({"required": ""})
        return self
    
    def role(self, value):
        self.attributes.update({"role": value})
        return self

    def sizes(self, value):
        self.attributes.update({"sizes": value})
        return self

    def spellcheck(self, value):
        if value in ["true" "false"]:
            self.attributes.update({"spellcheck": value})
        return self

    def src(self, value):
        self.attributes.update({"src": value})
        return self
    
    def style(self, value):
        self.attributes.update({"style": value})
        return self
    
    def subject(self, value):
        self.attributes.update({"subject": value})
        return self
    
    def tabindex(self, value):
        self.attributes.update({"tabindex": value})
        return self
    
    def title(self, value):
        self.attributes.update({"title": value})
        return self
    
    def type_(self, value):
        self.attributes.update({"type": value})
        return self
    
    def valign(self, value):
        if value in ["top", "middle", "bottom"]:
            self.attributes.update({"valign": value})
        return self
    
    def value(self, value):
        self.attributes.update({"value": value})
        return self
    
    def width(self, value):
        self.attributes.update({"width": value})
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