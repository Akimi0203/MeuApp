import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from .models import Produto
from .models import Preco_Produto
from django.contrib import messages #Biblioteca de mensagens Django
from .forms import ProdutoForm

def Meuapp(request):
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
     #print(cotacao)
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_dolar2 = cotacao['USDBRL']['create_date']
    return render(request, 'html.html', {'cotacao_dolar': cotacao_dolar, 'horario': cotacao_dolar2})


#Salvar_Produto
def dados(request):
    descricao = request.POST.get('descricao')
    codigo = request.POST.get('cod_Produto')
    #Antes de gravar, verificar se foi digitado algo!
    if codigo == "" or descricao == "":
        messages.info(request, "Digite um código e descrição do produto")
        return redirect('/Meuapp/produto/')
    else:
        if Produto.objects.filter(cod_Produto=codigo).exists():
            messages.info(request, 'Codigo de produto já cadastrado:')
            return redirect('/Meuapp/produto/')
        else:
            if Produto.objects.filter(descricao=descricao).exists():
                messages.info(request, 'Descrição de produto já cadastrado:')
                return redirect('/Meuapp/produto/')
            else:
                produto=Produto(
                cod_Produto=codigo,
                descricao=descricao
                 )
                produto.save()
                return consultar_ultimo(request)

    # preco = request.POST.get('preco')
    # preco_produto = Preco_Produto(
    #     valor=preco,
    #     cod_produto=Produto.objects.last()
    # )
    # print(preco)
    #preco_produto.save()


def consultar_ultimo(request):
    cons_ultimo = Produto.objects.last()
    #return render(request, 'ler_produto.html', {'cons_ultimo': cons_ultimo})
    return render(request, 'produto_cadastrado.html', {'cons_ultimo': cons_ultimo})

def consultar_todos(request):
    cons_todos = Produto.objects.all()
    return render(request, 'ler_produto.html', {'cons_todos': cons_todos})

def apagar(request, id):
    apagar_produto = Produto.objects.get(id=id)
    apagar_produto.delete()
    return consultar_todos(request)


def raiz_produto(request):
    return render(request,'produto_cadastrado.html')



def editar(request, id):
    produto = Produto.objects.filter(id=id).first()
    form = ProdutoForm(instance=produto)

    if (request.method =='POST'):
        form = ProdutoForm(request.POST, instance=produto)
        if (form.is_valid()):
            produto.save()
            return redirect('cons_todos')
        else:
            return render(request, 'editar.html', {'form': form, 'produto': produto})
    else:
        return render(request, 'editar.html', {'form': form, 'produto': produto})



    # return render(request, 'produto_cadastrado.html', {'cons_ultimo': cons_ultimo})








