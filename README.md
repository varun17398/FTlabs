# FTLabs backend development test

# Prerequisites

Django and Python 3

# Implementation

This is a search functionality developed using Django and Python.

I have created a virtualenv and developed all the code as this is a best practice and also recommend you the same to setup a different virtual environment install Django in it and then run this so there won't be any errors.

Inside the file in the root directory there is a folder called searching which is the core folder for my project. In that folder itself you will find all the necessary code.

I have used SQLite for storing the given data in this framework.

I have also created a superuser which we could get through Django for easy functionality for adding or removing operations on our database.

I have developed a UI with a search bar in which you can give input and you will get the output of 25 results based on your rankingh criteria.

In order to run this in your local system all you need to do is go inside the root folder i.e, ```ftlabs/mysite/``` after cloning and then run the command - ```python manage.py runserver``` and then hit the URL ```http://127.0.0.1:8000/searching/``` for entering in search bar and evaluation.

Entering a single letter might give reults in a second as you know that is the reason most of the autosearch functionalities include atleast 3 letters to enter but entering more than one letter is fast.

If the mentioned URL is not in your case then you need to go into ```ftlabs/mysite/searching/templates/searching/index.html``` and change the URL with respect to what you get.

By hitting the above url with desired string gives all the possible autocomplete words that can be displayed when a user actually enter that word in a search bar. As for this requirement I am even displaying the usage count along with the word which satisfies the given constraints.

Only 25 records are displayed atmost as requested.

The words are sorted based on the given requirement. As I haven't implemented the search bar with UI so everytime you want to get the results for a partial or complete word you need to change the input string in the URL and hit it again and the result takes less than a second which is pretty fast.

If at all there is any issue in evaluating it and checking you could also contact me anytinme through my mail.

