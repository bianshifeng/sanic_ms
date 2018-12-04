import sys

from sanic import Blueprint
from sanic.response import html

from src.config import CONFIG

html_bp = Blueprint('html_rss', url_prefix = 'html')
html_bp.static('/static/html_rss',CONFIG.BASE_DIR + '/statics/html_rss')



