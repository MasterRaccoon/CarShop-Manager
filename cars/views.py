from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
 
class CarsListView(ListView):
	model = Car
	template_name = 'cars.html'
	context_object_name = 'cars'

	def get_queryset(self):
		cars = super().get_queryset().order_by('brand__name','model')
		search = self.request.GET.get('search')
		if search:
			cars = cars.filter(
				Q(brand__name__icontains=search) | Q(model__icontains=search)
			)
		return cars

class CarDetailView(DetailView):
	model = Car
	template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
	model = Car
	form_class = CarModelForm
	template_name = 'new_car.html'
	success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
	model = Car
	form_class = CarModelForm
	template_name = 'car_update.html'
	
	def form_valid(self, form):
		car = form.save(commit=False)

		# Verifica se o checkbox para remover a foto está marcado
		if self.request.POST.get('photo-clear'):
			car.photo.delete(save=False)  # Remove o arquivo do sistema de arquivos
			car.photo = None  # Limpa o campo photo no banco de dados

		car.save()  # Salva a instância
		return super().form_valid(form)  # Retorna o sucesso da operação

	def get_success_url(self):
		return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
	model = Car
	template_name = 'car_delete.html'
	success_url = '/cars/'
