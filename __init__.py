"""PytSite AddThis Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

# Public API
if _plugman.is_installed(__name__):
    from . import _widget as widget


def plugin_load_uwsgi():
    """Hook
    """
    from pytsite import lang, tpl, router
    from plugins import permissions, settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('addthis_admin_settings_url', lambda language, args: settings.form_url('addthis'))

    # Permissions
    permissions.define_permission('addthis@manage_settings', 'addthis@manage_addthis_settings', 'app')

    # Settings
    settings.define('addthis', _settings_form.Form, 'addthis@addthis', 'fa fa-plus-square', 'addthis@manage_settings')

    # Events
    router.on_dispatch(_eh.router_dispatch)
