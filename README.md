# DishFinder

DishFinder is a web application for people who want to upload their favourite recipes and share them with others. Thanks to implementation of voting mechanism, viewers can save time and effort by finding best, most popular recipes with ease.
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user, I want to add new recipes, so I share them with other users.
- As a user, I want to update or delete my old recipes.
- As a user, I want to vote on recipes, so other users know how good/popular is given recipe.
- As a user, I want to know other people's opinion about any given recipe.
- As a user, I want to have an access to quick search option to look for recipes with particular keyword in title.
- As a user, I want to check recipes with particular, available ingredient.
- As a user, I want to visually check how many recipes with certain ingredient are in the database.
- As a user, I want to be able to see which users contributed how many recipes.
- As a user, I want to view all recipes in database.

### Wireframes

Examples of wireframes I've used for this project:
- [All recipes](https://github.com/chookmook29/cookbook/blob/master/wireframes/all.png)
- [Early idea of index page](https://github.com/chookmook29/cookbook/blob/master/wireframes/intro.png)
- [Detailed search](https://github.com/chookmook29/cookbook/blob/master/wireframes/search.png)
- [Single recipe view](https://github.com/chookmook29/cookbook/blob/master/wireframes/single_one.png)

Some concepts of the design and some features changed over time in the development process.

## Database Schema:

![Database Schema](/database_schema/db.png)

More detailed version as [html document](/database_schema/db.html).

## Features

 - Sign in/Register form - allows users to use existing account or create new account, adding to database. Followed by flash message and redirect.
 - Add/edit recipe form - user can create a new recipe, inserting to database or edit existing recipe by updating it.
 - Delete feature  - users that are logged in can delete recipe from database.
 - Filter by ingredient - this will allow the user to be shown all recipes from a specific cuisine which they have chosen from the homepage.
 - Sign Out - user will be logged out from current session, returning to index page while session data being erased.
 
### Existing Features
- Browsing feature - allows users browse recipes, by ingredient or all at once.
- Cookbook feature - allows users to create, delete and update their recipes, register and sign in.
- Voting feature - allows users to vote for or against existing recipes.
- Search feature - allows users to find recipes by using keyword.
- Summary feature - allows user to check who contributed most recipes.

### Features Left to Implement
- Make voting change recipe's position in show_all.html, after summing up negative and positive votes.
- Making popular recipes more exposed to viewers.
- More detailed recipes by adding more fields in database entries.
- More sophisticated search options.

## Technologies Used

- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses some **Bootstrap** elements for more responsive layout.
- [Python](https://www.python.org/)
    - Back-end was written in **Python** .
    - **vnev** library was used in development of the project.
- [Flask](http://flask.pocoo.org/)
    - The project was built **flask** microframework due to its simplicity.
    - **flask.session** was used to store all variables values. 
- [Jinja2](https://jinja.pocoo.org/)
    - Used for creating templates.
- [unit-test](https://docs.python.org/3/library/unittest.html)
    - Used for automated testing.
- [Balsamiq](https://balsamiq.com/)
    - Before development started, **Balsamiq** was used for wireframes.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
    - Adjusting elements of project's frontend.
- [mLab](https://mlab.com/)
    - Free MongoDB database.
- [PEP8]http://pep8online.com/
    - Used to check python syntax errors.
- [JSlint]https://www.jslint.com/
    - Used to check JS snippet.
- [Font Awesome](https://fontawesome.com/)
    - Icons for the application.



## Testing

## Testing

When writing backend code I used unittest before adding new functionalities. I have also manually tested views to see if scenarios from user stories are giving desirable results.
The project has been tested on various browsers, including Firefox, Chrome, Opera, and Safari. 
All tests can be found in test.py file.

### Automated tests for code logic:

- test_vote_logic(self) - checks if voting is working correctly
- test_list_dictionary(self) - checks if dictionary for d3 chart is being populated correctly
- test_length(self) - checks if username's incorrect length is detected
    
### Automated tests for deployed version:

- test_initial(self) - testing GET request of a index.html template and a response code  
- test_show_all(self)- testing GET request of show_all.html
- test_test_show_single(self) - testing if show_single.html template is deployed


### User testing:

Web application was also tested by group of users using similar scenarios as mentioned in manual testing. Feedback helped with further development.

## Deployment

The application is deployed at [DishFinder](https://dishfinderstage.herokuapp.com/).

In order to deploy, following changes has been made:
- Set 'debug' value in run.py file to False
- Added requirements.txt and Procfile, as required by heroku
- Set Heroku Config Vars:
    - IP to 0.0.0.0
    - PORT to 5000
    - environmental variables for AWS S3 account
    - app secret key
    - MongoDB configuration

To run it locally:
- Install python 3
- Install virtualenv
- Create virtual environment inside directory of this project
- Activate virtual environment
    - source venv/bin/activate
- Install flask packages using pip3 with virtualenv is activated:
	- pymongo 
	- bson
	- boto3 
- Start the web server with commands:
    - export FLASK_APP=run.py
    - flask run
- Type http://127.0.0.1:5000 address or http://localhost:5000 in your browser window


## Credits

### Content

- Images where taken from [Shutterstock.com](https://www.shutterstock.com/)
- Font was taken from [FontSquirrel.com](https://www.fontsquirrel.com/)
- Some sample images taken from[BBC Food](https://www.bbc.com/food) 

### Media

- The photos used in this site were obtained from [Shutterstock.com](https://www.shutterstock.com/)

### Acknowledgements

- Big thank you to my mentor [Antonija Šimić](https://github.com/tonkec/)
