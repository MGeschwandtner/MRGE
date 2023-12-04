# MRGE Case Study

## Task

Use Case for Data Engineering

### Challenge Overview

In this challenge, you will be tasked with designing and implementing a data pipeline that seamlessly integrates mage.ai, a cutting-edge data ingestion and transformation tool, with dbt (data build tool), a powerful analytics engineering tool. The goal is to demonstrate your ability to create a streamlined and scalable data processing workflow from raw data to actionable insights.


### Key Components

- Data Ingestion with Mage.ai
- Transformation and Modeling with dbt
- Pipeline Orchestration

## Architecture Thoughts

- for showcase reasons develop something lightweight
- can be partly local
- as we only use a little amount of ressources the dwh architecture can also be lightweight
  

## Architecture Decision
- go with etl process
- add bigquery as dwh
- use github for code documentation / revisiontool

### System Architecture:
![Document systems](https://github.com/MGeschwandtner/MRGE/assets/152589902/33ba999f-d550-4de9-9fee-76bc41ce5914)
### DWH Design:
![image](https://github.com/MGeschwandtner/MRGE/assets/152589902/615c7b1e-3672-4649-bc94-cbb0e0659968)


## Source 
- use a public api for showcase reasons
- https://www.api-football.com/news/post/how-to-get-all-teams-and-players-from-a-league-id

## Key Features
### Pipeline
- one pipeline which contains all steps of the elt process
- ![image](https://github.com/MGeschwandtner/MRGE/assets/152589902/9c2968ec-98fd-4bbe-bf4e-9db381ad0a4e)
### Have a modular approach for requesting the API
- https://github.com/MGeschwandtner/MRGE/blob/main/mage/utils/helpers/http_load.py
- https://github.com/MGeschwandtner/MRGE/blob/main/mage/data_loaders/teams_data_loader.py
### Make it backfillable in case of historic needs
- https://github.com/MGeschwandtner/MRGE/blob/e2a0849154be9e14ef2ee4c704d1f059e899ea13/mage/data_loaders/fixtures_data_loader.py#L23
### Have a modular approach for testing(not made tests first class citizens for the case study though - just for demo purpose right now)
- https://github.com/MGeschwandtner/MRGE/blob/main/mage/utils/helpers/load_tests.py

### have a flat output layer in the dwh for lightning speed in case of data visualization tools


