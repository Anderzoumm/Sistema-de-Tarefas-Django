from tarefas.models import Tarefa

from .erros import RegraDeNegocioError

# Regra de negócio: limite de tarefas pendentes por vez
LIMITE_PENDENTES = 3


def criar_tarefa(titulo):

    titulo = (titulo or '').strip()

    if not titulo:
        raise RegraDeNegocioError('O título da tarefa não pode ser vazio.')

    pendentes = Tarefa.objects.filter(status=Tarefa.PENDENTE)
    if pendentes.count() >= LIMITE_PENDENTES:
        raise RegraDeNegocioError(
            f'Você já tem {LIMITE_PENDENTES} tarefas pendentes. '
            'Conclua ou remova alguma antes de criar outra.'
        )

    if pendentes.filter(titulo__iexact=titulo).exists():
        raise RegraDeNegocioError('Já existe uma tarefa pendente com esse título.')

    return Tarefa.objects.create(titulo=titulo)