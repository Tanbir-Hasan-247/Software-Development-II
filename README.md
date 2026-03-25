# Skill Match and Collaboration Platform 🤝

A dynamic, skill-based networking and collaboration platform built with Django. This application enables users to connect based on their professional expertise, post job/collaboration opportunities, and apply for roles seamlessly.

## 🚀 Features

* **Secure Authentication & Authorization:** Robust user registration, login, profile management, and password update functionality.
* **Role-Based Access Control:** Differentiated dashboards and permissions for various user types.
* **Dynamic Profile Management:** Users can create and update their profiles, highlighting their specific skills and categories.
* **Job & Project Board:** Users can post collaboration opportunities with specific technical skill requirements.
* **Application System:** Seamless application tracking for both applicants and job posters.
* **Real-time Notifications:** Automated notifications for application statuses and platform updates.
* **Advanced Search & Filtering:** Filter jobs and collaboration opportunities dynamically based on categories and skills using AJAX.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Tailwind CSS / Bootstrap, Vanilla JavaScript (AJAX)
* **Database:** SQLite (Development) / MySQL (Production)
* **Architecture:** MTV (Model-Template-View)

## 📂 Project Structure

The project is divided into several modular Django apps:

* `loginpage/`: Handles user authentication, registration, profiles, and account management.
* `jobPost/`: Manages the creation, display, and application processes for collaboration opportunities.
* `Categories/`: Manages the different skill categories and tags used across the platform.

## ⚙️ Local Setup & Installation

Follow these steps to run the project locally on your machine:

**1. Clone the repository**
```bash
git clone [https://github.com/Tanbir-Hasan-247/Software-Development-II.git](https://github.com/Tanbir-Hasan-247/Software-Development-II.git)
cd Software-Development-II/skill_match_and_collaboration_platform
```
**2. Create a virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**
*(Ensure you have a `requirements.txt` file, or install Django manually)*
```bash
pip install django
```

**4. Apply database migrations**
```Bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser (Admin)**
```Bash
python manage.py createsuperuser
```
**6. Run the development server**
```Bash
python manage.py runserver
```
**7. Access the application**
*Open your web browser and navigate to http://127.0.0.1:8000/.

## 👨‍💻 Author

**Tanbir Hasan**
* GitHub: [@Tanbir-Hasan-247](https://github.com/Tanbir-Hasan-247)
* LinkedIn: [Tanbir Hasan](https://www.linkedin.com/in/tanbir-hasan-638075345/)
