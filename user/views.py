from django.shortcuts import render, HttpResponse
from django.http import HttpRequest


def login_form(request: HttpRequest):
    ...


def recieving_sth_from_browser(request: HttpRequest):
    ...


def sending_sth_to_browser(request: HttpRequest):
    ...


def saying_hi_to_browser(request: HttpRequest):
    return HttpResponse("HI ^^")
