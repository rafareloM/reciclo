# coding: utf-8
def user_info(request):
    """
    Context processor to add user information to all templates
    """
    if request.user.is_authenticated:
        return {
            'user_tipo': request.user.tipo,
            'user_tipo_display': request.user.get_tipo_display(),
            'is_admin': request.user.is_admin(),
            'is_curator': request.user.is_curator(),
            'is_producer': request.user.is_producer(),
        }
    return {}
