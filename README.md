# user-communities-api

This is a basic backend for a Communities System Management project made to practice my skills in RESTful API development using Django REST Framework.

# Technologies:

Django==5.0.2
djangorestframework==3.14.0

# API Documentation

## Endpoints

### Users

#### List all Users or Create a New One

-   URL: `/users/`
-   Method: `GET`, `POST`
-   Description: Retrieves a list of all users or creates a new user.
-   Response:
    -   Status Code: `200 OK` (for GET), `201 Created` (for POST)
    -   Body: Array of user objects (for GET), Created user object (for POST)

#### Retrieve, Update, or Delete a User

-   URL: `/users/{id}/`
-   Method: `GET`, `PUT`, `DELETE`
-   Description: Retrieves, updates, or deletes a specific user.
-   Parameters:
    -   `id` (integer): The user's unique identifier.
-   Response:
    -   Status Code: `200 OK` (for GET, PUT), `204 No Content` (for DELETE)
    -   Body: User object (for GET, PUT)

### Communities

#### List all Communities or Create a New One

-   URL: `/communities/`
-   Method: `GET`, `POST`
-   Description: Retrieves a list of all communities or creates a new community.
-   Response:
    -   Status Code: `200 OK` (for GET), `201 Created` (for POST)
    -   Body: Array of community objects (for GET), Created community object (for POST)

#### Retrieve, Update, or Delete a Community

-   URL: `/communities/{id}/`
-   Method: `GET`, `PUT`, `DELETE`
-   Description: Retrieves, updates, or deletes a specific community.
-   Parameters:
    -   `id` (UUID): The unique identifier of the community.
-   Response:
    -   Status Code: `200 OK` (for GET, PUT), `204 No Content` (for DELETE)
    -   Body: Community object (for GET, PUT)
