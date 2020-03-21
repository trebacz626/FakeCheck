from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import security
from . import views
from . import questionCollectionViews


urlpatterns = (
    # Login
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(next_page='index'), name="logout"),

    # Experts
    path("expert/", views.ExpertListView.as_view(), name="Expert_list"),
    path("expert/how_to_be/", views.ExpertHowToBe, name="Expert_how_to_be"),
    path("expert/detail/<int:pk>/", views.ExpertDetailView.as_view(), name="Expert_detail"),


    # Redactors
    path("redactor/", views.RedactorListView.as_view(), name="Redactor_list"),
    path("redactor/detail/<int:pk>/", views.RedactorDetailView.as_view(), name="Redactor_detail"),

    # Collections
    path("collection/", questionCollectionViews.QuestionCollectionListView.as_view(), name="QuestionCollection_list"),
    path("collection/create/", questionCollectionViews.QuestionCollectionCreateView.as_view(), name="QuestionCollection_create"),
    path("collection/detail/<int:pk>/", questionCollectionViews.QuestionCollectionDetailView.as_view(), name="QuestionCollection_detail"),
    path("collection/<int:pk>/question/<int:question_id>/", questionCollectionViews.QuestionCollectionViewQuestion.as_view(), name="QuestionCollection_question"),


    # Reviews
    path("review/create/<int:question_for_expert_id>/", views.ReviewCreateView.as_view(), name="Review_create"),
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

    # Questions for Experts
    path("question/", views.QuestionForExpertListView.as_view(), name="QuestionForExpert_list"),
    path("question/create/", views.QuestionForExpertCreateView.as_view(), name="QuestionForExpert_create"),
    path("question/detail/<int:pk>/", views.QuestionForExpertDetailView.as_view(), name="QuestionForExpert_detail"),
    path("question/update/<int:pk>/", views.QuestionForExpertUpdateView.as_view(), name="QuestionForExpert_update"),
)
