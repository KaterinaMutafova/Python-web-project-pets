from django.shortcuts import render, redirect

# Create your views here.
from Petstagram.common.forms import CommentForm
from Petstagram.common.models import Comment
from Petstagram.pets.forms import PetForm, EditPetForm
from Petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,

    }
    return render(request, 'pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    comments = Comment.objects.filter(pet=pet)

    comment_form = CommentForm()
    context = {
            'pet': pet,
            'comments': comments,
            'comment_form': comment_form,
    }
    return render(request, 'pet_detail.html', context)




def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet
    )
    like.save()
    return redirect('all-pets-photos')


def create_pet(request):
    template = 'pet_create.html'
    if request.method == "GET":
        form = PetForm()
        context = {
            'form': form
        }
        return render(request, template, context)
    form = PetForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('all-pets-photos')
    context = {
        'form': form
    }
    return render(request, template, context)


def edit_pet(request, pk):
    template = 'pet_edit.html'
    pet = Pet.objects.get(pk=pk)
    if request.method == "GET":
        form = EditPetForm(instance=pet)
        context = {
            'form': form
        }
        return render(request, template, context)
    form = EditPetForm(request.POST, request.FILES, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('all-pets-photos')
    form = EditPetForm(instance=pet)
    context = {
        'form': form
    }
    return render(request, template, context)


def delete_pet(request):
    pass



