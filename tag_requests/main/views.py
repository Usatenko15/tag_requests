from .models import Url_table
import datetime
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse

@csrf_exempt
def urls(request):
    if request.method == 'POST':
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; '
                                 'rv:80.0) Gecko/20100101 Firefox/80.0'}
        rs = requests.get(request.POST.get('url'), headers=headers)
        root = BeautifulSoup(rs.content, 'html.parser')
        occurrences = defaultdict(int)
        for tag in root.find_all():
            occurrences[tag.name] += 1
        post = Url_table()
        post.url = request.POST.get('url')
        post.text = occurrences.items()
        post.date = datetime.datetime.now()
        post.save()
        res = 'id: ' + str(post.id) + '\n' + 'url: ' + \
              post.url + '\n' + 'tags: ' + str(post.text) + \
              '\n' + 'time: ' + str(post.date)
        return HttpResponse(res)

    if request.method == 'GET':
        res =''
        for el in Url_table.objects.all():
            res = res + 'id: ' + str(el.id) + '\n'
            res = res + 'url: ' + el.url + '\n'
            res = res + 'tags: ' +el.text + '\n'
            res = res + 'time: ' + str(el.date) + '\n'+'\n'
        return HttpResponse(res)


def urls_id(request, url_id):
    if request.method == 'GET':
        try:
            url_res =Url_table.objects.get(pk=url_id)
            res = 'id: ' + str(url_res.id) + '\n' + 'url: ' + \
                  url_res.url + '\n' + 'tags: ' +url_res.text +\
                  '\n' + 'time: ' + str(url_res.date) + '\n'+'\n'
        except Url_table.DoesNotExist:
            raise Http404("URL does not exist")
        return HttpResponse(res)


