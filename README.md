# Book Scraper

Welcome to Book Scraper! This project is designed to scrape book data from a website and store it in a MySQL database.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you need to have the following installed on your system:

- Python (version 3.6 or higher)
- MySQL Server
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/bookscraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd bookscraper
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Make sure your MySQL server is running.

2. Update the MySQL connection details in the `SaveToMySQLPipeline` class in the `pipelines.py` file:

    ```python
    host = 'localhost'
    user = 'your-mysql-username'
    password = 'your-mysql-password'
    database = 'books'
    ```

3. Run the Scrapy spider to start scraping book data:

    ```bash
    scrapy crawl bookspider
    ```

4. Once the scraping is complete, you can query the MySQL database to view the scraped data.

### Customization

You can customize the project to suit your needs:

- Modify the spider (`bookscraper/spiders/bookspider.py`) to scrape data from a different website.
- Adjust the database schema in the `SaveToMySQLPipeline` class to store additional information.
- Extend the pipeline to perform additional processing on the scraped data.

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.


### Acknowledgments

- Thanks to [Scrapy](https://scrapy.org/) for providing a powerful web crawling and scraping framework.
- Inspired by the need to collect book data for various purposes.
