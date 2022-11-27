# -*- coding: utf-8 -*-

from django.shortcuts import render
import json

from django.shortcuts import render, redirect
from .forms import RegisterForm


def index(request):
    args = request.GET if request.method == 'GET' else request.POST
    args = request.GET if request.method == "GET" else json.loads(request.body)
    return render(request, 'index.html')
