function reformat() {

    let resu = document.getElementById("Shw-Data");
    resu.style.display = "flex";
    let dat = $("form").serializeArray();
    console.log(dat);
    dat = { "fro": dat };
    fetch("/data", {
        method: "POST",
        body: JSON.stringify(dat)
    }).then((result) => {
        return result.json();
    });
    // .then((data) => {
    //     current_speach = data["data"];
    //     // spk("You spoke : " + current_speach);
    //     instruct.innerText = "You spoke : " + current_speach;
    // });

    // Making Chart
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable(
            [['Year', 'Sales', 'Expenses'],
            ['2004', 1000, 400],
            ['2005', 1170, 460],
            ['2006', 660, 1120],
            ['2007', 1030, 540]]
        );

        var options = {
            title: 'Stock Previous Data Graph',
            // curveType: 'function',
            legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('chrt'));

        chart.draw(data, options);
    }
    // Finished
}