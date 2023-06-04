from django.shortcuts import render

# Create your views here.
def inv_add(request):
    return render(request,"inventory/inventory_add.html")

def inv_edit(request):
    return render(request,"inventory/inventory_edit.html")

def inv_list(request):
    return render(request,"inventory/inventory_list.html")

def inv_show(request):
    return render(request,"inventory/inventory_show.html")
