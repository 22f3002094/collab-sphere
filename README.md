# Collab Sphere 

This repository contains for the **Collab Sphere** project, a collaborative platform designed to enhance team productivity and communication. The project also includes a Vue.js frontend located in the `collab-sphere` directory.

---

[Watch Demo Video](https://drive.google.com/file/d/1gGrXuTS0a5IZwgTSUn2vwPwgNNRO3VXi/view?usp=sharing)



## Features
* Backend:
- User authentication and authorization
- RESTful API for frontend integration
- Modular Python backend (Flask/RESTAPI)
- Scalable and maintainable project structure
- Database support and data persistence


* Frontend (Vue.js):

- Responsive and dynamic user interface built with Vue 3
- Component-based architecture for reusability and maintainability
- Tailwind CSS integration for modern styling
- Vue Router for SPA navigation
- Vuex (or similar) for state management
- Pages for user onboarding, project management, and collaboration
- Integration with backend APIs for full-stack functionality


---

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- (Optional) Virtual environment tool like `venv` or `virtualenv`

---

## Folder Structure
```bash
collab-sphere-backend/
├── .myenv/                      # Python virtual environment (excluded from version control)
├── backend/                     # Python backend source code
│   
│   ├── api.py                   # API route definitions
│   ├── config.py                # Configuration settings
│   ├── initialdata.py           # Initial data seeding script
│   ├── models.py                # ORM models or schema definitions
├── instance/                    # Runtime configuration (e.g., secrets, DB URI)
├── collab-sphere/               # Vue.js frontend application
│   ├── node_modules/            # Frontend dependencies
│   ├── public/                  # Static files
│   │   └── index.html
│   ├── src/                     # Frontend source files
│   │   ├── assets/              # Static assets like CSS
│   │   │   └── tailwind.css
│   │   ├── components/          # Reusable Vue components
│   │   │   ├── AllSummary.vue
│   │   │   ├── CommentComp.vue
│   │   │   ├── Dummy.vue
│   │   │   ├── EducationalInfo.vue
│   │   │   ├── Feed.vue
│   │   │   ├── JobInfo.vue
│   │   │   ├── Navbar1.vue
│   │   │   ├── NoticePost.vue
│   │   │   ├── OnBoarding.vue
│   │   │   ├── PersonalInfo.vue
│   │   │   ├── PreferenceInfo.vue
│   │   │   ├── ProjectSetting.vue
│   │   │   └── TempComp.vue
│   │   ├── pages/               # Page-level components for routing
│   │   │   ├── AskAI.vue
│   │   │   ├── Home.vue
│   │   │   ├── MyProjects.vue
│   │   │   ├── NewProject.vue
│   │   │   ├── ProjectPage.vue
│   │   │   ├── SignIn.vue
│   │   │   ├── SignUp.vue
│   │   │   └── WelCome.vue
│   │   ├── App.vue              # Root component
│   │   ├── main.js              # App entry point
│   │   ├── router.js            # Vue Router configuration
│   │   ├── store.js             # Vuex store (state management)
│   ├── .gitignore
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── README.md
│   ├── tailwind.config.js
│   └── vue.config.js
├── .gitignore
├── app.py                       # Backend app entry point
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---


## Backend Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/collab-sphere-backend.git
    ```

2. Navigate to the project directory:
    ```bash
    cd collab-sphere-backend
    ```

3. (Optional but recommended) Create a virtual environment:
    ```bash
    python -m venv .myenv
    source .myenv/bin/activate  # On Windows: .myenv\Scripts\activate
    ```

4. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Configuration

1. Create an `instance/config.py` or use environment variables for sensitive information like database URLs and secret keys.
2. Example variables you may need:
    ```python
    SECRET_KEY = 'your-secret-key'
    DATABASE_URI = 'your-database-uri'
    ```

---

## Running the Backend

Run the Flask application :

```bash
python app.py
```

By default, it will be accessible at http://127.0.0.1:5000.


## Frontend Installation

```bash
cd collab-sphere
npm install
npm run serve
```





