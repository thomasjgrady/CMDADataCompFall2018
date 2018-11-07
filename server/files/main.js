var P = Plotly
plot = document.getElementById('plot')

x = []
for (var i = 0; i < 500; i ++) {
        x[i] = Math.random();
}

P.newPlot({
    x: x,
    type: 'histogram',

})
