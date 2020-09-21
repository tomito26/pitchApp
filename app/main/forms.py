from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField
   
   
class PitchForm(FlaskForm):
   category_id =SelectField('Selecte Category',choices=[('1','interview'),('2','Pick Up Lines'),('3','Promotion'),('4','Product')])
   content = TextAreaField('make a pitch',validators = [Required()])
   submit = SubmitField('Create Pitch')
   
   

class UpvoteForm(FlaskForm):
   '''
   Class to create a wtf form for upvoting a pitch
   '''
   submit = SubmitField('Upvote')
   
class DownvoteForm(FlaskForm):
   '''
   Class to create a wtf form for downvoting a pitch
   '''
   submit = SubmitField('Downvote')
   
class UpdateProfile(FlaskForm):
       bio = TextAreaField('Tell us about you.', validators=[Required()])
      