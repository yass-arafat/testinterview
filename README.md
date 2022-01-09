# How to run the project

- clone the project 
```
git clone https://github.com/yass-arafat/testinterview.git
```
- Start the server for local development:
```bash
docker-compose up -d --build
```
- Run a command inside the docker container:

```bash
python manage.py migrate
```

# How to test the code

- create a user calling the api
```
curl --location --request POST 'http://localhost:8000/api/v1/users/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 4b60ff69b432cd8a7a4879d2e000e30f8db72ebe' \
--data-raw '{
    "username": "yassir",
    "password": "test",
    "email": "test@test.com",
    "first_name": "test",
    "last_name": "user"
}'
```
this will provide a user code in the e.g
```
{
    "id": "85af6242-b0b4-4eca-a20a-598ec723dfb3",
    "username": "yassi",
    "first_name": "test",
    "last_name": "user",
    "email": "testy1@test.com",
    "auth_token": "fc65603ecc3c935d232f6034ace0b974ece689bb"
}
```
- now go to project directory `core/users/fixtures` and edit the articles.json file
replace the `user_id` with the user id got from the response
- Run a command inside the docker container:
`make` . it will insert a article with that user id
- now call the api to get the article list of the user
```
curl --location --request GET 'http://localhost:8000/api/v1/test/user/{user_id}/article' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 4b60ff69b432cd8a7a4879d2e000e30f8db72ebe' \
--data-raw ''
```
