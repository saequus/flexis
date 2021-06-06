from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

async def add_equal_sign(value: str) -> str:
    return value + '=='

def new_thing(request):
    return HttpResponse("Hello, world. You're at the polls index.")
