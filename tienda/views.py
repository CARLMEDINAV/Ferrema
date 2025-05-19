from django.shortcuts import render,redirect
from .forms import ClienteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def carrito(request):
    return render(request, 'carrito.html')

def index(request):
    return render(request, 'index.html')

def formulario_agregar_producto(request):
    return render(request, 'agregar_producto.html')

def listar_eliminar_producto(request):
    return render(request, 'listar_productos.html')




def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Puedes crear una vista 'login' después
    else:
        form = ClienteForm()
    return render(request, 'registro.html', {'form': form})