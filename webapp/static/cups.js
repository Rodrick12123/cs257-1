/*
cups.js
Rodrick and Thea
10 November 2021
*/

window.onload = initialize;

function initialize() {

    loadWorldCupCheckBoxes();    

    loadTeamsSelector();
    
    loadWorldCupsSelector();
    
    //loadSpecificTeamsSelector();
    
    loadPlayersSelector();

    loadPageTitle();
    

    let element = document.getElementById('team_selector');
    if (element) {
        element.onchange = onTeamsSelectionChanged;
    }
    

    let wc_element = document.getElementById('world_cup_selector');
    if (wc_element) {
        wc_element.onchange = onWorldCupsSelectionChanged;
    }
    
    /*
    let specific_team_element = document.getElementById('specific_team_selector');
    if (specific_team_element) {
        specific_team_element.onchange = onSpecificTeamsSelectionChanged;
    }
    
   

    

    let wc_queries = document.getElementById('p2');
    if (wc_queries) {
	wc_queries.onchange = onWCQueriesSelectionChanged;
    }
    
    */
  

}

function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function getBaseURL() {
let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/';
    return baseURL;
}    

function getParam(param){
    return new URLSearchParams(window.location.search).get(param);
}

function checkAll() {
    var boxes = document.getElementsByName('worldcup');
    currentState = boxes[0].checked;
    for (var i=0;i<boxes.length;i++) {
        if (boxes[i].type == "checkbox" ) {
	    
            if(currentState){
                boxes[i].checked = true;
            }else
                boxes[i].checked = false;
            }
    }
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
			+ '</label><br>'

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
    if (getParam('year') != null) {

    if (getParam('year').includes('all')) {

	let url = getAPIBaseURL() + '/Allcups/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let selectorBody = '<option selected>Countries</option>';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		if (team['team_name'] != '') {
		selectorBody += '<option value="' + team['id'] + '">'
                                + team['team_name'] + ' (' + team['team_abbreviation'] +')'
		                + '</option>/n';
		}}
	    let selector = document.getElementById('team_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }

	})

	.catch(function(error) {
		console.log(error);
	    });
    
    }

    else {
	allyears = getParam('year').split(',');
	for (i = 0; i < allyears.length; i++) {
	
	    year = allyears[i];
		let url = getAPIBaseURL() + '/' + year + '/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let selectorBody = '<option selected>Countries</option>';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		if (team['team_name'] != '') {
		selectorBody += '<option value="' + team['team_id'] + '">'
                                + team['year'] + ' ' + team['team_name'] + ' (' + team['team_abbreviation'] +')'
		                + '</option>/n';
		}}
	
	    let selector = document.getElementById('team_selector');
	    if (selector) {
		selector.innerHTML += selectorBody;
	    }

	})

	.catch(function(error) {
		console.log(error);
	    });
    }
    
	    }

    }

}

function onTeamsSelectionChanged() {
    let teamID = this.value;
    let url = getBaseURL() + 'AllCups/Team?team=' + teamID;
   
    window.location = url;
}



function loadPageTitle() {



   if (getParam('team') == null && getParam('year') != null) {

       let url = getAPIBaseURL() + '/Allcups/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(years) {

	    let titleBody = '';

	    if (!getParam('year').include('all')) {

	    for (let k = 0; k < years.length; k++) {
		let year = years[k];
		if (year['id'] == getParam('year')){
		titleBody += year['year'] + ' ' +year['location']+' World Cup';
		}
	    }
	    }
	    else {
		titleBody = "All World Cups";
	    }

	    let title = document.getElementById('page-title');
	    if (title) {
		title.innerHTML = titleBody;
	    }
	})
	
	.catch(function(error) {
		console.log(error);
	    });
}






    if (getParam('team') != null && getParam('year') == null) {

    let url = getAPIBaseURL() + '/Allcups/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let titleBody = '';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		if (team['id'] == getParam('team')){
		titleBody += team['team_name'] + ' - All World Cups';
		}
	    }


	    let title = document.getElementById('page-title');
	    if (title) {
		title.innerHTML = titleBody;
	    }
	})
	
	.catch(function(error) {
		console.log(error);
	    });
}

   if (getParam('team') != null && getParam('year') != null) {

       let url = getAPIBaseURL() + '/'+getParam('year')+'/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let titleBody = '';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		if (team['team_id'] == getParam('team') && team['wc_id'] == getParam('year')){
		titleBody += team['team_name'] + ' in the '+team['year']+' World Cup';
		}
	    }


	    let title = document.getElementById('page-title');
	    if (title) {
		title.innerHTML = titleBody;
	    }
	})
	
	.catch(function(error) {
		console.log(error);
	    });
}





}


