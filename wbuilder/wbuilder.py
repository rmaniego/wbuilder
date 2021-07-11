"""
    wBuilder v2.0
    (c) 2020 Rodney Maniego Jr.
    https://github.com/rmaniego/wbuilder
    MIT License
"""

import os
import html5lib
from bs4 import BeautifulSoup as bs

class WebBuilder:
    def __init__(self, html="<!doctype html>"):
        """
            Initialize class as an HTML document or a snippet
            ...
            Parameters
            ---
            html: string
                any valid html string
        """
        ## main html
        self.html_filepath = ""
        self.html_filename = ""
        self.html = parse(html)
        self.stylesheet = {}
        self.css_fonts = {}
        self.parent = None
        ## temporary tag
        self.Tag = "div"
        self.attributes = {}
        self.attributes.update({"id": ""})
        self.attributes.update({"class": ""})
        self.Content = ""
        self.html_escape = True

    def at(self, selector):
        """
            Finds the selector in the HTML object, else fails (deprecated)
            ...
            Parameters
            ---
            selector: string
                the element tag, id, class present in the HTML object, always the first element found
        """
        self.parent = None
        self.Tag = "div"
        insert_at = self.html.select(selector)
        if len(insert_at) >= 1:
            self.parent = insert_at[0]
        return self

    def find(self, selector):
        """
            Deprecated method, similar to at()
        """
        self.at(selector)
        return self
    
    def attrs(self, selector, attribute, value, index=-1, attrs=None):
        """
            Search
            ...
            Parameters
            ---
            selector: string
                valid html/css selector
            attribute: string
                valid html5 element attribute
            value: string
                value of the attribute
            index: int
                specific index to change; if -1, change all
            attrs: dict
        """
        found = {}
        if attrs is None:
            found = self.html.findAll(selector)
        else:
            if isinstance(attrs, dict):
                found = self.html.findAll(selector, attrs)
        count = len(found)
        if count > 0:
            if not isinstance(index, int):
                index = -1
            if index == -1:
                for i in range(0, count):
                    found[i].attrs.update({attribute: value})
            else:
                if index >= count:
                    index = count - 1
                found[index].attrs.update({attribute: value})
        return self

    def element(self, tag, Id="", Class=""):
        """
            Initializes the element with its basic attributes
            ...
            Parameters
            ---
            tag: string
                any valid HTML5 tag
            Id: string
                unique string
            Class: string
                useful when designing with CSS
        """
        if self.parent != None:
            self.Tag = verify(tag)
            if Id != "":
                self.attributes.update({"id": Id})
            if Class != "":
                self.attributes.update({"class": Class})
        return self

    ### element tags / shortcuts
    def a(self, Id="", Class=""):
        self.element("a", Id=Id, Class=Class)
        return self

    def abbr(self, Id="", Class=""):
        self.element("abbr", Id=Id, Class=Class)
        return self

    def acronym(self, Id="", Class=""):
        self.element("acronym", Id=Id, Class=Class)
        return self

    def address(self, Id="", Class=""):
        self.element("address", Id=Id, Class=Class)
        return self

    def applet(self, Id="", Class=""):
        self.element("applet", Id=Id, Class=Class)
        return self

    def area(self, Id="", Class=""):
        self.element("area", Id=Id, Class=Class)
        return self

    def article(self, Id="", Class=""):
        self.element("article", Id=Id, Class=Class)
        return self

    def aside(self, Id="", Class=""):
        self.element("aside", Id=Id, Class=Class)
        return self

    def audio(self, Id="", Class=""):
        self.element("audio", Id=Id, Class=Class)
        return self

    def b(self, Id="", Class=""):
        self.element("b", Id=Id, Class=Class)
        return self

    def base(self, Id="", Class=""):
        self.element("base", Id=Id, Class=Class)
        return self

    def basefont(self, Id="", Class=""):
        self.element("basefont", Id=Id, Class=Class)
        return self

    def bdi(self, Id="", Class=""):
        self.element("bdi", Id=Id, Class=Class)
        return self

    def bdo(self, Id="", Class=""):
        self.element("bdo", Id=Id, Class=Class)
        return self

    def big(self, Id="", Class=""):
        self.element("big", Id=Id, Class=Class)
        return self

    def blockquote(self, Id="", Class=""):
        self.element("blockquote", Id=Id, Class=Class)
        return self

    def body(self, Id="", Class=""):
        self.element("body", Id=Id, Class=Class)
        return self

    def br(self, Id="", Class=""):
        self.element("br", Id=Id, Class=Class)
        return self

    def button(self, Id="", Class=""):
        self.element("button", Id=Id, Class=Class)
        return self

    def canvas(self, Id="", Class=""):
        self.element("canvas", Id=Id, Class=Class)
        return self

    def caption(self, Id="", Class=""):
        self.element("caption", Id=Id, Class=Class)
        return self

    def center(self, Id="", Class=""):
        self.element("center", Id=Id, Class=Class)
        return self

    def cite(self, Id="", Class=""):
        self.element("cite", Id=Id, Class=Class)
        return self

    def code(self, Id="", Class=""):
        self.element("code", Id=Id, Class=Class)
        return self

    def col(self, Id="", Class=""):
        self.element("col", Id=Id, Class=Class)
        return self

    def colgroup(self, Id="", Class=""):
        self.element("colgroup", Id=Id, Class=Class)
        return self

    def data(self, Id="", Class=""):
        self.element("data", Id=Id, Class=Class)
        return self

    def datalist(self, Id="", Class=""):
        self.element("datalist", Id=Id, Class=Class)
        return self

    def dd(self, Id="", Class=""):
        self.element("dd", Id=Id, Class=Class)
        return self

    def Del(self, Id="", Class=""):
        self.element("del", Id=Id, Class=Class)
        return self

    def details(self, Id="", Class=""):
        self.element("details", Id=Id, Class=Class)
        return self

    def dfn(self, Id="", Class=""):
        self.element("dfn", Id=Id, Class=Class)
        return self

    def dialog(self, Id="", Class=""):
        self.element("dialog", Id=Id, Class=Class)
        return self

    def dir(self, Id="", Class=""):
        self.element("dir", Id=Id, Class=Class)
        return self

    def div(self, Id="", Class=""):
        self.element("div", Id=Id, Class=Class)
        return self

    def dl(self, Id="", Class=""):
        self.element("dl", Id=Id, Class=Class)
        return self

    def dt(self, Id="", Class=""):
        self.element("dt", Id=Id, Class=Class)
        return self

    def em(self, Id="", Class=""):
        self.element("em", Id=Id, Class=Class)
        return self

    def embed(self, Id="", Class=""):
        self.element("embed")
        return self

    def fieldset(self, Id="", Class=""):
        self.element("fieldset")
        return self

    def figcaption(self, Id="", Class=""):
        self.element("figcaption")
        return self

    def figure(self, Id="", Class=""):
        self.element("figure")
        return self

    def font(self, Id="", Class=""):
        self.element("font")
        return self

    def footer(self, Id="", Class=""):
        self.element("footer", Id=Id, Class=Class)
        return self

    def form(self, Id="", Class=""):
        self.element("form", Id=Id, Class=Class)
        return self

    def frame(self, Id="", Class=""):
        self.element("frame", Id=Id, Class=Class)
        return self

    def frameset(self, Id="", Class=""):
        self.element("frameset", Id=Id, Class=Class)
        return self

    def h1(self, Id="", Class=""):
        self.element("h1", Id=Id, Class=Class)
        return self

    def h2(self, Id="", Class=""):
        self.element("h2", Id=Id, Class=Class)
        return self

    def h3(self, Id="", Class=""):
        self.element("h3", Id=Id, Class=Class)
        return self

    def h4(self, Id="", Class=""):
        self.element("h4", Id=Id, Class=Class)
        return self

    def h5(self, Id="", Class=""):
        self.element("h5", Id=Id, Class=Class)
        return self

    def h6(self, Id="", Class=""):
        self.element("h6", Id=Id, Class=Class)
        return self

    def head(self, Id="", Class=""):
        self.element("head", Id=Id, Class=Class)
        return self

    def header(self, Id="", Class=""):
        self.element("header", Id=Id, Class=Class)
        return self

    def hr(self, Id="", Class=""):
        self.element("hr", Id=Id, Class=Class)
        return self

    def html(self, Id="", Class=""):
        self.element("html", Id=Id, Class=Class)
        return self

    def i(self, Id="", Class=""):
        self.element("i", Id=Id, Class=Class)
        return self

    def iframe(self, Id="", Class=""):
        self.element("iframe", Id=Id, Class=Class)
        return self

    def img(self, Id="", Class=""):
        self.element("img", Id=Id, Class=Class)
        return self

    def Input(self, Id="", Class=""):
        self.element("input", Id=Id, Class=Class)
        return self

    def ins(self, Id="", Class=""):
        self.element("ins", Id=Id, Class=Class)
        return self

    def kbd(self, Id="", Class=""):
        self.element("kbd", Id=Id, Class=Class)
        return self

    def label(self, Id="", Class=""):
        self.element("label", Id=Id, Class=Class)
        return self

    def legend(self, Id="", Class=""):
        self.element("legend", Id=Id, Class=Class)
        return self

    def li(self, Id="", Class=""):
        self.element("li", Id=Id, Class=Class)
        return self

    def link(self, Id="", Class=""):
        self.element("link", Id=Id, Class=Class)
        return self

    def main(self, Id="", Class=""):
        self.element("main", Id=Id, Class=Class)
        return self

    def map(self, Id="", Class=""):
        self.element("map", Id=Id, Class=Class)
        return self

    def mark(self, Id="", Class=""):
        self.element("mark", Id=Id, Class=Class)
        return self

    def meta(self, Id="", Class=""):
        self.element("meta", Id=Id, Class=Class)
        return self

    def meter(self, Id="", Class=""):
        self.element("meter", Id=Id, Class=Class)
        return self

    def nav(self, Id="", Class=""):
        self.element("nav", Id=Id, Class=Class)
        return self

    def noframes(self, Id="", Class=""):
        self.element("noframes", Id=Id, Class=Class)
        return self

    def noscript(self, Id="", Class=""):
        self.element("noscript", Id=Id, Class=Class)
        return self

    def object(self, Id="", Class=""):
        self.element("object")

    def ol(self, Id="", Class=""):
        self.element("ol", Id=Id, Class=Class)
        return self

    def optgroup(self, Id="", Class=""):
        self.element("optgroup", Id=Id, Class=Class)
        return self

    def option(self, Id="", Class=""):
        self.element("option", Id=Id, Class=Class)
        return self

    def output(self, Id="", Class=""):
        self.element("output", Id=Id, Class=Class)
        return self

    def p(self, Id="", Class=""):
        self.element("p", Id=Id, Class=Class)
        return self

    def param(self, Id="", Class=""):
        self.element("param", Id=Id, Class=Class)
        return self

    def picture(self, Id="", Class=""):
        self.element("picture", Id=Id, Class=Class)
        return self

    def pre(self, Id="", Class=""):
        self.element("pre", Id=Id, Class=Class)
        return self

    def progress(self, Id="", Class=""):
        self.element("progress", Id=Id, Class=Class)
        return self

    def q(self, Id="", Class=""):
        self.element("q", Id=Id, Class=Class)
        return self

    def rp(self, Id="", Class=""):
        self.element("rp", Id=Id, Class=Class)
        return self

    def rt(self, Id="", Class=""):
        self.element("rt", Id=Id, Class=Class)
        return self

    def ruby(self, Id="", Class=""):
        self.element("ruby", Id=Id, Class=Class)
        return self

    def s(self, Id="", Class=""):
        self.element("s", Id=Id, Class=Class)
        return self

    def samp(self, Id="", Class=""):
        self.element("samp", Id=Id, Class=Class)
        return self

    def script(self, Id="", Class=""):
        self.element("script", Id=Id, Class=Class)
        return self

    def select(self, Id="", Class=""):
        self.element("select", Id=Id, Class=Class)
        return self

    def small(self, Id="", Class=""):
        self.element("small", Id=Id, Class=Class)
        return self

    def source(self, Id="", Class=""):
        self.element("source", Id=Id, Class=Class)
        return self

    def span(self, Id="", Class=""):
        self.element("span", Id=Id, Class=Class)
        return self

    def strike(self, Id="", Class=""):
        self.element("strike", Id=Id, Class=Class)
        return self

    def strong(self, Id="", Class=""):
        self.element("strong", Id=Id, Class=Class)
        return self

    def style(self, Id="", Class=""):
        self.element("style", Id=Id, Class=Class)
        return self

    def sub(self, Id="", Class=""):
        self.element("sub", Id=Id, Class=Class)
        return self

    def summary(self, Id="", Class=""):
        self.element("summary", Id=Id, Class=Class)
        return self

    def sup(self, Id="", Class=""):
        self.element("sup", Id=Id, Class=Class)
        return self

    def svg(self, Id="", Class=""):
        self.element("svg", Id=Id, Class=Class)
        return self

    def table(self, Id="", Class=""):
        self.element("table", Id=Id, Class=Class)
        return self

    def tbody(self, Id="", Class=""):
        self.element("tbody", Id=Id, Class=Class)
        return self

    def td(self, Id="", Class=""):
        self.element("td", Id=Id, Class=Class)
        return self

    def template(self, Id="", Class=""):
        self.element("template", Id=Id, Class=Class)
        return self

    def textarea(self, Id="", Class=""):
        self.element("textarea", Id=Id, Class=Class)
        return self

    def tfoot(self, Id="", Class=""):
        self.element("tfoot", Id=Id, Class=Class)
        return self

    def th(self, Id="", Class=""):
        self.element("th", Id=Id, Class=Class)
        return self

    def thead(self, Id="", Class=""):
        self.element("thead", Id=Id, Class=Class)
        return self

    def Time(self, Id="", Class=""):
        self.element("time", Id=Id, Class=Class)
        return self

    def title(self, Id="", Class=""):
        self.element("title", Id=Id, Class=Class)
        return self

    def tr(self, Id="", Class=""):
        self.element("tr", Id=Id, Class=Class)
        return self

    def track(self, Id="", Class=""):
        self.element("track", Id=Id, Class=Class)
        return self

    def u(self, Id="", Class=""):
        self.element("u", Id=Id, Class=Class)
        return self

    def ul(self, Id="", Class=""):
        self.element("ul", Id=Id, Class=Class)
        return self

    def var(self, Id="", Class=""):
        self.element("var")
        return self

    def video(self, Id="", Class=""):
        self.element("video")
        return self

    def wbr(self, Id="", Class=""):
        self.element("wbr")
        return self

    ### content data
    def text(self, value, escape=True):
        self.html_escape = escape
        self.Content = value
        return self

    def html_string(self, value):
        self.html_escape = False
        self.Content = value
        return self

    ### attributes
    def attr(self, key, val):
        if self.parent != None:
            self.attributes.update({key: val})
        return self

    def action(self, val):
        if self.parent != None:
            self.attributes.update({"action": val})
        return self

    def accesskey(self, val):
        if self.parent != None:
            self.attributes.update({"accesskey": val})
        return self

    def align(self, val):
        if self.parent != None:
            if val in ["right", "left", "center"]:
                self.attributes.update({"align": val})
        return self

    def alt(self, val):
        if self.parent != None:
            self.attributes.update({"alt": val})
        return self

    def aria(self, key, val):
        if self.parent != None:
            self.attributes.update({f"aria-{key}": val})
        return self

    def Async(self):
        if self.parent != None:
            self.attributes.update({"async": ""})
        return self

    def autocomplete(self, val):
        if self.parent != None:
            if val in ["on", "off"]:
                self.attributes.update({"autocomplete": val})
        return self

    def autofocus(self):
        if self.parent != None:
            self.attributes.update({"autofocus": ""})
        return self

    def background(self, val):
        if self.parent != None:
            self.attributes.update({"background": val})
        return self

    def bgcolor(self, val):
        if self.parent != None:
            self.attributes.update({"bgcolor": val})
        return self

    def charset(self, val):
        if self.parent != None:
            self.attributes.update({"charset": val})
        return self

    def checked(self):
        if self.parent != None:
            self.attributes.update({"checked": "true"})
        return self

    """ def Class(self, val):  # use element shortcuts
        if self.parent != None:
            self.attributes.update({"class": val})
        return self """

    def content(self, val):
        if self.parent != None:
            self.attributes.update({"content": val})
        return self

    def contenteditable(self, val):
        if self.parent != None:
            if val in ["true", "false"]:
                self.attributes.update({"contenteditable": val})
        return self

    def contextmenu(self, val):
        if self.parent != None:
            self.attributes.update({"contextmenu": val})
        return self

    def crossorigin(self, val):
        if self.parent != None:
            self.attributes.update({"crossorigin": val})
        return self

    def data(self, key, val):
        if self.parent != None:
            data_key = "data"
            if key != "":
                data_key = f"data-{key}"
            self.attributes.update({data_key: val})
        return self

    def defer(self):
        if self.parent != None:
            self.attributes.update({"defer": ""})
        return self

    def For(self, val):
        if self.parent != None:
            self.attributes.update({"for": val})
        return self

    def disabled(self):
        if self.parent != None:
            self.attributes.update({"disabled": ""})
        return self

    def draggable(self, val):
        if self.parent != None:
            if val in ["true", "false", "auto"]:
                self.attributes.update({"draggable": val})
        return self

    def height(self, val):
        if self.parent != None:
            self.attributes.update({"height": val})
        return self

    def hidden(self):
        if self.parent != None:
            self.attributes.update({"hidden": ""})
        return self

    def href(self, val, cached=False):
        if self.parent != None:
            ts = str(timestamp())
            if not cached: val = f"{val}?t={ts}"
            self.attributes.update({"href": val})
        return self

    """ def Id(self, val): # use element shortcuts
        if self.parent != None:
            self.attributes.update({"id": val})
        return self """

    def icon(self, val):
        if self.parent != None:
            self.attributes.update({"icon": val})
        return self

    def integrity(self, val):
        if self.parent != None:
            self.attributes.update({"integrity": val})
        return self

    def item(self, val):
        if self.parent != None:
            self.attributes.update({"item": val})
        return self

    def itmprop(self, val):
        if self.parent != None:
            self.attributes.update({"itmprop": val})
        return self

    def maxlength(self, val):
        if self.parent != None:
            self.attributes.update({"maxlength": val})
        return self

    def List(self, val):
        if self.parent != None:
            self.attributes.update({"list": val})
        return self

    def method(self, val):
        if self.parent != None:
            if val in ["post", "get"]:
                self.attributes.update({"method": val})
        return self

    def minlength(self, val):
        if self.parent != None:
            self.attributes.update({"minlength": val})
        return self

    def name(self, val):
        if self.parent != None:
            self.attributes.update({"name": val})
        return self

    def onclick(self, val):
        if self.parent != None:
            self.attributes.update({"onclick": val})
        return self

    def placeholder(self, val):
        if self.parent != None:
            self.attributes.update({"placeholder": val})
        return self

    def readonly(self):
        if self.parent != None:
            self.attributes.update({"readonly": ""})
        return self

    def rel(self, val):
        if self.parent != None:
            self.attributes.update({"rel": val})
        return self

    def required(self):
        if self.parent != None:
            self.attributes.update({"required": ""})
        return self

    def role(self, val):
        if self.parent != None:
            self.attributes.update({"role": val})
        return self

    def sizes(self, val):
        if self.parent != None:
            self.attributes.update({"sizes": val})
        return self

    def spellcheck(self, val):
        if self.parent != None:
            if val in ["true", "false"]:
                self.attributes.update({"spellcheck": val})
        return self

    def src(self, val, cached=False):
        if self.parent != None:
            ts = str(timestamp())
            if not cached: val = f"{val}?t={ts}"
        self.attributes.update({"src": val})
        return self

    def style(self, val):
        if self.parent != None:
            self.attributes.update({"style": val})
        return self

    def subject(self, val):
        if self.parent != None:
            self.attributes.update({"subject": val})
        return self

    def tabindex(self, val):
        if self.parent != None:
            self.attributes.update({"tabindex": val})
        return self

    def target(self, val):
        if self.parent != None:
            self.attributes.update({"target": val})
        return self

    """ def title(self, val): # will find a workaround for this
        if self.parent != None:
            self.attributes.update({"title": val})
        return self """

    def Type(self, val):
        if self.parent != None:
            self.attributes.update({"type": val})
        return self

    def valign(self, val):
        if self.parent != None:
            if val in ["top", "middle", "bottom"]:
                self.attributes.update({"valign": val})
        return self

    def value(self, val):
        if self.parent != None:
            self.attributes.update({"value": val})
        return self

    def width(self, val):
        if self.parent != None:
            self.attributes.update({"width": val})
        return self

    ### css
    def css(self, selector, properties):
        data = {}
        if type(properties) == dict:
            data = self.stylesheet.get(selector, {})
            data.update(properties)
        elif type(properties) == str:
            for item in properties.split(";"):
                if item.strip() != "":
                    property, value = item.split(":")
                    data.update({property.strip(): value.strip()})
        self.stylesheet.update({selector: data})
        return self

    def font(self, font, filename):
        self.css_fonts.update({font: filename})
        return self

    ### utils
    def append(self, html, static=False, clear=True):
        """
            Parses the HTML snippet and append it to its parent element
            ...
            Parameters
            ---
            html: string
                any valid HTML string
            static: boolean
                for files located in the server
            clear: boolean
                clear element data
        """
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
                item.attrs[attr] = f"{{{{ url_for('static', filename='{source}') }}}}"

        ## append to parent
        self.parent.append(parsed)

        ## clean footprint
        if clear:
            self.parent = None
            self.Tag = "div"
            self.attributes = {}
            self.Content = ""
            self.html_escape = True
        return self

    def done(self, static=False, clear=True):
        """
            Compiles the element and append it to its parent element
            ...
            Parameters
            ---
            static: boolean
                for files located in the server
            clear: boolean
                clear element data
        """
        html = mkTag(self.Tag,
                     compile_attribs(self.attributes),
                     self.Content,
                     self.html_escape)
        self.append(html, static=static, clear=clear)
        return self

    def build(self):
        return self.html.prettify()

    def save_to_html(self, filepath="", filename=""):
        if filename == "": filename = "page.html"
        if filename[-5:] != ".html": filename = f"{filename}.html"
        fullpath = filename
        if filepath != "":
            make_dirs(filepath)
            fullpath = f"{filepath}/{filename}"
        file_write(fullpath, self.html.prettify())
        return self

    def save_stylesheet(self, filepath="", filename="", strict=False, sort=False):
        """
            Save stylesheet to file
            ...
            Parameters
            ---
            filepath: string
                directory of the stylesheet
            filename: string
                filename of the stylesheet
            strict: boolean
                only add properties found in allowlist
            sort: boolean
                sort the selectors and its properties
        """
        ## re-use css class
        stylesheet = Css(self.stylesheet, self.css_fonts, strict=strict, sort=sort)
        stylesheet.clean().save(filepath, filename)

