from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
	
	class Meta:
		model = Car
		fields = '__all__'
		help_texts = {
			'bio': 'Deixar este campo em branco gera uma bio automática com chatbot Gemini',
		}

	def clean_value(self):
		value = self.cleaned_data.get('value')
		if value < 10000:
			self.add_error('value', 'Valor mínimo do carro deve ser de R$10.000')
		return value

	def clean_photo(self):
		photo = self.cleaned_data.get('photo')
		if not photo:
			return None
		
		if photo.size > 5 * 1024 * 1024:
			self.add_error('photo', 'A foto não pode ser maior que 5MB')

		return photo
