var symbolMap = "js/symbol_map.vg.json";
vegaEmbed('#symbol_map', symbolMap).then(function (result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var countryBarChart = "js/country_barchart.vg.json";
vegaEmbed('#country_barchart', countryBarChart).then(function (result) {

}).catch(console.error);