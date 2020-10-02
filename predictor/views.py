from django.shortcuts import render, HttpResponse
import pickle
from statistics import mean,mode
from . models import Heart, Diabetes


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
        distype = request.POST['distype']
        model=["knnDia.pkl","rfDia.pkl",'logDia.pickle']
        result=[]
        proba=[]
        for i in model:
            file = open(f'static/{i}','rb')
            clf = pickle.load(file)
            file.close()
            feature1 = [pregnancies, glucose, bp, skin, insulin, bmi, diab, age]
            info1 = clf.predict_proba([feature1])[0][1]
            res=clf.predict([feature1])[0]
            result.append(res)
            proba.append(info1)
        final_prob=mean(proba)
        final_res = mode(result)

        data = {'name':name, 'age': age, 'bp': bp, 'glucose': glucose, 'skin': skin, 'bmi':bmi , 'pregnancies': pregnancies, 'insulin':insulin, 'diab':diab, 'distype':distype, 'proba':final_prob, 'result':final_res}
        return render(request,"result.html", data)
    return HttpResponse('Error')

def heartTest(request):
    if request.method=="POST" :
        name = request.POST['name']
        age = int(request.POST['age'])
        bp = int(request.POST['bp'])
        chol = int(request.POST['chol'])
        beat = int(request.POST['beat'])
        gender = int(request.POST['gender'])
        cp = int(request.POST['cp'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])
        distype = request.POST['distype']
        model=["knnHeart.pkl","rfHeart.pkl",'heart.pickle']
        result=[]
        proba=[]
        for i in model:
            file = open(f'static/{i}','rb')
            clf = pickle.load(file)
            file.close()
            feature1 = [age, gender, cp, bp, chol, fbs, restecg, beat, exang, oldpeak, slope, ca, thal]
            info1 = clf.predict_proba([feature1])[0][1]
            res=clf.predict([feature1])[0]
            result.append(res)
            proba.append(info1)
        final_prob=mean(proba)
        final_res = mode(result)
        print(final_prob, final_res)

        data = {'name':name, 'age': age, 'gender': gender, 'cp': cp, 'bp': bp, 'chol': chol, 'fbs': fbs, 'restecg':restecg , 'beat': beat, 'exang':exang, 'oldpeak':oldpeak, 'slope':slope, 'ca':ca, 'thal':thal,'distype':distype, 'proba':final_prob, 'result':final_res}
        return render(request,"result.html", data)
    return HttpResponse('Error')