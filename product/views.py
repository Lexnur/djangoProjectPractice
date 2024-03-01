from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Group, Lesson, Users
from product.serializers import ProductSerializer, LessonSerializer


def distribute_users(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    groups = Group.objects.filter(product=product)
    for group in groups:
        if not product.quantity_max:
            group.user_set.add(request.user)
            group.save()


def product_list(request):
    context = {
        'title': 'Product List',
        'products': Product.objects.all(),
        'lessons': Lesson.objects.all(),
        'groups': Group.objects.all(),
        'users': Users.objects.all(),
    }
    return render(request, 'index.html', context)


class ProductListView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # def get_queryset(self):
    #     product_id = self.kwargs['product_id']
    #     return Lesson.objects.filter(product_id=product_id)







