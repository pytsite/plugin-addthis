"""PytSite AddThis Plugin Event Handlers.
"""
from pytsite import settings as _settings, auth as _auth, lang as _lang, router as _router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    if not _settings.get('addthis.pub_id'):
        if _auth.get_current_user().has_permission('addthis.settings.manage'):
            msg = _lang.t('addthis@plugin_setup_required_warning')
            if not _settings.get('addthis.app_key') or not _settings.get('addthis.app_secret'):
                _router.session().add_warning_message(msg)
            else:
                _router.session().get_warning_message(msg)
