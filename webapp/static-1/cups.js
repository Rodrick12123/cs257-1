/*
cups.js
Rodrick and Thea
10 November 2021
*/

window.onload = initialize;

function initialize() {

    loadWorldCupCheckBoxes();

    

    // loadTeamsSelector();

    // let element = document.getElementById('team_selector');
    // if (element) {
    //     element.onchange = onTeamsSelectionChanged;
    // }
    


}

function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}


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

function loadTeamsSelector() {
    let url = getAPIBaseURL() + '/Allcups/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let selectorBody = '';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		//going to need to put 'id' as a return of the query, ok for now
		selectorBody += '<option value="' + team['id'] + '">'
                                + team['team_name'] + ' (' + team['team_abbreviation'] +')'
		                + '</option>\n';
	    }

	    let selector = document.getElementById('team_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}

function onTeamsSelectionChanged() {
    let teamID = this.value;
    let url = getAPIBaseURL() + '/books/author/' + teamID;

    fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(books) { //what is this query going to ask??????
		let tableBody = '';
		for (let k = 0; k < books.length; k++) {
		    let book = books[k];
            tableBody += '<tr>'
                            + '<td>' + book['title'] + '</td>'
                            + '<td>' + book['publication_year'] + '</td>'
		+ '</tr>\n';
		}

    let booksTable = document.getElementById('books_table');
    if (booksTable) {
	booksTable.innerHTML = tableBody;
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
            loadAllTeams()
            if (evt.value === "All player queries"){
                //loadTeamCups(teams);
            }

        }
        if (evt.name === "tselct"){
            // window.location.href="/CupsParticipated";
            tms = teamGetter()
            loadTeamCups(tms)
        }
    }


    if(evt.id === "p2"){
        if (evt.value === "All team queries") {
            teams = 'all'
            //loadTeamYear(years)
            if (evt.value === "All player queries"){
                //loadTeamCups(teams);
            }
        }
    }

}

function teamGetter() {
    let teams = [];
    
    checkboxes = document.getElementsByName('team');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        
        if(checkboxes[i].checked == true){

            val = checkboxes[i].value;
            
            teams.push(val);
        }
           
    }
        // save data value
    localStorage.setItem("teams", teams);
    return teams;
}
function loadAllTeams() {
    
    
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
        for (let k = 1; k < teams.length; k++) {
            let team = teams[k];
            // <td><input type="checkbox" name="brand">Apple</td>
            var checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = 'car';
            checkbox.name = 'interest';
            checkbox.value = 'car';
            tableBody += '<tr>'
                            + '<td>' + team['team_name'] + '</td>'
                            + '<td>' + team['team_abbreviation'] + '</td>'
                            + '<td>' + '<input type="checkbox" name="team"  id="'
                            + team['team_abbreviation'] + '" value="' + team['team_name'] + '">'+ '<td>'
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
    
    // let url = getAPIBaseURL() + '/<years>/teams/';
    let url = getAPIBaseURL() + '/' + years + '/teams/';
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
            let team = teams[k];
            tableBody += '<tr>'
                    
                            + '<td>' + team['teamyear'] + '</td>'
                            + '<td>' + team['team_abbreviation'] + '</td>'
                            + '<td>' + team['team_name'] + '</td>'
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

function loadTeamCups(teams) {
    
    let url = getAPIBaseURL() + '/cups/' + teams;
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
            let team = teams[k];
            tableBody += '<tr>'
                            + '<th>' + "World Cups"+'</th>'
                            + '<td>' + team['Worldcup'] + '</td>'
                            + '<th>' + "Team Name"+'</th>'
                            + '<td>' + team['Team Name'] + '</td>'
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
        //Put links here
        window.location.href="/AllCups";
        loadAllTeams();
    }else{
        if(yrs.length != 0){
            window.location.href="/SpecificCups";

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

