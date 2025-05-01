from flask import current_app as app
from backend.models import db, User, Role,Category , Project,Tag,ProjectNotice
from flask_security import hash_password


with app.app_context():
    db.create_all()

    userdatastore = app.security.datastore

    userdatastore.find_or_create_role(name = "admin", description = "Administrator")
    userdatastore.find_or_create_role(name = "user", description = "User")
    db.session.commit()

    if not userdatastore.find_user(email = "admin@gmail.com"):
        user = userdatastore.create_user(name = "admin", email = "admin@gmail.com" , password = hash_password("pass") , roles = ["admin"])
    if not userdatastore.find_user(email = "user1@gmail.com"):
        user = userdatastore.create_user(name = "user1", email = "user1@gmail.com" , password = hash_password("pass") , roles = ["user"])
    if not userdatastore.find_user(email = "Himanshu@gmail.com"):
        user = userdatastore.create_user(name = "Himanshu Saini", email = "Himanshu@gmail.com", password = hash_password("pass") , roles = ["user"])

    if Category.query.count() == 0:
        categories = [
            Category(name="Web Development"),
            Category(name="Mobile Development"),
            Category(name="Data Science"),
            Category(name="Machine Learning"),
            Category(name="AI & LLMs"),
            Category(name="Cybersecurity"),
            Category(name="Cloud Computing"),
            Category(name="DevOps"),
            Category(name="UI/UX Design"),
            Category(name="Game Development"),
            Category(name="Blockchain"),
            Category(name="Open Source"),
            Category(name="Competitive Coding"),
            Category(name="IoT & Robotics")
        ]
        db.session.add_all(categories)
        db.session.commit()
    if Tag.query.count() == 0:
        tags = [
            Tag(name="python"),
            Tag(name="javascript"),
            Tag(name="react"),
            Tag(name="vue"),
            Tag(name="flask"),
            Tag(name="django"),
            Tag(name="fastapi"),
            Tag(name="java"),
            Tag(name="c++"),
            Tag(name="nodejs"),
            Tag(name="sql"),
            Tag(name="mongodb"),
            Tag(name="firebase"),
            Tag(name="pandas"),
            Tag(name="numpy"),
            Tag(name="tensorflow"),
            Tag(name="pytorch"),
            Tag(name="api-integration"),
            Tag(name="docker"),
            Tag(name="kubernetes"),
            Tag(name="aws"),
            Tag(name="gcp"),
            Tag(name="linux"),
            Tag(name="figma"),
            Tag(name="html"),
            Tag(name="css"),
            Tag(name="tailwind"),
            Tag(name="openai"),
            Tag(name="llama"),
            Tag(name="github-actions"),
            Tag(name="web3"),
            Tag(name="solidity")
        ]
        db.session.add_all(tags)
        db.session.commit()

    
   
    if Project.query.count() == 0:
        web_dev = Category.query.filter_by(name='Web Development').first()
        ml = Category.query.filter_by(name='Machine Learning').first()
        devops = Category.query.filter_by(name='DevOps').first()
        python = Tag.query.filter_by(name="python").first()
        javascript = Tag.query.filter_by(name="javascript").first()
        react = Tag.query.filter_by(name="react").first()
        vue = Tag.query.filter_by(name="vue").first()
        flask = Tag.query.filter_by(name="flask").first()
        django = Tag.query.filter_by(name="django").first()
        fastapi = Tag.query.filter_by(name="fastapi").first()
        java = Tag.query.filter_by(name="java").first()
        c_plus_plus = Tag.query.filter_by(name="c++").first()
        nodejs = Tag.query.filter_by(name="nodejs").first()
        sql = Tag.query.filter_by(name="sql").first()
        mongodb = Tag.query.filter_by(name="mongodb").first()
        firebase = Tag.query.filter_by(name="firebase").first()
        pandas = Tag.query.filter_by(name="pandas").first()
        numpy = Tag.query.filter_by(name="numpy").first()
        tensorflow = Tag.query.filter_by(name="tensorflow").first()
        pytorch = Tag.query.filter_by(name="pytorch").first()
        api_integration = Tag.query.filter_by(name="api-integration").first()
        docker = Tag.query.filter_by(name="docker").first()
        kubernetes = Tag.query.filter_by(name="kubernetes").first()
        aws = Tag.query.filter_by(name="aws").first()
        gcp = Tag.query.filter_by(name="gcp").first()
        linux = Tag.query.filter_by(name="linux").first()
        figma = Tag.query.filter_by(name="figma").first()
        html = Tag.query.filter_by(name="html").first()
        css = Tag.query.filter_by(name="css").first()
        tailwind = Tag.query.filter_by(name="tailwind").first()
        openai = Tag.query.filter_by(name="openai").first()
        llama = Tag.query.filter_by(name="llama").first()
        github_actions = Tag.query.filter_by(name="github-actions").first()
        web3 = Tag.query.filter_by(name="web3").first()
        solidity = Tag.query.filter_by(name="solidity").first()

        projects = [
            Project(
                title="Build a Vue + Flask Web App",
                slug="build-a-vue-flask-web-app",
                description="Create a full-stack CRUD web app using Vue.js for frontend and Flask for backend.",
                
                created_by=3,
                categories=[web_dev],
                tags=[vue, flask]
            ),
            Project(
                title="Sentiment Analysis on Tweets",
                slug="sentiment-analysis-on-tweets",
                description="Use Python and scikit-learn to perform sentiment analysis on Twitter data.",
                
                created_by=3,
                categories=[ml],
                tags=[pandas, numpy]
            ),
            Project(
                title="Design Portfolio Website",
                slug="design-portfolio-website",
                description="A responsive personal portfolio using HTML, CSS, and JavaScript.",
                
                created_by=3,
                categories=[web_dev],
                tags=[javascript, html, css]
            ),
            
            Project(
                title="E-commerce Dashboard",
                slug="ecommerce-dashboard",
                description="Create an admin dashboard for an online store with data visualizations.",
                
                created_by=3,
                categories=[web_dev],
                tags=[ javascript , react, nodejs]
            ),
            Project(
                title="Loan Prediction ML Model",
                slug="loan-prediction-ml-model",
                description="Build a classification model to predict loan default using tabular data.",
                
                created_by=3,
                categories=[ml],
                tags=[ pandas, numpy]
            ),
            Project(
                title="To-do App with Firebase",
                slug="todo-app-with-firebase",
                description="Develop a real-time to-do list app using Vue.js and Firebase.",
                
                created_by=3,

                categories=[web_dev],
                tags=[firebase, vue]
            ),
            Project(
                title="Image Classification using CNNs",
                slug="image-classification-using-cnns",
                description="Classify images using convolutional neural networks (CNNs) with TensorFlow.",
                
                created_by=3,
                categories=[ml],
                tags=[tensorflow]
            ),
            Project(
                title="Online Code Editor",
                slug="online-code-editor",
                description="Build a collaborative online code editor with real-time sync.",
                
                created_by=3,
                categories=[web_dev],
                tags=[javascript, react]
            ),
            Project(
                title="Student Feedback Classifier",
                slug="student-feedback-classifier",
                description="Analyze student feedback and classify it as positive/negative using ML.",
                
                created_by=3,
                categories=[ml],
                tags=[pandas, numpy]
            ),
            Project(
                title="DevOps Automation Tool",
                slug="devops-automation-tool",
                description="Scripted automation tool for CI/CD using GitHub Actions.",
                
                created_by=3,
                categories=[devops],
                tags=[docker, kubernetes, aws]
            ),
            Project(
                title="Real-Time Weather App",
                slug="real-time-weather-app",
                description="Build a weather app using public weather APIs and display data live.",
                
                created_by=3,
                categories=[web_dev],
                tags=[javascript, api_integration]
            ),
            Project(
                title="Traffic Sign Detection",
                slug="traffic-sign-detection",
                description="Train an object detection model to recognize traffic signs.",
                
                created_by=3,
                categories=[ml],
                tags=[tensorflow, pytorch]
            ),
            Project(
                title="Build a URL Shortener",
                slug="build-a-url-shortener",
                description="Create a backend service that shortens URLs and tracks click stats.",
                
                created_by=3,
                categories=[web_dev],
                tags=[javascript, nodejs, sql]
            ),
            Project(
                title="Resume Ranking System",
                slug="resume-ranking-system",
                description="Develop an ML-based system that ranks resumes based on job requirements.",
                
                created_by=3,
                categories=[ml],
                tags=[ pandas, numpy]
            )]
        
        db.session.add_all(projects)
        db.session.commit()
        if ProjectNotice.query.count() == 0:
            notices = [
                ProjectNotice(
                    
                    title="Project 1 Notice1",
                    content="This is a notice for Project 1.",
                    user_id = 3,
                   
                    project_id=1
                ),
                ProjectNotice(
                    
                    title="Project 1 Notice2",
                    content="This is a notice for Project 1.",
                    user_id = 3,
                   
                    project_id=1
                ),
                ProjectNotice(
                  
                    title="Project 1 Notice 3",
                    content="This is a notice for Project 1.",
                    user_id = 3,
                 
                    project_id=1,
                )
            ]
            db.session.add_all(notices)
            db.session.commit()
    