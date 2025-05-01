from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String, unique=True, nullable=False)

    roles = db.Relationship('Role', backref='users', secondary='user_roles')
    projects = db.relationship('Project', backref='creator', lazy=True)
    profile = db.relationship('UserProfile', backref='user', uselist=False, cascade="all, delete-orphan")
    interests = db.relationship('ProjectInterest', backref='interested_user', lazy=True, cascade="all, delete-orphan")
    user_projects = db.relationship('UserProject', backref='participant', lazy=True, cascade="all, delete-orphan")
    saved_projects = db.relationship('SavedProject', backref='user', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='user', lazy=True, cascade="all, delete-orphan")  
    replies = db.relationship('Reply', backref='user', lazy=True, cascade="all, delete-orphan")

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


project_categories = db.Table('project_categories',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), nullable=False)
)

project_tags = db.Table('project_tags',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), nullable=False)
)


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False,unique=True)
    slug=db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    status = db.Column(db.String(20), default='open')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    interests = db.relationship('ProjectInterest', backref='project', lazy=True, cascade="all, delete-orphan")
    user_projects = db.relationship('UserProject', backref='project', lazy=True, cascade="all, delete-orphan")
    saved_by_users = db.relationship('SavedProject', backref='project', lazy=True, cascade="all, delete-orphan")
    tags = db.relationship('Tag', secondary=project_tags, backref='projects')
    categories = db.relationship('Category', secondary=project_categories, backref='projects')
    notices = db.relationship('ProjectNotice', backref='project', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='project', lazy=True)


class ProjectInterest(db.Model):
    __tablename__ = 'project_interest'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class SavedProject(db.Model):
    __tablename__ = 'saved_project'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class UserProject(db.Model):
    __tablename__ = 'user_project'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    status = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bio = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    github = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    website = db.Column(db.String(100))
    interests = db.Column(db.Text)
    languages = db.Column(db.Text)
    tools = db.Column(db.Text)
    skills = db.Column(db.Text)

    education = db.relationship('UserEducation', backref='user_profile', lazy=True, cascade="all, delete-orphan")
    jobs = db.relationship('UserJob', backref='user_profile', lazy=True, cascade="all, delete-orphan")


class UserEducation(db.Model):
    __tablename__ = 'user_education'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    current = db.Column(db.Boolean, default=False)


class UserJob(db.Model):
    __tablename__ = 'user_job'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    current_job = db.Column(db.Boolean, default=False)


class ProjectNotice(db.Model):
    __tablename__ = 'project_notice'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    like_count = db.Column(db.Integer, default=0)
    visibility = db.Column(db.String(20), default='public')
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    replies = db.relationship('Reply', backref='comment', lazy=True)


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
