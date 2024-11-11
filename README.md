# End-to-End Data Pipeline: Reddit Data Processing with Airflow, Celery, PostgreSQL, AWS Glue, and Redshift for Analytics
This project demonstrates an end-to-end data pipeline for extracting, processing, and analyzing Reddit data. The pipeline leverages Dockerized Airflow for orchestration, Celery for task distribution, and a series of AWS services to store, transform, and visualize the data.

## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
## Overview
This project builds a scalable data pipeline that pulls data from Reddit, processes it through Dockerized Airflow with task management by Celery, and stores it in PostgreSQL. The processed data is then uploaded to AWS S3, transformed using AWS Glue, and queried with Amazon Athena and Redshift for analysis and visualization in QuickSight, Tableau, and Power BI.

## Architecture
Here’s a high-level workflow of the pipeline:

1. **Reddit**: Source of raw data.
2. **Airflow**: Orchestrates the pipeline.
3. **Celery**: Manages task distribution in Airflow.
4. **PostgreSQL**: Stores initial processed data.
5. **AWS S3**: Storage of data for transformation.
6. **AWS Glue**: Data transformation and schema management.
7. **Amazon Athena & Redshift**: Data querying and analysis.
8. **Visualization**: Insights with QuickSight, Tableau, and Power BI.

## Technologies Used
- **Reddit API**: Data source
- **Docker**: Containerized environment
- **Apache Airflow**: Workflow orchestration
- **Celery**: Task queue
- **PostgreSQL**: Relational database for data storage
- **AWS S3**: Object storage for data files
- **AWS Glue**: ETL and data transformation
- **Amazon Athena**: SQL-based querying
- **Amazon Redshift**: Data warehousing
- **Visualization**: AWS QuickSight, Tableau, Power BI

## Setup and Installation
1. Clone the repository:
```bash
   git clone https://github.com/Navya2301/Reddit_DPE

```
2. Navigate to the project directory:
```
cd your-repo-name
```
3. Set up the Docker containers with Airflow, Celery, and PostgreSQL:
```
docker-compose up

```
4. Configure AWS credentials for accessing S3, Glue, Athena, and Redshift.
5. Run the initial DAG in Airflow to start the pipeline

## Usage
1. Schedule and monitor the pipeline in Airflow.
2. Data transformations occur automatically in AWS Glue.
3. Query data in Athena and Redshift.
4. Use QuickSight, Tableau, or Power BI to visualize the insights.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


