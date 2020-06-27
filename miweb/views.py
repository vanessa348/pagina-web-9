from django.shortcuts import render, HttpResponse

def index(request):
    lista_peliculas = ["titanic","mulan","up","caca"]
    context = { "peliculas": lista_peliculas,
                "numero_de_peliculas": len(lista_peliculas)} 
    return render(request, "index.html",context)

def contacto(request):
    return HttpResponse("mi mail es vanvenegas@alumnos.uai.cl")


