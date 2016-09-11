from wtforms import Form, BooleanField, DateTimeField, TextAreaField, TextField, SelectField
from wtforms.validators import Length, required

class FeatureRequestForm(Form):
    title = TextField('Title', [Length(max=80)])
    description = TextField([Length(max=2000)])
    client = SelectField('Select client:',
            choices=[('1', 'Client 1'), ('2', 'Client 2'), ('3', 'Client 3'), ('4', 'Client 4'), ('5', 'Client 5')])


if __name__ == '__main__':
    form = FeatureRequestForm()
    print(form.client)