class Css:
    def __init__(self, stylesheet={}, fonts={}, strict=False, sort=False):
        """
            Initialize CSS class
            ...
            Parameters
            ---
            stylesheet: dict
                a valid dictionary of selectors and proprties
            strict: boolean
                only add properties found in allowlist
            sort: boolean
                sort the selectors and its properties
        """
        self.stylesheet = stylesheet
        self.css_fonts = fonts
        self.strict = strict
        self.sort = sort
        self.allowlist = ["align-content", "align-items", "align-self", "animation", "animation-delay", "animation-direction", "animation-duration", "animation-fill-mode", "animation-iteration-count", "animation-name", "animation-play-state", "animation-timing-function", "backface-visibility", "background", "background-attachment", "background-clip", "background-color", "background-image", "background-origin", "background-position", "background-repeat", "background-size", "border", "border-bottom", "border-bottom-color", "border-bottom-left-radius", "border-bottom-right-radius", "border-bottom-style", "border-bottom-width", "border-collapse", "border-color", "border-image", "border-image-outset", "border-image-repeat", "border-image-slice", "border-image-source", "border-image-width", "border-left", "border-left-color", "border-left-style", "border-left-width", "border-radius", "border-right", "border-right-color", "border-right-style", "border-right-width", "border-spacing", "border-style", "border-top", "border-top-color", "border-top-left-radius", "border-top-right-radius", "border-top-style", "border-top-width", "border-width", "bottom", "box-shadow", "box-sizing", "caption-side", "clear", "clip", "color", "column-count", "column-fill", "column-gap", "column-rule", "column-rule-color", "column-rule-style", "column-rule-width", "column-span", "column-width", "columns", "content", "counter-increment", "counter-reset", "cursor", "direction", "display", "empty-cells", "flex", "flex-basis", "flex-direction", "flex-flow", "flex-grow", "flex-shrink", "flex-wrap", "float", "font", "font-family", "font-size", "font-size-adjust", "font-stretch", "font-style", "font-variant", "font-weight", "height", "justify-content", "left", "letter-spacing", "line-height", "list-style", "list-style-image", "list-style-position", "list-style-type", "margin", "margin-bottom", "margin-left", "margin-right", "margin-top", "max-height", "max-width", "min-height", "min-width", "opacity", "order", "outline", "outline-color", "outline-offset", "outline-style", "outline-width", "overflow", "overflow-x", "overflow-y", "padding", "padding-bottom", "padding-left", "padding-right", "padding-top", "page-break-after", "page-break-before", "page-break-inside", "perspective", "perspective-origin", "position", "quotes", "resize", "right", "tab-size", "table-layout", "text-align", "text-align-last", "text-decoration", "text-decoration-color", "text-decoration-line", "text-decoration-style", "text-indent", "text-justify", "text-overflow", "text-shadow", "text-transform", "top", "transform", "transform-origin", "transform-style", "transition", "transition-delay", "transition-duration", "transition-property", "transition-timing-function", "vertical-align", "visibility", "white-space", "width", "word-break", "word-spacing", "word-wrap", "z-index"]

    def clean(self):
        """ Use when adding bulk selectors, removes unsupported properties """
        stylesheet = {}
        if type(self.stylesheet) == dict:
            for selector, data in self.stylesheet.items():
                if self.strict:
                    for property in data:
                        if property not in self.allowlist:
                            data.pop(property)
                stylesheet.update({selector: data})
        self.stylesheet = stylesheet
        return self

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
            self.stylesheet.update({selector: {}})
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
            self.stylesheet.update({selector: {}})
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
        for name, source in self.css_fonts.items():
            stylesheet.insert(0, f"@font-face {{ font-family: {name}; src: url('{source}'); }}")
        return "\n".join(stylesheet)

    def save(self, filepath="", filename=""):
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
        if filename == "": filename = "design.css"
        if filename[-4:] != ".css": filename = f"{filename}.css"
        fullpath = filename
        if filepath != "":
            make_dirs(filepath)
            fullpath = f"{filepath}/{filename}"
        file_write(fullpath, self.build())
        return self

