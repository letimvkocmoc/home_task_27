import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ad


def index(request):
    response = {
        'status': 'ok'
    }
    return JsonResponse(response, status=200, safe=False)


class CatView(View):

    def get(self, request):
        all_cat = Category.objects.all()

        return JsonResponse([{'id': cat.id, 'name': cat.name} for cat in all_cat], safe=False)


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse([{'id': cat.id, 'name': cat.name}], safe=False)


class CatListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return JsonResponse([{'id': cat.id, 'name': cat.name} for cat in self.object_list], safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Category
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        new_cat = Category.objects.create(name=data.get('name'))
        return JsonResponse({'id': new_cat.id, 'name': new_cat.name}, safe=False)


class CatUpdateView(UpdateView):
    model = Category
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        self.object.name = data.get('name')
        self.object.save()
        return JsonResponse({'id': self.object.id, 'name': self.object.name})


class CatDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        cat = self.get_object()
        super().delete(request, *args, **kwargs)
        return JsonResponse({'id': cat.id})


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
