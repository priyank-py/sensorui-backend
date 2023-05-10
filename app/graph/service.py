from flask import current_app
from app.utils import internal_err_resp


class GraphService:
    @staticmethod
    def get_temperature_data(username):
        """ Get user data by username """
        # if not (user := User.query.filter_by(username=username).first()):
        #     return err_resp("User not found!", "user_404", 404)
        
        query = '''
    from(bucket: "weather")
    |> range(start: -5m)
    |> filter(fn: (r) => r["_measurement"] == "temperature")
    |> filter(fn: (r) => r["_field"] == "value")
    |> filter(fn: (r) => r["source"] == "random")
    |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    |> keep(columns: ["_time", "value"])
    '''

        from .utils import get_client

        try:
            # temp_data = get_client
            tables = get_client.query_data_frame(query, org="Priyank")
            result = tables[["_time", "value"]].to_json(orient='records')
            # return json.dumps(result)
            # resp = message(True, "User data sent")
            # resp["user"] = user_data
            return result, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()