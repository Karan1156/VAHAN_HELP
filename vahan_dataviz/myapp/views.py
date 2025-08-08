from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import requests
import pandas as pd
from datetime import datetime

# Dates
start_date = "2025-01-01"
end_date = datetime.now().strftime("%Y-%m-%d")

# API URL
url = f"https://parivahanmitra.com/finance-task-export-json?startDate=${start_date}&endDate=${end_date}"

# Fetch Data
response = requests.get(url)
data = response.json()

def home(request):
    return JsonResponse(data,safe=False)