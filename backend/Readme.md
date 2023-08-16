# Django Image Upload with Log and DB user Validation App

This is a Django REST API project that allows you to upload and retrieve images while logging relevant information about the uploads.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (>=3.6)
- Django (>=3.0)
- `cx_Oracle` library for Oracle database interactions (if using Oracle)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nicoriver9/Django-ImageUpload-Log-DB-UserValidation.git
   cd image-storage-api

2. Install the required Python packages:

        pip install -r requirements.txt

3. Create a .env file in the root directory of your project and set the necessary environment variables. For example:

        ENGINE= XE
        NAME= your_db_name
        USER= your_db_user
        PASSWORD= your_db_password
        HOST= your_db_host
        PORT= your_db_port

        IMAGE_DIRECTORY=your_image_directory

# Usage
1. Run the Django development server:  

    python manage.py runserver

Open your browser and visit http://localhost:8000 to access the API documentation (Swagger).

## Image Upload
 * Endpoint: /api/upload/
 * Method: POST
 * Form data:
    * `name` (string): The name of the image.
    * `image_base64` (string): The image in base64 format.
    * `user` (string): The user for validation.
    * `service` (string): The service for validation.
## Image Retrieval
* `Endpoint`: /api/get_images/
* `Method`: GET
* `Returns` a list of images with their names and base64-encoded data.
## Frontend with React
To visualize the images in the frontend, follow these steps:

1. Navigate to the frontend directory:  
        
        cd frontend/image-viewer

2.  Install the required dependencies:
        
        npm install

3. Start the React development server:

        npm start

4. Open your browser and visit http://localhost:3000 to see the images displayed in the React app.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.