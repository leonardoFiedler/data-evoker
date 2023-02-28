# data-evoker

Welcome to data-evoker, a tiny library that generates data based on an existing schema. Sometimes you have a data pipeline and needs to generate some sample data to test if you jobs are doing well.
In this scenario, there are a lot of troubles:

1. Data sensitivity
2. Low data generation
3. Manually data generation

The objective of Data Evoker library is to easily generate fake data and integrate with your data pipeline, making it easy to create load testing and local development tests.

Data Evoker receives a [JSON Schema](https://json-schema.org) like file and outputs JSON files according to the pattern received.

## Installation process

1. Clone repo inside your computer
2. Install [Poetry](https://python-poetry.org) if it's not already installed
3. Use the command `poetry --version` to check if Poetry is already installed
4. Install the dependencies using the command: `poetry install`

## Roadmap development

1. Validate JSON Schema file
2. Delimite types and options accepted