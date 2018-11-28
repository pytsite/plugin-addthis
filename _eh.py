"""PytSite AddThis Plugin Events Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, router as _router, reg as _reg
from plugins import auth as _auth, assetman as _assetman


def router_dispatch():
    """'pytsite.router.dispatch' handler
    """
    pub_id = _reg.get('addthis.pub_id')

    if pub_id:
        _assetman.inline_js('<script src="//s7.addthis.com/js/300/addthis_widget.js#pubid={}"></script>'.format(pub_id))
    elif _auth.get_current_user().has_role('dev'):
        _router.session().add_warning_message(_lang.t('addthis@plugin_setup_required_warning'))
