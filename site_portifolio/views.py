from django.shortcuts import render

# Create your views here.

def home(request):
    nome= 'Bianca'
    conhecimentos = ['HTML', 'CSS', 'JavaScript', 'Phyton', 'Django', 'Git', 'Tamborim', 'Dar cambalhotas', 'Plantar bananeira']
    return render(request, 'index.html', {'conhecimentos': conhecimentos, 'nome': nome})