import requests
import json
import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.template.loader import get_template
from django.shortcuts import render, reverse
from bs4 import BeautifulSoup
import random
from datetime import datetime
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class GetOptions:
    def __init__(self, title):
        self.baseUrl = 'https://www.thesaurus.com/browse/{}'
        self.title = title

    def __get_content(self):
        response = requests.get(self.baseUrl.format(self.title))
        if response.status_code == 200:
            parsed = BeautifulSoup(response.text, 'html.parser')
            return parsed
        else:
            return []
       
    def get_words(self):
        parsed = self.__get_content()
        options = list()
        if parsed:
            numbs = parsed.find_all(class_='css-133coio')
            for numb in numbs:
                if self.title != numb.text and not numb.text in options:
                    options.append(numb.text)
            options = list(sorted(options, key=lambda k: random.random()))
            if len(options) > 4: return options[:4]
            else: return options
        else: return []

def default_create_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = six.text_type(user.id)
        ts = six.text_type(timestamp)
        is_active = six.text_type(user.is_active)
        return f"{user_id}{ts}{is_active}"

class SendEmailConfirm:
    def send(self, user, subject, operation, path):
        token = user_tokenizer.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = settings.BASE_URL + reverse(path, kwargs={'user_id': user_id, 'token': token})
        message = get_template('confirm_email.html').render({'confirm_url': url, 'operaion': operation})
        subject = subject
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=[to_email],
        )
        email.content_subtype = 'html'
        email.send()

def confirm_token(user_id, token):
    user_id = force_text(urlsafe_base64_decode(user_id))

    user = User.objects.get(id=user_id)

    if user and user_tokenizer.check_token(user, token):
        user.is_confirmed = True
        user.confirmed_on = datetime.now()
        user.save()
    else:
        raise ValueError(_('User does not exist or Token is incorrect'))
    return user


user_tokenizer = UserTokenGenerator()