function onWCQueriesSelectionChanged() {

    let url = getAPIBaseURL() + 'Allcups/attendance';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(attendances) {
	    let resultsBody = '<table><tr><th>World Cup</th><th>Attendance</th>';
	    for (let k = 0; k < attendances.length; k++) {
		let attendance = attendances[k];
		resultsBody += '<tr><td>'+attendance['year']+'</td><td>'
		    + attendance['attendance'] +'</td>';
		}
	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = selectorBody;
	    }

	})

	.catch(function(error) {
		console.log(error);
	    });

}

function loadSpecificTeamsSelector() {

    //need to get <year> from home page when sending to this page
    let url = getAPIBaseURL() + '/<year>/teams/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams) {
	    let selectorBody = '<option selected>Countries</option>';
	    for (let k = 0; k < teams.length; k++) {
		let team = teams[k];
		if (team['team_name'] != '') {
		selectorBody += '<option value="' + team['id'] + '">'
                                + team['team_name'] + ' (' + team['team_abbreviation'] +')'
		                + '</option>/n';
		}}
	    let selector = document.getElementById('team_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }

	})

	.catch(function(error) {
		console.log(error);
	    });
}

/*
function onSpecificTeamsSelectionChanged() {
    let teamID = this.value;
    let url = getBaseURL() + 'AllCups/Team?team=' + teamID;
   
    window.location = url;
}
*/




function loadWorldCupsSelector() {

    if (getParam('team') != '') {

	let url = getAPIBaseURL() + '/Allcups/'+getParam('team')+'/cups';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(worldcups) {
	    let selectorBody = '<option selected>World Cups</option>';
	    for (let k = 0; k < worldcups.length; k++) {
		let worldcup = worldcups[k];
		//going to need to put 'id' as a return of the query, ok for now
		selectorBody += '<option value="' + worldcup['id'] + '">'
                                + worldcup['wc_location'] + ' ' + worldcup['wc_year']
		                + '</option>/n';
	    }

	    let selector = document.getElementById('world_cup_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}
}


function onWorldCupsSelectionChanged() {
    let worldcupID = this.value;
    let teamID = getParam('team');
    let url = getBaseURL() + 'SpecificCups/Team?year='+ worldcupID+'&team='+teamID;
   
    window.location = url;
}



function loadPlayersSelector() {

    if (getParam('team') != null && getParam('year') != null) {

	let url = getAPIBaseURL() + '/'+getParam('year')+'/'+getParam('team')+'/roster';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let selectorBody = '<option selected>Players</option>';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		selectorBody += '<option value="' + player['id'] + '">'
                                + player['surname'] + ', ' + player['given_name']
		                + '</option>/n';
	    }

	    let selector = document.getElementById('player_selector');
	    if (selector) {
		selector.innerHTML = selectorBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}
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

            loadAllTeams()

        }
        if (evt.name === "tselct"){
            // window.location.href="/CupsParticipated";
            tms = teamGetter()
            loadTeamCups(tms)
        }
        if (evt.value === "Teams that won gold medals"){
            loadGoldMedals()
        }
        if (evt.value === "Number of Medals Teams Won"){
            loadMedalCount()
        }
    }


    if(evt.id === "p2"){
        if (evt.value === "Teams that won gold medals") {            
            loadGoldMedals(years)
        }
        if (evt.value === "Number of Medals Teams Won"){
            loadMedalCount(years)
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

function loadMedalCount(years=Null) {
    let url = getAPIBaseURL() + '/medals?years=' + years;
    
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
        tableBody = '<tr>'
                    + '<TH>'+ 'Worldcup' +'</TH>'
                    + '<TH>'+ 'Team Name' +'</TH>'
                    + '<TH>'+ 'Number Of Medals' +'</TH>'
                    + '</tr>\n';
        for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            // <td><input type="checkbox" name="brand">Apple</td>
        
            tableBody +=   
                            '<tr ALIGN="CENTER">'
                            + '<td>' + team['Worldcup'] + '</td>'
                            + '<td>' + team['Team Name'] + '</td>'
                            + '<td>' + team['Medals'] + '</td>'
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

function loadGoldMedals(years=Null){
    

    let url = getAPIBaseURL() + '/gold/teams?years=' + years;
    
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
        tableBody = '<tr>'
                    + '<TH>'+ 'Abbreviation' +'</TH>'
                    + '<TH>'+ 'Team Name' +'</TH>'
                    + '<TH>'+ 'Worldcups' +'</TH>'
                    + '</tr>\n';
        for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            // <td><input type="checkbox" name="brand">Apple</td>
            
            tableBody +=    '<tr ALIGN="CENTER">'
                            + '<td>' + team['Abbreviation'] + '</td>'
                            + '<td>' + team['Team Name'] + '</td>'
                            + '<td>' + team['Worldcup'] + '</td>'
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
    let cLength = localStorage.getItem("checkLength");
    if((yrs.length +1) == cLength){
        //Put links here
        window.location.href="/AllCups";
        loadAllTeams();
    }else{
        if(yrs.length != 0){
            window.location.href="/SpecificCups?year="+yrs;

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
    localStorage.setItem("checkLength", checkboxes.length);
    
    return years;
}

