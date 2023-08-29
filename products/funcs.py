from django.forms import model_to_dict

from .models import *


def get_list(model, prod_id):
    return [model_to_dict(model.objects.filter(product=prod_id)[i]) for i in
            range(len(model.objects.filter(product=prod_id)))]


def product_to_model(prod):
    prod['images'] = get_list(Image, prod['id'])
    prod['tags'] = get_list(Tag, prod['id'])
    prod['reviews'] = get_list(Review, prod['id'])
    prod['specifications'] = get_list(Specification, prod['id'])
    prod['price'] = float(prod['price'])
    return prod


def basket_product_to_model(prod):
    for i in range(len(prod)):
        prod[i] = model_to_dict(prod[i])
        prod[i]['product'] = model_to_dict(Product.objects.filter(id=prod[i]['product'])[0])
        prod[i]['product'] = product_to_model(prod[i]['product'])
        prod[i]['product']['count'] = prod[i]['count']

    return prod
