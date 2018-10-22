import assetman from '@pytsite/assetman';
import setupWidget from '@pytsite/widget';

setupWidget('plugins.addthis._widget.AddThis', widget => {
    assetman.loadJS('//s7.addthis.com/js/300/addthis_widget.js#pubid=' + widget.data('pubId'))
});
