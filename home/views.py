import json

from django.http import HttpResponse
from django.shortcuts import render

from home.models import Product, ProductImage, BaseModel, Category, CategorySub, Banner, User


# 搜索查询商品信息
def search_shops(request):
    result = {}
    li = []
    try:
        keywords = request.GET.get('key')
        products = Product.objects.filter(name__contains=keywords)
        for product in products:
            product_imgs = ProductImage.objects.filter(pid=product.id)
            product.imgs = BaseModel.qs_to_dict(product_imgs)
            li.append(product.to_dict())
        result.update(state=200, msg='success', data=li)
    except BaseException as e:
        result.update(state=201, msg='失败')
    return HttpResponse(json.dumps(result), content_type='Application/json')


def show_shop_cate(request):
    result = {}
    li = []
    try:
        cate_list = Category.objects.all()
        banners = BaseModel.qs_to_dict(Banner.objects.all())
        result.update(banners=banners)
        for cate in cate_list:
            cate_list = CategorySub.objects.filter(cid=cate.id)
            cate.subs = cate.qs_to_dict(cate_list)

            li.append(cate.to_dict())
        result.update(state=200, msg='success', data=li)
    except:
        result.update(state=200, msg='失败')
    return HttpResponse(json.dumps(result), content_type='Application/json')


def show_shop_detail(request):
    result = {}
    li = []
    try:
        products = Product.objects.all()
        for product in products:
            product_list = ProductImage.objects.filter(pid=product.id)
            product.imgs = product.qs_to_dict(product_list)
            li.append(product.to_dict())
        result.update(state=200, msg='success', data=li)
    except:
        result.update(state=200, msg='success')
    return HttpResponse(json.dumps(result), content_type='Application/json')


def get_shop_img(request):
    result = {}
    li = []
    try:
        pid = request.GET.get('pid')
        products = Product.objects.filter(id=pid)

        for product in products:
            product_img = ProductImage.objects.filter(pid=product.id)
            product.img_list = BaseModel.qs_to_dict(product_img.filter(type='type_single'))
            product.review_count = product.review_set.count()

            product.order_count = product.orderitem_set.count()

            li.append(product.to_dict())
        result.update(state=200, msg='success', data=li)
    except:
        result.update(state=200, msg='失败')
    return HttpResponse(json.dumps(result), content_type='Application/json')


def login(request):
    try:
        if request.method == 'GET':
            username = request.GET.get('username')
            password = request.GET.get('password')
            users = User.objects.filter(name=username)
            if users:
                for user in users:
                    if user.password == password:
                        return HttpResponse('登录成功')
                    else:
                        return HttpResponse('密码错误')
            else:
                return HttpResponse('用户名不存在,请注册')
    except:
        return HttpResponse('网络错误')



