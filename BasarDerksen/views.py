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
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseBadRequest
from .models import ShoppingItem
import json
from .models import User

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        authentificationCode = 78

        print(username + ' =Username ' +  password + ' =Password ' + str(authentificationCode) + ' =AuthentificationCode')
        if authentificationCode % 78 == 0:
            new_user = User.objects.create(username=username, password=password, authentificationCode=authentificationCode)
            new_user.save()
            all_Users = User.objects.all()
            return render(request, 'index.html', {'all_Users': all_Users})
        else:
            print("Wrong authenificationCode")
            return HttpResponse("Wrong authenificationCode")

    all_Users = User.objects.all()
    return render(request, 'index.html', {'all_Users': all_Users})

def cassa(request):
    all_items = ShoppingItem.objects.filter(done=0)
    for item in all_items:
        print(item.number)
    total_earnings = get_total_earnings()  # Call the get_total_earnings function
    return render(request, 'cassa.html', {'all_items': all_items, 'total_earnings': total_earnings})






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
    


def Gunterhans(request):
    return render(request, 'Gunterhans.html')
def sys(request):
    return render(request, 'syshelp.html')
def agb(request):
    return render(request, 'AGB.html')
def kundeninfo(request):
    all_items = ShoppingItem.objects.all
    return render(request, 'kundeninfo.html', {'all_items': all_items} )


def delete_all_items(request):
    products.objects.all().delete()
    ShoppingItem.objects.all().delete()


    return HttpResponse("Alle Daten aus den Modellen 'Product' und 'ShoppingItem' wurden gelöscht." )
    
  

def start(request):
    return render(request, 'start.html')

def help(request):
    all_items = products.objects.all

    return render(request, 'help.html', {'all_items': all_items})

from django.http import JsonResponse



from django.http import JsonResponse
from .models import ShoppingItem # Ersetze mit deinem Modells

# Variable, um den letzten Zeitstempel zu speichern
last_checked = None

def check_for_update(request):
    global last_checked  # Verwende eine globale Variable, um den letzten Zeitstempel zu speichern

    # Wenn last_checked noch None ist, prüfe, ob es ShoppingItem-Objekte gibt
    if last_checked is None:
        if ShoppingItem.objects.exists():
            last_checked = ShoppingItem.objects.latest('modified_at').modified_at
        else:
            last_checked = None  # oder ein Default-Datum

    # Wenn last_checked immer noch None ist, gibt es keine ShoppingItem-Objekte
    if last_checked is None:
        return JsonResponse({"reload": False})

    # Überprüfen, ob neue Daten in der Datenbank vorhanden sind
    new_items = ShoppingItem.objects.filter(modified_at__gt=last_checked)
    if new_items.exists():
        last_checked = new_items.latest('modified_at').modified_at  # Update last_checked
        return JsonResponse({"reload": True})

    return JsonResponse({"reload": False})

def get_total_earnings():
    total_earnings = sum(item.price for item in ShoppingItem.objects.all())
    print(total_earnings)
    return total_earnings
from .models import products

def numberpro(request):
    #shop = request.POST['ProShop']
    shop = request.POST['ProShop']
    print(request.POST['ProShop'])
    print("Shop value:", shop)
    all_products = products.objects.filter(shop=shop)
    print(all_products)
    print(all_products.query)
    
    return render(request, 'TESTSERVER.html', {'items_all': all_products})

def Handy(request):
    return render(request, 'handyversion.html')

def TEST(request):
    next_pronumber = None
    
    if request.method == 'POST':
            shop = request.POST['shop']
            next_pronumber = products.objects.filter(shop=shop).count() + 1
            shop = request.POST['shop']  # Kundennummer aus der Anfrage abrufen
            name = request.POST['name']  # Artikelname aus der Anfrage abrufen
            pronumber = Decimal(request.POST['pronumber'])
            if request.POST['price'] == '':
                price = 0 
            else:
                price = Decimal(request.POST['price'])  # Preis in Decimal umwandeln
            print('Received Data: ' + shop + ', ' + name + ', ' + str(price) + ',' + str(pronumber))

            if name == '':  # Check if name is empty
                # Delete the object with the corresponding pronumber
                products.objects.filter(pronumber=pronumber).delete()
                print('Deleted object with pronumber', pronumber)
            else:
                existing_item = products.objects.filter(pronumber=pronumber).first()
                print('debug')
                if existing_item:
                    # Wenn der Eintrag existiert, aktualisiere den Namen und addiere den neuen Preis
                    existing_item.price = price  # Neuen Preis zum bestehenden Preis addieren
                    existing_item.name = name
                    existing_item.shop = shop # Neuen Namen anhängen
                    existing_item.pronumber = pronumber
                    existing_item.save()  # Änderungen speichern
                    print('existing' + shop + ', ' + name + ', ' + str(price) )
                else:
                    # Wenn kein Eintrag existiert, einen neuen erstellen
                    products.objects.create(shop=shop, name=name, price=price, pronumber=pronumber)
                    print('new' + shop + ', ' + name + ', ' + str(price) )

      # or however you're getting the shop value
    
    all_products = products.objects.all()
    return render(request, 'TESTSERVER.html', {  'all_products': all_products,'next_pronumber': next_pronumber})
