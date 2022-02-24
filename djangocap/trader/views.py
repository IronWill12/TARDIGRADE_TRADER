from django.shortcuts import render, redirect
from django.conf import settings
from .models import Crypto
from django.contrib import messages
from .forms import CryptoForm
# settings.TWILIO_TOKEN
# settings.TWILIO_SID
# Crypto compare API key b206d4402c92be5235d6396e6d40475632f0ca7df216bb9e54b72ef79b7454f7
import cryptocompare
#from twilio.rest import Client
import time
#from secrets import token, sid


from requests import request

def home (request):
     import requests
     import json

     if request.method == 'POST':
          ticker = request.POST['ticker']
          api_request = requests.get("https://min-api.cryptocompare.com/data/generateAvg?fsym="+ ticker +"&tsym=USD&e=Kraken")

          try:
               api = api_request.json() # json.loads(api_request.content.raw)

          except Exception as error:
               api = "error1"
          return render(request, 'home.html', {'api': api})
     else:
          return render(request, 'home.html', {'ticker': "Enter a Crypto ticker symbol above"})



def aboutme (request):
     return render (request, 'aboutme.html', {})

def your_crypto (request):
     import requests
     import json
     if request.method == 'POST':
          form = CryptoForm(request.POST or None)
          if form.is_valid():
               form.save()
               messages.success(request, ("The Crypto Has Been Added To Your Portfolio!"))
               return redirect('your_crypto')
     else:
          ticker = Crypto.objects.all()
          output = []
          for ticker_item in ticker:
               api_request = requests.get(
               "https://min-api.cryptocompare.com/data/generateAvg?fsym=" + str(ticker_item) + "&tsym=USD&e=Kraken")

               try:
                    api = api_request.json()  # json.loads(api_request.content.raw)
                    output.append(api)
               except Exception as e:
                    api = "error1"
          return render (request, 'your_crypto.html', {'ticker': ticker, 'output': output})

def delete(request, crypto_id):
     item = Crypto.objects.get(pk=crypto_id)
     item.delete()
     messages.success(request, ("The Crypto Has Been Removed From Your Portfolio!"))
     return redirect(your_crypto)

# Create your views here.
