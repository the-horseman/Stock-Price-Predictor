function reformat() {
    // Changing the display
    let resu = document.getElementById("Shw-Data");
    let recc = document.getElementById("ppl-wtch");
    recc.style.display = "block";
    resu.style.display = "flex";
    // Changed the display


    // Getting data from site
    let dat = $("form").serializeArray();
    console.log(dat);
    // Got all data from site


    // People Also Watch Started
    let ext1 = { "viewed": String(dat[0].value) };
    fetch("/view", {
        method: "POST",
        body: JSON.stringify(ext1)
    }).then((result) => {
        return result.json();
    }).then((final) => {
        let ex = final["ans"];
        document.getElementById("sugst1").innerText = ex[0][0];
        document.getElementById("sugst2").innerText = ex[1][0];
        document.getElementById("sugst3").innerText = ex[2][0];
        document.getElementById("sugst4").innerText = ex[3][0];
        document.getElementById("sugst5").innerText = ex[4][0];

        document.getElementById("sugst_dat1").innerText = "Return = " + String(ex[0][1]) + "%";
        document.getElementById("sugst_dat2").innerText = "Return = " + String(ex[1][1]) + "%";
        document.getElementById("sugst_dat3").innerText = "Return = " + String(ex[2][1]) + "%";
        document.getElementById("sugst_dat4").innerText = "Return = " + String(ex[3][1]) + "%";
        document.getElementById("sugst_dat5").innerText = "Return = " + String(ex[4][1]) + "%";

    });
    // People Also Watch finished


    // Getting Predictions
    // Got Predictions


    // Getting Graph data
    let arr = [[]];
    ext2 = { "sto": String(dat[0].value), "gra": String(dat[1].value), "tme": String(dat[2].value) };
    fetch("/graph", {
        method: "POST",
        body: JSON.stringify(ext2)
    }).then((result) => {
        return result.json();
    }).then((data) => {
        arr = data["fin_dat"];
        let arr1 = ["Dates", String(dat[1].value)];
        arr.unshift(arr1);
        google.charts.load('current', { 'packages': ['corechart'] });
        google.charts.setOnLoadCallback(drawChart);
    });
    function drawChart() {
        var data = google.visualization.arrayToDataTable(arr);
        var options = {
            title: 'Stock Previous Data Graph',
            // curveType: 'function',
            pointSize: dat[2].value == "1_year" ? 2 : 4,
            legend: { position: 'bottom' },
        };
        var chart = new google.visualization.LineChart(document.getElementById('chrt'));
        chart.draw(data, options);
    }
    // Got Graph Data


    // Scrolling Down
    $('html, body').animate({
        'scrollTop': $("#Shw-Data").position().top
    }, 1000);
    // Finished
}