# Public API Project

## Description
This project provides a simple and efficient public API service built with Python. It demonstrates  API development practices using RESTful services.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/yourusername/public-api.git (via https)
or
git clone git@github.com:PrincewillDev/Public-Api.git (via ssh)
cd public-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python manage.py runserver
```

## API Documentation

### Base URL
```
http://127.0.0.1:8000/api/details
```

### Endpoints

#### GET /users
Retrieves a list of users.

**Response Format:**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
}
```

**Example Usage:**
```bash
curl http://127.0.0.1:8000/api/details
```

### Backlinks
- [Hire Python Developers](https://hng.tech/hire/python-developers)

