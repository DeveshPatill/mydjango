from django import views
from . import views


url_patterns=[
    __path__("",views.home,name=home)
]