from django.shortcuts import render,redirect
from. models import Category,Good,Comment,Basket,BasketItem,Saved,SavedGood
from.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q


def show_home_page(request):
    categories = Category.objects.all()
    goods=Good.objects.filter(is_available=True)
    total_goods=goods.count()
    for category in categories:
        category.goods_count=goods.filter(category=category).count()
    category_id=request.GET.get('category')
    if category_id:
        goods=goods.filter(category_id=category_id)

    subcategory_id=request.GET.get('subcategory')
    if subcategory_id:
        goods=goods.filter(subcategory_id=subcategory_id)

    context = {
        'categories': categories,
        'goods':goods,
        'total_goods':total_goods
    }
    return render(request,'main/index.html',context)


def add_to_basket(request,good_id):
    if not request.user.is_authenticated:
        return redirect('users:login_page')

    good=get_object_or_404(Good,id=good_id)
    basket,basket_created=Basket.objects.get_or_create(user=request.user)
    basket_item,item_created=BasketItem.objects.get_or_create(
                basket=basket,
                good=good,
                defaults={'quantity':1}
                    )
    if not item_created:
                basket_item.quantity += 1
                basket_item.save()


    context={
        'basket':basket,
        'basket_item':basket_item
    }
    return redirect('basket_page')


def add_quantity(request,item_id):
        basket_item=get_object_or_404(BasketItem,id=item_id)
        if basket_item.basket.user==request.user:
            basket_item.quantity +=1
            basket_item.save()
        return redirect('basket_page')

def reduce_quantity(request,item_id):
    basket_item=get_object_or_404(BasketItem,id=item_id)
    if basket_item.basket.user==request.user:
     if basket_item.quantity>1:
        basket_item.quantity-=1
        basket_item.save()
     else:
        basket_item.delete()
    return redirect('basket_page')

def show_basket_page(request):
    basket=Basket.objects.get(user=request.user)
    basket_items=BasketItem.objects.filter(basket=basket) if basket else []
    total_basket_items=basket_items.count()
    context={
        'basket':basket,
        'basket_items':basket_items,
        'total_basket_items':total_basket_items
    }
    return render(request,'main/basket.html',context)

def delete_basket_item(request,item_id):
        basket_item=get_object_or_404(BasketItem,id=item_id)
        if basket_item.basket.user == request.user:
            basket_item.delete()
        return redirect('basket_page')

def show_good_page(request,good_id):
    good=Good.objects.get(id=good_id)
    comments=Comment.objects.filter(good=good)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.good = good
            form.author = request.user
            form.save()
            return redirect('good_page',good.id)
    else:
        form = CommentForm()

    context={
        'good':good,
        'form':form,
        'comments':comments
    }
    return render(request,'main/good_page.html',context)

def delete_comment(request,comment_id):
        comment=Comment.objects.get(id=comment_id)
        good_id=comment.good.id
        comment.delete()
        return redirect('good_page',good_id)


def add_to_saved(request,good_id):
    if not request.user.is_authenticated:
        return redirect('users:login_page')

    good=get_object_or_404(Good,id=good_id)
    saved,saved_created=Saved.objects.get_or_create(user=request.user)
    saved_good,saved_good_created=SavedGood.objects.get_or_create(
                saved=saved,
                good=good,

                    )

    context={
        'saved':saved,
        'saved_good':saved_good
    }
    return redirect('saved_page')

def show_saved_page(request):
    saved=Saved.objects.get(user=request.user)
    saved_goods=SavedGood.objects.filter(saved=saved) if saved else []
    total_saved_goods=saved_goods.count()
    context={
        'saved':saved,
        'saved_goods':saved_goods,
        'total_saved_goods':total_saved_goods

    }
    return render(request,'main/saved.html',context)


def delete_saved_goods(request, good_id):
        saved_good = get_object_or_404(SavedGood, id=good_id)
        if saved_good.saved.user == request.user:
            saved_good.delete()
        return redirect('saved_page')

def search(request):
    query=request.GET.get('q')
    if not query:
        goods=Good.objects.all()
    else:
        goods=Good.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )

    context={
        'goods':goods,
        'query':query
    }
    return render(request,'main/search.html',context)




