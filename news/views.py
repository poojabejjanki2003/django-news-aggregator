from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

# Create your views here.
#view for scraping new
# def scrape(request, name):
#     Headline.objects.all().delete() #remove all existing records from table
#     session = requests.Session()
#     #useragent helps server to identify origin of request
#     #we are imitating request as google bot
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     #google bot is crawler program
#     #session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
#     url = f"https://www.theonion.com/{name}"
#     content = session.get(url).content
#     #print(content)#raw content
#     soup = BSoup(content, "html.parser")

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape(request, name):
    Headline.objects.all().delete()

    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"https://www.theonion.com/{name}"
    response = session.get(url, verify=False)

    soup = BSoup(response.content, "html.parser")
    articles = soup.find_all("article")

    for article in articles[:15]:
        try:
            link = article.find("a")["href"]
            title = article.find("h2").text.strip()
            img_tag = article.find("img")
            image = img_tag["src"] if img_tag else ""

            headline = Headline(
                title=title,
                url=link,
                image=image
            )
            headline.save()
        except:
            continue

    return redirect("/news")

    #print(soup)


    # finding all new div using common class
    # News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})


    count=0
    for article in News:
        count=count+1

        if count<20:
            #extracting news link,img url,title for each news
            main = article.find_all("a", href=True)
            linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
            link = linkx["href"]
            titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
            title = titlex.text
            imgx = article.find("img")["data-src"]
            #storing extracted data to model
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = imgx
            new_headline.save()
            #saving details to table
    return redirect("/news")


def news_list(request):
    #fetching records stored in Headline model
    headlines = Headline.objects.all()[::-1]#store records in reverse order
    current_url = request.build_absolute_uri()
    context = {
        "object_list": headlines,"currenturl":current_url
    }
    return render(request, "home.html", context)

def statichome(request):
    return render(request, "homestatic.html")
def home(request):
    return render(request, "homestatic.html") 

# def breakinghome(request):
#     Headline.objects.all().delete()
#     session = requests.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = f"https://www.theonion.com/latest"
#     content = session.get(url).content
#     soup = BSoup(content, "html.parser")

#     News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})
#     count=0
#     for article in News:
#         count=count+1

#         if count<=8:
#             main = article.find_all("a", href=True)

#             linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
#             link = linkx["href"]

#             titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
#             title = titlex.text

#             imgx = article.find("img")["data-src"]

#             new_headline = Headline()
#             new_headline.title = title
#             new_headline.url = link
#             new_headline.image = imgx
#             new_headline.save() ##saving each record to news_headline
    
#     headlines = Headline.objects.all()[::-1]
#     context = {
#         "object_list": headlines,
#     }

#     return render(request, "home.html", context)


# context is a dictionary using which we can pass values to templates from views,return render(request,"about.html") return redirect("about.html")


def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def report(request):
    return render(request,"report.html")
def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
def contact_submit(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        country = request.GET.get('country')
        subject = request.GET.get('subject')

        return render(request, 'contact.html')

    return render(request, 'contact.html')