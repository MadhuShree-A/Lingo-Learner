from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, LanguageViewSet, CourseViewSet, LessonViewSet, ExerciseViewSet,
                    UserProgressViewSet, UserXPViewSet, AchievementViewSet, UserAchievementViewSet,
                    DiscussionViewSet, LeaderboardViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'user-progress', UserProgressViewSet)
router.register(r'user-xp', UserXPViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'user-achievements', UserAchievementViewSet)
router.register(r'discussions', DiscussionViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

