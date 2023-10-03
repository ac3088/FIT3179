var symbolMap = "js/symbol_map.vg.json";
vegaEmbed('#symbol_map', symbolMap).then(function (result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var deathsBarChart = "js/deaths_barchart.vg.json";
vegaEmbed('#deaths_barchart', deathsBarChart).then(function (result) {

}).catch(console.error);

var costBarChart = "js/cost_barchart.vg.json";
vegaEmbed('#cost_barchart', costBarChart).then(function (result) {

}).catch(console.error);
