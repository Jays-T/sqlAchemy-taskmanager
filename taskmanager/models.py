from taskmanager import db


class Category(db.Model):
    # schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


class Task(db.Model):
    # schema for Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    day_id = db.Column(db.Integer, db.ForeignKey("day.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2} | Day: {3}".format(
            self.id, self.task_name, self.is_urgent, self.day_id
        )


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_name = db.Column(db.String(10), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="day", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.day_name
