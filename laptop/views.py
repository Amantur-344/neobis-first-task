from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from laptop.forms import LaptopCreateUpdateForm
from laptop.models import Laptop, Gadget


def main_page(request):
    laptops = Laptop.objects.all().order_by('-date_created')
    gadgets = Gadget.objects.all().order_by('-date_created')

    context = {
        'laptops': laptops,
        'gadgets': gadgets,
    }
    return render(request, 'laptops/index.html', context)


def laptop_detail(request, pk):
    laptop = Laptop.objects.filter(id=pk).first()

    context = {
        'laptop': laptop,
    }
    return render(request, 'laptops/laptop-single.html', context)


def gadget_detail(request, pk):
    gadget = Gadget.objects.filter(id=pk).first()

    context = {
        'gadget': gadget,
    }
    return render(request, 'laptops/gadget-single.html', context)


@login_required
def create_laptop(request):
    if request.method == 'POST':
        form = LaptopCreateUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            laptop = form.save(commit=False)
            laptop.save()
            return redirect('main_page')
    form = LaptopCreateUpdateForm()
    context = {
        'form': form
    }
    return render(request, 'laptops/laptop_create.html', context)
