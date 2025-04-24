from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.category import CategoryList, CategoryDetail
from .views.company import CompanyList, CompanyDetail

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("category/", CategoryList.as_view(), name="category_list"),
    path("category/<uuid:pk>", CategoryDetail.as_view(), name="category_detail"),

    path("company/", CompanyList.as_view(), name="company_list"),
    path("company/<uuid:pk>", CompanyDetail.as_view(), name="company_detail"),
]
