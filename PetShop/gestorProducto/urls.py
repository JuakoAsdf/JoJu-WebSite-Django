from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('inicio',views.inicio, name='inicio'),
    path('adultocat',views.alimentoadultocat, name='adultocat'),
    path('gatitocat',views.alimentogatito, name='gatitocat'),
    path('accesocat',views.accesoriocat, name='accesocat'),
    path('adultodog',views.alimentoadultodog, name='adultodog'),
    path('cachorrodog',views.alimentocachorro, name='cachorrodog'),
    path('accesodog',views.accesoriodog, name='accesodog'),
    path('adopta',views.adopcion, name='adopta'),
    path('nosotro',views.nosotros, name='nosotro'),
    path('log',views.loginPage, name='log'),
    path('buscar',views.buscar, name='buscar'),
<<<<<<< HEAD
    path('regis',views.registerPage, name='regis'),
    path('logout', views.logout, name='logout'),
]

=======
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
>>>>>>> 1e9e3d29f208ae4cce7c03b6a776119185f59bf0
