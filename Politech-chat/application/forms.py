from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, BooleanField, PasswordField, EmailField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Email
from application.models import User

class MessageForm(FlaskForm):    # Create Message Form
    body = StringField('', [Length(min=1)], render_kw={'autofocus': True})
    submit = SubmitField('Отправить')

class Sign_in(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                             Length(min=2, max=100)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                             Length(min=2, max=100)])
    remember = BooleanField("Запомнить меня")                                        
    submit = SubmitField('Вход')

class Sign_up(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),
                                             Length(min=2, max=100)])
    firstname = StringField('Фамилия', validators=[DataRequired(),
                                             Length(min=2, max=100)])           
    username = StringField('Username', validators=[DataRequired(),
                                             Length(min=2, max=100)])                              
    gmail = EmailField('Ведите Gmail',validators = [Email()])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                             Length(min=8, max=100)])                                                                                
    kyrs = IntegerField('Ведите курс', validators=[DataRequired(), NumberRange(min=1, max=4)])

    submit = SubmitField('Авторизация')                                             
    
    def validate_readbilet(self, username):
        username = User.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('Это имя уже используется')
        
