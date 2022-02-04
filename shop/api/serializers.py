from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import Category, Product


class CategorySerializer(ModelSerializer):
    child_categories = SerializerMethodField(
        read_only=True, method_name='get_children')

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'child_categories')

    @staticmethod
    def get_children(obj):
        queryset = obj.get_descendants().order_by('id')
        return CategorySerializer(queryset, many=True).data


class CategoryCardsSerializer(ModelSerializer):
    cards = SerializerMethodField(read_only=True, method_name='get_cards')

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'cards']

    @staticmethod
    def get_cards(obj):
        descendants_queryset = obj.get_descendants()
        cards = []
        for descendant in descendants_queryset:
            if descendant.depth == 4:
                cards.append(descendant)
        return CardDetailSerializer(cards, many=True).data


class CardDetailSerializer(ModelSerializer):
    scope = SerializerMethodField(read_only=True, method_name='get_scope')
    diameter = SerializerMethodField(read_only=True,
                                     method_name='get_diameter')
    length = SerializerMethodField(read_only=True, method_name='get_length')
    color = SerializerMethodField(read_only=True, method_name='get_color')
    main_image = SerializerMethodField(read_only=True,
                                       method_name='get_main_image')
    images_by_colors = SerializerMethodField(read_only=True,
                                             method_name='get_image_by_colors')

    class Meta:
        model = Category
        fields = ('name', 'scope', 'diameter', 'length', 'color',
                  'main_image', 'images_by_colors')

    @staticmethod
    def get_scope(obj):
        queryset = obj.products.values('scope')
        return {i['scope'] for i in queryset}

    @staticmethod
    def get_diameter(obj):
        queryset = obj.products.values('diameter')
        return {i['diameter'] for i in queryset}

    @staticmethod
    def get_length(obj):
        queryset = obj.products.values('length')
        return {i['length'] for i in queryset}

    @staticmethod
    def get_color(obj):
        queryset = obj.products.values('color')
        return {i['color'] for i in queryset}

    @staticmethod
    def get_main_image(obj):
        queryset = obj.products.values('image').first()
        return queryset

    @staticmethod
    def get_image_by_colors(obj):
        queryset = obj.products.values()
        return {i['color']: i['image'] for i in queryset}


class ProductSerializer(ModelSerializer):
    image = SerializerMethodField('get_image')

    class Meta:
        model = Product
        fields = ('name', 'description', 'scope', 'diameter',
                  'length', 'color', 'image', 'card_id')

    @staticmethod
    def get_image(self, obj):
        image = obj.get('image')
        return image


class CardProductsSerializer(ModelSerializer):
    products = SerializerMethodField(
        read_only=True, method_name='get_products')

    class Meta:
        model = Category
        fields = ('products',)

    @staticmethod
    def get_products(obj):
        queryset = obj.products.values()
        return ProductSerializer(queryset, many=True).data
