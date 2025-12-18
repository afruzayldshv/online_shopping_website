from django.urls import path
from. import views

urlpatterns=[
    path('',views.show_home_page,name='home_page'),
    path('add_basket/<str:good_id>/',views.add_to_basket,name='add_to_basket'),
    path('basket',views.show_basket_page,name='basket_page'),
    path('delete_basket_item/<str:item_id>/',views.delete_basket_item,name='delete_basket_item'),
    path('basket/add/<str:item_id>/',views.add_quantity,name='add_quantity'),
    path('basket/reduce/<str:item_id>/',views.reduce_quantity,name='reduce_quantity'),
    path('goods/<str:good_id>/',views.show_good_page,name='good_page'),
    path('delete_comment/<str:comment_id>/',views.delete_comment,name='delete_comment'),
    path('saved/',views.show_saved_page,name='saved_page'),
    path('add_saved/<str:good_id>/',views.add_to_saved,name='add_to_saved'),
    path('delete_saved_good/<str:good_id>/',views.delete_saved_goods,name='delete_saved_goods'),
    path('search/',views.search,name='search')
]