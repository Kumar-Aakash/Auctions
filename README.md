# Auctions Project

Welcome to the Auctions project! This web application simulates an online auction platform where users can list items for auction, place bids, and interact with the auction process.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User Registration and Authentication
- Listing Items for Auction
- Placing Bids on Listings
- Watching Listings
- Automatic Auction Closing
- Categorized Listings and Search
- User Profiles
- Admin Panel for Management

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.11)
- Django (version 4.2)

### Installation

1. Clone this repository to your local machine:

```shell
git clone https://github.com/Kumar-Aakash/Auctions.git
```

2. Change directory to the project folder:

```shell
cd Auctions  
```

3. Install the required dependencies:

```shell
pip install -r requirements.txt
```


4. Set up the database:

```shell
python manage.py makemigrations 
python manage.py migrate
```


5. Create a superuser for accessing the admin panel:

```shell
python manage.py createsuperuser
```

6. Start the development server:

```shell
python manage.py runserver
```

#### Access the application in your web browser at http://127.0.0.1:8000/


# Usage
- Register an account or log in if you already have one.
- Create auction listings for items you want to sell.
- Browse through existing listings, place bids, and watch items.
- Admin users can manage users, listings, and other application aspects through the admin panel.

# Contributing
We welcome contributions from the community! To contribute to the project, follow these steps:



1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Implement your changes.
4. Create a pull request describing your changes and their purpose.

<br />

# License
This project is licensed under the MIT License

