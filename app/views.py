from django.shortcuts import render
from . import views
import requests,json
# Create your views here.

def index(request):
    req = requests.get('https://nepalcorona.info/api/v1/data/nepal')
    
    # display all data
    # req = req.json()
    # for i,j in req.items():
    #     print(i,j)
    
    # display specific data
    r = req.text
    f = json.loads(r)

    positive = f["tested_positive"]
    negative = f["tested_negative"]
    total = f["tested_total"]
    isolated = f["in_isolation"]
    quarantined = f["quarantined"]
    rdt = f["tested_rdt"]
    pending = f["pending_result"]
    recovered = f["recovered"]
    dead = f["deaths"]
    updated = f["updated_at"]

    data = {
        # display all data
        # 'req' : req,

        # display specific data
        'positive' : positive,
        'negative' : negative,
        'total' : total,
        'isolated' : isolated,
        'quarantined' : quarantined,
        'rdt' : rdt,
        'pending' : pending,
        'recovered' : recovered,
        'dead' : dead,
        'updated' : updated.split('T')[0],
    }

    return render(request, 'index.html', data)
