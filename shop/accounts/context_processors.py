from .models import Profile

def user_info(request):
    if request.user.is_authenticated():
        user = request.user
        extend_fields = Profile.objects.get_or_create(user=user)
        try:
            extend_fields = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            extend_fields = Profile.objects.create(user=user)
            extend_fields.save()

        context = {
            'extend_fields': extend_fields,
        }
        return context

    return {"login": "login"}
