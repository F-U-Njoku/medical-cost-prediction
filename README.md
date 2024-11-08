# Medical Cost Prediction API

<p align="center">
  <img src="./Images/banner.webp" alt="Medical Insurance.">
</p>

A machine learning-powered API that predicts medical insurance costs based on patient demographics and health indicators. Built with Flask and scikit-learn, deployed on AWS Elastic Beanstalk.

## Overview

This API uses a Random Forest model trained on medical insurance data to predict potential medical costs. The model takes into account various factors such as age, BMI, smoking status, and region to make its predictions.

## Technical Architecture

- **Framework**: Flask
- **ML Framework**: scikit-learn
- **Model**: Random Forest Regressor (max_depth=5, n_estimators=400)
- **Deployment**: AWS Elastic Beanstalk with Docker
- **API Protocol**: REST
- **Input/Output**: JSON

## Installation

### Local Development

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install dependencies using Pipenv:
```bash
pip install pipenv
pipenv install
```

3. Run the application:
```bash
pipenv run python predict.py
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t med-cost-predictor .
```

2. Run the container:
```bash
docker run -p 8080:8080 med-cost-predictor
```

### AWS Elastic Beanstalk Deployment

1. Initialize Elastic Beanstalk:
```bash
eb init
```

2. Create and deploy the environment:
```bash
eb create med-app-env
```

## API Endpoints

### Health Check
- `GET /`
- `GET /health`
  - Returns API health status
  - Response: `{"status": "healthy"}`

### Prediction Endpoint
- `POST /predict`
  - Accepts JSON input with patient information
  - Returns predicted medical cost

Example request:
```json
{
    "age": 35,
    "sex": "male",
    "bmi": 26.5,
    "children": 2,
    "smoker": "no",
    "region": "northeast"
}
```

Example response:
```json
{
    "predicted_medical_cost": 12345.67,
    "status": "success"
}
```

## Error Handling

The API includes comprehensive error handling:
- 400: Bad Request (invalid input data)
- 500: Internal Server Error

Error response format:
```json
{
    "error": "Error description",
    "details": "Additional error details" (optional)
}
```

## Model Information

- **Algorithm**: Random Forest Regressor
- **Features**: age, sex, bmi, children, smoker status, region
- **Target Variable**: Medical costs (log-transformed)
- **Model Performance**: [Add your model's performance metrics]

## Dependencies

- Python 3.11
- Flask
- scikit-learn
- numpy
- pandas
- gunicorn (for production deployment)

## Development and Testing

1. Run tests:
```bash
# Add your test command here
```

2. Local development server:
```bash
python predict.py
```

## Contributing

[Add your contribution guidelines here]

## License

[Add your license information here]

## Contact

[Add your contact information here]
