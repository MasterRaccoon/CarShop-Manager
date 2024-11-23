# CarShop-Manager  

The **CarShop-Manager** is a prototype built with Django for managing car dealerships. This project showcases vehicle management features, automatic description generation, and professional hosting for demonstration purposes.  

## Features  

- **Vehicle Management**:  
  - Add, edit, and delete vehicles.  
  - Detailed listings with descriptions automatically generated using [Gemini](https://gemini.ai).  

- **User Authentication**:  
  - **User Registration**: Create an account to access the system.  
  - **Login/Logout**: Secure user login and logout functionality.  
  - **Access Control**: Certain features are accessible only to logged-in users.  

- **Database**:  
  - Powered by PostgreSQL for secure and efficient data storage.  

- **Infrastructure and Hosting**:  
  - Hosted on AWS with the application served via **NGINX**, **uWSGi**, and managed by **Systemd**.  

## Live Demo  

View the project prototype here:  
[http://98.85.107.198/cars/](http://98.85.107.198/cars/)  

> **Note**: This IP is static as it uses an AWS Elastic IP configuration.  

## Project Structure  

The prototype is divided into the following key components:  

1. **Backend**:  
   - Django Framework for server-side logic and database management.  

2. **Database**:  
   - PostgreSQL configured for both local and remote use (via Aiven for production).  

3. **Servers**:  
   - **NGINX** for load balancing and web serving.  
   - **uWSGi** for serving the Python application.  
   - **Systemd** for process management.  

## Requirements  

- Python 3.10+  
- Django 4.x  
- PostgreSQL 14+  
- Configured virtual environment  

## Setup Instructions  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/carshop-manager.git
   cd carshop-manager
