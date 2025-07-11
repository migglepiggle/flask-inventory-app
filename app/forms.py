from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class InventoryForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(max=100)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    unit = StringField('Unit (e.g., kg, L, pcs)', validators=[DataRequired(), Length(max=50)])
    category = SelectField(
        'Category',
        choices=[
            ('vegetables', 'Vegetables'),
            ('meat', 'Meat'),
            ('dairy', 'Dairy'),
            ('drinks', 'Drinks'),
            ('other', 'Other')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')
