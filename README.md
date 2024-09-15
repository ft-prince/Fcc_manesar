# FCC Manesar

## Description

FCC Manesar is a Django project designed to manage stations and their associated media. It includes functionality for creating stations, associating products, and handling media files (PDFs, videos).

## Features

- Manage stations and their details.
- Upload and handle various media types (PDFs, videos).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ft-prince/Fcc_manesar.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Fcc_manesar
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser (optional but recommended):

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

Navigate to `http://127.0.0.1:8000/` in your browser to access the application.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the Renata License.
