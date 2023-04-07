import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def index(request):
    response = {
        'status': 'ok'
    }
    return JsonResponse(response, status=200, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):

    def get(self, request):
        all_cat = Category.objects.all()

        return JsonResponse([{'id': cat.id, 'name': cat.name} for cat in all_cat], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_cat = Category.objects.create(name=data.get('name'))

        return JsonResponse([{'id': new_cat.id, 'name': new_cat.name}], safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):

    def get(self, request):
        all_ads = Ad.objects.all()

        return JsonResponse([{'id': ad.id,
                              'name': ad.name,
                              'author': ad.author,
                              'price': ad.price,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published} for ad in all_ads], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)

        return JsonResponse([{'id': ad.id,
                              'name': ad.name,
                              'author': ad.author,
                              'price': ad.price,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published} for ad in new_ad], safe=False)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse([{'id': cat.id, 'name': cat.name}], safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse([{'id': ad.id,
                              'name': ad.name,
                              'author': ad.author,
                              'price': ad.price,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published}], safe=False)
