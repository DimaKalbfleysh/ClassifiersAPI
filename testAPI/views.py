from django.shortcuts import render
import requests
# Create your views here.
from django.views import View


class Test(View):
    def get(self, request):
        return render(request, 'testAPI/test.html')


class ViewAll(View):
    def get(self, request):
        json = requests.get('http://localhost:8000/api/v1/classifier/branch/?parent=Parent').json()
        root = get_root(json['data'][0]['attributes'])
        json = requests.get('http://localhost:8000/api/v1/classifier/full_tree/?root={}'.format(root)).json()
        return render(request, 'testAPI/view_all.html', context={'json': json,
                                                                 'root': root})


def get_root(json):
    if json['parent'] is not None:
        json = json['parent']
        get_root(json)
    root = json['name']
    return root


def get_all_tree(root):
    tree = {}
    # for children in root.children_classifiers.all():
