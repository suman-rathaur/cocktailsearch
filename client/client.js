function onClickedSearch() {
    var cocktail = document.getElementById("uicocktail").value; // Get value from input
    document.getElementById("uiEstimatedBars").style.display = "block"; // Show the result


    var estBars = document.getElementById("uiEstimatedBars");
    var url = "http://127.0.0.1:5000/search";

    $.post(url, {
        cocktail: cocktail,
    }, function(data, status) {
        console.log(data.estimated_bar);
        estBars.innerHTML = "<h2>" + data.estimated_bar.toString() + "</h2>"; // Correct the HTML insertion
        console.log(status);
    });


}