"""PytSite AddThis Plugin Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class Form(_settings.Form):
    def _on_setup_widgets(self):
        """Hook.
        """
        self.add_widget(_widget.input.Text(
            uid='setting_pub_id',
            weight=10,
            label=_lang.t('addthis@pub_id'),
            required=True,
            help=_lang.t('addthis@pub_id_setup_help'),
            rules=_validation.rule.Regex(pattern='ra-[0-9a-f]{16}')
        ))

        super()._on_setup_widgets()
