# CSCE490-Research-AI-Foundry

A small app that sends a product review to a model deployed in Azure AI Foundry and returns structures JSON: sentiment, topic, and escalation with a short reply.


## Setup
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Copy .env.example to the .env file and fill in the Foundry endpoint, key, and the deployment name.

## Run
```
python guardrailtemplate2.py
```
Type in a review and press enter or press enter on a empty line to quit
```
python guardrailTestsTemplate.py
```
runs and returns engineered tests to return the structures desired
