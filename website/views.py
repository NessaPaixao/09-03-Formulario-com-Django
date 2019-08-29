from django.shortcuts import render
from website.models import Pessoa, Ong
# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

    return render(request, 'index.html')

def pessoas(request):
    p = Pessoa.objects.filter(ativo=True).all()

    contexto = {
        'pessoas': p
    }
    return render(request, 'pessoas.html', contexto)

def ong(request):

    if request.method == 'POST':
        ong = Ong()
        ong.nome = request.POST.get('nome')
        ong.sobrenome = request.POST.get('sobrenome')
        ong.nome_ong = request.POST.get('nome_ong')
        ong.email = request.POST.get('email')
        ong.str_cep = request.POST.get('str_cep')
        ong.str_numero = request.POST.get('str_numero')
        ong.referencia = request.POST.get('referencia')
        ong.telefone = request.POST.get('telefone')
        ong.horario_atendimento = request.POST.get('horario_atendimento')
        ong.observacao = request.POST.get('observacao')
        ong.save()

        contexto = {
            'nome': ong.nome
        }
        return render(request, 'ong.html', contexto)

    return render(request, 'ong.html')

def ongs_cadastradas(request):
    o = Ong.objects.all()

    contexto = {
        'Ongs': o
    }
    return render(request, 'ongs.html', contexto)
