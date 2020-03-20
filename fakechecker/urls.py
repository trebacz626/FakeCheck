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
    path("fakechecker/Expert/", views.ExpertListView.as_view(), name="fakechecker_Expert_list"),
    path("fakechecker/Expert/create/", views.ExpertCreateView.as_view(), name="fakechecker_Expert_create"),
    path("fakechecker/Expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="fakechecker_Expert_detail"),
    path("fakechecker/Expert/update/<int:pk>/", views.ExpertUpdateView.as_view(), name="fakechecker_Expert_update"),
    path("fakechecker/Redactor/", views.RedactorListView.as_view(), name="fakechecker_Redactor_list"),
    path("fakechecker/Redactor/create/", views.RedactorCreateView.as_view(), name="fakechecker_Redactor_create"),
    path("fakechecker/Redactor/detail/<int:pk>/", views.RedactorDetailView, name="fakechecker_Redactor_detail"),
    path("fakechecker/Redactor/update/<int:pk>/", views.RedactorUpdateView.as_view(), name="fakechecker_Redactor_update"),
    path("fakechecker/QuestionCollection/", views.QuestionCollectionListView.as_view(), name="fakechecker_QuestionCollection_list"),
    path("fakechecker/QuestionCollection/create/", views.QuestionCollectionCreateView.as_view(), name="fakechecker_QuestionCollection_create"),
    path("fakechecker/QuestionCollection/detail/<int:pk>/", views.QuestionCollectionDetailView.as_view(), name="fakechecker_QuestionCollection_detail"),
    path("fakechecker/QuestionCollection/update/<int:pk>/", views.QuestionCollectionUpdateView.as_view(), name="fakechecker_QuestionCollection_update"),
    path("fakechecker/Review/", views.ReviewListView.as_view(), name="fakechecker_Review_list"),
    path("fakechecker/Review/create/<int:question_for_expert_id>/", views.ReviewCreateView.as_view(), name="fakechecker_Review_create"),
    path("fakechecker/Review/detail/<int:pk>/", views.ReviewDetailView.as_view(), name="fakechecker_Review_detail"),
    path("fakechecker/Review/update/<int:pk>/", views.ReviewUpdateView.as_view(), name="fakechecker_Review_update"),
    path("fakechecker/Category/", views.CategoryListView.as_view(), name="fakechecker_Category_list"),
    path("fakechecker/Category/create/", views.CategoryCreateView.as_view(), name="fakechecker_Category_create"),
    path("fakechecker/Category/detail/<str:pk>/", views.CategoryDetailView.as_view(), name="fakechecker_Category_detail"),
    path("fakechecker/Category/update/<str:pk>/", views.CategoryUpdateView.as_view(), name="fakechecker_Category_update"),
    path("fakechecker/Question/", views.QuestionListView.as_view(), name="fakechecker_Question_list"),
    path("fakechecker/Question/create/", views.QuestionCreateView, name="fakechecker_Question_create"),
    path("fakechecker/Question/detail/<int:pk>/", views.QuestionDetailView.as_view(), name="fakechecker_Question_detail"),
    path("fakechecker/Question/update/<int:pk>/", views.QuestionUpdateView.as_view(), name="fakechecker_Question_update"),
    path("fakechecker/QuestionFromUser/", views.QuestionFromUserListView.as_view(), name="fakechecker_QuestionFromUser_list"),
    path("fakechecker/QuestionFromUser/create/", views.QuestionFromUserCreateView.as_view(), name="fakechecker_QuestionFromUser_create"),
    path("fakechecker/QuestionFromUser/detail/<int:pk>/", views.QuestionFromUserDetailView.as_view(), name="fakechecker_QuestionFromUser_detail"),
    path("fakechecker/QuestionFromUser/update/<int:pk>/", views.QuestionFromUserUpdateView.as_view(), name="fakechecker_QuestionFromUser_update"),
    path("fakechecker/QuestionForExpert/", views.QuestionForExpertListView.as_view(), name="fakechecker_QuestionForExpert_list"),
    path("fakechecker/QuestionForExpert/create/", views.QuestionForExpertCreateView.as_view(), name="fakechecker_QuestionForExpert_create"),
    path("fakechecker/QuestionForExpert/detail/<int:pk>/", views.QuestionForExpertDetailView.as_view(), name="fakechecker_QuestionForExpert_detail"),
    path("fakechecker/QuestionForExpert/update/<int:pk>/", views.QuestionForExpertUpdateView.as_view(), name="fakechecker_QuestionForExpert_update"),
)
