from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.shortcuts import render

def show_dino(request, name):
    data = {
        "dinosaurs": [
            "Ty4annosaurus",
            "Stgosaurus",
            "<b>Raptor</b>",
            "Triceratops",
        ],
        "now": datetime.now(),
        "test": "<i>Rana Sal</i>"
    }

    return render(request, name + ".html", data)
