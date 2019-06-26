 $(document).ready(function(){



      $.getJSON($SCRIPT_ROOT + '/getData', function(data) {


       var ctx = document.getElementById("myChart").getContext('2d');

                   var mile1Json = data[1];
                   var mile2Json = data[2];

                   var dates = [];
                   var mile1Dates = [];
                   var mile1Times = [];
                   var mile2Dates = [];
                   var mile2Times = [];



                   for (key in mile2Json)
                   {
                        dates.push(key);
                        mile2Times.push(mile2Json[key]);
                   }

                   dates.sort(function(a,b){return new Date(b.date) - new Date(a.date);});

      var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                 datasets: [ {
                      label: '2 Miles',
                      data: mile2Times,
                      backgroundColor: "rgba(255,153,0,0.4)"
                    }],
            },
            options: {
                scales: {
                 xAxes: [{
                    ticks: {
                    autoSkip: false,
                    maxRotation: 90,
                    minRotation: 45
                    },
                    type: 'time',
                    distribution: 'series',
                    time: {
                        unit: 'month'
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Date'
                      }

                    }],
                 yAxes: [{
                      ticks: {
                            suggestedMin: 15
                          },
                      scaleLabel: {
                        display: true,
                        labelString: 'Time (min)'
                      }

                 }]
                }
            }
        });

      });

});

