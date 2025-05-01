from flask import current_app as app
from flask import request,jsonify
from flask_security import auth_required, verify_password,auth_required,hash_password,current_user
# from backend.models import db,User,LibRec,BG,Department,Project,UserProjectAssignment
from backend.models import db, User,UserProfile,UserEducation,UserJob,Project,Category,Tag , ProjectInterest,Comment,Reply,ProjectNotice
from flask_restful import Resource, Api,marshal_with, fields,reqparse
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
import re
api = Api()



class AuthApi(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        print(email)
        password = data.get('password')
        print(password)
        user = app.security.datastore.find_user(email=data.get('email'))
        print(user)
        if user and verify_password(password, user.password):
            profile = UserProfile.query.filter_by(user_id=user.id).first()
            onboarding_completed = False
            if profile:
                onboarding_completed = True
            return {"message": "Login successful", "user": {"id": user.id, "name": user.name,"token" :user.get_auth_token() , "onboarding_completed": onboarding_completed}}, 200
        else:
            return {"message": "Invalid credentials"}, 401

class RegisterApi(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not name or not email or not password:
            return {"message": "Missing required fields"}, 400
        if app.security.datastore.find_user(email=email):
            return {"message": "User already exists"}, 400
        new_user =app.security.datastore.create_user(name=name, email=email, password=hash_password(password))
        
        db.session.commit()
        return {"message": "User created successfully"}, 201        

def parse_date(date_str):
    try:
        if date_str:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        pass
    return None

def format_date(date):
    return date.strftime('%Y-%m-%d') if date else None
class ProfileApi(Resource):
    @auth_required('token')
    def post(self):
        data = request.get_json()
        print(data)
        if not data:
            return {"error": "No input data provided"}, 400

        
        interests = data.get("interests", [])
        programming_languages = data.get("programmingLanguages", [])
        tools = data.get("tools", [])

        # ---------------------
        # PERSONAL INFO
        # ---------------------
        personal = data.get("personalinfo", {})
        print("personal", personal)
        firstname = personal.get("firstname", "").strip()
        lastname = personal.get("lastname", "").strip()

        print("first name", firstname)
        if not firstname or not lastname:
            print("yes")
            return {"error": "First and last name are required."}, 400

        # Upsert UserProfile
        profile = UserProfile.query.filter_by(user_id=current_user.id).first()
        if not profile:
            profile = UserProfile(user_id=current_user.id)

        profile.bio = personal.get("bio", "")
        profile.age = int(personal.get("age") or 0)
        profile.gender = personal.get("gender", "")
        profile.city = personal.get("city", "")
        profile.country = personal.get("country", "")
        profile.github = personal.get("github", "")
        profile.linkedin = personal.get("linkedin", "")
        profile.website = personal.get("website", "")
        profile.interests = ",".join(interests)
        profile.languages = ",".join(programming_languages)
        profile.tools = ",".join(tools)

        db.session.add(profile)
        db.session.commit()

        # ---------------------
        # EDUCATION
        # ---------------------
        education_list = data.get("educationList", [])
        UserEducation.query.filter_by(profile_id=profile.id).delete()

        for edu in education_list:
            if not edu.get("institution") or not edu.get("degree"):
                continue

            education = UserEducation(
                profile_id=profile.id,
                institution=edu["institution"],
                degree=edu["degree"],
                start_date=parse_date(edu.get("startYear")),
                end_date=parse_date(edu.get("endYear")) if not edu.get("present") else None,
                current=edu.get("present", False)
            )
            db.session.add(education)

        # ---------------------
        # JOBS
        # ---------------------
        job_list = data.get("jobList", [])
        UserJob.query.filter_by(profile_id=profile.id).delete()

        for job in job_list:
            if not job.get("company") or not job.get("position"):
                continue

            user_job = UserJob(
                profile_id=profile.id,
                company=job["company"],
                position=job["position"],
                start_date=parse_date(job.get("startDate")),
                end_date=parse_date(job.get("endDate")) if not job.get("currentJob") else None,
                current_job=job.get("currentJob", False)
            )
            db.session.add(user_job)

        db.session.commit()
        return {"message": "Profile updated successfully"}, 200
    def get(self):
        user = current_user
        profile = user.profile

        return {
            'name': user.name,
            'profile': {
                'bio': profile.bio,
                'linkedin': profile.linkedin,
                'github': profile.github,
                'website': profile.website,
                'skills': profile.languages,
                'tools': profile.tools,
                'interests': profile.interests,
                'education': [
                    {
                        'id': edu.id,
                        'institution': edu.institution,
                        'degree': edu.degree,
                        'start_date': format_date(edu.start_date),
                        'end_date': format_date(edu.end_date),
                        'current': edu.current
                    } for edu in profile.education
                ],
                'jobs': [
                    {
                        'id': job.id,
                        'company': job.company,
                        'position': job.position,
                        'start_date': format_date(job.start_date),
                        'end_date': format_date(job.end_date),
                        'current_job': job.current_job
                    } for job in profile.jobs
                ]
            }
        },200

# print(current_user.id)



def serialize_project(project, cu=None):
    has_shown_interest = False
    if cu:
        has_shown_interest = any(interest.user_id == cu.id for interest in project.interests)

    return {
        "id": project.id,
        "title": project.title,
        "slug": project.slug,
        "description": project.description,
        "status": project.status,
        "created_at": project.created_at.strftime("%b %d, %Y %I:%M %p"),
        "tags": [tag.name for tag in project.tags],
        "categories": [cat.name for cat in project.categories],
        "created_by": project.creator.name if project.creator else None,
        "interests": len(project.interests),
        "interested_by_user": has_shown_interest
    }



class FeedApi(Resource):
    @auth_required('token')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        projects = Project.query.filter(Project.created_by != current_user.id).paginate(
    page=page, per_page=per_page, error_out=False
)       
        print(projects.items)

        serialized_projects = [serialize_project(project,current_user) for project in projects.items]
        return {
            "projects": serialized_projects,
            "total": projects.total,
            "page": projects.page,
            "pages": projects.pages
        }



def create_project_slug(title):
    # Convert to lowercase
    lower_case_title = title.lower()

    # Replace spaces and underscores with hyphens
    hyphenated_title = re.sub(r'[\s_]+', '-', lower_case_title)

    # Remove non-alphanumeric characters except for hyphens
    slug = re.sub(r'[^a-z0-9-]', '', hyphenated_title)

    # Ensure the slug is not empty
    return slug if slug else 'untitled-project'

    
class ProjectApi(Resource):
    @auth_required('token')
    def post(self):
        data = request.get_json()

        title = data.get('title')
        description = data.get('description')
        tag_names = data.get('tags', [])
        category_names = data.get('categories', [])

        if not title or not description:
            return {'error': 'Title and description are required'}, 400

        # Fetch or create tags
        slug = create_project_slug(title)
        tags = []
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
                db.session.add(tag)
            tags.append(tag)

        # Fetch or create categories
        categories = []
        for name in category_names:
            category = Category.query.filter_by(name=name).first()
            if not category:
                category = Category(name=name)
                db.session.add(category)
            categories.append(category)

        # Create project
        print(tags)
        new_project = Project(
            title=title,
            description=description,
            slug=slug,
            created_by=current_user.id,  # Assumes Flask-Login
            tags=tags,
            categories=categories
        )

        db.session.add(new_project)
        db.session.commit()


        return {'message': 'Project created successfully', 'project_id': new_project.id}, 201

    def get(self, slug):
        project = Project.query.filter_by(slug=slug).first()
        if not project:
            return {'error': 'Project not found'}, 404

        serialized_project = serialize_project(project)
        return serialized_project, 200

# class CategoryApi(Resource):
#     @auth_required('token')
#     def get(self):
#         categories = Category.query.all()
#         return {"categories": [category.name for category in categories]
class MyProjectsApi(Resource):
    @auth_required('token')
    def get(self):
        
        if request.args.get("query") =="created":
            projects = Project.query.filter_by(created_by=current_user.id).all()

            serialized_projects = [serialize_project(project) for project in projects]
            return {
                "projects": serialized_projects,
            }
        elif request.args.get("query") == "interested":
            projects = Project.query.join(ProjectInterest).filter(ProjectInterest.user_id == current_user.id).all()
            serialized_projects = [serialize_project(project) for project in projects]
            return {
                "projects": serialized_projects,
            }

existing_usernames = ["johndoe", "janedoe", "admin"]

class UserApi(Resource):
    def post(self):
        
        action = request.args.get("action")
        if action == "checkusername":
            payload = request.get_json(force=True)  
            username = payload.get("username", "").strip().lower()
            return { "exists": username.lower() in [u.lower() for u in existing_usernames] }, 200

        return { "error": "Invalid action" }, 400


class UtilityApi(Resource):
    @auth_required('token')
    def post(self):
        if request.args.get("action") == "showinterest":
            slug = request.args.get("slug")
            project = Project.query.filter_by(slug=slug).first()
            if not project:
                return {'error': 'Project not found'}, 404
            if ProjectInterest.query.filter_by(user_id=current_user.id , project_id = project.id).first():
                return {'error': 'Already shown interest'}, 400
            interest = ProjectInterest(user_id=current_user.id, project_id=project.id)
            db.session.add(interest)
            db.session.commit()
            return {'message': 'Interest shown successfully'}, 200
        elif request.args.get("action") == "postnotice":
            slug = request.args.get("slug")
            project = Project.query.filter_by(slug=slug).first()
            if not project:
                return {'error': 'Project not found'}, 404
            data = request.get_json()
            title = data.get('title')
            content = data.get('content')
            visibility = data.get('visibility', 'public')
            if not title or not content:
                return {'error': 'Title and content are required'}, 400
            new_notice = ProjectNotice(
                title=title,
                content=content,
                visibility=visibility,
                project_id=project.id,
                user_id=current_user.id
            )
            db.session.add(new_notice)      
            db.session.commit()
            return {'message': 'Notice posted successfully'}, 201
        

        return { "error": "Invalid action" }
    @auth_required('token')
    def get(self):
        if request.args.get("action") == "fetchnotices":
            slug = request.args.get("slug")
            project = Project.query.filter_by(slug=slug).first()
            if not project:
                return {'error': 'Project not found'}, 404
            notices = ProjectNotice.query.filter_by(project_id=project.id).order_by(desc(ProjectNotice.timestamp)).all()
            serialized_notices = []
            for notice in notices:
                serialized_notices.append({
                    "id": notice.id,
                    "title": notice.title,
                    "content": notice.content,
                    "likes": notice.like_count,
                    "visibility": notice.visibility,
                    "project_id": notice.project_id,
                    "author": notice.project.creator.name,
                    "timestamp": notice.timestamp.strftime("%b %d, %Y %I:%M %p")

                })
            return {"notices": serialized_notices}, 200
        elif request.args.get("action") == "fetchinterested":
            slug = request.args.get("slug")
            project = Project.query.filter_by(slug=slug).first()
            if not project:
                return {'error': 'Project not found'}, 404
            interests = ProjectInterest.query.filter_by(project_id=project.id).all()
            serialized_interests = []
            for interest in interests:
                serialized_interests.append({
                    "id": interest.id,
                    "user_id": interest.user_id,
                    "username": interest.interested_user.name
                })
            print(serialized_interests)
            return  serialized_interests, 200



class CommentApi(Resource):
    @auth_required('token')
    def get(self):
        slug = request.args.get("slug")
        if not slug:
            return {'error': 'Project slug is required'}, 400
        project = Project.query.filter_by(slug=slug).first_or_404()
        comments = Comment.query.filter_by(project_id=project.id).all()
        result = []
        for c in comments:
            result.append({
                "id": c.id,
                "text": c.text,
                "username": c.user.name,
                "timestamp": c.timestamp.strftime("%d %b %I:%M %p"),
                "replies": [{
                    "text": r.text,
                    "username": r.user.name,
                    "timestamp": r.timestamp.strftime("%d %b %I:%M %p")
                } for r in c.replies]
            })
        return {"comments": result}, 200
    @auth_required('token')
    def post(self):
        slug= request.args.get("slug")
        if not slug:
            return {'error': 'Project slug is required'}, 400
        data = request.get_json()
        project = Project.query.filter_by(slug=slug).first_or_404()
        new_comment = Comment(
            text=data['text'],
            user_id=current_user.id,
            project_id=project.id
        )
        db.session.add(new_comment)
        db.session.commit()
        return {"message": "Comment added"}, 201

class ReplyApi(Resource):
    @auth_required('token')
    def post(self):
        data = request.get_json()
        comment_id = request.args.get("comment_id")
        if not comment_id:
            return {'error': 'Comment ID is required'}, 400
        comment = Comment.query.get_or_404(comment_id)
        new_reply = Reply(
            text=data['text'],
            user_id=current_user.id,
            comment_id=comment.id
        )
        db.session.add(new_reply)
        db.session.commit()
        return jsonify({"message": "Reply added"}), 201
    
api.add_resource(AuthApi, '/api/signin')
api.add_resource(RegisterApi, '/api/signup')
api.add_resource(ProfileApi,"/api/user-profile")
api.add_resource(FeedApi,"/api/feed")
api.add_resource(ProjectApi,"/api/project" ,"/api/project/<string:slug>")
api.add_resource(UtilityApi,"/api/utilities")
api.add_resource(CommentApi,"/api/comments")
api.add_resource(MyProjectsApi,"/api/myprojects")
api.add_resource(UserApi,"/api/user")