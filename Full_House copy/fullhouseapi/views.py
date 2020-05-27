from django.shortcuts import render
from .models import HappyPage, SadPage,ExpectationPage
#from django.http import HttpResponseRedirect

from django.shortcuts import redirect 


# Create your views here.
def base_view(request):
    return render(request,'base.html')


def happy_view(request):
    allHappyThings = HappyPage.objects.all()
    return render(request,'happy.html',{'all_Happy_Things':allHappyThings})

def addHappy_view(request):
    new_item = HappyPage(content = request.POST['content'])
    new_item.save()
    allHappyThings = HappyPage.objects.all()
    # return render(request,'happy.html',{'all_Happy_Things':allHappyThings})
    return redirect('/happy')

def sad_view(request):
    allSadThings = SadPage.objects.all()
    return render(request,'sad.html',{'all_sad_Things':allSadThings})

def addSad_view(request):
    new_item = SadPage(content = request.POST['content'])
    new_item.save()
    allSadThings = SadPage.objects.all()
    return redirect('/sad')

def deleteSad_view(request,sadThing_id):
    item_to_delete = SadPage.objects.get(id=sadThing_id)
    item_to_delete.delete()
    return redirect('/sad/')

def expectation_view(request):
    allExpectations = ExpectationPage.objects.all()
    return render(request,'expectations.html',{'all_expectations':allExpectations})

def addExpectation_view(request):
    new_item = ExpectationPage(content = request.POST['content'])
    new_item.save()
    allExpectations = ExpectationPage.objects.all()
    print(allExpectations)
    return redirect('/expectation')

def deleteExpectation_view(request,expectation_id):
    print(expectation_id)
    item_to_delete = ExpectationPage.objects.get(id=expectation_id)
    item_to_delete.delete()
    return redirect('/expectation')