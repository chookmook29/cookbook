# DishFinder

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.
 
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

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses some **Bootstrap** elements for more responsive layout.
- [Python](https://www.python.org/)
    - Back-end was written in **Python** .
    - **vnev** library was used in development of the project.
    - **random** module was used with dictionaries.
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



## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
