from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now



from datetime import datetime

# Create your views here.
@api_view(["GET"])
def intern_details(request):
    data = {
        "email": "princewillfidelis1@gmail.com",
        "current_datetime": now().isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/PrincewillDev/Public-Api"
    }
    return JsonResponse(data, status=status.HTTP_200_OK)