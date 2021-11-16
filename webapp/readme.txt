AUTHORS: Rodrick Lankford and Thea Traw

DATA: Our data is about all of the World Cups from 1930-2014, and it includes data about teams, players, matches, and the World Cups themselves. 

FEATURES CURRENTLY WORKING:
- Can choose All Cups checkbox on home page and it takes you to the All Cups page (where all teams that have competed in any World Cup appear in dropdown)
- On All Cups page, can choose a team, which takes you to the team's All Time page
- On team's All Time Page, World Cups that the team competed in load into dropdown
- Can choose a World Cup and that takes you to a page about the specific team in a specific World Cup (where the team's roster loads into a dropdown)
- Home button in nav bar takes you to home page
- Queries for "Teams that won gold medals" are working endpoints

FEATURES NOT YET WORKING:
- Cannot yet ask queries specific to the page through the select box (most api endpoints are written, but they don't display anything yet)
- From home page to a specific World Cup page, the latter does not load right 
- Help button in navbar takes you to api/help right now, but will take you to better instructions/something more helpful later
- Queries to get the amount of medals a team has needs to be fixed
- The query that loads all the cups a specified team participated needs to be fixed (broke in merge).
- titles for pages also broke

Other notes:
- realize that carrying variables in the url is not particularly security-friendly, will be keeping in mind for revision
- also realize that the end-point design is not very clean, also will definitely changed
