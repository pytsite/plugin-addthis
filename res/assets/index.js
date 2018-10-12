const assetman = require('@pytsite/assetman');

require('@pytsite/widget').onWidgetLoad('plugins.addthis._widget.AddThis', (widget) => {
    assetman.loadJS('//s7.addthis.com/js/300/addthis_widget.js#pubid=' + widget.data('pubId'))
});
