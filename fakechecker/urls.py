from django.urls import path, include
from . import views


urlpatterns = (
    # Login
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(next_page='index'), name="logout"),

    # Experts
    path("expert/", views.ExpertListView.as_view(), name="Expert_list"),
    path("expert/create/", views.ExpertCreateView.as_view(), name="Expert_create"),
    path("expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="Expert_detail"),
    path("expert/update/<int:pk>/", views.ExpertUpdateView.as_view(), name="Expert_update"),

    # Redactors
    path("redactor/", views.RedactorListView.as_view(), name="Redactor_list"),
    path("redactor/create/", views.RedactorCreateView.as_view(), name="Redactor_create"),
    path("redactor/detail/<int:pk>/", views.RedactorDetailView, name="Redactor_detail"),
    path("redactor/update/<int:pk>/", views.RedactorUpdateView.as_view(), name="Redactor_update"),

    # Collections
    path("collection/", views.QuestionCollectionListView.as_view(), name="QuestionCollection_list"),
    path("collection/create/", views.QuestionCollectionCreateView.as_view(), name="QuestionCollection_create"),
    path("collection/detail/<int:pk>/", views.QuestionCollectionDetailView.as_view(), name="QuestionCollection_detail"),
    path("collection/update/<int:pk>/", views.QuestionCollectionUpdateView.as_view(), name="QuestionCollection_update"),

    # Reviews
    path("review/create/<int:question_for_expert_id>/", views.ReviewCreateView.as_view(), name="Review_create"),
    path("review/detail/<int:pk>/", views.ReviewDetailView.as_view(), name="Review_detail"),
    path("review/update/<int:pk>/", views.ReviewUpdateView.as_view(), name="Review_update"),

    # Categories
    path("category/", views.CategoryListView.as_view(), name="Category_list"),
    path("category/create/", views.CategoryCreateView.as_view(), name="Category_create"),
    path("category/detail/<str:pk>/", views.CategoryDetailView.as_view(), name="Category_detail"),
    path("category/update/<str:pk>/", views.CategoryUpdateView.as_view(), name="Category_update"),

    # Questions from users
    path("question/asked/", views.QuestionFromUserListView.as_view(), name="QuestionFromUser_list"),
    path("question/asked/create/", views.QuestionFromUserCreateView.as_view(), name="QuestionFromUser_create"),
    path("question/asked/detail/<int:pk>/", views.QuestionFromUserDetailView.as_view(), name="QuestionFromUser_detail"),
    path("question/asked/update/<int:pk>/", views.QuestionFromUserUpdateView.as_view(), name="QuestionFromUser_update"),

    # Questions for Experts
    path("question/", views.QuestionForExpertListView.as_view(), name="QuestionForExpert_list"),
    path("question/create/", views.QuestionForExpertCreateView.as_view(), name="QuestionForExpert_create"),
    path("question/detail/<int:pk>/", views.QuestionForExpertDetailView.as_view(), name="QuestionForExpert_detail"),
    path("question/update/<int:pk>/", views.QuestionForExpertUpdateView.as_view(), name="QuestionForExpert_update"),
)
