from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
from ..permissions import SitePermission as Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
