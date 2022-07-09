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
| https://she-codes-crowdfunding-miao.herokuapp.com/users/  | POST      | <pre><code>{</code><br><code>  "username": "test",</code><br><code>  "email": "test@mysite.com",</code><br><code>  "password": "password",</code><br><code>  "bio": "bio",</code><br><code>  "avatar": "https://avatar.com",</code><br><code>}</code></pre> | N/A          |
 
