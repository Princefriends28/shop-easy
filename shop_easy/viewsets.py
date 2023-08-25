from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed


class GlobalViewSet(viewsets.ModelViewSet):
    def _allowed_methods(self):
        allowed_method = []

        app_model = str(self.queryset.model._meta).split('.')
        try:
            if self.request.user.has_perm('{}.view_{}'.format(app_model[0], app_model[1])):
                allowed_method.append('GET')
                allowed_method.append('OPTIONS')
            if self.request.user.has_perm('{}.add_{}'.format(app_model[0], app_model[1])):
                allowed_method.append('POST')
            if self.request.user.has_perm('{}.delete_{}'.format(app_model[0], app_model[1])):
                allowed_method.append('DELETE')
            if self.request.user.has_perm('{}.change_{}'.format(app_model[0], app_model[1])):
                allowed_method.append('PUT')
                allowed_method.append('PATCH')

            return allowed_method
        except AuthenticationFailed:
            return allowed_method
