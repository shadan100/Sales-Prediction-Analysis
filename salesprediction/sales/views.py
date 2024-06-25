from django.shortcuts import render
import joblib
import os 
import numpy as np

def form(request):
    if request.method == 'GET':
        return render(request, 'sales/sales.html')
    else:
        item_weight = float(request.POST['item_weight'])
        item_fat_content = float(request.POST['item_fat_content'])
        item_visibility = float(request.POST['item_visibility'])
        item_type = float(request.POST['item_type'])
        item_mrp = float(request.POST['item_mrp'])
        outlet_establishment_year = float(request.POST['outlet_establishment_year'])
        outlet_size = float(request.POST['outlet_size'])
        outlet_location_type = float(request.POST['outlet_location_type'])
        outlet_type = float(request.POST['outlet_type'])

        X = np.array([[item_weight,item_fat_content,item_visibility,item_type,item_mrp,outlet_establishment_year,
        outlet_size,outlet_location_type,outlet_type]])
        scaler_path = os.path.join(r'E:\MCA\Python Programming\Sales Prediction Analysis\models\sc.sav')
        sc = joblib.load(scaler_path)
        X_std = sc.transform(X)
        model_path = os.path.join(r'E:\MCA\Python Programming\Sales Prediction Analysis\models\xgb.sav')
        model = joblib.load(model_path)
        y_pred = model.predict(X_std)

        return render(request, 'sales/sales.html',{'predict':y_pred})
        