from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class AuthBackend(ModelBackend):
    def authenticate(self, request, identifier=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=identifier) | Q(email__iexact=identifier))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=identifier) | Q(email__iexact=identifier)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user