from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import render
from social.exceptions import AuthCanceled, AuthFailed, AuthUnknownError, AuthTokenError, AuthMissingParameter, AuthStateMissing, AuthStateForbidden, AuthAlreadyAssociated, AuthTokenRevoked, AuthForbidden
from requests.exceptions import (ConnectionError)#, ConnectTimeout, ReadTimeout, SSLError, ProxyError)

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if type(exception) == AuthCanceled:
            return render(request, "travelplans/login.html", {})
        elif type(exception) == AuthFailed:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthUnknownError:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthTokenError:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthMissingParameter:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthStateMissing:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthStateForbidden:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthAlreadyAssociated:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthTokenRevoked:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == AuthForbidden:
            return render(request, "travelplans/error.html", {})
        elif type(exception) == ConnectionError:
            return render(request, "travelplans/conn_error.html", {})
        elif type(exception) == ConnectTimeout:
            return render(request, "travelplans/conn_error.html", {})
        else:
            pass
            
