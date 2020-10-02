from django.shortcuts import render
import pickle
from statistics import mean,mode


# Create your views here.
def home(request):
    return render(request,"home.html")

def heart(request):    
    return render(request,"heart.html")

def diabetes(request):    
    return render(request,"diabetes.html")    

def diaTest(request):
    if request.method=="POST" :
        name = request.POST['name']
        age = int(request.POST['age'])
        bp = int(request.POST['bp'])
        glucose = int(request.POST['glucose'])
        skin = int(request.POST['skin'])
        bmi = float(request.POST['bmi'])
        pregnancies = int(request.POST['preg'])
        insulin = int(request.POST['insulin'])
        diab = float(request.POST['diab'])
        # distype = request.POST['distype']
        model=["knn_dia.pkl","rf_dia.pkl","log_dia.pkl"]
        result=[]
        proba=[]
        for data in model:
            file = open(f'static/{data}', 'rb')
            print(file)
            clf = pickle.load(file)
            file.close()
            feature1 = [pregnancies, glucose, bp, skin, insulin, bmi, diab, age]
            info1 = clf.predict_proba([feature1])[0][1]
            res=clf.predict([feature1])
            result.append(res)
            proba.append(info1)
        final_prob=mean(proba)
        final_res = mode(result)
        print(final_prob, final_res)
    return render(request,"home.html")

   
        


