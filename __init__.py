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
    from pytsite import lang, tpl, permissions, settings
    from . import _settings_form

    if not lang.is_package_registered(__name__):
        lang.register_package(__name__)

    if not tpl.is_package_registered(__name__):
        tpl.register_package(__name__)

    if not permissions.is_permission_defined('addthis.settings.manage'):
        permissions.define_permission('addthis.settings.manage', 'pytsite.addthis@manage_addthis_settings', 'app')

    if not settings.is_defined('addthis'):
        settings.define('addthis', _settings_form.Form, 'pytsite.addthis@addthis', 'fa fa-plus-square',
                        'addthis.settings.manage')


_init()
