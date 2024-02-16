from django.urls import path
from django.conf import settings
from store import views
from django.conf.urls.static import static
from store.views import index,signup,login,logout,cartpage
from store.views.order import order_display
from store.views.admin import admin_view
from store.views.admin_add_product import admin_addproduct
from store.views.admin_login import admin_log
from store.views.admin_orders import adminorder
from store.views.admin_logout import adminlogout
from store.views.admin_update import adminupdate




urlpatterns = [
    path('',index.as_view()),
    path('sign/',signup.as_view(),name='sign'),
    path('login/',login.as_view(),name='login'),
    path('adminlogout/',adminlogout.as_view(),name='adminlogout'),
    path('cartpage/',cartpage.as_view(),name='cartpage'),
    path('order/', order_display.as_view(),name='order'),
    path('admin_view/',admin_view.as_view(),name='admin_view'),
    path('adminaddproduct/', admin_addproduct.as_view(), name='adminaddproduct'),
    path('admin_log/',admin_log.as_view(),name='admin_log'),
    path('/logout/',logout.as_view(),name='logout'),
    path('update/',adminupdate.as_view(),name='update'),
    path('adminorder/',adminorder.as_view(),name='adminorder'),



]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




