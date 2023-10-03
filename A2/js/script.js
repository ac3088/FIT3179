var symbolMap = "js/symbol_map.vg.json";
vegaEmbed('#symbol_map', symbolMap).then(function (result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var deathsBarchart = "js/deaths_barchart.vg.json";
vegaEmbed('#deaths_barchart', deathsBarchart).then(function (result) {

}).catch(console.error);

var costBarchart = "js/cost_barchart.vg.json";
vegaEmbed('#cost_barchart', costBarchart).then(function (result) {

}).catch(console.error);

var affectedScatterplot = "js/affected_scatterplot.vg.json";
vegaEmbed('#affected_scatterplot', affectedScatterplot).then(function (result) {

}).catch(console.error);

var regionPiechart = "js/region_piechart.vg.json";
vegaEmbed('#region_piechart', regionPiechart).then(function (result) {

}).catch(console.error);

var dtypePieChart = "js/dtype_piechart.vg.json";
vegaEmbed('#dtype_piechart', dtypePieChart).then(function (result) {

}).catch(console.error);