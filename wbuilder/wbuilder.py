"""
    wBuilder v3.0
    (c) 2020 Rodney Maniego Jr.
    https://github.com/rmaniego/wbuilder
    MIT License
"""

import os
import time
import random
import hashlib
from namari import Namari
from arkivist import Arkivist
from bs4 import BeautifulSoup as bs


class WebBuilder:
    def __init__(self, filepath=None, html=None):
        self.rels = Namari()
        self.filepath = filepath
        self.html = parse(html, "<!DOCTYPE html>")
        if html is None:
            self.rels.insert(["html", "head", "body"])
        self.selectors = Arkivist()
        self.Html5Tags = _getHtml5Tags()
        self.CSS3Attributes = _getAttributes()
        self.Html5Properties = _getProperties()
        self.autoWbIDs = []
        self.selector = None
        self.nth = None
        random.seed(1024)
    
    def at(self, selector, **kwargs):
        self.nth = None
        self.selector = None
        if isinstance((nth:=kwargs.get("nth", None)), int):
            self.nth = nth
        if isinstance(selector, str): # and self.rels.contains(selector):
            self.selector = selector
        return self
    
    def append(self, tag, id=None, data=None, text=None, html=None, escape=True, static=False, style=None, cached=True, **kwargs):
        if self.selector is not None:
            id2 = None
            attribs = {}
            attribs["tag"] = "div"
            if tag in self.Html5Tags:
                attribs["tag"] = tag
            if isinstance(text, str):
                attribs["html"] = text
            if isinstance(html, str):
                attribs["html"] = html
            attribs["escape"] = isinstance(escape, bool) and bool(escape)
            attribs["static"] = isinstance(static, bool) and bool(static)
            attribs["cached"] = isinstance(cached, bool) and bool(cached)
            if isinstance(id, str):
                attribs["class"] = []
                for i in id.split(" "):
                    if i[0] == "#":
                        id2 = i
                    else:
                        attribs["class"].append(i.replace(".", ""))
            while (id2 is None) or (id2 in self.selectors):
                id2 = _newId()
            self.autoWbIDs.append(id2)
            if isinstance(data, dict):
                for name, value in data:
                    if not len(name):
                        if "data-" not in name:
                            name = "data-" + str(name)
                        attribs[name] = value
            if isinstance(style, str):
                styling = {}
                for property in style.split(";"):
                    if len(property) > 0:
                        data = property.split(":")
                        if len(data) > 1:
                            if (key:=data[0].strip()) != "":
                                if self.CSS3Attributes.contains(key):
                                    if len((value:=data[1].strip())):
                                        styling.update({key: value})
                attribs["style"] = styling
            if isinstance(style, dict):
                styling = {}
                for key, value in style.items():
                    if self.CSS3Attributes.contains(key):
                        styling.update({key: value})
                attribs["style"] = styling
            for key, value in kwargs.items():
                key = key.lower().replace("_", "")
                if key in self.Html5Properties:
                    attribs[key] = value
            self.rels.set(self.selector, id2)
            self.selectors.set(id2, attribs)
        return self
    
    def prop(self, selector, property, value):
        if property == "style":
            return self.inlineCss(selector, value, reset=False)
        if property in self.Html5Properties or "data-" in property:
            if not (selector in self.selectors):
                self.selectors[selector] = {}
                self.selectors[selector].update({property: ""})
            self.selectors[selector][property] = value
    
    def inlineCss(self, selector, style, reset=False):
        if selector not in self.selectors:
            self.selectors[selector] = {"style": {}}
        if reset:
            self.selectors[selector].update({"style": {}})
        if isinstance(style, str):
            for property in style.split(";"):
                if len(property) > 0:
                    data = property.split(":")
                    if len(data) > 1:
                        if (key:=data[0].strip()) != "":
                            if self.CSS3Attributes.contains(key):
                                if len((value:=data[1].strip())):
                                    self.selectors[selector]["style"].update({key: value})
        if isinstance(style, dict):
            for key, value in style.items():
                if self.CSS3Attributes.contains(key):
                    if "style" not in self.selectors[selector]:
                        self.selectors[selector].update({"style": {key: value}})
                    else:
                        self.selectors[selector]["style"].update({key: value})
    
    def toJson(self, filepath):
        used = []
        json = Arkivist(filepath).reset()
        for selector, children in self.rels.items():
            for child in children:
                used.append(child)
                attribs = self.selectors[child]
                attribs["id"] = child
                attribs["selector"] = selector
                json.set(json.count(), attribs)
        for selector, attribs in self.selectors.items():
            if selector not in used:
                if len(attribs) > 0:
                    attribs["id"] = selector
                    attribs["selector"] = selector
                    json.set(json.count(), attribs)
        json.save()
    
    def fromJson(self, source):
        self.html = parse(None, "<!DOCTYPE html>")
        self.rels = Namari()
        self.selectors = Arkivist()
        self.rels.insert(["html", "head", "body"])
        
        json = {}
        if isinstance(source, dict):
            json = Arkivist().load(source)
        if isinstance(source, str):
            json = Arkivist(source)
        for _, attribs in json.items():
            selector = attribs["selector"]
            id = attribs["id"]
            if id != selector:
                self.rels.set(selector, id)
            self.selectors.set(id, attribs)

    def build(self):
        used = []
        for selector, children in self.rels.items():
            if len(parent:=self.html.select(selector)) > 0:
                for child in children:
                    used.append(child)
                    attribs = self.selectors.get(child, [])
                    if len(attribs) > 0:
                        element = _newTag(child, attribs)
                        parsed = parse(element)
                        if attribs["static"]:
                            if (tag:=attribs["tag"]) in ("link", "img", "script"):
                                attr = "href"
                                if tag in ("img", "script"):
                                    attr = "src"
                                for item in parsed.find_all(tag):
                                    source = item.attrs[attr]
                                    item.attrs[attr] = f"{{{{ url_for('static', filename='{source}') }}}}"
                        parent[0].append(parsed)
        for selector, attribs in self.selectors.items():
            if selector not in used:
                if len(attribs) > 0:
                    for parent in self.html.select(selector):
                        for property, value in attribs.items():
                            if property in self.Html5Properties and property != "id":
                                styles = ""
                                if property == "style" and isinstance(value, dict):
                                    for key, val in value.items():
                                        styles += f" {key}: {val};"
                                    value = styles.strip()
                                parent.attrs[property] = value
        for id in self.autoWbIDs:
            for element in self.html.find_all(id=id.replace("#", "")):
                del element.attrs["id"]
        return self.html.prettify()

    def save(self, filepath=None):
        if filepath is None:
            filepath = self.filepath
        if isinstance(filepath, str):
            filename = filepath.split("/")[-1]
            if len(filename):
                if filename[-5:] != ".html":
                    filename += ".html"
                fullpath = filename
                if len((filepath:=filepath.split("/"))) > 1:
                    fullpath = filepath[0:-2] + "/"
                _newFile(fullpath, self.build())

