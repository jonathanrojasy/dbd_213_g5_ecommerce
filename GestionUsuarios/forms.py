from django.forms import ModelForm, EmailInput, TextInput

from GestionUsuarios.models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'id_usuario': 'SP'+'cod_documento',
            'correo_electronico': EmailInput(attrs={'type':'email'}),
            'telefono': TextInput(attrs={'type':'email'})

        }





