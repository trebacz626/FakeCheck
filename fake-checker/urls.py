from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Review", api.ReviewViewSet)
router.register("Category", api.CategoryViewSet)
router.register("Question", api.QuestionViewSet)
router.register("Expert", api.ExpertViewSet)
router.register("Redactor", api.RedactorViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("fake-checker/Review/", views.ReviewListView.as_view(), name="fake-checker_Review_list"),
    path("fake-checker/Review/create/", views.ReviewCreateView.as_view(), name="fake-checker_Review_create"),
    path("fake-checker/Review/detail/<int:pk>/", views.ReviewDetailView.as_view(), name="fake-checker_Review_detail"),
    path("fake-checker/Review/update/<int:pk>/", views.ReviewUpdateView.as_view(), name="fake-checker_Review_update"),
    path("fake-checker/Category/", views.CategoryListView.as_view(), name="fake-checker_Category_list"),
    path("fake-checker/Category/create/", views.CategoryCreateView.as_view(), name="fake-checker_Category_create"),
    path("fake-checker/Category/detail/<int:pk>/", views.CategoryDetailView.as_view(), name="fake-checker_Category_detail"),
    path("fake-checker/Category/update/<int:pk>/", views.CategoryUpdateView.as_view(), name="fake-checker_Category_update"),
    path("fake-checker/Question/", views.QuestionListView.as_view(), name="fake-checker_Question_list"),
    path("fake-checker/Question/create/", views.QuestionCreateView.as_view(), name="fake-checker_Question_create"),
    path("fake-checker/Question/detail/<int:pk>/", views.QuestionDetailView.as_view(), name="fake-checker_Question_detail"),
    path("fake-checker/Question/update/<int:pk>/", views.QuestionUpdateView.as_view(), name="fake-checker_Question_update"),
    path("fake-checker/Expert/", views.ExpertListView.as_view(), name="fake-checker_Expert_list"),
    path("fake-checker/Expert/create/", views.ExpertCreateView.as_view(), name="fake-checker_Expert_create"),
    path("fake-checker/Expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="fake-checker_Expert_detail"),
    path("fake-checker/Expert/update/<int:pk>/", views.ExpertUpdateView.as_view(), name="fake-checker_Expert_update"),
    path("fake-checker/Redactor/", views.RedactorListView.as_view(), name="fake-checker_Redactor_list"),
    path("fake-checker/Redactor/create/", views.RedactorCreateView.as_view(), name="fake-checker_Redactor_create"),
    path("fake-checker/Redactor/detail/<int:pk>/", views.RedactorDetailView.as_view(), name="fake-checker_Redactor_detail"),
    path("fake-checker/Redactor/update/<int:pk>/", views.RedactorUpdateView.as_view(), name="fake-checker_Redactor_update"),
)
