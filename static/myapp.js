function reformat() {

    // Calling all the buttons
    let cnt_bk = document.getElementById("cnt_bk");
    let contact = document.getElementById("contact");
    let mail = document.getElementById("mail");
    let lnk_to_pro = document.getElementById("lnk_to_pro");
    let pro_lnk = document.getElementById("pro_lnk");
    let not = document.getElementById("not");
    let not_txt = document.getElementById("not_txt");
    let bg_img = document.getElementById("bg-img");
    let results = document.getElementById("results");
    let chrt = document.getElementById("chrt");
    let pred = document.getElementById("pred");
    let ext = document.getElementById("ext");
    // Finished 

    // CSS changes 
    ext.style.top = "85%";
    cnt_bk.style.top = "160%";
    contact.style.top = "160%";
    mail.style.top = "173%";
    lnk_to_pro.style.top = "160%";
    pro_lnk.style.top = "173%";
    not.style.top = "160%";
    not_txt.style.top = "170%";
    bg_img.style.height = "180%";
    results.style.display = "block";
    chrt.style.display = "block";
    pred.style.display = "block";
    // Finished

    let dat = $("form").serializeArray();
    console.log(dat);
    dat = {"fro" : dat};
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

    // Animating Scroll
    $('html, body').animate({
        'scrollTop': $("#results").position().top
    }, 1000);
    // Finished
}