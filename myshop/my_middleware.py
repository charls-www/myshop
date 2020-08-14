from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.get_raw_uri(), '<----------1')
