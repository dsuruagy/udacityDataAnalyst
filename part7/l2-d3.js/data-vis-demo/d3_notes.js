d3.select('.main').html(undefined);
var svg = d3.select('.main').append('svg');
svg.attr('width',600).attr('height', 300);

var y = d3.scale.linear().domain([15, 90]).range([250, 0]);
var x = d3.scale.log().domain([250, 100000]).range([0, 600]);
var r = d3.scale.sqrt().domain([52070,1380000000]).range([10,40]);

svg.append('circle').attr('cx', x(13330)).attr('cy', y(77)).attr('r', r(1380000000)).attr('fill', 'red');