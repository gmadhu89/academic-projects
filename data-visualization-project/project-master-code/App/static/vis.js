var genre_list = ['Fighting', 'Strategy', 'Adventure', 'Action', 'Role-Playing', 
'Shooter', 'Platform', 'Action-Adventure', 'MMO', 'Puzzle', 'Sports', 'Racing', 
'Simulation', 'Music', 'Misc'];

var content_rating_list = ['T', 'E10', 'M', 'RP', 'E'];

var platform_list = ['PS3', 'X360', 'PC', 'PS4', 'NS', 'XOne', 'XBL', 'PSN', 'XB', 
'PSV', '3DS', 'WiiU', 'And', 'OSX', 'Linux', 'WW', 'PS', 'SAT', 'NGage', 'iOS', 
'PS2', 'DS', 'Wii', 'PSP', 'N64', 'DC', 'GB', 'DSiW', 'GBA'];

var price_range = [0, 5500];

var top_publisher_list = ["True", "False"];

var expected_rating_list = Array.from(Array(11).keys())

$(document).ready(function() {
  $('select').niceSelect();
});


// Menu Bar Design
d3.select("#input_panel")
.style("background-color","#FAF9F6")
var heading = d3.select("#input_panel")
.append("h3")
.text("What does your game look like?")
var genre = d3.select("#input_panel")
.append("div")
.attr("class","col-12");
genre.append("p").text("Genre:");
genre.append("button").text("Select One");

var platform = d3.select("#input_panel")
.append("div")
.attr("class","col-12")
platform.append("p").text("Platform:");
platform.append("button").text("Select One");


var content_rating = d3.select("#input_panel")
.append("div")
.attr("class","col-12")
content_rating.append("p").text("Content Rating:");
content_rating.append("button").text("Select One");

 
var price = d3.select("#input_panel")
.append("div")
.attr("class","col-12")
price.append("p").text("Price:");
price.append("button").text("Select One");



var publisher = d3.select("#input_panel")
.append("div")
.attr("class", "col-12")

publisher.append("p").text("Is Top Publisher:")

var publisherSelect = publisher.append('select')
    .on('change', function(d) {
        // var select = d3.select("#input_panel").select("select");
        // createMapAndLegend(world, gameData, 
        //     ddSelect.node().options[ddSelect.node().selectedIndex].value);
    })
    // .style("margin-left", "10px");
$('select').niceSelect('destroy');
publisherSelect.selectAll('option')
    .data(top_publisher_list)
    .enter()
    .append('option')
    .attr('value', function(d){ return d; })
    .text(function(d){ return d; })



// function ddKeyChanged(world, gameData) {
//     var ddSelect = d3.select("body").select("#dropdown").select("select");
//     createMapAndLegend(world, gameData,
//             ddSelect.node().options[ddSelect.node().selectedIndex].value);
// }

getPlaytime("Action", "M", "PC", 4000)

function getPlaytime(genre, content_rating, platform, price) {
    fetch('/playtime?genre='+genre
        +'&content_rating='+content_rating
        +'&platform='+platform
        +'&price='+price)
    .then(function(response) {
        return response.json();
    }).then(function(text) {
        console.log(text)
    });
}

getSales("na", 1.0, 8, "True")

function getSales(region, year_since_release, expected_rating, is_top_publisher) {
    fetch('/sales?region='+region+'&year_since_release='+year_since_release+'&expected_rating='+expected_rating+'&is_top_publisher='+is_top_publisher)
    .then(function(response) {
        return response.json();
    }).then(function(text) {
        console.log(text)
    });
}
