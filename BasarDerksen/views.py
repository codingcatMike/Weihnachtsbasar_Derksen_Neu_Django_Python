from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingItem
import json
from decimal import Decimal


from django.shortcuts import render
from django.http import JsonResponse
from .models import ShoppingItem

def Testshop(request):
    if request.method == 'POST':
        number = request.POST['number']  # Kundennummer aus der Anfrage abrufen
        name = request.POST['name']  # Artikelname aus der Anfrage abrufen
        price = Decimal(request.POST['price'])  # Preis in Decimal umwandeln

        # Überprüfen, ob ein Eintrag mit dieser Kundennummer existiert
        existing_item = ShoppingItem.objects.filter(number=number).first()

        if existing_item:
            # Wenn der Eintrag existiert, aktualisiere den Namen und addiere den neuen Preis
            existing_item.price += price  # Neuen Preis zum bestehenden Preis addieren
            existing_item.name += f', {name}' # Neuen Namen anhängen
            existing_item.save()  # Änderungen speichern
            message = f'Updated item for customer number {number}: {existing_item.name}'
        else:
            # Wenn kein Eintrag existiert, einen neuen erstellen
            ShoppingItem.objects.create(number=number, name=name, price=price)
            message = f'Added new item for customer number {number}: {name}'

        # Debugging-Ausgabe
        print(message)

        # JSON-Antwort zurückgeben, um die Frontend-Benachrichtigung zu ermöglichen
        return JsonResponse({'status': 'success', 'message': message})

    # Alle Artikel abrufen, die nicht als erledigt markiert sind
    all_items = ShoppingItem.objects.filter(done=0)
    return render(request, 'PlätzchenShop.html', {'all_items': all_items})


def index(request):
    return render(request, 'index.html')

def cassa(request):
    all_items = ShoppingItem.objects.filter(done=0)
    for item in all_items:
        print(item.number)
    return render(request, 'cassa.html', {'all_items': all_items})



from django.http import JsonResponse, HttpResponseBadRequest
from .models import ShoppingItem
import json

def update_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data['itemId']
        done = data['done']

        # Update the item in the database
        item = ShoppingItem.objects.get(id=item_id)
        item.done = 1
        item.save()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        return HttpResponseBadRequest('Invalid request method')
    

def Shop_1(request):
    return render(request, 'Shop1.html')
def Shop_2(request):
    return render(request, 'Shop2.html')
def Shop_3(request):
    return render(request, 'Shop3.html')
def Shop_4(request):
    return render(request, 'Shop4.html')
def Shop_5(request):
    return render(request, 'Shop5.html')
def Shop_6(request):
    return render(request, 'Shop6.html')
def Shop_7(request):
    return render(request, 'Shop7.html')
def Gunterhans(request):
    return render(request, 'Gunterhans.html')

from django.http import JsonResponse



from django.http import JsonResponse
from .models import ShoppingItem # Ersetze mit deinem Modells

# Variable, um den letzten Zeitstempel zu speichern
last_checked = None

def check_for_update(request):
    global last_checked  # Verwende eine globale Variable, um den letzten Zeitstempel zu speichern

    # Wenn last_checked noch None ist, initialisiere es
    if last_checked is None:
        last_checked = ShoppingItem.objects.latest('modified_at').modified_at

    # Überprüfen, ob neue Daten in der Datenbank vorhanden sind
    new_items = ShoppingItem.objects.filter(modified_at__gt=last_checked)
    if new_items.exists():
        last_checked = new_items.latest('modified_at').modified_at  # Update last_checked
        return JsonResponse({"reload": True})

    return JsonResponse({"reload": False})
