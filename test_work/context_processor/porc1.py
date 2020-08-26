from django.template.response import TemplateResponse
from test_app.models import Posts

def changeColor_White(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table-striped table-bordered"
    return(TemplateResponse(request, 'test1.html', context))

def changeColor_Black(request):
    context = {'info':Posts.get_data(self=Posts)}
    context['borders'] = "table-striped table-bordered"
    return(TemplateResponse(request, 'test1.html', context))