from django.views.generic import TemplateView
from .models import Alcance

class Home(TemplateView):
    template_name = "home_page.html"

    def get_context_data(self, **kwargs):

        alcance = Alcance.objects.all()
        
        return {'descripcion':alcance}