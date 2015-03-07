from django.views.generic import UpdateView
from TaskManager.models import Task
from django.forms import ModelForm
from django.core.urlresolvers import reverse

class Form_task_time(ModelForm):
    #en esta linea, creamos una forma que extiende ModelForm. Las views UpdateView and CreateView CBV estan
    #basadas en un systema ModelForm
    class Meta:
        model =Task
        fields = ['time_elapsed']
        #esto para para definir los campos que aparecederan en la forma

class Task_update_time(UpdateView):
    model = Task
    template_name = 'en/public/update_task_developer.html'
    #TODO esta sin terminar, pagina 223
