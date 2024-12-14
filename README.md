# Django API with Swagger Documentation

## 📋 Description

This repository demonstrates the development of a Django-based API with Swagger documentation to facilitate understanding and testing of endpoints. The API is designed to manage a simple CRUD system for worker salaries.

## 🚀 Features

- RESTful API built with Django and Django REST Framework
- Swagger documentation for easy API interaction and testing
- Endpoints for managing worker data and their salaries
- Modular and scalable architecture for future extensions

## 🛠️ Technologies Used

- **Python** (base language)
- **Django** (web framework)
- **Django REST Framework (DRF)** (for building APIs)
- **drf-yasg** (for generating Swagger documentation)

## 📦 Installation

### Requirements

- Python 3.x
- Django
- Django REST Framework
- drf-yasg

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/IsaacMartins12/Django-api-swagger
    ```

2. Navigate to the project directory:
    ```bash
    cd Django-api-swagger
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the Swagger documentation in your browser at:
    ```
    http://127.0.0.1:8000/swagger/
    ```

## 📑 API Endpoints

- **`POST /workers/`**: Create a new worker with salary details.
- **`GET /workers/`**: Retrieve a list of all workers.
- **`GET /workers/<id>/`**: Retrieve details of a specific worker by ID.
- **`PUT /workers/<id>/`**: Update the details of a specific worker.
- **`DELETE /workers/<id>/`**: Delete a worker by ID.

## 🧑‍💻 Contribution

We welcome contributions to improve this project. Feel free to submit pull requests or report issues on the [Issues page](https://github.com/IsaacMartins12/Django-api-swagger/issues).

### Contribution Steps

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a Pull Request with a detailed description of your changes.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

