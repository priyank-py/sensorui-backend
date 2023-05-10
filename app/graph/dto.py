from flask_restx import Namespace, fields


class GraphDto:

    api = Namespace("graph", description="Graph related response.")
    data_resp = api.model(
        "Temperature Response",
        {
            "_time": fields.String,
            "message": fields.Float,
        },
    )