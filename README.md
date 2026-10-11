# CSCE490-Research-AI-Foundry

A small applet that sends a product review to a model deployed in Azure AI Foundry and returns structures JSON: sentiment, topic, and escalation with a short reply.


## Setup
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Copy .env.example to the .env file and fill in the Foundry endpoint, key, and the deployment name.
You need to deploy a model in AI foundry and grab the information from there for this to work

## Run
```
python guardrailtemplate2.py
```
Type in a review and press enter or press enter on a empty line to quit
```
python guardrailTestsTemplate.py
```
runs and returns engineered tests to return the structures desired
