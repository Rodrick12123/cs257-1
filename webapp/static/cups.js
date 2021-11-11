/*
cups.js
Rodrick and Thea
10 November 2021
*/

window.onload = initialize;

function initialize() {
    //loadYearsSelector();

    loadWorldCupCheckBoxes();

    /*    let element = document.getElementById('year_selector');
    if (element) {
	element.onchange = onYearsSelectionChanged;
	} */   
}

function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

/*

function loadYearsSelector() {
    let url = getAPIBaseURL() + '/Allcups/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(worldcups) {
	    let selectorBody = '';
	    for (let k = 0; k < worldcups.length; k++) {
		let worldcup = worldcups[k];
		selectorBody += '<option value="' + worldcup['id'] + '">'
                                + worldcup['wc_location'] + ' ' + worldcup['wc_year']
		+ '</option>\n';
	    }

	    let selector = document.getElementById('year_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	});
}
*/



function loadWorldCupCheckBoxes() {
    let url = getAPIBaseURL() + '/Allcups/';

    fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(worldcups) {
		let checkBoxesBody = '';
		for (let k = 0; k < worldcups.length; k++) {
		    let worldcup = worldcups[k];
		    world_cup_year = worldcup['wc_year']
		    world_cup_location = worldcup['wc_location']
		    checkBoxesBody += '<input type="checkbox" name="worldcup" id="'
			+world_cup_year + '" value="' + world_cup_year + '">\n'
			+'<label for ="' + world_cup_year + '">' + world_cup_location+' '+world_cup_year
			+ '</label>\n'

		}

		let boxes = document.getElementById('check_boxes_container');
		if (boxes) {
		    boxes.innerHTML = checkBoxesBody;
		}
	    })

        .catch(function(error) {
                console.log(error);
	    });
}


function dataSelect(evt) {

    let years = localStorage.getItem("year");
    if(evt.id === "Players"){
        alert("coming Soon")
    }
    if(evt.id === "Teams"){
        alert("coming Soon")
    }
    if(evt.id === "Stats"){
        alert("coming Soon")
    }
    if(evt.id === "p3"){
        
        if (evt.value === "All team queries") {
            teams = 'all'
            //loadAllTeams()
            if (evt.value === "All player queries"){
                //loadAllPlayers(teams);
            }

        }
    }
    //NEED TO FIGURE OUT HOW TO GET YEARS
    if(evt.id === "p2"){
        if (evt.value === "All team queries") {
            teams = 'all'
            //loadTeamYear(years)
            if (evt.value === "All player queries"){
                //loadAllPlayers(teams);
            }
        }
    }
    
    
    // let element = document.getElementById('data');
    // if (element) {
    //     alert('hello');
    //     //element.onchange = onAuthorsSelectionChanged;
    // }

}
function loadAllTeams() {
    window.location.href="/mockup3";
    let url = getAPIBaseURL() + '/Allcups/teams/';

    // Send the request to the teamss API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(teams) {
        // Add the <option> elements to the <select> element
        let tableBody = '';
        for (let k = 0; k < teams.length; k++) {
            let teams = teamss[k];
            tableBody += '<tr>'
                            + '<td>' + teams['coach'] + '</td>'
                            + '<td>' + teams['teamname'] + '</td>'
                            + '<td>' + teams['year'] + '</td>'
                            + '</tr>\n';
        }

        let res = document.getElementById('results');
        if (res) {
            res.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function loadTeamYear(years) {
    window.location.href="/mockup2";
    let url = getAPIBaseURL() + '/<years>/teams/';

    // Send the request to the teamss API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(teams) {
        // Add the <option> elements to the <select> element
        let tableBody = '';
        for (let k = 0; k < teams.length; k++) {
            let teams = teamss[k];
            tableBody += '<tr>'
                            + '<td>' + teams['coach'] + '</td>'
                            + '<td>' + teams['teamname'] + '</td>'
                            + '<td>' + teams['year'] + '</td>'
                            + '</tr>\n';
        }

        let res = document.getElementById('results');
        if (res) {
            res.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function loadAllPlayers(teams) {
    if(teams == 'all'){
        teams = [1930,1934,1938,1950,1954,1958,1962,1966,
            1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014]
    }
    window.location.href="/mockup2";
    let url = getAPIBaseURL() + '/<teams>/players/';

    // Send the request to the teamss API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(teams) {
        // Add the <option> elements to the <select> element
        let tableBody = '';
        for (let k = 0; k < teams.length; k++) {
            let teams = teamss[k];
            tableBody += '<tr>'
                            + '<td>' + teams['coach'] + '</td>'
                            + '<td>' + teams['teamname'] + '</td>'
                            + '<td>' + teams['year'] + '</td>'
                            + '</tr>\n';
        }

        let res = document.getElementById('results');
        if (res) {
            res.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function valGetter() {
    yrs = yearGetter()
    if(yrs.includes("all")){
        
        loadAllTeams();
    }else{
        if(yrs.length != 0){
            loadTeamYear(yrs)
        }
        else{
            alert("You Must Print Something")
        }
    }
}

function yearGetter() {  

    let years = [];
    checkboxes = document.getElementsByName('worldcup');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        
        if(checkboxes[i].checked == true){
            val = checkboxes[i].value;
            years.push(val);
        }
           
    }
        // save data value
    localStorage.setItem("year", years);
    return years;
}

