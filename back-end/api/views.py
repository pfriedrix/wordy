import random

from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from googletrans import Translator
from rest_framework import status, views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     RetrieveUpdateAPIView, ListCreateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Collection, User, Word
from .permissions import IsAuthor
from .serializers import (
    CollectionSerializer,
    PasswordChangeSeializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    TitleSerializer,
    TokenSerializer,
    UserSerializer,
    WordSerializer,
)
from .utils import GetOptions, SendEmailConfirm, confirm_token, default_create_token


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def get_response_data(self, user, message):
        return {
            'detail': _(message),
            'token': self.token
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        send_email = SendEmailConfirm()
        send_email.send(user, "WORDY CONFIRM EMAIL", "Confirm Email", "confirm")
        message = "Email confirmation has been sent"
        return Response(
            self.get_response_data(user, message), status=status.HTTP_201_CREATED,
        )

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        self.token = default_create_token(user)
        return user


class PasswordChangeView(GenericAPIView):
    serializer_class = PasswordChangeSeializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved")})


class ConfirmEmailView(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request, user_id, token):
        try:
            confirm_token(user_id, token)
        except ValueError as error:
            message = error
        else:
            message = "Account confirmed"
        return Response({"message": message,}, status=status.HTTP_202_ACCEPTED,)


class UserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        if self.request.user.is_confirmed:
            return self.request.user


class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        logout(request)
        response = Response(
            {"detail": _("Successfully logged out")}, status=status.HTTP_200_OK
        )
        return response


class PasswordResetView(GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        user = User.objects.get(email=email)
        send_email = SendEmailConfirm()
        send_email.send(user, "PASSWORD RESET", "Reset", "confirm-reset")
        return Response(
            {"detail": _("Password rest email has been sent")},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    user = None

    def get(self, request, user_id, token):
        self.confirmed = False
        message = None
        try:
            self.user = confirm_token(user_id, token)
        except ValueError as error:
            message = error
        else:
            message = _("Reset confirmed")
            self.confirmed = True
        return Response({"message": message,}, status=status.HTTP_202_ACCEPTED,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data.get("new_password")
        if self.user and self.confirmed:
            self.user.set_password(new_password)

        return Response({"detail": _("New password has been saved")})


class CollectionViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
        IsAuthor,
    )
    serializer_class = CollectionSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Collection.objects.filter(user=user)

class WordsInCollection(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAuthor,)
    serializer_class = WordSerializer
    
    def get_queryset(self):
        collection = self.kwargs['pk']
        return Word.objects.filter(collection=collection)
        

class WordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthor)
    serializer_class = WordSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Word.objects.filter(user=user)


class TranslatorView(views.APIView):
    serializer_class = TitleSerializer
    permission_classes = [AllowAny,]

    def post(self, request):
        translator = Translator()
        title = request.data["title"]
        translation = translator.translate(title, dest="ru").text
        if translation:
            return Response(
                {
                    "title": title,
                    "status": status.HTTP_201_CREATED,
                    "translation": translation.lower(),
                }
            )
        else:
            return Response({"title": title, "status": status.HTTP_404_NOT_FOUND,})


class GetRandomWordsCollections(views.APIView):
    serializer_class = WordSerializer
    permission_classes = (
        IsAuthenticated,
        IsAuthor,
    )

    def get(self, request, pk):
        user = self.request.user.id
        pk = self.kwargs["pk"]
        words = Word.objects.filter(user=user, collection=pk)
        words = [word for word in words if word.progress < 100]
        randomOrder = list(
                sorted(words, key=lambda x: random.random()))
        if len(words) < 10: return Response({
            'collection': pk,
            'words': [{'id': word.id, 'title': word.title, 'translation': word.translation} for word in randomOrder] })
        else:
            return Response({
            'collection': pk,
            'words': [{'id': word.id, 'title': word.title, 'translation': word.translation} for word in randomOrder[:10]], })


class OptionsView(views.APIView):
    permission_classes = (
        IsAuthenticated,
        IsAuthor,
    )

    def get(self, request, pk):
        origin = Word.objects.get(id=pk)
        options = GetOptions(origin.title).get_words()
        if not options or len(options) < 3:
            last = 4 - len(options)
            words = Word.objects.all()
            randWords = list(sorted(words, key=lambda x: random.random()))[:last]
            last_options = [word.title for word in randWords]
            options += last_options
        options.append(origin.title)
        return Response({
            'options': sorted(options, key=lambda x: random.random()),
            'origin': {
                'title': origin.title,
                'translation': origin.translation,
                'progress': origin.progress,
                'id': origin.id
            },
        })

class ImproveProgressView(views.APIView):
    permission_classes = (IsAuthenticated, IsAuthor,)

    def post(self, request, pk):
        message = None
        word = None
        try:
            word = Word.objects.get(id=pk)
        except ObjectDoesNotExist:
            message = _("Word doesn't exist")
        else:
            word.progress += 10
            word.save()
            message = _("Progress increased on 10xp")
        return Response({
            'detail': message
        }, status=status.HTTP_202_ACCEPTED)
