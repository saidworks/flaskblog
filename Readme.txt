A project created using python(flask),sqlalchemy sqlite that allows to create,modify, update and delete post.
to run the app:

1. install required libraries using : pip install -r /path/to/requirements.txt
2. define flask app variable using : $env:FLASK_APP="main"
3. run the flask app
    a. to create post add "/create" after the website url
    b. to upate post add "{id}/update" after the website url
    c. to delete post add "{id}/delete" after the website url
    d. to read a post add "/{id}" after the website url