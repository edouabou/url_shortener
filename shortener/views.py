from django.shortcuts import render, redirect, get_object_or_404

from .models import MiniURL
from .forms import MiniURLForm

def liste(request):
	""" Affichage des redirections """
	minis = MiniURL.objects.order_by('-nb_acces')
	return render(request, 'shortener/liste.html', locals())

def nouveau(request):
	""" Ajout d'une redirection """
	if request.method == "POST":
		form = MiniURLForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(liste)
	else:
		form = MiniURLForm()
	return render(request, 'shortener/nouveau.html', {'form': form})

def redirection(request, code):
	""" Redirection vers l'URL enregistrée """
	mini = get_object_or_404(MiniURL, code=code)
	mini.nb_acces += 1
	mini.save()
	return redirect(mini.url, permanent=True)