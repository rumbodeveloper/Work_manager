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
    form_class = Form_task_time
    #en estal inea, imponemos nuestra CBV para usar el model form que
    #hemos creado. Cuando no defines esta linea, Django automaticamente
    #genera un model form
    success_url = 'public_index'
    def get_success_url(self):
        return reverse(self.success_url)

