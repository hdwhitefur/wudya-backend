from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from wudya import views

router = routers.DefaultRouter()
router.register(r'options', views.OptionView, 'option')
router.register(r'optionpairs', views.OptionPairView, 'optionpair')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/optionpairs/<int:id>/vote/', views.VoteView),
    path('api/', include(router.urls))
]
