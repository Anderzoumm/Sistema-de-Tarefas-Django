from django.db import models


class Tarefa(models.Model):
    # Opções possíveis para o status da tarefa
    PENDENTE = 'pendente'
    CONCLUIDA = 'concluida'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (CONCLUIDA, 'Concluída'),
    ]

    titulo = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=PENDENTE,
    )
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo