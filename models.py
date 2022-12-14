from marshmallow import fields, Schema, validates_schema, ValidationError


VALID_CVD = (
    "filter",
    "map",
    "unique",
    "sort",
    "limit"
)


class Request(Schema):
    filename = fields.Str(required=True)
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema()
    def validate_cmd(self, values, *args, **kwargs):
        if values["cmd1"] not in VALID_CVD:
            raise ValidationError("cmd1: недопустимый параметр")
        if values["cmd2"] not in VALID_CVD:
            raise ValidationError("cmd2: недопустимый параметр")
        return values
