// window.onload = initialize;

// function initialize() {
//     let element = document.getElementById('dataSelect');
//     if (element) {
//         element.onchange = onAuthorsSelectionChanged;
//     }
// }

function dataSelect(evt) {
    //Figure this out
    yrs = yearGetter();
    alert(yrs)
    if (evt.value === "All team queries" && evt.id === "p3") {
        teams = 'all'
        //loadAllTeams()
    }
    //NEED TO FIGURE OUT HOW TO GET YEARS
    if (evt.id === "p2" && evt.value === "All team queries") {
        //loadTeamYear(years)
    }
    if (evt.value === "All player queries"){
        //loadAllPlayers(teams);
    }
    
    // let element = document.getElementById('data');
    // if (element) {
    //     alert('hello');
    //     //element.onchange = onAuthorsSelectionChanged;
    // }

}
function loadAllTeams() {
    window.location.href="mockup3.html";
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
    window.location.href="mockup2.html";
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
    window.location.href="mockup2.html";
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

// function valGetter() {  
                
//     let years = [];
//     checkboxes = document.getElementsByName('worldcup');
//     for (var i = 0, n = checkboxes.length; i < n; i++) {
        
//         if(checkboxes[i].checked == true){
//             if(checkboxes[i].value == "all"){
//                 loadAllTeams();
//                 // window.location.href="mockup3.html";
//                 return;
//             }else{
//                 val = checkboxes[i].value;
//                 years.push(val);
//             }
//         }
           
//     }
    
//     if (years.length != 0){
//         loadTeamYear(years);
//         //window.location.href="mockup2.html";
//     }
//     else{
//         alert("You Must Print Something")
//     }
// }

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
    return years;
}

