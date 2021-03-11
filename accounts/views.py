from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import ClienteForm

# Create your views here.

def index(request):
    clientes = Customer.objects.all()

    return render(request, 'index.html', {'clientes' : clientes})

def create(request):
    form = ClienteForm()

    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    contexto = {'form': form}
    return render(request, 'create.html', contexto)

def delete(request, pk):
    cliente = get_object_or_404(Customer, id=pk)

    if request.method == 'POST':
        cliente.delete()

        return redirect('/')
    
def edit(request, pk):
    cliente = get_object_or_404(Customer, id=pk)

    # crea y rellana el formulario con los datos de cliente
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    contexto = {'form':form}

    return render(request, 'edit.html', contexto)
    
