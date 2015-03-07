from django.views.generic import DetailView
from TaskManager.models import Developer, Task
from django.db.models import Q


class Developer_detail(DetailView):
    model = Developer
    template_name = 'en/public/developer_detail.html'
    def get_context_data(self,**kwargs):
        '''Esto sobreescribe el metodo get_context_data()'''
        context=super(Developer_detail,self).get_context_data(**kwargs)
        #Esto permite llamar el metodo de la superclase. Sin esta linea no tendriamos el contexto basico
        task_dev = Task.objects.filter(Q(developer1=self.object) | Q(developer2=self.object))
        #Esto nos permite obtener la lista de las tareas del desarrollador.
        #utilizamos self.object, que es un objeto tipo Developer ya definido por la clase DetailView
        context['task_dev']=task_dev
        #en esta linea agregamos la lista de tareas al contexto.
        return context

