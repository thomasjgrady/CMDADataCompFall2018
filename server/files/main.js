var P = Plotly
plot = document.getElementById('plot')
scat = document.getElementById('scatter')

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

var data = []

query('select BURDEN from raw where REGION = 1 limit 1000', function (result) {
    console.log(result);
    data [0] = {
        x: result['BURDEN'],
        type: 'histogram',
        opacity: 0.5,
        markers: {
            color: 'red'
        },
        xbins: {start: 0, size: 0.05, end: 2}
    };

});

query('select BURDEN from raw where REGION = 2 limit 1000', function (result) {
    console.log(result);
    data [1] = {
        x: result['BURDEN'],
        type: 'histogram',
        opacity: 0.5,
        markers: {
            color: 'green'
        },
        xbins: {start: 0, size: 0.05, end: 2}
    };
});

query('select BURDEN from raw where REGION = 3 limit 1000', function (result) {
    console.log(result);
    data [2] = {
        x: result['BURDEN'],
        type: 'histogram',
        opacity: 0.5,
        markers: {
            color: 'blue'
        },
        xbins: {start: 0, size: 0.05, end: 2}
    };
});

query('select BURDEN from raw where REGION = 4 limit 1000', function (result) {
    console.log(result);
    data [3] = {
        x: result['BURDEN'],
        type: 'histogram',
        opacity: 0.5,
        markers: {
            color: 'yellow'
        },
        xbins:{ start: 0, size: 0.05, end: 2}
    };
});

var layout = {barmode: 'overlay'};
console.log(data);

P.newPlot('scatter', data, layout);
