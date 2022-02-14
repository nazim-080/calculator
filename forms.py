from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import InputRequired, NumberRange


class SquareForm(FlaskForm):
    side = FloatField('Длина стороны', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class RectangleForm(FlaskForm):
    length = FloatField('Длина', validators=[InputRequired(), NumberRange(min=1)])
    width = FloatField('Ширина', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class TriangleForm(FlaskForm):
    side_a = FloatField('Сторона A', validators=[InputRequired(), NumberRange(min=1)])
    side_b = FloatField('Сторона B', validators=[InputRequired(), NumberRange(min=1)])
    angle = FloatField('Угол между A и B', validators=[InputRequired(), NumberRange(min=1, max=180)])
    submit = SubmitField('Ввести')


class TrapezoidForm(FlaskForm):
    upper_base = FloatField('Верхнее основание', validators=[InputRequired(), NumberRange(min=1)])
    lower_base = FloatField('Нижнее основание', validators=[InputRequired(), NumberRange(min=1)])
    height = FloatField('Высота', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class RhombForm(FlaskForm):
    side = FloatField('Сторона', validators=[InputRequired(), NumberRange(min=1)])
    angle = FloatField('Угол', validators=[InputRequired(), NumberRange(min=1, max=179)])
    submit = SubmitField('Ввести')


class CircleForm(FlaskForm):
    radius = FloatField('Радиус', validators=[InputRequired(), NumberRange(min=1, max=360)])
    submit = SubmitField('Ввести')


class PyramidForm(FlaskForm):
    base_side = FloatField('Сторона основания', validators=[InputRequired(), NumberRange(min=1)])
    height = FloatField('Высота', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class CubeForm(FlaskForm):
    side = FloatField('Ребро', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class SphereForm(FlaskForm):
    radius = FloatField('Радиус', validators=[InputRequired(), NumberRange(min=1, max=360)])
    submit = SubmitField('Ввести')


class ParallelepipedForm(FlaskForm):
    length = FloatField('Длина', validators=[InputRequired(), NumberRange(min=1)])
    width = FloatField('Ширина', validators=[InputRequired(), NumberRange(min=1)])
    height = FloatField('Высота', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Ввести')


class CylinderForm(FlaskForm):
    height = FloatField('Высота', validators=[InputRequired(), NumberRange(min=1)])
    radius = FloatField('Радиус', validators=[InputRequired(), NumberRange(min=1, max=360)])
    submit = SubmitField('Ввести')


class ConeForm(FlaskForm):
    height = FloatField('Высота', validators=[InputRequired(), NumberRange(min=1)])
    radius = FloatField('Радиус', validators=[InputRequired(), NumberRange(min=1, max=360)])
    submit = SubmitField('Ввести')
