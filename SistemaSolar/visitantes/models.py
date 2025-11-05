from django.db import models


class Visitante(models.Model):
    nome_completo = models.CharField (verbose_name = 'Nome completo',
                                      max_length = 100)
    
    data_nascimento = models.DateField(verbose_name = 'Data de Nascimento',
                                       auto_now = False,
                                       auto_now_add = False,
                                       help_text="Insira a data no formato dd-mm-aaaa"
                                       )

    horario_visita = models.DateTimeField(verbose_name = 'Horário de Visita no Site',
                                              auto_now_add = True
                                            )

    email = models.EmailField(verbose_name= "E-mail de contato",
                              max_length= 100, 
                              unique= True)

    opcoes = [
        ('5', '5 - Bom'),
        ('6', '6 - Muito Bom'),
        ('7', '7 - Ótimo'),
        ('8', '8 - Excelente'),
        ('9', '9 - Maravilhoso'),
        ('10', '10 - Perfeito'),
    ]

    nota = models.CharField(verbose_name = 'Deixe sua avaliação sobre o site',
                            choices = opcoes,
                             max_length = 10,
                             default= '10',
                             )
    
    comentario = models.TextField(verbose_name = 'Deixe seu comentário',
                                   max_length=500,
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'

    def __str__(self):
        return self.nome_completo

    


# Create your models here.
