# OdogwuStore  
An E-Commerce web web application that functions as an online retailer for all products. The goal is to provide users with simple, safe and fast experience with ease of navigation. The product was designed with flask framework and python at the backend; HTML, CSS, JQuery at the frontend; and Postgres Database. Go to [Langugues, Libraries and Tools](#languages-libraries-and-tools) to view detailed list.
<br>
<details>
<summary> Current Updates to Note:</summary>
- Only the <a href="https://o-store.onrender.com/o-seller">seller</a> section has been completed
<br>
- You can login to test the seller section using &nbsp;&nbsp; email: udokaife7@gmail.com   &nbsp;&nbsp;  password: o-store
<br>
- The main section (buyer page) is currently under developement, only the <a href="https://o-store.onrender.com">homepage</a> has been designed
</details>

## Table of Contents
- [Introduction](#introduction)
- [Services](#services)
- [Site Scope](#site-scope)
- [Features](#features)
- [Langugues, Libraries and Tools](#languages-libraries-and-tools)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)
- [Disclaimer](#disclaimer)

## Introduction
The E-Commerce web app have three users:
* `Seller` : A partner of OdogwuStores that can add, update and track products that they want to market
* `buyer` : A user of OdogwuStores that can browse products, like, add to cart and purchase the products
* `admin` : A user that can delete or approve orders; add and update products

## Services
There are four services that will be implemented by the E-commerce app

## O-STORE
This is the main section of the e-commerce web app and also the main service rendered. This will involve buyers and potential buyers browsing the available products, add products to cart, purchasing products, creating account and updating their information. [Go Here](/api/routes/buyer) for more details
<details>
  <Summary>Pictures of the O-STORE</Summary>
  <br>
    <img src="/gh_images/buyer2.jpeg">
    <br>
    <img src="/gh_images/buyer3.jpeg">
</details>

### O-SELLER
This is a dedicated section for product owners and merchants who want to use the platform to display and sell their products. It will involve sellers and potential sellers to create account, update account, add products and update products. [Go Here](/api/routes/seller) for more details
<details>
  <Summary>Pictures of the O-SELLER</Summary>
    <br>
    <img src="/gh_images/seller2.jpeg">
    <br>
    <img src="/gh_images/seller3.jpeg">
</details>

### O-PAY
Coming up

### O-LOGISTICS
Coming up

## Site Scope
The expectations of the web app users can be modelled as user stories below

| As a...                  | I can...                                                   | So I can...                                                                 |
| :------------            |   :------------------------                                |        :--------------------------                                          |
|As a buyer               | I can see all products           |  so that I can select some to purchase.                                          |
|As a buyer               | I can view individual products                          |so that I can see the rating, details, specifications, price, quantity
|As a buyer               |I can search for a product by name or category           |so that I can find a product easily and quickly
|As a buyer               |I can sort available products in order of prices or brand |so that I can make informed decision and manage purchase and expense parameters
|As a buyer               |I can add items I want into a bag                        |so that I can easily add or remove items
|As a buyer                |I can view the total of my purchase                       |so that I can make informed decision on how much I am spending
|As a buyer             |I can easily register an account                       |so that I will be able to view my profile
|As a buyer             |I can easily Login and Logout                          |so that I can access my personal information
|As a buyer             |I can easily recover my password                       |so that I can log back into my profile
|As a buyer             |I can have a personalized user profile                 |so that I can view my order history update my user profile and save my payment confirmation
|As a buyer             |I can Subscribe to sites newsletter                    |so that I can receive informative newsletters and benefit from any deals available
|As a buyer               |I can pay for products in my shopping bag securely     |so that I can feel safe and confident using my card on the site
|As a seller             |I can easily register an account                       |so that I will be able to view my profile and products I have added
|As a seller             |I can easily Login and Logout                          |so that I can access my personal account
|As a seller             |I can easily recover my password                       |so that I can log back into my personal account
|As a seller             |I can easily add products                              |so that I can update my product catalogue when I get new products
|As a seller            |I can easily update each product information            |so that I can reflect the current market value of prices, discounts and stock
|As an admin        |I can view a data entry form                           |so that I can add, update and delete products and posts

## Features
The contents and navigations of each section are defined in their Readme
- [Go Here for Buyer Features](/api/routes/buyer)
- [Go Here for Seller Features](/api/routes/seller)
- [Logistics Features in progress...](/api/routes/)
- [Banking Features in progress....](/api/routes/)

## Languages, Libraries and Tools
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [Flask-Login](https://flask-login.readthedocs.io/)
* [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
* [Python Pillow](https://pillow.readthedocs.io/en/stable)
* [WTForms](https://wtforms.readthedocs.io/)
* [SqlAlchemy](https://www.sqlalchemy.org/)
* [Psycopg2: PostgreSQl](https://www.postgresql.org/)
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [jQuery](https://jquery.com/)
* [Cloudinary](https://cloudinary.com/)
* Store APIs to load products: [FakeStoreApi](https://fakestoreapi.com/) [FakeShopApi](https://www.fakeshop-api.com/)

## Disclaimer
This site was developed for educational purposes only. _Binael Nchekwube 2023_
