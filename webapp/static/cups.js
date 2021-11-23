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
    displayStats();
    
    //loadWorldCupsSelector();
    
    //loadSpecificTeamsSelector();
    
    //loadPlayersSelector();

    loadPageTitle();

    //loadTeamYear();
    

    
     let element = document.getElementById('team_selector');
     if (element) {
         element.onchange = onTeamsSelectionChanged;
     }

    /*
    let wc_element = document.getElementById('world_cup_selector');
    if (wc_element) {
        wc_element.onchange = onWorldCupsSelectionChanged;
    }
    */
    
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
    /*
    let roster_button = document.getElementById('roster');
    if (roster_button) {
	roster_button.onchange = onRosterButtonPressed;
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

function loadTeamsSelector(cups=null) {
  
    if (getParam('year') != null) {
        allyears = getParam('year').split(',');
        // alert(cups)
        let url = getAPIBaseURL() + '/' + allyears + '/teams/';
        if(cups != null){
            url = getAPIBaseURL() + '/' + cups + '/teams/';
        }
            

        fetch(url, {method: 'get'})

        .then((response) => response.json())

        .then(function(teams) {
            let selectorBody = '<option value = "Teams" selected>Teams</option>';
            for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            if (team['team_name'] != '') {
                selectorBody += '<option value="' + team['team_name'] + '">'
                                        + team['team_name'] + ' (' + team['team_abbreviation'] +')'
                                + '</option>/n';
                }
            }
        
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

function onTeamsSelectionChanged() {
    let teamName = this.value;
    /*
    let url = getBaseURL() + 'OneCup?year='+getParam('year')+'&team=' + teamID;
    */
    window.team_selected = teamName;

    //window.location = url;
}



