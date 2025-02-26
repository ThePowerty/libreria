from django.http import Http404
from django.core.exceptions import PermissionDenied

def user_can_delete_model(model):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            try:
                instance = model.objects.get(pk=kwargs["pk"])
            except model.DoesNotExist:
                raise Http404

            if request.user == instance.created_by:
                return function(request, *args, **kwargs)

            raise PermissionDenied

        return wrap
    return decorator