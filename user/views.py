from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

name = ""

def login_form(request):
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<form action="http://localhost:8000/user/post/" method="POST">
    <input type="text" id="username" name="username" placeholder="username" >
    <input type="password" id="password" name="password" placeholder="password" >
    <button type="submit" >login</button>
</form>    
</body>
</html>
    """
    return HttpResponse(html)

def recieving_sth_from_browser(request):
    global name
    name = request.POST['username']
    pasw = request.POST['password']
    return HttpResponse("submitted")


def sending_sth_to_browser(request):
    global name
    return HttpResponse(f"Name={name}")


def saying_hi_to_browser(request):
    return HttpResponse("HI ^^")