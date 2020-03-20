from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Expert", api.ExpertViewSet)
router.register("Redactor", api.RedactorViewSet)
router.register("QuestionCollection", api.QuestionCollectionViewSet)
router.register("Review", api.ReviewViewSet)
router.register("Category", api.CategoryViewSet)
router.register("Question", api.QuestionViewSet)
router.register("QuestionFromUser", api.QuestionFromUserViewSet)
router.register("QuestionForExpert", api.QuestionForExpertViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("expert/", views.ExpertListView.as_view(), name="fakechecker_Expert_list"),
    path("expert/create/", views.ExpertCreateView.as_view(), name="fakechecker_Expert_create"),
    path("expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="fakechecker_Expert_detail"),
    path("expert/update/<int:pk>/", views.ExpertUpdateView.as_view(), name="fakechecker_Expert_update"),
    path("redactor/", views.RedactorListView.as_view(), name="fakechecker_Redactor_list"),
    path("redactor/create/", views.RedactorCreateView.as_view(), name="fakechecker_Redactor_create"),
    path("redactor/detail/<int:pk>/", views.RedactorDetailView, name="fakechecker_Redactor_detail"),
    path("redactor/update/<int:pk>/", views.RedactorUpdateView.as_view(), name="fakechecker_Redactor_update"),
    path("collection/", views.QuestionCollectionListView.as_view(), name="fakechecker_QuestionCollection_list"),
    path("collection/create/", views.QuestionCollectionCreateView.as_view(), name="fakechecker_QuestionCollection_create"),
    path("collection/detail/<int:pk>/", views.QuestionCollectionDetailView.as_view(), name="fakechecker_QuestionCollection_detail"),
    path("collection/update/<int:pk>/", views.QuestionCollectionUpdateView.as_view(), name="fakechecker_QuestionCollection_update"),
    path("review/", views.ReviewListView.as_view(), name="fakechecker_Review_list"),
    path("review/create/<int:question_for_expert_id>/", views.ReviewCreateView.as_view(), name="fakechecker_Review_create"),
    path("review/detail/<int:pk>/", views.ReviewDetailView.as_view(), name="fakechecker_Review_detail"),
    path("review/update/<int:pk>/", views.ReviewUpdateView.as_view(), name="fakechecker_Review_update"),
    path("category/", views.CategoryListView.as_view(), name="fakechecker_Category_list"),
    path("category/create/", views.CategoryCreateView.as_view(), name="fakechecker_Category_create"),
    path("category/detail/<str:pk>/", views.CategoryDetailView.as_view(), name="fakechecker_Category_detail"),
    path("category/update/<str:pk>/", views.CategoryUpdateView.as_view(), name="fakechecker_Category_update"),
    path("question/asked/", views.QuestionFromUserListView.as_view(), name="fakechecker_QuestionFromUser_list"),
    path("question/asked/create/", views.QuestionFromUserCreateView.as_view(), name="fakechecker_QuestionFromUser_create"),
    path("question/asked/detail/<int:pk>/", views.QuestionFromUserDetailView.as_view(), name="fakechecker_QuestionFromUser_detail"),
    path("question/asked/update/<int:pk>/", views.QuestionFromUserUpdateView.as_view(), name="fakechecker_QuestionFromUser_update"),
    path("question/", views.QuestionForExpertListView.as_view(), name="fakechecker_QuestionForExpert_list"),
    path("question/create/", views.QuestionForExpertCreateView.as_view(), name="fakechecker_QuestionForExpert_create"),
    path("question/detail/<int:pk>/", views.QuestionForExpertDetailView.as_view(), name="fakechecker_QuestionForExpert_detail"),
    path("question/update/<int:pk>/", views.QuestionForExpertUpdateView.as_view(), name="fakechecker_QuestionForExpert_update"),
)
