from .views import *

from django.urls import path, re_path

from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView, ResendEmailVerificationView

urlpatterns = [
    path("sign-up/", RegisterView.as_view()),
    path("sign-in/", LoginView.as_view()),
    path("sign-out/", LogoutView.as_view()),

    path("account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("account-confirm-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),
    re_path(r"^account-confirm-email/(?P<key>[-:\w]+)/$", VerifyEmailView.as_view(), name="account_confirm_email"),
    path("email/resend/", ResendEmailVerificationView.as_view(), name="resend_email"),
    
    path("password/reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password/reset/confirm/<id>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password/change/", PasswordChangeView.as_view(), name="password_change")
]