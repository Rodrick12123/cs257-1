AUTHORS: Rodrick Lankford and Thea Traw

DATA: Our data is about all of the World Cups from 1930-2014, and it includes data about teams, players, matches, and the World Cups themselves. 

You can get our data from Kaggle @ https://www.kaggle.com/abecklas/fifa-world-cup?select=WorldCupPlayers.csv
Our background image is from https://www.istockphoto.com/vector/football-ground-field-vector-illustration-gm978332866-265920605

FEATURES CURRENTLY WORKING:
- You can select any combination of World Cups from the checkboxes on the home page (one, many, or if you choose All Cups, all checkboxes are automatically filled for you)
- If you choose just one World Cup, you are taken to a page that loads into a drop down all of the teams that competed in that World Cup
- Depending on the field chosen in the teams dropdown (either a specific team or 'teams') you can click a button that gives you the roster (if you chose a team), the top 10 goal scorers (either of all teams or your chosen one), and the matches played (either all matches or just the ones with your team)
- These results get printed onto the screen
- If you had chosen many World Cups on the home page, then you are taken to a different page, where all the teams that have competed in any of those selected World Cups are loaded into a drop down
- The years you selected are also loaded into a dropdown, and they reflect your teams dropdown selection (if you choose a team that only competed in one of those WCs, then the years dropdown will only display that one year)
- You can use these dropdowns as filters
- If you choose one of the options in the medals dropdown and click the 'medal data' button, the corresponding results will print
- You can get the top 10 scorers over all the WCs you chose (if you don't select a team) or for a list for a specific team across those WCs
- You can also see the attendance of the World Cups (either for all years or for a specific one you choose)
- The match results button depends on the team (or no team) that you select as well as the year (or no year) that you select, and then it prints out the corresponding results
- There is also a home button (the page logo) 
- There's also a help button (a question mark) that takes you to the api doc

FEATURES NOT YET WORKING:
- The Kaggle data had weird issues with some special characters in names, and so there are replacement symbols in our data that end up getting displayed---this would have to get manually fixed
- The aesthetic of the website could definitely be nicer
- Printing out the resulting data into a table could be displayed in a prettier way than just text onto the screen

Other notes:
- With more time, we would have made a player page where you could look at individual players and ask questions about them
- We also would implement more questions that the user could ask the data