class FromJSONBuild:
    def __init__(self, json, document=None):
        self.json = None
        if isinstance(json, dict):
            self.json = json
        self.document = None
        if isinstance(document, str):
            self.document = document
    
    def append(self, json):
        if isinstance(json, dict):
            self.json.update(json)
        return self
    
    def clear(self):
        self.json = None
        return self
    
    def build(self):
        self.html = WebBuilder(self.document)
        for element in self.json.values():
            tag = element.get("tag", "")
            selector = element.get("selector", "body")
            blocklist = ("selector", "tag", "Id", "Class", "static", "index")
            if tag != "":
                self.html.at(selector)
                Id = element.get("Id", "")
                Class = element.get("Class", "")
                self.html.element(tag, Id, Class)
                
                for key, value in element.items():
                    if key not in blocklist:
                        if key == "text":
                            self.html.text(value)
                        elif key == "html_string":
                            self.html.html_string(value)
                        else:
                            self.html.attr(key, value)
                static = False
                if element.get("static", "") == "True":
                    static = True
                self.html.done(static=static)
            else:
                index = element.get("index", -1)
                for key, value in element.items():
                    if key not in blocklist:
                        self.html.attrs(selector, key, value, index=index)
        return self.html.build()

### html utils
def parse(html):
    if "!doctype" not in html:
        return bs(html, 'html.parser')
    return bs(html, "html5lib")

