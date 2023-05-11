from flask_jwt_extended import jwt_required
from flask_restx import Resource
from flask import Flask, jsonify, request

from .utils import get_client, get_datetime

from .dto import GraphDto

api = GraphDto.api

@api.route('/temperature')
class Temperature(Resource):

    @jwt_required()
    def get(self):
        start_date = get_datetime(request.args.get('startDate'))
        end_date = get_datetime(request.args.get('endDate'))

        try:
            query = f'''
        from(bucket: "weather")
        |> range(start: {start_date}, stop: {end_date})
        |> filter(fn: (r) => r["_measurement"] == "temperature")
        |> filter(fn: (r) => r["_field"] == "value")
        |> filter(fn: (r) => r["source"] == "random")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        |> keep(columns: ["_time", "value"])
        '''
            tables = get_client().query_data_frame(query, org="Priyank")
            result = tables[["_time", "value"]].set_index('_time').rename(columns={"value": "temperature"}).to_dict(orient='dict')['temperature']
            result = tables[["_time", "value"]].to_json(orient='records')
            return result

        except Exception as e:
            return jsonify({"e": str(e), "query": query})


@api.route('/precipitation')
class Precipitation(Resource):

    @jwt_required()
    def get(self):
        start_date = get_datetime(request.args.get('startDate'))
        end_date = get_datetime(request.args.get('endDate'))

        try:
            query = f'''
        from(bucket: "weather")
        |> range(start: {start_date}, stop: {end_date})
        |> filter(fn: (r) => r["_measurement"] == "precipitation")
        |> filter(fn: (r) => r["_field"] == "value")
        |> filter(fn: (r) => r["source"] == "random")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        |> keep(columns: ["_time", "value"])
        '''
            tables = get_client().query_data_frame(query, org="Priyank")
            result = tables[["_time", "value"]].set_index('_time').rename(columns={"value": "temperature"}).to_dict(orient='dict')['temperature']
            result = tables[["_time", "value"]].to_json(orient='records')
            return result

        except Exception as e:
            return jsonify({"e": str(e), "query": query})


@api.route('/humidity')
class Humidity(Resource):
    
    @jwt_required()
    def get(self):
        start_date = get_datetime(request.args.get('startDate'))
        end_date = get_datetime(request.args.get('endDate'))

        try:
            query = f'''
        from(bucket: "weather")
        |> range(start: {start_date}, stop: {end_date})
        |> filter(fn: (r) => r["_measurement"] == "humidity")
        |> filter(fn: (r) => r["_field"] == "value")
        |> filter(fn: (r) => r["source"] == "random")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        |> keep(columns: ["_time", "value"])
        '''
            tables = get_client().query_data_frame(query, org="Priyank")
            result = tables[["_time", "value"]].set_index('_time').rename(columns={"value": "temperature"}).to_dict(orient='dict')['temperature']
            result = tables[["_time", "value"]].to_json(orient='records')
            return result

        except Exception as e:
            return jsonify({"e": str(e), "query": query})
        

@api.route('/wind_speed')
class WindSpeed(Resource):
    
    @jwt_required()
    def get(self):
        start_date = get_datetime(request.args.get('startDate'))
        end_date = get_datetime(request.args.get('endDate'))

        try:
            query = f'''
        from(bucket: "weather")
        |> range(start: {start_date}, stop: {end_date})
        |> filter(fn: (r) => r["_measurement"] == "wind_speed")
        |> filter(fn: (r) => r["_field"] == "value")
        |> filter(fn: (r) => r["source"] == "random")
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        |> keep(columns: ["_time", "value"])
        '''
            tables = get_client().query_data_frame(query, org="Priyank")
            result = tables[["_time", "value"]].set_index('_time').rename(columns={"value": "temperature"}).to_dict(orient='dict')['temperature']
            result = tables[["_time", "value"]].to_json(orient='records')
            return result

        except Exception as e:
            return jsonify({"e": str(e), "query": query})
