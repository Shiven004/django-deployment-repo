#Import modules here.
from django.views.generic import TemplateView

#Define View here
class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'
