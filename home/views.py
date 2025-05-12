from django.shortcuts import render,HttpResponse

# Create your views here.
######### Navigation row return
def index(request):
    return render(request,"index.html")
    #return HttpResponse("This is homepage")

def articles(request):
    return render(request,"homepage_html_folder/articles.html")
    #return HttpResponse("This is shop page")

def practiceset(request):

    return render(request,"homepage_html_folder/practiceset.html")

def interviewquestionset(request):
    return render(request,"homepage_html_folder/interviewquestionset.html")

###### Latest Articles return


def differencesupervisedunsupervised(request):

    return render(request,"latest_articles/differencesupervisedunsupervised.html")

def featureengineering(request):

    return render(request,"latest_articles/featureengineering.html")


def datasciencemistakes(request):

    return render(request,"latest_articles/datasciencemistakes.html")



#### Articles page Return

def introductiontodatascience(request):
    return render(request,"articles_list/introductiontodatascience.html")

###### Practicset Page return


def machinelearningmcq(request):

    return render(request,"quiz_list/machinelearningmcq.html")

def pythoncoding(request):

    return render(request,"quiz_list/pythoncoding.html")

def statisticquiz(request):

    return render(request,"quiz_list/statisticquiz.html")

def projectTips(request):

    return render(request,"Interviewtips/projectTips.html")

def numpypandas(request):

    return render(request,"quiz_list/numpypandas.html")