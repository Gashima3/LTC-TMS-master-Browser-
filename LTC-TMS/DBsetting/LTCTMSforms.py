#
# User Management Forms
# author: Mason Hoffman, Nathan Yost
# created: 2/13/2018
# latest: 2/13/2018
# purpose: Team B's form classes for WTForms
#

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, \
    BooleanField, FieldList, FormField, FileField, RadioField, SelectField, \
    TextAreaField, HiddenField
from wtforms.validators import InputRequired, EqualTo, Email, DataRequired

# Login form
class LoginForm(FlaskForm):
    staffID = StringField('staffID', [InputRequired()])
    password = PasswordField('password', [InputRequired()])
    loginButton = SubmitField('Login')


# Requirement 29, 30
class EditSuper(FlaskForm):
    #person = StringField("Person being editted (ie: email)", [Email(), InputRequired()])
    #is_supervisor = BooleanField("Is Supervisor?")
#    password = StringField("*Password", [InputRequired()])
    phone = StringField("Phone")
    fname = StringField("*First Name", [InputRequired()])
    mname = StringField("Middle Name")
    lname = StringField("*Last Name", [InputRequired()])
    gender = RadioField("*Gender", choices = [("male","Male"),("female","Female"),("other","Other")])
    birthday = DateField("*Birthday", format="%Y-%m-%d")
    affiliation = StringField("*Affiliation", [InputRequired()])
    ethnicity = StringField("*Ethnicity", [InputRequired()])
    picture = StringField("Picture")
    submit = SubmitField("Submit Edit")


class EditSenior(FlaskForm):
    #person = StringField("Person being editted (ie: email)", [Email(), InputRequired()])
    #is_supervisor = BooleanField("Is Supervisor?")
    phone = StringField("Phone")
    fname = StringField("*First Name", [InputRequired()])
    mname = StringField("Middle Name")
    lname = StringField("*Last Name", [InputRequired()])
    gender = RadioField ("*Gender", choices = [("male","Male"),("female","Female"),("other","Other")])
    birthday = DateField("*Birthday", format="%Y-%m-%d")
    affiliation = StringField("*Affiliation", [InputRequired()])
    ethnicity = StringField("*Ethnicity", [InputRequired()])
    picture = StringField("Picture")
    submit = SubmitField("Submit Edit")


# Requirement 31
class AddUser(FlaskForm):
    supervisor_email = StringField("Supervisor", [InputRequired()])
    user = BooleanField("Assign User")
    submit = SubmitField("Add User(s)")


# Requirement 33
class AssignUser(FlaskForm):
    supervisor = StringField("Supervisor", [InputRequired()])
    user = StringField("User", [InputRequired()])
    submit = SubmitField("Re-assign user")


class DetailedStep(FlaskForm):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    title = StringField('Detailed Step Name:')
    voice_button_title = SubmitField('SPEECH')
    stepText = TextAreaField('Detailed Step Description:')
    voice_button_stepText = SubmitField('SPEECH')
    image = FileField('Upload Image for Detailed Step:')
    detailed_step_removal = SubmitField('- Detailed Step')

    @staticmethod
    def process_data(data):
        return data


class MainStep(FlaskForm):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    title = StringField('Main Step Title:')
    voice_button_title = SubmitField('SPEECH')
    requiredItem = StringField('Required Items:')
    voice_button_requiredItem = SubmitField('SPEECH')
    stepText = TextAreaField('Main Step Description:')
    voice_button_stepText = SubmitField('SPEECH')
    audio = FileField('Upload Audio:')
    image = FileField('Upload Image:')
    video = FileField('Upload Video:')

    detailed_steps = FieldList(FormField(DetailedStep), min_entries=0)

    add_detailed_step = SubmitField('+ Detailed Step')
    main_step_removal = SubmitField('- Main Step')

    @staticmethod
    def process_data(data):
        return data


class CreateTaskForm(FlaskForm):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    title = StringField('Task Name:', validators=[DataRequired()])
    voice_button_title = SubmitField('SPEECH')
    description = TextAreaField('Description:')
    voice_button_description = SubmitField('SPEECH')
    image = FileField('Upload image for Task:')

    main_steps = FieldList(FormField(MainStep), min_entries=0)

    add_main_step = SubmitField('+ Main Step')
    save = SubmitField('Save')
    activation = BooleanField('Activate task for personal use?', default=False)
    publish = BooleanField('Publish task for use by everyone?', default=False)
    keywords = TextAreaField('Keywords:')


    claim = HiddenField("")

    @staticmethod
    def process_data(data):
        return data


class TaskAssignmentForm(FlaskForm):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    assigned_users = SelectField('Select user...', choices=[])
    assign_task_button = SubmitField('Assign Task')
    view_assigned_tasks_button = SubmitField('View Assigned Tasks')
    tasks = SelectField('Select task...', choices=[])
    assign_button = SubmitField('Assign')
    remove_button = SubmitField('Remove')

    @staticmethod
    def process_data(data):
        return data
