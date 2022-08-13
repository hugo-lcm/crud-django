from django.db import models

# Create your models here.


class Cliente(models.Model):  # herança

    SEXO_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Nenhuma das opções')
    )

    nome = models.CharField(max_length=100, blank=False)  # charfield = varchar
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(
        max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    def __str__(self):  # na hora de listar os clientes, retorna o nome do cliente ao invés do endereço de memória
        return self.nome
