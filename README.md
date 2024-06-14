# csv_file_uploder

User Registration and Authentication: Users can create accounts, log in, and log out using the allauth package.This ensures secure access to the CSV uploader and allows for user-specific functionalities.

CSV File Upload: Users can upload CSV files through a user-friendly interface. The uploader supports the uploading of files with comma-separated values.

Data Processing: The uploaded CSV files can be processed to extract meaningful information. Various operations such as filtering, sorting, and data manipulation can be performed on the uploaded data.

# Installation

To run the CSV uploader project locally, follow these steps: Clone the repository from GitHub: git clone [repository_url]

Navigate to the project directory: cd csv-uploader-project

Create a virtual environment : python -m venv myenv

Activate the virtual environment : myenv/Script/activate

Install the required dependencies : pip install -r requirements.txt

Set up the database : python manage.py migrate

Start the development server : python manage.py runserver

# Configuration

Open the project's settings file: csv_uploader/settings.py. Locate the INSTALLED_APPS section and ensure that the following apps are included: INSTALLED_APPS = ['allauth','allauth.account']

Set up the authentication backend: AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend','allauth.account.auth_backends.AuthenticationBackend']

# Usage

Register a new account or log in using an existing account.

Once logged in, navigate to the CSV uploader section.

Click on the "Upload CSV" button and select a CSV file to upload.

After the file is uploaded, perform the desired operations on the data.