function loadPageTitle() {


   if (getParam('year') != null) {

       let url = getAPIBaseURL() + '/Allcups/';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(worldcups) {

	    let titleBody = '';
	    
	    allyears = getParam('year').split(',');

	    if (allyears.length == 20) {
		titleBody = "All World Cups (1930-2014)";
	    }
	    else {
		done = 0;
	    for (let k = 0; k < worldcups.length; k++) {
		let worldcup = worldcups[k];

		if (allyears.includes(worldcup['wc_year'].toString())){
		  titleBody += worldcup['wc_location'] + ' ' +worldcup['wc_year'];
		  if (done < allyears.length - 1) {
		  titleBody += ' - '; 
		  }
		  done ++;
		  }
	    }
	    }

	    //remove extra characters at end of title
	    //figure out how to do dot character
	    //	    titleBody = titleBody[:-3];
	    

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
    /*
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
    */





}


function displayStats() {
    let url = getAPIBaseURL() + '/medals/'+getParam('year')+'/';

    fetch(url, {method: 'get'})

	.then((response) => response.json())

	.then(function(medals) {
		let medalsBody = '';
		for (let k = 0; k < medals.length; k++) {
		    let medal = medals[k];
		    first = medal['firstplace'];
		    second = medal['secondplace'];
		    third = medal['thirdplace'];
		    medalsBody += '<tr>' + 
			          '<td>' + first + '</td>'
			          + '<td>' + second+'</td>'
			          + '<td>'+third+'</td>'
			          + '</tr>';

		}

		let table = document.getElementById('medals_table');
		if (table) {
		    table.innerHTML += medalsBody;
		}
	    })

        .catch(function(error) {
                console.log(error);
	    });
}




function onRosterButtonPressed() {
    
	if (window.team_selected != null && window.team_selected != 'Teams') {
	let url = getAPIBaseURL() + '/'+getParam('year')+'/'+window.team_selected+'/roster';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let rosterBody = '';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		rosterBody += '<tr><td>'
                                + player['surname'] + ', ' + player['given_name']
		                + '</td></tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = rosterBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}

else {
    alert('Please choose a team!');
}

}



function onGoalsButtonPressed() {
    if (window.team_selected != null && window.team_selected != 'Teams') {
	let url = getAPIBaseURL() + '/allmatches/goals?team='+window.team_selected+'&year='+getParam('year');

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let scorersBody = '<tr><th>Player</th><th>Goal Count</th></tr>';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		scorersBody += '<tr><td>'
                                + player['surname'] + ', ' + player['given_name']
		                + '</td><td>' + player['goals'] + '</td></tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = scorersBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}

else {
    	let url = getAPIBaseURL() + '/allmatches/goals?year='+getParam('year');

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let scorersBody = '<tr><th>Player</th><th>Goal Count</th></tr>';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		scorersBody += '<tr><td>'
                                + player['surname'] + ', ' + player['given_name']
		                + '</td><td>' + player['goals'] + '</td></tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = scorersBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });

}

}





function onManyGoalsButtonPressed() {
    if (window.team_selected != null && window.team_selected != 'Teams') {

	let url = getAPIBaseURL() + '/allmatches/goals?team='+window.team_selected+'&year='+getParam('year');

	fetch(url, {method: 'get'})

	    .then((response) => response.json())
	    
	    .then(function(players) {

		    let scorersBody = '<tr><th>Player</th><th>Goal Count</th><th>Year</th></tr>';	   

		    for (let k = 0; k < players.length; k++) {
			let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
			scorersBody += '<tr><td>'
			    + player['surname'] + ', ' + player['given_name']
		           + '</td><td>' + player['goals'] + '</td></tr>';
			scorers[scorers.length] = [player['surname'], player['given_name'], player['goals']];
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = scorersBody;
	    }

	  
	})

	.catch(function(error) {
		console.log(error);
	    });
	}



    else if (getParam('year').split(',').length == 20) {
    	let url = getAPIBaseURL() + '/allmatches/goals';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let scorersBody = '<tr><th>Player</th><th>Goal Count</th></tr>';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		scorersBody += '<tr><td>'
                                + player['surname'] + ', ' + player['given_name']
		                + '</td><td>' + player['goals'] + '</td></tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = scorersBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });

}





else {
    	let url = getAPIBaseURL() + '/allmatches/goals?year='+getParam('year');

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(players) {
	    let scorersBody = '<tr><th>Player</th><th>Goal Count</th></tr>';
	    for (let k = 0; k < players.length; k++) {
		let player = players[k];
		//going to need to put 'id' as a return of the query, ok for now
		scorersBody += '<tr><td>'
                                + player['surname'] + ', ' + player['given_name']
		                + '</td><td>' + player['goals'] + '</td></tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = scorersBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });

}

}










function onMatchResultsButtonPressed() {
   if (window.team_selected == null || window.team_selected == 'Teams') {

       let url = getAPIBaseURL() + '/allmatches/'+getParam('year');

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(matches) {
	    let matchesBody = '<tr>' +
                              '<th>Date</th>' +
                              '<th>Stage</th>' +
                              '<th>Stadium</th>' +
		              '<th>City</th>' +
		              '<th>Match-up</th>' +
                              '<th>Result</th>' +		 
		              '</tr>;';
	    for (let k = 0; k < matches.length; k++) {
		let match = matches[k];
		//going to need to put 'id' as a return of the query, ok for now
		matchesBody += '<tr>' +
                               '<td>' + match['date'] + '</td>' +
		               '<td>' + match['stage'] + '</td>' + 
		               '<td>' + match['stadium'] + '</td>' + 
		               '<td>' + match['city'] + '</td>' + 
		               '<td>' + match['home_team'] + ' vs. ' + match['away_team'] + '</td>' +
		               '<td>' + match['home_score'] + ' - ' + match['away_score'] + '</td>' +
		               '</tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = matchesBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}

   else {

       //gets just the matches that a specific team played
       //global variable?

       let url = getAPIBaseURL() + '/allmatches/'+getParam('year')+'?team='+window.team_selected;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(matches) {
	    let matchesBody = '<tr>' +
                              '<th>Date</th>' +
                              '<th>Stage</th>' +
                              '<th>Stadium</th>' +
		              '<th>City</th>' +
		              '<th>Match-up</th>' +
                              '<th>Result</th>' +		 
		              '</tr>;';
	    for (let k = 0; k < matches.length; k++) {
		let match = matches[k];
		//going to need to put 'id' as a return of the query, ok for now
		matchesBody += '<tr>' +
                               '<td>' + match['date'] + '</td>' +
		               '<td>' + match['stage'] + '</td>' + 
		               '<td>' + match['stadium'] + '</td>' + 
		               '<td>' + match['city'] + '</td>' + 
		               '<td>' + match['home_team'] + ' vs. ' + match['away_team'] + '</td>' +
		               '<td>' + match['home_score'] + ' - ' + match['away_score'] + '</td>' +
		               '</tr>';
	    }

	    let results = document.getElementById('results');
	    if (results) {
		results.innerHTML = matchesBody;
	    }
	})

	.catch(function(error) {
		console.log(error);
	    });
}



}



function loadAttendances(years=null) {

    let url = getAPIBaseURL() + '/Allcups/attendance';
    if(years){
        url = getAPIBaseURL() + '/Allcups/attendance?years=' + years;
    }

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(attendances) {
	    let tableBody = '';
        tableBody = '<tr>'
                    + '<TH>'+ 'Attendance' +'</TH>'
                    + '<TH>'+ 'Worldcup' +'</TH>'
                    + '</tr>\n';
        for (let k = 0; k < attendances.length; k++) {
            let attend = attendances[k];
            // <td><input type="checkbox" name="brand">Apple</td>
            
            tableBody +=    '<tr ALIGN="CENTER">'
                            + '<td>' + attend['attendance'] + '</td>'
                            + '<td>' + attend['year'] + '</td>'
                            + '</tr>\n';
        }

        let res = document.getElementById('results');
        if (res) {
            res.innerHTML = tableBody;
        }

	})

	.catch(function(error) {
		console.log(error);
	    });

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




function loadWorldCupsSelector(teams=null) {
    if (getParam('year') != null) {
        allyears = getParam('year').split(',');
        let url = getAPIBaseURL() + '/worldcups/' + allyears + '/' + teams + '/';

        fetch(url, {method: 'get'})

        .then((response) => response.json())

        .then(function(worldcups) {
            let selectorBody = '<option selected>World Cups</option>';
            for (let k = 0; k < worldcups.length; k++) {
            let worldcup = worldcups[k];
            //going to need to put 'id' as a return of the query, ok for now
            selectorBody += '<option value="' + worldcup['Worldcup'] + '">'
                                    + worldcup['Worldcup'] 
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
	    let selectorBody = '<option selected>Roster</option>';
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





function matchResults(){
    let years = getParam('year')
    let tms = localStorage.getItem("team_filter");
    let cups = localStorage.getItem("cup_filter");

    if(cups && tms ){
        alert(cups)
        alert(tms)
        //loadMatches(cups,tms)
    }else{
        if(cups){
            loadMatches(cups)
        }
        if(tms){

            // Wont work with teams
            //loadMatches(years, teams)
            
        }
        if(cups == null && tms == null){
            
            loadMatches(years)
        }
    } 
    localStorage.removeItem("cup_filter");
    localStorage.removeItem("team_filter");
    alert('check')
    //alert(cups)
}

function dataSelect(evt) {
    let years = getParam('year')
    
    
    
    // let cups = null
    // let teams = null
    if(evt.id === "medal_choice"){
        
        localStorage.setItem("medal", evt.value);
    }
    if(evt.id === "team_selector"){
        //alert(evt.value)
        
        if(evt.value != 'Teams'){
            
            localStorage.setItem("team_filter", evt.value);
            
            let teams = localStorage.getItem("team_filter");
            //let element = document.getElementById('world_cup_selector');
            loadWorldCupsSelector(teams)
            // element.value.selected =true;
            // select('world_cup_selector', element.value)
            
        }
    }
    if(evt.id === "world_cup_selector"){
        //alert(evt.value)
     
        if(evt.value != 'World Cups'){
            localStorage.setItem("cup_filter", evt.value);
            let cups = localStorage.getItem("cup_filter");
            //let element = document.getElementById('team_selector');
            loadTeamsSelector(cups);

            // select('team_selector', element.value)
        }
    }
    
    if(evt.id === "match-results"){

        // let teams = localStorage.getItem("team_filter");
        // let cups = localStorage.getItem("cup_filter");

        // if(cups && teams ){
        //     alert('yes')
        //     loadMatches(cups, teams)
        //     localStorage.removeItem("cup_filter");
        //     localStorage.removeItem("team_filter");
        // }else{
        //     if(cups){

        //         loadMatches(cups)
        //         localStorage.removeItem("cup_filter");
        //     }else if(teams){
                
        //         loadMatches(years,teams)
        //         localStorage.removeItem("team_filter");
        //     }else{
        //         loadMatches(years)
        //     }
        // } 
    }
    if(evt.id === "attend"){
        let cups = localStorage.getItem("cup_filter");
        alert('ok')
        alert(cups)
        if(cups){
            loadAttendances(cups)
            localStorage.removeItem("cup_filter");
        }else{
            alert(years)
            loadAttendances(years)
        }
    }

    if(evt.id === "m-data"){
        let cups = localStorage.getItem("cup_filter");
        let medal = localStorage.getItem("medal");
        if(medal){
            if(cups){
                loadMedalData(cups,medal)
                localStorage.removeItem("cup_filter");
            }else{
                loadMedalData(years,medal)
            }
            
        }else{
            if(cups){
                loadMedalData(cups)
                localStorage.removeItem("cup_filter");
            }else{
                loadMedalData(years)
            }
        }
        
    }

    if(evt.id === "p3"){
        
        if (evt.value === "All WC queries") {
            alert('yes')
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


function loadMatches(years,teams=null) {
    
    if(teams){
        alert("teams")
        url = getAPIBaseUrl() + '/matches/' + years +'?teams=' + teams;
    }else{
        url = getAPIBaseURL() + '/matches/' + years;
    }
    // Send the request to the teamss API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())
    
    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    
    .then(function(matches) {
        
        // Add the <option> elements to the <select> element
        let tableBody = '';
        tableBody = '<tr>'
                    + '<TH>'+ 'Worldcup' +'</TH>'
                    + '<TH>'+ 'Date' +'</TH>'
                    + '<TH>'+ 'Stage' +'</TH>'
                    + '<TH>'+ 'Stadium' +'</TH>'
                    + '<TH>'+ 'City' +'</TH>'
                    + '<TH>'+ 'Match-Up' +'</TH>'
                    + '<TH>'+ 'Result' +'</TH>'
                    + '</tr>\n';
        for (let k = 0; k < matches.length; k++) {
            let match = matches[k];
            // <td><input type="checkbox" name="brand">Apple</td>
        
            tableBody +=   
                            '<tr ALIGN="CENTER">' +
                            '<td>' + match['Worldcup'] + '</td>' +
                            '<td>' + match['date'] + '</td>' +
                            '<td>' + match['stage'] + '</td>' + 
                            '<td>' + match['stadium'] + '</td>' + 
                            '<td>' + match['city'] + '</td>' + 
                            '<td>' + match['home'] + ' vs. ' + match['away'] + '</td>' +
                            '<td>' + match['hscore'] + ' - ' + match['ascore'] + '</td>' 
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

function loadMedalData(years, medal=null){
    let url = getAPIBaseURL() + '/medals/' + years + '/';
    if(medal == 'Gold'){
        url = getAPIBaseURL() + '/gold/teams?years=' + years; 
        
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(teams) {
            
            // Add the <option> elements to the <select> element
            let tableBody = '';
        
            tableBody = '<tr>'
                        + '<TH>'+ 'World Cup' +'</TH>'
                        + '<TH>'+ 'Firstplace' +'</TH>'
                        + '<TH>'+ 'Abbreviation' +'</TH>'
                        + '</tr>\n';
            for (let k = 0; k < teams.length; k++) {
                let team = teams[k];
                // <td><input type="checkbox" name="brand">Apple</td>
                
                tableBody +=    '<tr ALIGN="CENTER">'
                                + '<td>' + team['Worldcup'] + '</td>'
                                + '<td>' + team['Team Name'] + '</td>'
                                + '<td>' + team['Abbreviation'] + '</td>'
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
    if(medal == 'Silver'){
        url = getAPIBaseURL() + '/silver/teams?years=' + years; 
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(teams) {
            
            // Add the <option> elements to the <select> element
            let tableBody = '';
        
            tableBody = '<tr>'
                        + '<TH>'+ 'World Cup' +'</TH>'
                        + '<TH>'+ 'Secoundplace' +'</TH>'
                        + '<TH>'+ 'Abbreviation' +'</TH>'
                        + '</tr>\n';
            for (let k = 0; k < teams.length; k++) {
                let team = teams[k];
                // <td><input type="checkbox" name="brand">Apple</td>
                
                tableBody +=    '<tr ALIGN="CENTER">'
                                + '<td>' + team['Worldcup'] + '</td>'
                                + '<td>' + team['Team Name'] + '</td>'
                                + '<td>' + team['Abbreviation'] + '</td>'
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
    
    if(medal == 'Bronze'){
        url = getAPIBaseURL() + '/bronze/teams?years=' + years;
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(teams) {
            
            // Add the <option> elements to the <select> element
            let tableBody = '';
        
            tableBody = '<tr>'
                        + '<TH>'+ 'World Cup' +'</TH>'
                        + '<TH>'+ 'Thirdplace' +'</TH>'
                        + '<TH>'+ 'Abbreviation' +'</TH>'
                        + '</tr>\n';
            for (let k = 0; k < teams.length; k++) {
                let team = teams[k];
                // <td><input type="checkbox" name="brand">Apple</td>
                
                tableBody +=    '<tr ALIGN="CENTER">'
                                + '<td>' + team['Worldcup'] + '</td>'
                                + '<td>' + team['Team Name'] + '</td>'
                                + '<td>' + team['Abbreviation'] + '</td>'
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
    if(medal == null){    
        fetch(url, {method: 'get'})
        .then((response) => response.json())
        .then(function(teams) {
            
            // Add the <option> elements to the <select> element
            let tableBody = '';
        
            tableBody = '<tr>'
                        + '<TH>'+ 'World Cup' +'</TH>'
                        + '<TH>'+ 'Firstplace' +'</TH>'
                        + '<TH>'+ 'Secoundplace' +'</TH>'
                        + '<TH>'+ 'Thirdplace' +'</TH>'
                        + '</tr>\n';
            for (let k = 0; k < teams.length; k++) {
                let team = teams[k];
                // <td><input type="checkbox" name="brand">Apple</td>
                
                tableBody +=    '<tr ALIGN="CENTER">'
                                + '<td>' + team['year'] + '</td>'
                                + '<td>' + team['firstplace'] + '</td>'
                                + '<td>' + team['secondplace'] + '</td>'
                                + '<td>' + team['thirdplace'] + '</td>'
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
}


function loadGoldMedals(years=null){
    

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
    

    //years = getParam('year');

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
    
    // if(yrs[0] == "all"){
    //     alert(yrs[0])
    //     yrs.remove(0)
    //     alert(yrs)
    // }
    // if((yrs.length) == cLength){
    //     //Put links here
    //     window.location.href="/AllCups";
    //     loadAllTeams();
    // }else{
    if(yrs.length == 1){
        window.location.href="/OneCup?year="+yrs;

        loadTeamYear(yrs)
    }else if(yrs.length != 0){
        window.location.href="/ManyCups?year="+yrs;

        loadTeamYear(yrs)
    }else{
        alert("You Must Print Something")
    }
    // }
    
    
}

function yearGetter() {  

    let years = [];
    checkboxes = document.getElementsByName('worldcup');
    for (var i = 0, n = checkboxes.length; i < n; i++) {
        
        if(checkboxes[i].checked == true){
            val = checkboxes[i].value;
            if(val != "all"){
                years.push(val);
            }
        }
    }
    
        // save data value
    localStorage.setItem("year", years);
    localStorage.setItem("checkLength", checkboxes.length);
    
    return years;
}

