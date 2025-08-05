from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'stocks', views.StockViewSet, basename='stock')

urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),

    # API urls
    path('api/', include(router.urls)),
]
