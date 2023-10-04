from django.contrib.auth.models import Group, User


def on_user_login(user: User, token: dict):

    if not user.is_staff:
        user.is_staff = True
        user.save()

    default_group = Group.objects.get(name="default")
    if default_group not in user.groups.all():
        user.groups.add(default_group)
