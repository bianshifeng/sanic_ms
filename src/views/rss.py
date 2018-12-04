# !/usr/bin/env python

from sanic import Sanic
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape

import sys
#开启异步特性 要求3.6+
enable_async = sys.version_info >= (3,6)

app = Sanic()

# jinja2 config

env = Environment(
    loader = PackageLoader('views.rss','../templates'),
    autoescape = select_autoescape(['html','xml','tpl']),
    enable_async = enable_async)


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template  = await temlate.render_async(**kwargs)
    return html(rendered_template)


@app.route("/")
async def index(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = [1,2,3,3,3,3,3]
    data = []
    for article in articles:
        data.append({"title":"bianshifeng","link":article})
    return json(data)

@app.route("/html")
async def rss_html(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = [1,2,3,4,5,6,7]
    data =[]
    for article in articles:
        data.append({
            "title": "bianshifeng",
            "link":article,
            "published":article
            })
    return await template('rss.html',articles = data)


