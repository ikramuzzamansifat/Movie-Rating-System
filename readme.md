# Movie Rating System

### Description 
This project implements a movie rating system using the Flask web framework in Python. The system allows users to register, login, and logout, after which they can perform various actions such as adding movies, rating movies, viewing all movies, and searching for movies by keyword.

## Technolgy Used

- Programming Language: Python (Flask framework)
- Database: No database 

## Setup Instructions: 
- Clone the project or download it. 
- Make sure your system has python installed. 
- run the command: 
    `pip install -r requirements.txt` 

## Key Features 
- User Management: Users can register with their name, email, password, and phone number. They can also login using their credentials and logout when done.
- Movie Management: Authenticated users can add new movies to the system. Each movie has attributes such as name, genre, release date, and rating.
- Rating System: Users can rate movies on a scale of 1 to 5. The system ensures that only authenticated users can rate movies, and the rating is within the valid range.
- Search Functionality: Users can search for movies by keyword. The system returns a list of movies matching the search criteria along with their average ratings.

## Implementation details 
- Data for users, movies, and ratings is stored in memory, as no external database is used.
- Proper error handling and JSON responses are provided for various scenarios, such as missing fields during registration, invalid login credentials, and movie not found during rating.
- Regular expressions are used for case-insensitive keyword matching while searching for movies.

## Assumptions Made: 
- The system does not use a database and stores data in memory. Therefore, data will be lost upon restarting the server.
- User authentication is based on email and password only.
- Movie ratings are assumed to be between 1 and 5.
- The application assumes basic user management functionalities such as registration, login, and logout.


## Solution Overview: 
- The application provides functionalities for user registration, login, logout, adding movies, viewing all movies, rating movies, and searching for movies by keyword.
- User authentication is implemented using email and password.
- Proper error handling and responses in JSON format are provided for various scenarios.

## Problems Faced: 
- Since no database is used, managing data in memory could be challenging for large-scale applications. However, for the scope of this assignment, it provides a simple solution.
- The application does not persist data between server restarts. Using a database would solve this issue but was not allowed as per the instructions.


## Note: 
- Attached is a copy of my CV as requested.

