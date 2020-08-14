from django.shortcuts import render
from django.contrib import messages
from .models import PostDetail
import pandas as pd

def post(request):
    if request.method == "GET":
        return render(request,'csv.html')


    csv_f=request.FILES['csv']
    
    if not csv_f.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    else:   
        if request.method == "POST":
            csv_file = pd.read_csv(csv_f)
            products = []
            for i in range(len(csv_file)):
                products.append(
                    PostDetail(
                    firstname = csv_file.iloc[i][0],
                    lastname = csv_file.iloc[i][1],
                    city = csv_file.iloc[i][2],
                    mobile = csv_file.iloc[i][3],
                    address = csv_file.iloc[i][4],
                    )
                )
            
            PostDetail.objects.bulk_create(products)
            messages.success(request,'Data Saved Successfully')
    

    

    return render(request,'csv.html')
