from django.shortcuts import render
from django.http import HttpResponseRedirect
from emaillist.models import Emaillist


# url과
def index(request):
    emaillist_list = Emaillist.objects.all().order_by('-id')
    #id컬럼의 역순으로 정렬하겠다.
    #emaillist_list은 리스트로 반환된다.
    data = {'emaillist_list': emaillist_list}
    return render(request, 'emaillist/index.html', data) #settings.py에서 INSTALLED_APPS가 돈다.

def form(request):
    return render(request, 'emaillist/form.html')

def add(request):#request에 입력한 데이터가 들어있음
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    # return render(request, 'success.html')
    return HttpResponseRedirect('/emaillist')