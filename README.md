The SoChem Portal is the online platform for interaction and collaboration for the members of Society of Chemical Engineers,
IIT (BHU), Varanasi.

As on 04th Feb, 2020- the work on this project has been started by the SoChem Informatics Team.

Instructions for Collaborators
---
Use these instructions to setup the app locally on your system and make contributions.

1. Create a fork of this repository.
2. Pull the forked repository's contents onto your machine.
3. Setup the virtual environment required by the app.

    ```
        // Create the virtual environment 
        python -m venv env
    
        // Activate the virtual environment
        source env/bin/activate
    
        // Install the requirements
        pip install -r requirements.txt
    ```
4. The application currently requires the following environment variables to run:
   * SECRET_KEY : (For development, you may set any value of this variable, but don't change it once set.)
        ```
        export SECRET_KEY="anyvalueyouliketohavehere"
        ```
     *Note: *You will have to set the environment variable everytime you restart the virtual environment.*
     
5. Start the django development server:
    ```
    python manage.py runserver
    ```