class Css:
    def __init__(self, csssheet=None, strict=False, sort=False):
        """
            Initialize CSS class
            ...
            Parameters
            ---
            csssheet: dict
                a valid dictionary of selectors and proprties
            strict: boolean
                only add properties found in CSS3Attributes
            sort: boolean
                sort the selectors and its properties
        """
        self.csssheet = Arkivist()
        if isinstance(csssheet, dict):
            self.csssheet.update(csssheet)
        self.fonts = Arkivist()
        self.strict = isinstance(strict, dict) and bool(strict)
        self.sort = isinstance(sort, dict) and bool(sort)
        self.CSS3Attributes = _getAttributes()

    def clean(self):
        """ Use when adding bulk selectors, removes unsupported properties """
        if self.strict:
            for selector, properties in self.csssheet.items():
                for property in properties:
                    if property not in self.CSS3Attributes:
                        properties.pop(property)
            csssheet[selector] = properties

    def add(self, selector, properties):
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
        if isinstance(properties, dict):
            if self.strict:
                for property in properties:
                    if property not in self.CSS3Attributes:
                        properties.pop(property)
            self.csssheet[selector].update(properties)

    def fromString(self, selector, data):
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
        properties = {}
        if isinstance(data, str):
            for item in data.split(";"):
                if item.strip() != "":
                    if not (self.strict and (property not in self.CSS3Attributes)):
                        property, value = item.split(":")
                        properties.update({property.strip(): value.strip()})
        self.csssheet[selector].update(properties)

    def get(self, selector):
        """
            Returns the property-value pairs of the selector
            ...
            Parameters
            ---
            selector: string
                CSS selector
        """
        return self.csssheet.get(selector, {})

    def remove(self, selector):
        """
            Removes the selector from the csssheet
            ...
            Parameters
            ---
            selector: string
                CSS selector
        """
        self.csssheet.pop(selector, None)

    def font(self, name, source):
        if isinstance(name, str) and isinstance(source, str):
            self.fonts[name] = source

    def build(self):
        """
            Returns a parsed, plain-text version of the csssheet
        """
        csssheet = []
        for selector, data in self.csssheet.items():
            attributes = []
            if self.sort:
                data = dict(sorted(data.items()))
            for attr, value in data.items():
                attributes.append(f"{attr}: {value};")
            cleaned = " ".join(attributes)
            csssheet.append(f"{selector} {{ {cleaned} }} ")
        if self.sort:
            csssheet.sort()
        for name, source in self.fonts.items():
            csssheet.insert(0, f"@font-face {{ font-family: {name}; src: url('{source}'); }}")
        return "\n".join(csssheet)

    def save(self, filepath):
        """
            Save the
            ...
            Parameters
            ---
            filepath: string
                directory of the csssheet
        """
        if isinstance(filepath, str):
            filename = filepath.split("/")[-1]
            if len(filename):
                if filename[-4:] != ".css":
                    filename += ".css"
                fullpath = filename
                if len((filepath:=filepath.split("/")) > 1):
                    fullpath = filepath[0:-2] + "/"
                _newFile(fullpath, self.build())

