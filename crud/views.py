from django.shortcuts import render, get_object_or_404


from .models import Monedas

# Create your views here.
def index(request):

    monedas = Monedas.objects.all()
    context = {'monedas': monedas, 'titulo': 'Monedas'}
    return render(request, 'crud/index.html', context)

def editar(request, pk):

    moneda = get_object_or_404(Monedas, pk=pk)
    context = {'moneda': moneda}
    return render(request, 'crud/editar.html', context)
