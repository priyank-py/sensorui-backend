from flask_restx import Api
from flask import Blueprint

# Import auth namespace
from .controller import api as graph_ns

graph_bp = Blueprint("graph", __name__)

graph = Api(
    graph_bp, title="Graph", description="All graph related APIs"
)

# API namespaces
graph.add_namespace(graph_ns)