### html utils
def parse(html, default=None):
    if html is not None:
        return bs(html, 'html.parser')
    return bs(default, "html5lib")

def _newId():
    id = str(time.time())
    id += "-" + str(random.randint(0, random.randint(0, 2048)))
    return "#" + hashlib.md5(id.encode("utf-8")).hexdigest()

def _newTag(id, attribs):
    data = f"id=\"{id}\"".replace("#", "")
    for key, value in attribs.items():
        if key in ("tag", "selector", "id", "class", "text", "html", "escape", "static", "cached"):
            if key == "class" and len(value) > 0:
                value = " ".join(value)
                data +=f"{key}=\"{value}\""
            continue
        if key not in ("async", "defer", "disabled", "hidden", "readonly", "required"):
            if value != "":
                if key in ("href", "src"):
                    if not attribs["cached"]:
                        if "?" in value:
                            value = f"{value}&t=" + str(int(time.time()))
                        else:
                            value = f"{value}?t=" + str(int(time.time()))
                elif key == "style" and isinstance(value, dict):
                    styles = ""
                    for key, val in value.items():
                        styles += f" {key}: {val};"
                    value = styles.strip()
                data +=f"{key}=\"{value}\""
            continue
        data += f" {key}"
    html = attribs.get("html", "")
    if attribs["escape"] and len(html) > 0:
        codes = { "&": "&amp;", '"': "&quot;", "'": "&apos;", "<": "&lt;", ">": "&gt;" }
        html = "".join([codes.get(c, c) for c in html])
    tag = attribs["tag"]
    if tag not in ["meta", "link", "br", "input", "img"]:
        return f"<{tag} {data} >{html}</{tag}>"
    return f"<{tag} {data}>"

