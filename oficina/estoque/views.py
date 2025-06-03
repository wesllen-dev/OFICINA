from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemEstoque
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque
        fields = '__all__'

def dashboard(request):
    itens = ItemEstoque.objects.all()
    return render(request, 'estoque/dashboard.html', {'itens': itens})

def novo_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'estoque/form_item.html', {'form': form, 'titulo': 'Novo Item'})

def entrada_estoque(request, item_id):
    item = get_object_or_404(ItemEstoque, id=item_id)
    if request.method == 'POST':
        valor = int(request.POST.get('valor'))
        item.quantidade += valor
        item.save()
        return redirect('dashboard')
    return render(request, 'estoque/form_item.html', {'form': None, 'titulo': f'Entrada de Estoque - {item.nome}', 'item': item})

def saida_estoque(request, item_id):
    item = get_object_or_404(ItemEstoque, id=item_id)
    if request.method == 'POST':
        valor = int(request.POST.get('valor'))
        item.quantidade -= valor
        item.save()
        return redirect('dashboard')
    return render(request, 'estoque/form_item.html', {'form': None, 'titulo': f'Saída de Estoque - {item.nome}', 'item': item})
