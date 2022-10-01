from multiprocessing import context
from django.shortcuts import render ,redirect
from .models import *
from django.http.response import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.


def disp_doc(request):
    context = {}
    context ['data'] = Doctor.model

    
