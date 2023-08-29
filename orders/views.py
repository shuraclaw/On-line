from pprint import pprint

from django.http import JsonResponse

import json

from django.http import HttpResponse
from django.forms.models import model_to_dict

from .models import *
from products.funcs import basket_product_to_model


def basket(request):
    if request.method == "GET":
        print('[GET] /api/basket/')
        basket_dict = model_to_dict(Basket.objects.filter(user_id=request.user.id)[0])
        basket_dict['products'] = basket_product_to_model(basket_dict['products'])

        data = []
        for i in range(len(basket_dict['products'])):
            data.append(basket_dict['products'][i]['product'])

        data.sort(key=lambda x: x['title'])

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)
        id = body['id']
        count = body['count']
        print('[POST] /api/basket/   |   id: {id}, count: {count}'.format(id=id, count=count))

        if not Basket.objects.filter(user_id=request.user.id):
            Basket.objects.create(user_id=request.user.id)

        basket = Basket.objects.filter(user_id=request.user.id)[0]

        if not BasketProduct.objects.filter(product_id=id, user_id=request.user.id):
            BasketProduct.objects.create(product_id=id, count=count, user_id=request.user.id)
            basket.products.add(BasketProduct.objects.filter(product_id=id, user_id=request.user.id)[0])
        else:
            basket_product = BasketProduct.objects.filter(product_id=id, user_id=request.user.id)[0]
            basket_product.count += count
            basket_product.save()

        basket.save()

        basket_dict = model_to_dict(Basket.objects.filter(user_id=request.user.id)[0])
        basket_dict['products'] = basket_product_to_model(basket_dict['products'])

        data = []
        for i in range(len(basket_dict['products'])):
            data.append(basket_dict['products'][i]['product'])

        data.sort(key=lambda x: x['title'])

        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        body = json.loads(request.body)
        id = body['id']
        count = body['count']
        print('[DELETE] /api/basket/   |   id: {id}, count: {count}'.format(id=id, count=count))

        basket = Basket.objects.filter(user_id=request.user.id)[0]
        basket_product = BasketProduct.objects.filter(product_id=id, user_id=request.user.id)[0]

        if basket_product.count > count:
            basket_product.count -= count
            basket_product.save()
        else:
            basket.products.remove(basket_product)
            basket.save()
            basket_product.delete()

        basket_dict = model_to_dict(Basket.objects.filter(user_id=request.user.id)[0])
        basket_dict['products'] = basket_product_to_model(basket_dict['products'])

        data = []
        for i in range(len(basket_dict['products'])):
            data.append(basket_dict['products'][i]['product'])

        data.sort(key=lambda x: x['title'])

        return JsonResponse(data, safe=False)


def orders(request):
    pass
    # if request.method == "POST":
    #     data = [
    #         {
    #             "id": 123,
    #             "category": 55,
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
    #     ]
    #     return JsonResponse(data, safe=False)


def orders(request):
    pass
    # if request.method == 'GET':
    #     data = [
    #         {
    #             "id": 123,
    #             "createdAt": "2023-05-05 12:12",
    #             "fullName": "Annoying Orange",
    #             "email": "no-reply@mail.ru",
    #             "phone": "88002000600",
    #             "deliveryType": "free",
    #             "paymentType": "online",
    #             "totalCost": 567.8,
    #             "status": "accepted",
    #             "city": "Moscow",
    #             "address": "red square 1",
    #             "products": [
    #                 {
    #                     "id": 123,
    #                     "category": 55,
    #                     "price": 500.67,
    #                     "count": 12,
    #                     "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
    #                     "title": "video card",
    #                     "description": "description of the product",
    #                     "freeDelivery": True,
    #                     "images": [
    #                         {
    #                             "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    #                             "alt": "Image alt string"
    #                         }
    #                     ],
    #                     "tags": [
    #                         {
    #                             "id": 12,
    #                             "name": "Gaming"
    #                         }
    #                     ],
    #                     "reviews": 5,
    #                     "rating": 4.6
    #                 }
    #             ]
    #         },
    #         {
    #             "id": 123,
    #             "createdAt": "2023-05-05 12:12",
    #             "fullName": "Annoying Orange",
    #             "email": "no-reply@mail.ru",
    #             "phone": "88002000600",
    #             "deliveryType": "free",
    #             "paymentType": "online",
    #             "totalCost": 567.8,
    #             "status": "accepted",
    #             "city": "Moscow",
    #             "address": "red square 1",
    #             "products": [
    #                 {
    #                     "id": 123,
    #                     "category": 55,
    #                     "price": 500.67,
    #                     "count": 12,
    #                     "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
    #                     "title": "video card",
    #                     "description": "description of the product",
    #                     "freeDelivery": True,
    #                     "images": [
    #                         {
    #                             "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    #                             "alt": "Image alt string"
    #                         }
    #                     ],
    #                     "tags": [
    #                         {
    #                             "id": 12,
    #                             "name": "Gaming"
    #                         }
    #                     ],
    #                     "reviews": 5,
    #                     "rating": 4.6
    #                 }
    #             ]
    #         }
    #     ]
    #     return JsonResponse(data, safe=False)
    #
    # elif request.method == 'POST':
    #     data = {
    #         "orderId": 123,
    #     }
    #     return JsonResponse(data)
    #
    # return HttpResponse(status=500)


def order(request, id):
    pass
    # if (request.method == 'GET'):
    #     data = {
    #         "id": 123,
    #         "createdAt": "2023-05-05 12:12",
    #         "fullName": "Annoying Orange",
    #         "email": "no-reply@mail.ru",
    #         "phone": "88002000600",
    #         "deliveryType": "free",
    #         "paymentType": "online",
    #         "totalCost": 567.8,
    #         "status": "accepted",
    #         "city": "Moscow",
    #         "address": "red square 1",
    #         "products": [
    #             {
    #                 "id": 123,
    #                 "category": 55,
    #                 "price": 500.67,
    #                 "count": 12,
    #                 "date": "Thu Feb 09 2023 21:39:52 GMT+0100 (Central European Standard Time)",
    #                 "title": "video card",
    #                 "description": "description of the product",
    #                 "freeDelivery": True,
    #                 "images": [
    #                     {
    #                         "src": "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-ryabchiki-14.jpg",
    #                         "alt": "Image alt string"
    #                     }
    #                 ],
    #                 "tags": [
    #                     {
    #                         "id": 12,
    #                         "name": "Gaming"
    #                     }
    #                 ],
    #                 "reviews": 5,
    #                 "rating": 4.6
    #             },
    #         ]
    #     }
    #     return JsonResponse(data)
    #
    # elif request.method == 'POST':
    #     data = {"orderId": 123}
    #     return JsonResponse(data)
    #
    # return HttpResponse(status=500)


def payment(request, id):
    print('qweqwewqeqwe', id)
    return HttpResponse(status=200)
