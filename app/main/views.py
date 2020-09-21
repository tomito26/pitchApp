from flask import render_template,redirect,url_for,abort,request
from . import main
from .forms import CommentsForm,UpdateProfile,PitchForm,UpvoteForm,DownvoteForm
from ..models import User,Pitch,Comment,PitchCategory,Downvote,Upvote
from .. import db,photos
import markdown2


#views
@main.route('/')
def index():
    '''
    View root page function that reeturns the index page and its data
    
    '''
    title = 'Home- Welcome PitchApp an applications that builds you'
    pitches = Pitch.get_all_pitches()
    
    
    
    return render_template('index.html' ,title = title,pitches=pitches)

@main.route('/interview/pitches/')
def all():
    '''
    View root page that returns the index page and its data
    '''
    pitches = Pitch.get_all_pitches()
    title = 'Interview Pitches'
    
   
    return render_template('interview.html', title=title,pitches = pitches)

@main.route('/pick_up_lines/pitches/')
def pick_up_lines():
    title = 'Pick Up Lines'
    pitches = Pitch.get_all_pitches()
    
    return render_template('pick_up_lines.html',title=title ,pitches = pitches)


@main.route('/promotion/pitches/')
def promotion():
    '''
    View root function that returns the index page and its data
    '''
    pitches = Pitch.get_all_pitches()
    title = 'Promotion Pitches'
    
    return render_template('promotion.html' ,title=title)
    
@main.route('/product/pitches/')
def product():
    '''
    view root funtion that returns the index page and its data
    '''
    title = 'Prroduct Pitches'
    pitches = Pitch.get_all_pitches()
    
    return render_template('product.html', title = title, pitches = pitches)

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
    found_pitch = Pitch.query.get(pitch_id)
    title = pitch_id
    
    pitch_comments = Comment.get_comments(pitch_id)
    return render_template('pitch.html' ,title = title,found_pitch = found_pitch,pitch_comments = pitch_comments )


@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    Function that creates new pitches
    '''
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    
    if category is None:
        abort(404)
        
        
    if form.validate_on_submit():
        pitch=form.content.data
        category_id = form.category_id.data
        new_pitch = Pitch(pitch=pitch,category_id = category_id)
        
        new_pitch.save_pitch()
        return redirect(url_for('main.all'))
    
    
    return render_template('new_pitch.html',new_pitch_form =form ,category = category )


@main.route('/category/<int:id>')
def category(id):
    '''
    Function that returns pitches based on the entered category
    '''
    category = PitchCategory.query.get(id)
    
    if category is None:
        abort(404)
        
    pitches_in_category = Pitch.get_pitch(id)
    return render_template('category.html',category = category,pitches = pitches_in_category)
@main.route('/pitch/comments/new/<int:id>', methods = ['GET','POST'])
@login_required
def  new_comment(id):
    form=  CommentsForm
    vote_form =UpvoteForm
    if form.validate_on_submit():
        new_comment = Comment(pitch_id = id,comment=form.comment.data,username=current_user.username)
        new_comment.save_comments()
        return redirect(url_for('main.all'))
    
    
    return render_template('new_comment.html',comment_form = form,vote_form = vote_form )


@
