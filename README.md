# Recipe App

Recipe application build as part of the following course: https://www.udemy.com/the-complete-guide-to-angular-2/

Comprised of two parts: a front-end web application, written in Angular 6, and a backend API written in Django. This deviates from the course, which used Firebase as its backend, mainly as a source for Angular HTTP requests via the HttpClient.

The course has been extended to include the use of Django, Django REST framework, PostgreSQL/SQLite, Docker, Celery, and RabbitMQ.

The purpose of this repo was initially to work with the Angular course and learn Angular, but has been extended to consolidate knowledge of Docker/containers, as well as DevOps practices. It also allowed for exploration of libraries that can work in concert with Django REST Framework, as well as investigate things such as periodic tasks in Celery.

Features:

- Dockerized environment, with docker-compose used to coordinate 6 different containers
- An Angular front-end application, served from an Nginx container.
- An API written using Django REST Framework, which is queried by the Angular front-end using the HttpClient
- JWT authentication using the rest-framework-jwt library
- PostgreSQL database within the Docker environment
- SQLite database for non-container development
- Celery worker and Celery cron tasks used to implement potentially long-running operations
- RabbitMQ message broker for the Celery tasks
- Use of the factory-boy library to generate fake data for the application
- Use of django-filters library to provide granular filtering of REST framework responses