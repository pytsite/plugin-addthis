"""AddThis Plugin Init.
"""
# Public API
from . import _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    """Init wrapper.
    """
    from pytsite import lang, tpl, permissions, settings, router
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='addthis')
    tpl.register_package(__name__, alias='addthis')

    # Lang globals
    lang.register_global('addthis_admin_settings_url', lambda language, args: settings.form_url('addthis'))

    # Permissions
    permissions.define_permission('addthis.settings.manage', 'addthis@manage_addthis_settings', 'app')

    # Settings
    settings.define('addthis', _settings_form.Form, 'addthis@addthis', 'fa fa-plus-square',
                    'addthis.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)


_init()
