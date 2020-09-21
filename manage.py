from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Comment,Pitch,PitchCategory,Upvote,Downvote
from flask_migrate import Migrate,MigrateCommand

# creating app instance 
app = create_app('development')
migrate = Migrate(app,db)



manager = Manager(app)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User,Comment = Comment, Pitch = Pitch,PitchCategory = PitchCategory,Downvote = Downvote,Upvote = Upvote)
if __name__ == '__main__':
    manager.run()