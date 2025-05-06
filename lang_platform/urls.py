"""
URL configuration for lang_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses.views import home_view
from courses.views import login_view
from courses.views import logout_view
from courses.views import register_view
from courses.views import language_selection_view, select_language_view
from courses.views import dashboard_view
from courses.views import lesson_view
from courses.views import submit_answer
from courses.views import next_lesson
from courses.views import leaderboard_view
from courses.views import profile_view
from courses.views import shop_view
from courses.views import quests_view
from courses.views import claim_quest_reward
from courses.views import progress_dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("select-language/", language_selection_view, name="language_selection"),
    path("save-language/", select_language_view, name="select_language"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("lesson/<int:lesson_id>/", lesson_view, name="lesson"),
    path("submit_answer/", submit_answer, name="submit_answer"),
    path('next-lesson/<int:lesson_id>/', next_lesson, name='next_lesson'),
    path("leaderboard/", leaderboard_view, name="leaderboard"),
    path("profile/", profile_view, name="profile"),
    path("shop/", shop_view, name="shop"),
    path("quests/", quests_view, name="quests"),
    path("claim-quest/<int:quest_id>/", claim_quest_reward, name="claim_quest"),
    path("progress_dashboard/", progress_dashboard_view, name="progress_dashboard"),
]
