from api.models.domain.networkx_graph_impl import NetworkxGraphImpl
from api.repositories.general.graph_drawing_repository import DrawingRepository
from api.repositories.general.graph_repository import GraphRepository
from api.services.general.graph_service import GraphService

GraphService().save_graph(NetworkxGraphImpl("cool_graph"), False)
