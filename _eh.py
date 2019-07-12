"""PytSite AddThis Plugin Events Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, router, reg
from plugins import auth, assetman


def router_dispatch():
    """'pytsite.router.dispatch' handler
    """
    pub_id = reg.get('addthis.pub_id')

    if pub_id:
        assetman.inline_js('<script src="//s7.addthis.com/js/300/addthis_widget.js#pubid={}"></script>'.format(pub_id))
    elif auth.get_current_user().has_role('dev'):
        router.session().add_warning_message(lang.t('addthis@plugin_setup_required_warning'))
