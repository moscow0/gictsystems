import json

import requests
from django.shortcuts import render
from django.views.generic import TemplateView


class Post(TemplateView):
    template_name = 'post.html'
    url = "http://developers.gictsystems.com/api/dummy/submit"


    def get(self, request):
        return render(request, self.template_name, {
            'url': ''
        })

    def post(self, request):
        data = {
            "full names": request.POST.get("names"),
            "address": request.POST.get("address"),
            "phone": request.POST.get("phone"),
            "email": request.POST.get("email")
        }
        res = requests.request('POST', url=self.url, data=json.dumps(data))
        print(res.json())
        return render(request, self.template_name, {
            'message': res.json()
        })



class Index(TemplateView):
    template_name = 'index.html'



class Get(TemplateView):
    template_name = 'items.html'

    def get(self, request):
        url = 'http://developers.gictsystems.com/api/dummy/items'
        r = requests.get(url, headers={'Authorization': 'Bearer %s' % 'ALDJAK23423JKSLAJAF23423J23SAD3'})

        return render(request, self.template_name, {
            'items': r.json()
        })



