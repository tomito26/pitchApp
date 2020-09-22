from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,current_user
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio  = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')
    downvotes  = db.relationship('Downvote',backref = 'user',lazy = 'dynamic')
    upvotes = db.relationship('Upvote',backref = 'user',lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
        


class Pitch(db.Model):
    __tablename__ = 'pitch'
    
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255))
    category_id = db.Column(db.Integer)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy='dynamic')
    upvotes = db.relationship('Upvote',backref = 'pitch',lazy = 'dynamic')
    downvotes = db.relationship('Downvote',backref = 'pitch',lazy = 'dynamic')
    
    
    def save_pitch(self):
        '''
        Function that saves the piches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the database and returns all the pictches
        '''
        return Pitch.query.all()
    
    @classmethod
    def get_pitches_by_category(cls,category_id):
        '''
        Function that queries the database and returns the pitches based on the category passed to it
        '''
        
        return Pitch.query.filter_by(category_id=category_id)
    
class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.String, primary_key = True)
    comment = db.Column(db.String)
    image_path =  db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    username = db.Column(db.String)
    
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(pitch_id=id).all()
        return comments
    
    @classmethod
    def clear_(cls):
        Comment.all_comments.clear
    
    
class PitchCategory:
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ = 'pitchcategories'
    id = db.Column(db.Integer,primary_key=True)
    name_of_category = db.Column(db.String(255))
    category_description = db.Column(db.String(255))
    
    @classmethod
    def get_categories(cls):
        '''
        This function fetches all the categories from database
        '''
        categories = PitchCategory.query.all()
        return categories

class Downvote(db.Model):
    
    __tablename__ = 'downvotes'
    
    '''
    function that stores user votes
    '''
    
    id = db.Column(db.Integer,primary_key = True)
    downvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_votes(self):
        db.session.add(self)
        db.session.commit()
        
        
    @classmethod
    def add_downvotes(cls,id):
        downvote_pitch = Downvote(user = current_user,pitch_id = id)
        downvote_pitch.save_downvotes()
    
    @classmethod
    def get_votes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
    
        
    def __repr__(self):
        return f'{self.id_user},{self.pitch_id}'
    
    
class Upvote(db.Model):
    
    __tablename__ = 'upvotes'
    '''
    Function stores user votes
    '''
    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    
    def save_votes(self):
        db.session.add(self)
        db.session.commit()
        
    
    @classmethod
    def add_upvotes(cls,id):
        upvote = Upvote.query.filter_by(pitch_id = id).all()
        
        
    def __repr__(self):
        return f'{self.id_user}:{self.picth_id}'