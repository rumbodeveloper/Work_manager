from django.views.generic.list import ListView
# en esta linea, importamos clase ListView
from TaskManager.models import Project


class Project_list(ListView):
    model=Project
    template_name = 'en/public/project_list.html'
    paginate_by = 5

    def get_queryset(self):
        #en esta linea sobreescribimos el metodo get_queryset original
        #para que nos traiga los datos ordenados por titulo
        queryset = Project.objects.all().order_by('title')
        return queryset