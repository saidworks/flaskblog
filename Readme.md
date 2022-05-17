# Flask app
> A Flask app that allows user to create,modify and delete post or read all posts.

## Installation 
To get all dependencies installed clone this repository run the server from the root directory of the project by entering the following commands in the your terminal:
           
```sh
    pip install -r /path/to/requirements.txt
    $env:FLASK_APP="main"
    flask run
```

## Endpoints
After running the app, the following endpoints are available:
- You can add a post with the following URL:
    ```sh
    http://127.0.0.1:5000//create
    ```
 
- You can get all of the posts you made so far on the main page or with the following URL::
    ```sh
    http://127.0.0.1:5000/
    ```
- You can get a specific post with its specific id as parameter the following URL:
    ```sh
      http://127.0.0.1:5000/{id}
    ```
- You can update a specific post with its specific id as parameter the following URL:
    ```sh
      http://127.0.0.1:5000/{id}/update
    ```
- You can delete a specific post with its specific id as parameter the following URL:
    ```sh
      http://127.0.0.1:5000/{id}/delete
    ```



## Tech Stack
-  Python 
-  Flask
-  SQLAlchemy
-  Sqlite
-  Gunicorn
-  Heroku CLI


