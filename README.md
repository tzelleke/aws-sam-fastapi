# AWS SAM FastAPI app

This is a demo project that uses AWS SAM to deploy a simple FastAPI app to AWS Lambda.

It includes [Powertools for AWS Lambda](https://docs.powertools.aws.dev/lambda/python/latest/) for enhanced logging and tracing in AWS.

It uses Poetry for dependency management and pytest for testing.

## Deployment to AWS

### Deploy from local machine

You can manually deploy the app to AWS using the AWS SAM CLI.

```bash
sam build --use-container
sam deploy --guided
```

### Deploy from CD pipeline

You can also deploy the app from a GitHub Actions workflow to AWS.

```bash
sam pipeline init --bootstrap
```

This command will initiate an interactive assistant that guides you through creating the necessary AWS infrastructure resources.
