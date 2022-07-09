# she-codes-crowdfunding-api-project-miaozhaod
This is a Django Rest Framework assignment subbmited for She-Codes-Django-Project

## The title of the website
📷 PixelFoto

## A paragraph detailing the purpose and target audience for the website
Raise funds for photographers who would like to hold their own exhibitions, the supporters can raise funds for the photographers they like, and if the goal is achieved, those who support the photographer can get a free ticket for the exhibition.

## The features your MVP will include
- [x] Authentication: Login
- [x] Authentication: Sign up
- [x] CRUD of project with suitable permissions

## At least 3 addtional features you would like to include if you reach your MVP
- [x] Request user can update their profile
- [x] A logged in user can make a pledge
- [x] The supporter can delete their pledge

## An API specification
| Endpoint                                                  | Method    | Body                   | Authorization |
| --------------------------------------------------------- | --------- | ---------------------- | ------------- |
| **Users and Authentication Endpoints:**|
| https://she-codes-crowdfunding-miao.herokuapp.com/users | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/users/[id] | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/users/  | POST | <pre><code>{</code><br><code>  "username": "test",</code><br><code>  "email": "test@mysite.com",</code><br><code>  "password": "password",</code><br><code>  "bio": "bio",</code><br><code>  "avatar": "https://avatar.com",</code><br><code>}</code></pre> | N/A          |
| https://she-codes-crowdfunding-miao.herokuapp.com/users/[id]/ | PUT | <pre><code>{</code><br><code>  "anyKey": "anyValue",</code><br><code>}</code></pre> | Bearer Token          |
| https://she-codes-crowdfunding-miao.herokuapp.com/api-token-auth/ | POST | <pre><code>{</code><br><code>  "username": "username",</code><br><code>  "password": "password",</code><br><code>}</code></pre> | N/A |
| **Projects Endpoints:**|
| https://she-codes-crowdfunding-miao.herokuapp.com/projects | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/projects/[id] | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/projects/ | POST | <pre><code>{</code><br><code>  "title": "title",</code><br><code>  "description": "description",</code><br><code>  "location": "location",</code><br><code>  "goal": 100,</code><br><code>  "image": "https://image.com",</code><br><code>  "date_due": "date_due",</code><br><code>  "is_open": true,</code><br><code>  "date_created": "date_created",</code><br><code>}</code></pre> | Bearer Token |
| https://she-codes-crowdfunding-miao.herokuapp.com/projects/[id] | PUT | <pre><code>{</code><br><code>  "anyKey": "anyValue",</code><br><code>}</code></pre> | Bearer Token |
| https://she-codes-crowdfunding-miao.herokuapp.com/projects/[id] | DELETE | N/A | Bearer Token |
| **Pledges Endpoints:**|
| https://she-codes-crowdfunding-miao.herokuapp.com/pledges | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/pledges/[id] | GET | N/A | N/A |
| https://she-codes-crowdfunding-miao.herokuapp.com/pledges/ | POST | <pre><code>{</code><br><code>  "amount": 10,</code><br><code>  "comment": "comment",</code><br><code>  "anonymous": false,</code><br><code>  "id": 1,</code><br><code>}</code></pre> | Bearer Token |
| https://she-codes-crowdfunding-miao.herokuapp.com/pledges/[id] | DELETE | N/A | Bearer Token |









