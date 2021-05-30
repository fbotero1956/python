

from wtforms import(
    Form,
    StringField,
    FloatField,
    IntegerField,
    TextField,
    SubmitField,
    validators
)

class ProductForm(Form):
    style = {"style": "width:100%"}
    name = StringField("Name",
                        [validators.required(), validators.length(min=4, max=45)],
                        render_kw=style)
    price = FloatField("Price", [validators.required()], render_kw=style)
    quantity = IntegerField("Quantity", [validators.required()], render_kw=style)
    description = TextField("Description", [validators.required()], render_kw=style)

class ReviewForm(Form):
    style = {"style": "width:100%"}
    name = StringField("Name",
                        [validators.required(), validators.length(min=4, max=45)],
                        render_kw=style)
    reviewText = TextField("Review", [validators.required()], render_kw=style)

class ProdReviewForm(Form):
    style = {"style": "width:100%"}
    name = StringField("Name",
                        [validators.required(), validators.length(min=4, max=45)],
                        render_kw=style)
    reviewText = TextField("Review", [validators.required()], render_kw=style)