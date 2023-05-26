from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, BooleanField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError, Email
from application.model import User


class Sign_up(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(),
                                             Length(min=2, max=100)])
    firstname = StringField('Фамилия', validators=[DataRequired(),
                                             Length(min=2, max=100)])                                        
    gmail = StringField('Ведите Gmail',validators = [Email()])
    readbilet = StringField('Username', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                             Length(min=8, max=100)])                                                                                
    cover = FileField('Лицо', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Авторизация')                                             
    
    def validate_readbilet(self, readbilet):
        readbilet = User.query.filter_by(readbilet=readbilet.data).first()
        if readbilet:
            raise ValidationError('Номер читательского билета уже используется')
