from rest_framework import viewsets
from .models import Alcance
from .serializer import AlcanceSerializer

class AlcanceViewSet(viewsets.ModelViewSet):
    queryset = Alcance.objects.all()
    serializer_class = AlcanceSerializer


# class Home(TemplateView):
#     template_name = "home_page.html"

#     def get_context_data(self, **kwargs):

#         alcance = Alcance.objects.all()
        
#         return {'descripcion':alcance}