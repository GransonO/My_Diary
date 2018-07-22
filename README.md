[![Build Status](https://travis-ci.org/GransonO/My_Diary.svg?branch=develop)](https://travis-ci.org/GransonO/My_Diary)

[![Maintainability](https://api.codeclimate.com/v1/badges/641fd6175f184e959490/maintainability)](https://codeclimate.com/github/GransonO/My_Diary/maintainability)

[![Coverage Status](https://coveralls.io/repos/github/GransonO/My_Diary/badge.svg?branch=develop)](https://coveralls.io/github/GransonO/My_Diary?branch=develop)

# My_Diary
A web application with a diary functionality.
Aimed for better understanding the wed dev-basics( HTML, CSS $ JAVASCRIPT) and utilizing the python Flask framework. 

## Project Overview
MyDiary is an online journal where users can pen down their thoughts and feelings. 

### Required Features
1.	Users can create an account and log in.
2.	Users can view all entries to their diary.
3.	Users can view the contents of a diary entry.
4.	Users can add or modify an entry.
### Additional
5.	Users can set and get daily notifications that prompt them to add an entry to their diary.

## Directives
●	No use of any css frameworks e.g bootstrap, materialize  
●	No use of downloaded or an already built website template.

# API End Points
## Necessary Tools
### Server side Framework: ​<​Flask Python Framework>
### Linting Library: ​<​Pylint, a Python Linting Library​>
### Style Guide: ​<​PEP8 Style Guide​>
### Testing Framework: ​<​PyTest, a Python Testing Framework​>

## Project Guidelines
On Pivotal Tracker, create user stories to setup and test API endpoints that do the
following using data structures
○ Get all diary entries.
○ Get a specific diary entry.
○ Add an entry
○ Modify an entry.
On Pivotal Tracker create stories to capture any other tasks not captured above. The
tasks can be feature, bug or chore for this challenge.
Setup the server side of the application using the specified framework.
Setup linting library and ensure that your work follows the specified style guide
requirements.
Setup test framework.6. Version your API using url versioning starting, with the letter “v”. A simple ordinal
number would be appropriate and avoid dot notation such as 2.5. An example of this
will be​ : ​https://somewebapp.com/api/v1/users​.
Using separate branches for each feature, create version 1 (v1) of your RESTful API to power front-end pages
At minimum, you should have the following API endpoints working:
EndPoint Functionality
### GET /entries Fetch all entries
### GET /entries/<entryId> Fetch a single entry
### POST /entries Create an entry
### PUT /​entries​ /<​entryId​ > Modify an entry
Write tests for the API endpoints
Ensure to test all endpoints and see that they work using Postman.
Integrate ​TravisCI​ for Continuous Integration in your repository (with ​ReadMe​ badge).
Integrate test coverage reporting (e.g. Coveralls) with badge in the ​ReadMe.
Obtain CI badges (e.g. from Code Climate and Coveralls) and add to ​ReadMe​.
Ensure the app gets hosted on Heroku
