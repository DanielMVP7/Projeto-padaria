from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):

    ESCOLHA_SEXO = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    )

    id_cliente = models.AutoField(primary_key=True)

    nome_completo = models.CharField(
        max_length=80,
        null=False,
        blank=False
        )
    

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
        )
    senha = models.CharField(
        default='',
        max_length=30,
        null=False,
        blank=False
    )

    data_nascimento = models.DateField(
        blank=True,
        null=True
        )
    
    sexo = models.CharField(
        max_length=1,
        choices=ESCOLHA_SEXO
        )
    
    foto = models.ImageField(
        null=True,
        blank=True
        )
    
class Produto(models.Model):

    Pão = models.IntegerField(
        null=False,
        blank=False
    )

    Bolo = models.IntegerField(
        null=False,
        blank=False
    )

    Presunto = models.IntegerField(
        null=False,
        blank=False
    )

    Queijo = models.IntegerField(
        null=False,
        blank=False
    )

class Info(models.Model):

    DIN_OU_CART = (
        ('d', 'Dinheiro'),
        ('c', 'Cartão'),
    )

    Endereço = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    Forma_de_pagamento = models.CharField(
        max_length=1,
        choices=DIN_OU_CART
    )

    Precisa_de_Troco = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )


