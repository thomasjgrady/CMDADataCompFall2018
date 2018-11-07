var P = Plotly
plot = document.getElementById('plot')

function query(sql, cb) {
    var result = axios.get('/sql', {
        params: {sql: sql}
    }).then(function (results) {
        cb(results.data.result)
    })
}

x = []
for (var i = 0; i < 500; i ++) {
    x[i] = Math.random();
}

query('select BURDEN from raw limit 1000', function (result) {
    console.log(result);
    P.newPlot('plot', [{
        x: result['BURDEN'],
        type: 'histogram',
        xbins: {start: 0, size: 0.05, end: 5},
    }])
});
