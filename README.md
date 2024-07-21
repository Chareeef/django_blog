# Django Blog

## Overview

For my first Django project, I worked on this Blog pplication was developed by following a YouTube tutorial by [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&si=NNzYCy0nEx5za9a0). It includes additional functionalities such as a "Quote of the Day" feature and file upload to AWS S3. The project served as a comprehensive learning experience, covering various aspects of Django development, including settings manipulation, models, views, pagination, and deployment.

## Features

- **User Registration and Profiles**: Users can create accounts, log in, and set their profile pictures.
- **Posting and Viewing**: Users can create posts, view posts from others with pagination, and manage their own posts.
- **Pagination**: Efficiently handles pagination for displaying large datasets.
- **Quote of the Day**: Displays a new quote every day.

## Learning Objectives

1. **Django Settings**: Learned how to manipulate Django settings to customize the application environment.
2. **Models and Views**: Gained in-depth knowledge of creating and managing models and views in Django.
3. **Pagination**: Implemented pagination to manage and display large datasets effectively.
4. **AWS S3 Integration**: Integrated AWS S3 for storing and retrieving application files.
5. **Deployment**: Deployed the application on Heroku, ensuring a smooth and scalable deployment process. ([My deployed version](https://youssef-django-blog-392795c250e4.herokuapp.com/))

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up AWS S3**:

   - Configure your AWS S3 Bucket and obtain your access keys.
   - Update your `settings.py` file with the AWS S3 configuration.

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Deployment

The application is deployed on Heroku. To deploy your own version:

1. **Install Heroku CLI**:

   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**:

   ```bash
   heroku login
   ```

3. **Create a New Heroku App**:

   ```bash
   heroku create your-app-name
   ```

4. **Deploy to Heroku**:

   ```bash
   git push heroku main
   ```

5. **Set Up Heroku Environment Variables**:
   - Configure your environment variables for AWS S3 and other settings on Heroku.

## Credits

- [Corey Schafer](https://github.com/CoreyMSchafer): Original tutorial and foundational code.
