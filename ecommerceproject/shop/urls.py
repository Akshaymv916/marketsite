from django.urls import path,include
from. import views
app_name='shop'

urlpatterns = [
    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='product_by_category'),

    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),
    path('abou',views.about,name='about'),
    path('cont',views.contact,name='contact'),
    path('log',views.login_view,name='login'),
    path('sign',views.signup,name='sign'),
    path('so',views.sort,name='sort'),
    path('lowto', views.lwtohi, name='lh'),
    path('higto', views.hitolw, name='hl')

]