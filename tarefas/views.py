from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Tarefa
from .services.criar_tarefa import criar_tarefa
from .services.erros import RegraDeNegocioError


def lista_tarefas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')

        try:
            criar_tarefa(titulo)
            messages.success(request, 'Tarefa criada com sucesso!')
        except RegraDeNegocioError as erro:
            messages.error(request, str(erro))

        return redirect('lista_tarefas')

    tarefas = Tarefa.objects.order_by('-criada_em')
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})


def remover(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.filter(id=tarefa_id).first()

        if tarefa is None:
            messages.error(request, 'Essa tarefa não existe ou já foi removida.')
        else:
            tarefa.delete()
            messages.success(request, f'Tarefa "{tarefa.titulo}" removida.')

    return redirect('lista_tarefas')