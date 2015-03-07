from django.views.generic import UpdateView
from django.core.urlresolvers import reverse

class UpdateViewCustom(UpdateView):
    template_name = 'en/public/cbv/UpdateViewCustom.html'
    url_name=''
    #esta linea se emplea para crear la propiedad url_name. Esta propiedad nos ayudara a definir el nombre de las
    #url actuales. De esta forma podemos agregar el link en el atributo action de la forma
    def get_success_url(self):
        return reverse(self.success_url)
    def get_context_data(self, **kwargs):
        context=super(UpdateViewCustom,self).get_context_data(**kwargs)
        model_name = self.model._meta.verbose_name.title()
        context['model_name']=model_name
        context['url_name']=self.url_name
        return  context
