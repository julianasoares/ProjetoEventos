from appeventos.forms import *
from appeventos.models import *
from appeventos.models import Evento
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms import modelform_factory
from django.shortcuts import render,redirect


def home(request):
   return render(request,'base.html')

def orcamento_new(request):
    if (request.method=="POST"):
        orcamento_form=OrcamentoForm(request.POST)
        if (orcamento_form.is_valid()):
            orcamento=orcamento_form.save(commit=False)
            orcamento_formset=OrcamentoFormSet(request.POST,instance=orcamento)
            if (orcamento_formset.is_valid()):
                orcamento_form.save()
                orcamento_formset.save()
                return redirect('evento_list')
        else:
            orcamento_formset=OrcamentoFormSet(request.POST)
    else:
        orcamento_form=OrcamentoForm()
        orcamento_formset=OrcamentoFormSet()
    dados={'form_orcamento':orcamento_form,'form_orcamento_item':orcamento_formset}
    return render(request,'evento_form.html',dados)

