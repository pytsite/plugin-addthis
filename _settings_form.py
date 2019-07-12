"""PytSite AddThis Plugin Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang, validation
from plugins import widget, settings


class Form(settings.Form):
    def _on_setup_widgets(self):
        """Hook.
        """
        self.add_widget(widget.input.Text(
            uid='setting_pub_id',
            weight=10,
            label=lang.t('addthis@pub_id'),
            required=True,
            help=lang.t('addthis@pub_id_setup_help'),
            rules=validation.rule.Regex(pattern='ra-[0-9a-f]{16}')
        ))

        super()._on_setup_widgets()
