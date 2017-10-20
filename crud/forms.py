from django import forms

class MonedasForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control',
                                        'placeholder': 'Nombre de la moneda'
        }),
        label='Nombre',
        max_length=30
    )
    abreviacion = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control',
                                        'placeholder': 'Abreviación'
        }),
        label='Abreviación',
        max_length=3
    )
