from django import path
from . import views


url_patterns=[
    path("",views.home,name=home),