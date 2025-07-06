# ecommerce-demo-dashboard
project:
  title: E-commerce Sales Analytics Dashboard
  description: |
    A fully containerised, modular analytics project. Generate synthetic sales and product data using Python,
    load it into a MySQL database, and visualize business metrics with interactive dashboards in Metabase.
    Features modular ETL scripts, Docker Compose stack, and is automation-ready.
  stack:
    - Python (pandas, requests, faker)
    - MySQL (Docker)
    - Metabase (Business Intelligence)
    - Adminer (DB admin UI)
    - Docker Compose
  structure:
    - data/: Generated CSVs and data
    - scripts/: ETL Python scripts
    - dashboards/:  ![Dashboard pdf](images/Metabase-Ecommerce-Dashboard.pdf)
    - requirements.txt
    - docker-compose.yml
    - .env
    - README.md
  how_to_run:
    - Clone the repo and fill .env with MySQL credentials
    - Start stack: docker compose up -d
    - Setup Python env & pip install -r requirements.txt
    - Run ETL scripts: fetch_products.py, generate_sales.py, load_to_mysql.py
    - Visit Metabase at http://localhost:3000 and build dashboards
    - (Optional) Visit Adminer at http://localhost:8080 for manual SQL
  dashboards:
    - Sales by product category/type
    - Gross margins and discounts
    - Sales by channel (e-commerce, direct)
    - Sales by customer segment
    - Customer churn/retention
    - Avg SKUs per customer
  features:
    - End-to-end ETL pipeline, SQL modeling, and dashboarding in one project
    - Code is modular, ready for Airflow/cron automation
    - Easy to adapt for real datasets or APIs
    - Clean, clear code—ready for demos or interviews