def _getHtml5Tags():
    return list("a,abbr,acronym,address,applet,area,article,aside,audio,b,base,basefont,bdi,bdo,big,blockquote,body,br,button,canvas,caption,center,cite,code,col,colgroup,data,datalist,dd,del,details,dfn,dialog,dir,div,dl,dt,em,embed,fieldset,figcaption,figure,font,footer,form,frame,frameset,h1,h6,head,header,hr,html,i,iframe,img,input,ins,kbd,label,legend,li,link,main,map,mark,meta,meter,nav,noframes,noscript,object,ol,optgroup,option,output,p,param,picture,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strike,strong,css,sub,summary,sup,svg,table,tbody,td,template,textarea,tfoot,th,thead,time,title,tr,track,tt,u,ul,var,video,wbr".split(","))

def _getAttributes():
    pairs = Namari()
    for x in list("align-content,align-items,align-self,animation,animation-delay,animation-direction,animation-duration,animation-fill-mode,animation-iteration-count,animation-name,animation-play-state,animation-timing-function,backface-visibility,background,background-attachment,background-clip,background-color,background-image,background-origin,background-position,background-repeat,background-size,border,border-bottom,border-bottom-color,border-bottom-left-radius,border-bottom-right-radius,border-bottom-css,border-bottom-width,border-collapse,border-color,border-image,border-image-outset,border-image-repeat,border-image-slice,border-image-source,border-image-width,border-left,border-left-color,border-left-css,border-left-width,border-radius,border-right,border-right-color,border-right-css,border-right-width,border-spacing,border-css,border-top,border-top-color,border-top-left-radius,border-top-right-radius,border-top-css,border-top-width,border-width,bottom,box-shadow,box-sizing,caption-side,clear,clip,color,column-count,column-fill,column-gap,column-rule,column-rule-color,column-rule-css,column-rule-width,column-span,column-width,columns,content,counter-increment,counter-reset,cursor,direction,display,empty-cells,flex,flex-basis,flex-direction,flex-flow,flex-grow,flex-shrink,flex-wrap,float,font,font-family,font-size,font-size-adjust,font-stretch,font-css,font-variant,font-weight,height,justify-content,left,letter-spacing,line-height,list-css,list-css-image,list-css-position,list-css-type,margin,margin-bottom,margin-left,margin-right,margin-top,max-height,max-width,min-height,min-width,opacity,order,outline,outline-color,outline-offset,outline-css,outline-width,overflow,overflow-x,overflow-y,padding,padding-bottom,padding-left,padding-right,padding-top,page-break-after,page-break-before,page-break-inside,perspective,perspective-origin,position,quotes,resize,right,tab-size,table-layout,text-align,text-align-last,text-decoration,text-decoration-color,text-decoration-line,text-decoration-css,text-indent,text-justify,text-overflow,text-shadow,text-transform,top,transform,transform-origin,transform-css,transition,transition-delay,transition-duration,transition-property,transition-timing-function,vertical-align,visibility,white-space,width,word-break,word-spacing,word-wrap,z-index".split(",")):
        pairs.set(x, x.replace("-", ""))
    return pairs
    
def _getProperties():
    return list("accesskey,align,background,bgcolor,class,content,contenteditable,contextmenu,draggable,height,hidden,id,item,itemprop,spellcheck,style,subject,tabindex,title,valign,width,async,defer,disabled,hidden,readonly,required,sizes,src,rel,icon,type,href,charset,name,text,http-equiv,title,colspan,rowspan,lang".split(","))

def _newFolders(filepath):
    try:
        if not os.path.exists(filepath):
            return os.makedirs(filepath)
    except:
        return False

def _newFile(filepath, content):
    try:
        with open(filepath, "w+") as f:
            f.write(content)
    except:
        pass