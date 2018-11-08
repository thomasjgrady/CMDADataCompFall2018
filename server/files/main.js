var P = Plotly
plot = document.getElementById('plot')

function query(sql, cb) {
    var multiple = 0;
    if (sql.indexOf(';') > -1) multiple = 1;
    var result = axios.get('/sql', {
        params: {sql: sql, multiple: multiple}
    }).then(function (results) {
        if (results.data.error) {
            console.error(results.data.error);
        } else {
            cb(results.data.result);
        }
    })
}

// pro tip: don't use semicolons if you only have one sql statement!
// (it fucks it up)
query('select BURDEN from raw limit 100000', function (result) {
    query = result[0];
    P.newPlot('big_plot', [{
        x: query['BURDEN'],
        type: 'histogram',
        xbins: {start: 0, size: 0.05, end: 5},
    }])
});


var q = 'select BURDEN from raw where REGION = 1;' +
        'select BURDEN from raw where REGION = 2;' +
        'select BURDEN from raw where REGION = 3;' +
        'select BURDEN from raw where REGION = 4';

var xbins = {start: 0, size: 0.05, end: 5};
 
query(q, function (result) {
    // note that result is an array for each query!
    query1 = result[0];
    query2 = result[1];
    query3 = result[2];
    query4 = result[3];
    P.newPlot('plot1', [{
        x: query1['BURDEN'],
        type: 'histogram',
        xbins: xbins,
    }], {title: 'Region 1'})

    P.newPlot('plot2', [{
        x: query2['BURDEN'],
        type: 'histogram',
        xbins: xbins,
    }], {title: 'Region: 2'})

    P.newPlot('plot3', [{
        x: query3['BURDEN'],
        type: 'histogram',
        xbins: xbins,
    }], {title: 'Region: 3'})

    P.newPlot('plot4', [{
        x: query4['BURDEN'],
        type: 'histogram',
        xbins: xbins,
    }], {title: 'Region: 4'})
});
