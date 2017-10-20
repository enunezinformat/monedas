from django.shortcuts import render, get_object_or_404, redirect, reverse
from crud.forms import MonedasForm


from .models import Monedas

# Create your views here.
def index(request):

    monedas = Monedas.objects.all().order_by('id')

    context = {'monedas': monedas, 'titulo': 'Monedas'}
    return render(request, 'crud/index.html', context)


def nuevo(request):

    if request.method == 'POST':
        print("En POST")

        form = MonedasForm(request.POST)

        if form.is_valid():
            print("Formulario válido")

            moneda = Monedas()
            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']

            moneda.save()

            print("moneda grabada" + str(moneda.id))

            return redirect(reverse('crudindex'))

    else:
        print("Creando nueva moneda")
        form = MonedasForm()

    context = {'formulario': form}
    return render(request, 'crud/nuevo.html', context)


def eliminar(request, pk):

    moneda = get_object_or_404(Monedas, pk=pk)

    if request.method == 'POST':
        print("En POST")

        moneda.delete()

        print("Moneda borrada")

        return redirect(reverse('crudindex'))

    else:
        print("estoy consultando")

        m = {'nombre': moneda.nombre,
            'abreviacion': moneda.abreviacion
        }

        form = MonedasForm(m)

    context = {'moneda': moneda, 'formulario': form}
    return render(request, 'crud/eliminar.html', context)


def editar(request, pk):

    moneda = get_object_or_404(Monedas, pk=pk)

    if request.method == 'POST':
        print("En POST")

        form = MonedasForm(request.POST)

        if form.is_valid():
            print("Formulario válido")

            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']
            moneda.save()

            print("moneda grabada !!!")

            return redirect(reverse('crudindex'))

    else:
        print("estoy consultando")

        m = {'nombre': moneda.nombre,
            'abreviacion': moneda.abreviacion
        }

        form = MonedasForm(m)

    context = {'moneda': moneda, 'formulario': form}
    return render(request, 'crud/editar.html', context)
