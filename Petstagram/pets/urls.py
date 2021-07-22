from django.urls import path

from Petstagram.pets import views
from Petstagram.pets.views import list_pets, pet_details, like_pet, edit_pet, delete_pet





urlpatterns = [
    path('', list_pets, name='all-pets-photos'),
    path('create_pet/', views.create_pet, name='create_pet'),
    path('details/<int:pk>', views.pet_details, name='pet-details'),
    path('edit_pet/<int:pk>', views.edit_pet, name='edit_pet'),
    path('delete_pet/<int:pk>', views.delete_pet, name='delete_pet'),
    path('like/<int:pk>', like_pet, name='like pet')

]