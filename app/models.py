from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_field=50)
    pai = models.CharField(max_field=50)
    mae = models.CharField(max_field=50)
    cpf = models.CharField(max_field=11)
    data_nasc = models.DateField(),
    email = models.EmailField(),
    cidade = models.ForeignKey(Cidade,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=50)
    telefone = models.Charfield(max_length=13)

    def __str__(self):
        return self.nome

class AreaDoSaber(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(AreaDoSaber,
                                   on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.instituicao}'

class Periodo(models.Model):
    periodo = models.PositiveIntegerField()

    def __str__(self):
        return self.periodo

class Disciplina(models.Model):
    nome = models.CharField(50)
    area_saber = models.ForeignKey(AreaDoSaber,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, 
                                    on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,
                            on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa,
                               on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.pessoa} {self.curso} {self.instituicao}'
    
class Avaliacao(models.Model):
    descricao = models.CharField(50)
    curso = models.ForeignKey(Curso,
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.curso}'

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso,
                              on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,
                                   on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.disciplina} {self.numero_faltas}'

class Turma(models.Model):
    nome = models.CharField(50)
    turno = models.CharField(50)

    def __str__(self):
        return f'{self.nome} {self.turno}'



    



    

    




