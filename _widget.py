"""PytSite AddThis Widget.
"""
from pytsite import html as _html
from plugins import assetman as _assetman, settings as _settings, widget as _widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

_valid_box_types = (
    'inline_share_toolbox', 'addthis_inline_share_toolbox',
    'sharing_toolbox', 'addthis_sharing_toolbox',
    'recommended_horizontal', 'addthis_recommended_horizontal',
)


class AddThis(_widget.Abstract):
    """AddThis Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init
        """
        super().__init__(uid, **kwargs)

        self._pub_id = _settings.get('addthis.pub_id')
        if not self._pub_id:
            raise RuntimeError("Setting 'addthis.pub_id' is not defined.")

        self._box_type = kwargs.get('box_type', _valid_box_types[0])
        if self._box_type not in _valid_box_types:
            raise RuntimeError("Invalid type: '{}'. Valid types are: {}.".format(self._box_type, str(_valid_box_types)))

        if not self._box_type.startswith('addthis_'):
            self._box_type = 'addthis_' + self._box_type

        # To support previous version of AddThis container naming convention
        if self._box_type == 'addthis_inline_share_toolbox':
            self._box_type += ' addthis_sharing_toolbox'

        self._url = kwargs.get('url')

        self._css += ' widget-addthis'

        _assetman.preload('//s7.addthis.com/js/300/addthis_widget.js#pubid=' + self._pub_id)

    def _get_element(self, **kwargs) -> _html.Element:
        """Get HTML element of the widget
        """
        div = _html.Div(css=self._box_type)

        if self._url:
            div.set_attr('data_url', self._url)
        if self._title:
            div.set_attr('data_title', self._title)

        return div
