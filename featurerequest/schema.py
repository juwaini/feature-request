from marshmallow import Schema, fields, pprint

class FeatureRequestSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    description = fields.Str()
    client = fields.Integer()
    client_priority = fields.Integer()
    target_date = fields.Date()
    ticket_url = fields.Str()
    product_area = fields.Str()

class ClientSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    email = fields.Email()
    date_created = fields.Date()
    date_edited = fields.Date()
