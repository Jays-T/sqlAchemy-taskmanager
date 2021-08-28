from taskmanager import db

class UserAccount(db.Model):
    """
    User capable of adding tasks

    :param str email: email address of user
    :param str username: username of user
    :param str password: encrypted password for the user
    
    """
    __tablename__ = "user_account"

    email = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(12), nullable=False)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    tasks = db.relationship("Task", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username

    def user_tasks(self):
        return self.tasks

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


class Task(db.Model):
    # schema for Task model
    user = db.Column(db.Integer, db.ForeignKey('user_account.email', ondelete="CASCADE"), nullable=False)
    created_by = db.relationship("UserAccount", backref="user_account.username", lazy=True)
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey("day.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2} | Day: {3} | Created By: {4}".format(
            self.id, self.task_name, self.is_urgent, self.day_id, self.created_by
        )


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_name = db.Column(db.String(10), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="day", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.day_name
