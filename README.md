# FTLabs backend development test

#Prerequisites

Django and Python

This is a search functionality developed using Django and Python.

Inside the file in the root directory there is a folder called searching which is the core folder for my project. In that folder itself you will find all the necessary code.

I have used SQLite for storing the given data in this framework.

I have also created a superuser which we could get through Django for easy functionality for adding or removing operations on our database.

In order to get the results when you search for a word (partial/complete) you need to give your input word in the url itself which goes like ```http://127.0.0.1:8000/searching/<inputstring>/```

By hitting the above url with desired string gives all the possible autocomplete words that can be displayed when a user actually enter that word in a search bar. As for this requirement I am even displaying the usage count along with the word which satisfies the given constraints.

Only 25 records are displayed atmost as requested.

The words are sorted based on the given requirement. As I haven't implemented the search bar with UI so everytime you want to get the results for a partial or complete word you need to change the input string in the URL and hit it again and the result takes less than a second which is pretty fast.

In order to run this in your local system all you need to do is go inside the root folder after cloning and then run the command - ```python manage.py runserver``` and then hit the above mentioned URL for the results and evaluation.
