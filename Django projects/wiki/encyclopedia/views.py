from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entrypage(request,title):
    entry = util.get_entry(title)

    if entry is not None:
        entry = markdown2.markdown(entry)
    context = {'entry':entry,'title':title}
    
    return render(request,'encyclopedia/entrypage.html',context)






def search(request):
    mylist = []
    searchkey = str(request.POST.get('q'))

    entries = util.list_entries()

    for entry in entries:
        if searchkey.lower() in entry.lower():
            if searchkey.lower() == entry.lower():
                entry = util.get_entry(entry)
                entry = markdown2.markdown(entry)
                print (entry)
                return render(request,'encyclopedia/entrypage.html',{'entry':entry,'title':searchkey})
            content = util.get_entry(entry)
            mylist.append((entry,content))
    

    context ={'searchlist':mylist,'searchkey':searchkey}
    return render(request,'encyclopedia/searchresult.html',context)


def createentry(request):
    checker = request.POST.get('edit')
    if request.method == "POST":
        title =str(request.POST.get('title'))
        content = str(request.POST.get('content'))

        if title == "" or title is None:
            errormessage = "There should be a title for this entry"
            
            context = {'errormessage':errormessage,'content':content}
            return render(request,'encyclopedia/createentry.html',context)

        else:
            
            entries = util.list_entries()
            if checker is None:
                for entry in entries:
                    if title.lower() == entry.lower():
                        errormessage = "An entry already exist with that title"
                        context = {'errormessage':errormessage,'content':content}
                        return render (request,'encyclopedia/createentry.html',context)
            

            util.save_entry(title,content)

            entry = util.get_entry(title)

            entry = markdown2.markdown(entry)

            return render(request,'encyclopedia/entrypage.html',{'entry':entry,'title':title})


    
        
    return render(request,'encyclopedia/createentry.html')



def editpage(request,title):
    entrytitle = ""
    for entry in util.list_entries():
        if title.lower() == entry.lower():
            entrytitle = entry
            break
    
    entry = util.get_entry(title)    

    context = {'title':entrytitle,'content':entry} 

    return render (request,'encyclopedia/createentry.html',context)



def randompage(request):
    mylist = util.list_entries()

    if mylist is not None:
        title = random.choice(mylist)

        entry = util.get_entry(title)
        entry = markdown2.markdown(entry)

        context = {'entry':entry,'title':title}

    
        return render(request,'encyclopedia/entrypage.html',context)

    



        

        



