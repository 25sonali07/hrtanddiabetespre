from django.shortcuts import render, HttpResponse, redirect
import pickle
from statistics import mean,mode
from . models import Heart, Diabetes, Feedback
import json, requests
from django.contrib import messages


# Create your views here.

def getdata(url):
    r= requests.get(url)
    return json.loads(r.text)

def home(request):
    url = "https://covid19.mathdro.id/api/countries/india"
    data = getdata(url)

    sConfirmed = data['confirmed']['value']
    sRecovered = data['recovered']['value']
    sDeath = data['deaths']['value']
    sActive = sConfirmed-sRecovered-sDeath

    data = {'active':sActive, 'confirmed':sConfirmed, 'recovered': sRecovered, 'death':sDeath}

    return render(request,"home.html", data)

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
        final_prob=round(final_prob,2)*100
        final_res = mode(result)
        # Fixing Graph Values 
        graph = [{'accuracy':71.8,'score':75.5, 'algo':'KNN'},{'accuracy':75.3,'score':68.2, 'algo':'Logistic'},{'accuracy':77.5,'score':75.5, 'algo':'Random Forest'}]

        # Saving in database 
        diabetes = Diabetes(name=name, age=age, bp=bp, glucose=glucose, skin=skin, bmi=bmi, pregnancies=pregnancies, insulin=insulin, diab=diab, probability=final_prob, result=final_res)
        diabetes.save()

        data = {'name':name, 'age': age, 'bp': bp, 'glucose': glucose, 'skin': skin, 'bmi':bmi , 'pregnancies': pregnancies, 'insulin':insulin, 'diab':diab, 'distype':distype, 'proba':final_prob, 'result':final_res, 'graph':graph}

        if final_res==0:
            messages.success(request, 'You have less chance of diabetes problem !! ')
        else:
            messages.error(request, "You have chances of diabetes problem... Please contact your doctor as soon as possible.")

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
        final_prob=round(final_prob,2)*100
        final_res = mode(result)
        # Fixing Graph Values 
        graph = [{'accuracy':90.7,'score':84.48, 'algo':'KNN'},{'accuracy':73.7,'score':80.5, 'algo':'Logistic'},{'accuracy':89.4,'score':81.8, 'algo':'Random Forest'}]

         # Saving in database
        heart = Heart(name=name, age=age, gender=gender, cp=cp, bp=bp, chol=chol, fbs=fbs, restecg=restecg, beat=beat, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, probability=final_prob, result=final_res)
        heart.save()

        data = {'name':name, 'age': age, 'gender': gender, 'cp': cp, 'bp': bp, 'chol': chol, 'fbs': fbs, 'restecg':restecg , 'beat': beat, 'exang':exang, 'oldpeak':oldpeak, 'slope':slope, 'ca':ca, 'thal':thal,'distype':distype, 'proba':final_prob, 'result':final_res, 'graph':graph}

        if final_res==0:
            messages.success(request, 'You have less chance of heart problem !! ')
        else:
            messages.error(request, "You have chances of heart problem... Please contact your doctor as soon as possible.")
        return render(request,"result.html", data)

    return HttpResponse('Error')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        feedback = Feedback(name=name, email=email, message=message)
        feedback.save()

        messages.success(request, 'Thanks for your valuable feedback !!')
        return redirect('home')

    messages.error(request, 'OOPS !! We have some error in our system... Please try again after sometime')
    return HttpResponse('Error')

