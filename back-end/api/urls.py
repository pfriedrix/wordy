from django.urls import include, path

from .views import (ConfirmEmailView, GetRandomWordsCollections,
                    LogoutView, OptionsView, PasswordChangeView,
                    PasswordResetView, RegisterView, TranslatorView, UserView, PasswordResetConfirmView, CollectionViewSet, WordViewSet, WordsInCollection, ImproveProgressView, GetLearntWordsView, GetXPSView)
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

router = SimpleRouter()

router.register('collections', CollectionViewSet, basename='collections')
router.register('words', WordViewSet, basename='words')

urlpatterns = [
    path('auth/sign-up', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/logout', LogoutView.as_view()),
    path('auth/token/verity', TokenVerifyView.as_view()),
    path('user', UserView.as_view()),
    path('user/learnt', GetLearntWordsView.as_view()),
    path('user/xps', GetXPSView.as_view()),
    path('auth/password/change', PasswordChangeView.as_view()),
    path('auth/password/reset', PasswordResetView.as_view()),
    path('auth/password/confirm/<str:user_id>/<str:token>', PasswordResetConfirmView.as_view(), name='confirm-reset'),
    path('translator', TranslatorView.as_view()),
    path('collections/<int:pk>/words', WordsInCollection.as_view()),
    path('collections/<int:pk>/get-random-order', GetRandomWordsCollections.as_view()),
    path('words/<int:pk>/options', OptionsView.as_view()),
    path('words/<int:pk>/learn', ImproveProgressView.as_view()),
    path('auth/confirm/<str:user_id>/<str:token>', ConfirmEmailView.as_view(), name='confirm'),
]

urlpatterns += router.urls