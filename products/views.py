from pprint import pprint

from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import *
from .funcs import get_list, product_to_model


def banners(request):
    data = []

    for i in range(1, 4):
        prod = model_to_dict(Product.objects.filter(category=i)[0])
        data.append(prod)
        data[i - 1]['images'] = get_list(Image, prod['id'])
        data[i - 1]['tags'] = get_list(Tag, prod['id'])
        data[i - 1]['reviews'] = get_list(Review, prod['id'])
        data[i - 1]['specifications'] = get_list(Specification, prod['id'])

    return JsonResponse(data, safe=False)


def categories(request):
    data = []

    for cat in CatalogItemCategory.objects.all():
        cat = model_to_dict(cat)
        data.append(cat)
        data[len(data) - 1]['image'] = model_to_dict(Image.objects.filter(catalogitemcategory=cat['id'])[0])
        data[len(data) - 1]['subcategories'] = [
            model_to_dict(CatalogItemSubcategory.objects.filter(catalogitemcategory=cat['id'])[i]) for i in
            range(len(CatalogItemSubcategory.objects.filter(catalogitemcategory=cat['id'])))]

        for subcat in data[len(data) - 1]['subcategories']:
            subcat['image'] = model_to_dict(Image.objects.filter(catalogitemsubcategory=subcat['id'])[0])

    return JsonResponse(data, safe=False)


def catalog(request):
    pass
    # data = {
    #     "items": [
    #         {
    #             "id": 123,
    #             "category": 123,
    #             "price": 500.67,
    #             "count": 12,
    #             "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
    #             "title": "video card",
    #             "description": "description of the product",
    #             "freeDelivery": True,
    #             "images": [
    #                 {
    #                     "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    #                     "alt": "hello alt",
    #                 }
    #             ],
    #             "tags": [
    #                 {
    #                     "id": 0,
    #                     "name": "Hello world"
    #                 }
    #             ],
    #             "reviews": 5,
    #             "rating": 4.6
    #         }
    #     ],
    #     "currentPage": randrange(1, 4),
    #     "lastPage": 3
    # }
    # return JsonResponse(data)


def productsPopular(request):
    data = []

    for i in range(8):
        if len(Product.objects.all()) == i:
            break

        prod = model_to_dict(Product.objects.all()[i])
        data.append(prod)
        data[i] = product_to_model(data[i])

    return JsonResponse(data, safe=False)


def productsLimited(request):
    data = []

    for prod in Product.objects.all():
        if not prod.limited:
            continue

        prod = model_to_dict(prod)
        data.append(prod)
        data[len(data) - 1] = product_to_model(data[len(data) - 1])

    return JsonResponse(data, safe=False)


def sales(request):
    pass
    # data = {
    #     'items': [
    #         {
    #             "id": 123,
    #             "price": 500.67,
    #             "salePrice": 200.67,
    #             "dateFrom": "2023-05-08",
    #             "dateTo": "2023-05-20",
    #             "title": "video card",
    #             "images": [
    #                 {
    #                     "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    #                     "alt": "hello alt",
    #                 }
    #             ],
    #         }
    #     ],
    #     'currentPage': randrange(1, 4),
    #     'lastPage': 3,
    # }
    # return JsonResponse(data)


def product(request, id):
    data = model_to_dict(Product.objects.get(id=id))

    data['images'] = get_list(Image, data['id'])
    data['tags'] = get_list(Tag, data['id'])
    data['reviews'] = get_list(Review, data['id'])
    data['specifications'] = get_list(Specification, data['id'])

    return JsonResponse(data)


def tags(request):
    data = [tag for tag in Tag.objects.all().values()]

    return JsonResponse(data, safe=False)


def productReviews(request, id):
    pass
    # data = [
    #     {
    #         "author": "Annoying Orange",
    #         "email": "no-reply@mail.ru",
    #         "text": "rewrewrwerewrwerwerewrwerwer",
    #         "rate": 4,
    #         "date": "2023-05-05 12:12"
    #     },
    #     {
    #         "author": "2Annoying Orange",
    #         "email": "no-reply@mail.ru",
    #         "text": "rewrewrwerewrwerwerewrwerwer",
    #         "rate": 5,
    #         "date": "2023-05-05 12:12"
    #     },
    # ]
    # return JsonResponse(data, safe=False)
