# mirroir_mirroir

## Key components of this app

1. This app utilizes the flask framework. Provides the framework for routing, handling requests, and rendering templates.
   
2. Flask login manages user sessions, handles login and logout functionality and restricts access to certain routes.

3. SQLAlchemy acts the object-relational mapper ( whatever that means) to interact with the PostgresAQL database. Basically, it allows you to define database models(tables) as Python classes and perform database operations using Python code instead of raw SQL.

4. PostgresSQL database stores persistent data such as user accounts, friend relationships and messages.

5. HTML Templates and frontend is pf course handled by HTML, CSS and Javascript(react?) to create the user interface, the magical mirroir effects and forms for user interaction. 
