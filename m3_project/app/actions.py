from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import PermissionAddWindow, UserAddWindow


class ContentTypePack(ObjectPack):
    model = ContentType

    # в доке objectpack.ModelEditWindow, а тут из objectpack.ui
    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_menu = True


class UserPack(ObjectPack):
    model = User

    add_window = edit_window = UserAddWindow
    add_to_menu = True


class GroupPack(ObjectPack):
    model = Group

    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_menu = True


class PermissionPack(ObjectPack):
    model = Permission

    add_window = edit_window = PermissionAddWindow

    add_to_menu = True
