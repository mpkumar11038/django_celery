# Django Celery Scrapper

This Django Celery project is designed to scrape proxy data from a website and store it in a database asynchronously using Celery tasks.

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install project dependencies using pip:

4. Apply database migrations:

5. Make migrations for the 'scrapper' app:

6. Apply migrations for the 'scrapper' app:

## Usage

1. Start the Celery worker:

2. Start Celery Beat for periodic task scheduling:

3. Run the Django development server:

4. Access the Django admin interface to view scraped proxy data:

## Notes

- The `scrape_proxies` task is scheduled to run periodically using Celery Beat. You can adjust the frequency of this task in the `CELERY_BEAT_SCHEDULE` setting in `settings.py`.
- Proxy data scraped from the website is stored in the database using Django models defined in the 'scrapper' app.
- The scraping logic is implemented in the `scrape_proxies` task located in `scrapper/tasks.py`.