def mkTag(tag, attribs="", content="", html_escape=True):
    tag = verify(tag)
    data = attribs
    if type(attribs) == dict:
        data = compile_attribs(attribs)
    if data != "":
        data = data.strip()
        data = f" {data}"
    if html_escape:
        content = escape(content)
    if tag not in ["meta", "link", "br", "input", "img"]:
        return f"<{tag} {data} >{content}</{tag}>"
    else:
        return f"<{tag} {data} />"

def verify(tag):
    if tag not in [
            "a", "abbr", "acronym", "address", "applet", "area", "article",
            "aside", "audio", "b", "base", "basefont", "bdi", "bdo", "big",
            "blockquote", "body", "br", "button", "canvas", "caption",
            "center", "cite", "code", "col", "colgroup", "data", "datalist",
            "dd", "del", "details", "dfn", "dialog", "dir", "div", "dl",
            "dt", "em", "embed", "fieldset", "figcaption", "figure", "font",
            "footer", "form", "frame", "frameset", "h1", "h6", "head",
            "header", "hr", "html", "i", "iframe", "img", "input", "ins",
            "kbd", "label", "legend", "li", "link", "main", "map", "mark",
            "meta", "meter", "nav", "noframes", "noscript", "object", "ol",
            "optgroup", "option", "output", "p", "param", "picture", "pre",
            "progress", "q", "rp", "rt", "ruby", "s", "samp", "script",
            "section", "select", "small", "source", "span", "strike",
            "strong", "style", "sub", "summary", "sup", "svg", "table",
            "tbody", "td", "template", "textarea", "tfoot", "th", "thead",
            "time", "title", "tr", "track", "tt", "u", "ul", "var",
            "video", "wbr"]:
        return "div"
    return tag

def compile_attribs(attributes):
    formatted = []
    if type(attributes) == dict:
        for key, value in attributes.items():
            if value != "":
                if key not in ["async", "defer", "disabled", "hidden", "readonly", "required"]:
                    formatted.append(f"{key}='{value}'")
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