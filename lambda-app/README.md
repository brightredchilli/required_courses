# Overview

This folder is the deployment folder for the 'Required Courses' project
developed in Fall 2017, deployed for AWS Lambda.

The project is expected to produce a file named main.py, with a function called
`handler`.

The project is deployed with scripts to rule them all. Scripts can be found in
the scripts folder.

# Set up for development

To set the machine up for development, install pyenv and pyenv-virtualenv first.

Then, create an env from Python 3.8 or higher

`pyenv virtualenv required_courses`

then be sure to set the local env name

`pyenv local required_courses`

Install dependencies:

`pip install -r requirements.txt`


scripts/bundle`: Bundles the zip file for aws lambda distribution, produces a
two zip files:

1. `lambda_distribution_layer.zip` : Bundles the dependencies for the app to be
   included as a lambda layer
2. `lambda_distribution_app.zip` : Bundles the app



