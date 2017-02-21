from appeventos.models import *
from django.forms import ModelForm
from django.forms.models import inlineformset_factory


class OrcamentoForm(ModelForm):
    class Meta:
        model=OrcamentoEvento
        fields=('nome','email','cpf','telefone1','telefone2','rua','bairro',
                'numero','cidade','tipoEvento','dataEvento','quantPessoas','horaExtra')

class OrcamentoItemForm(ModelForm):
    class Meta:
        model = OrcamentoEventoItem
        fields = ('idItem', 'quantidade')
        error_messages = {
            'idItem': {
                'required': 'Informe o Item',
            },
            'quantidade': {
                'required': 'Informe a Quantidade',
            }
        }
OrcamentoFormSet = inlineformset_factory(OrcamentoEvento, OrcamentoEventoItem, fields=('idItem', 'quantidade'),can_delete=False)
