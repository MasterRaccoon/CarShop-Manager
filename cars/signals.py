from django.db.models.signals import pre_save, post_delete, post_save
from django.db.models import Sum
from django.dispatch import receiver
from django.core.files.storage import default_storage
from cars.models import Car, CarInventory
# from openai_api.client import get_car_ai_bio
from gemini_api.client import get_car_ai_bio

# Deletar foto da pasta media/ caso o caminho da foto seja removido do bd
@receiver(pre_save, sender=Car)
def delete_photo_when_removed_from_db(sender, instance, **kwargs):
	if instance.pk:
		try:
			old_instance = Car.objects.get(pk=instance.pk)
		except Car.DoesNotExist:
			return
		old_photo = old_instance.photo
		if old_photo and not instance.photo:
			if default_storage.exists(old_photo.name):
				default_storage.delete(old_photo.name)

# Deletar foto da pasta media/ caso o carro seja removido do bd
@receiver(post_delete, sender=Car)
def delete_photo_on_delete(sender, instance, **kwargs):
	if instance.photo:
		if default_storage.exists(instance.photo.name):
			default_storage.delete(instance.photo.name)

# Gerar Bio do carro caso nao seja informada
@receiver(pre_save, sender=Car)
def generate_car_bio(sender, instance, **kwargs):
	if not instance.bio:
		ai_bio = get_car_ai_bio(
			instance.model, instance.brand, instance.model_year
		)
		instance.bio = ai_bio

# atualiza o inventario de carros e o valor do inventario
def car_inventory_update():
	cars_count = Car.objects.all().count()
	cars_value = Car.objects.aggregate(total_value = Sum('value'))['total_value']
	CarInventory.objects.create(cars_count = cars_count, cars_value = cars_value)

@receiver(post_save, sender=Car)
def car_update_if_save(sender, instance, **kwargs):
	car_inventory_update()

@receiver(post_delete, sender=Car)
def car_update_if_delete(sender, instance, **kwargs):
	car_inventory_update()