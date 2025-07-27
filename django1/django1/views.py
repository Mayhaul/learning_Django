# User Request
#     ↓
# urls.py → matches path → views.py
#     ↓
# View logic runs → generates response
#     ↓
# Response sent back to user

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Mehuuu")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Kidda")

def contact(request):
    return HttpResponse("@Mayhaul.__")

