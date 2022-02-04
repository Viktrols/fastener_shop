from rest_framework import mixins, viewsets

from api.models import Category
from api.serializers import (CategorySerializer,
                             CategoryCardsSerializer,
                             CardDetailSerializer,
                             CardProductsSerializer)


class RetrieveListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class RetrieveViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class CategoriesViewSet(RetrieveListViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.parser_context['kwargs'].get('pk'):
            return CategoryCardsSerializer
        return CategorySerializer


class CardDetailViewSet(RetrieveViewSet):
    queryset = Category.objects.filter(depth=4)
    serializer_class = CardDetailSerializer


class ProductsViewSet(RetrieveViewSet):
    queryset = Category.objects.filter(depth=4)
    serializer_class = CardProductsSerializer
