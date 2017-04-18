from django.shortcuts import render
from django.http import HttpResponse
from cms_templates_app.models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def barra(request):
    if request.user.is_authenticated():
        login = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        login = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    resp = "Las direcciones disponibles son: "
    lista_pages = Pages.objects.all()
    for page in lista_pages:
        resp += ("<br>-<a href='/" + page.name + "'>" + page.name +
                 "</a> --> " + page.page)

    return HttpResponse(login + resp)

def barraAnnotated(request):
    if request.user.is_authenticated():
        login = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        login = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    content = "Las direcciones disponibles son: "
    lista_pages = Pages.objects.all()
    for page in lista_pages:
        content += ("<br>-<a href='/" + page.name + "'>" + page.name +
                 "</a> --> " + page.page)

    plantilla = get_template("miplantilla.html")
    resp = Context({'title': login, 'content': content})

    return HttpResponse(plantilla.render(resp))

@csrf_exempt
def process(request, req):
    if request.user.is_authenticated():
        login = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        login = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    if request.method == "GET":
        try:
            page = Pages.objects.get(name=req)
            resp = "La página solicitada es /" + page.name + " -> " + page.page
        except Pages.DoesNotExist:
            resp = "La página introducida no está en la base de datos. Créala:"
            resp += "<form action='/" + req + "' method='POST'>"
            resp += "Nombre: <input type='text' name='nombre'>"
            resp += "<br>Página: <input type='text' name='page'>"
            resp += "<input type='submit' value='Enviar'></form>"
    elif request.method == "POST":
        if request.user.is_authenticated():
            nombre = request.POST['nombre']
            page = request.POST['page']
            pagina = Pages(name=nombre, page=page)
            pagina.save()
            resp = ("Has creado la página " + nombre +
                    " con ID " + str(pagina.id))
        else:
            resp = "Necesitas <a href='/login/'>hacer login</a>"
    elif request.method == "PUT":
        if request.user.is_authenticated():
            try:
                page = Pages.objects.get(name=req)
                resp = "Ya existe una página con ese nombre"
            except Pages.DoesNotExist:
                page = request.body
                pagina = Pages(name=req, page=page)
                pagina.save()
                resp = "Has creado la página " + req
        else:
            resp = "Necesitas <a href='/login/'>hacer login</a>"

    else:
        resp = "Error. Method not supported."

    return HttpResponse(login + resp)


@csrf_exempt
def processAnnotated(request, req):
    if request.user.is_authenticated():
        login = ("Logged in as " + request.user.username +
                 ". <a href='/logout/'>Logout</a><br/><br/>")
    else:
        login = "Not logged in. <a href='/login/'>Login</a><br/><br/>"

    if request.method == "GET":
        try:
            page = Pages.objects.get(name=req)
            content = "La página solicitada es /" + page.name + " -> " + page.page
        except Pages.DoesNotExist:
            content = "La página introducida no está en la base de datos. Créala:"
            content += "<form action='/" + req + "' method='POST'>"
            content += "Nombre: <input type='text' name='nombre'>"
            content += "<br>Página: <input type='text' name='page'>"
            content += "<input type='submit' value='Enviar'></form>"
    elif request.method == "POST":
        if request.user.is_authenticated():
            nombre = request.POST['nombre']
            page = request.POST['page']
            pagina = Pages(name=nombre, page=page)
            pagina.save()
            content = ("Has creado la página " + nombre +
                    " con ID " + str(pagina.id))
        else:
            content = "Necesitas <a href='/login/'>hacer login</a>"
    elif request.method == "PUT":
        if request.user.is_authenticated():
            try:
                page = Pages.objects.get(name=req)
                content = "Ya existe una página con ese nombre"
            except Pages.DoesNotExist:
                page = request.body
                pagina = Pages(name=req, page=page)
                pagina.save()
                content = "Has creado la página " + req
        else:
            content = "Necesitas <a href='/login/'>hacer login</a>"

    else:
        content = "Error. Method not supported."

    plantilla = get_template("miplantilla.html")
    resp = Context({'title': login, 'content': content})

    return HttpResponse(plantilla.render(resp))
