from django.shortcuts import render

from django.views.generic import TemplateView

class HomepageView(TemplateView): 
    template_name = 'index.html'

    
