# View file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    #get the text 
    djtext=request.POST.get('text','default')
    removepu=request.POST.get('removepunc','off')
    uppercase=request.POST.get('capitalize','off')
    lowercase=request.POST.get('lower','off')
    newlineremover=request.POST.get('newline','off')
    spaceremover=request.POST.get('space','off')
    charactercount=request.POST.get('count','off')
    if removepu=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
       
    if uppercase=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Converted into UpperCase','analyzed_text':analyzed}
        djtext=analyzed
      
    
    if lowercase=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.lower()
        params={'purpose':'Converted into lowercase','analyzed_text':analyzed}
        djtext=analyzed
   
    
    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char
        
        params={'purpose':'Newlineremover','analyzed_text':analyzed}
        djtext=analyzed
     
    
    if spaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Spaceremover','analyzed_text':analyzed}
        djtext=analyzed
    

            
    return render(request,'analyze.html',params)



    if (removepu !='on' and newlineremover!='on' and spaceremover!='on' and uppercase!='on' and lowercase!='on'):
        return HttpResponse("Error")
    


# def lower(request):
#     return HttpResponse("lowe case")

