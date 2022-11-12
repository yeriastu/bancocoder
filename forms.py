from django import forms

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    nro_cuenta = forms.IntegerField ()
    documento = forms.IntegerField()