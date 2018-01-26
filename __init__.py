"""PytSite AddThis Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _widget as widget


def plugin_load_uwsgi():
    """Hook
    """
    from pytsite import lang, tpl, router
    from plugins import settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('addthis_admin_settings_url', lambda language, args: settings.form_url('addthis'))

    # Settings
    settings.define('addthis', _settings_form.Form, 'addthis@addthis', 'fa fa-plus-square', 'dev')

    # Events
    router.on_dispatch(_eh.router_dispatch)
