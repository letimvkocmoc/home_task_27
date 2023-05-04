import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category


# class CatListView(ListView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         return JsonResponse([{'id': cat.id, 'name': cat.name} for cat in self.object_list.order_by('name')], safe=False)
#
#
# class CatDetailView(DetailView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         cat = self.get_object()
#         return JsonResponse([{'id': cat.id, 'name': cat.name}], safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CatCreateView(CreateView):
#     model = Category
#     fields = '__all__'
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         new_cat = Category.objects.create(name=data.get('name'))
#         return JsonResponse({'id': new_cat.id, 'name': new_cat.name}, safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CatUpdateView(UpdateView):
#     model = Category
#     fields = '__all__'
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         data = json.loads(request.body)
#         self.object.name = data.get('name')
#         self.object.save()
#         return JsonResponse({'id': self.object.id, 'name': self.object.name})
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CatDeleteView(DeleteView):
#     model = Category
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         cat = self.get_object()
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'id': cat.id})
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
