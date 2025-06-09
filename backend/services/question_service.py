from exceptions.errors import BadRequestError, InternalServerError
from k8s.connection import KubernetesConnection

class QuestionService:
    MAX_PROMPT_CHARS = 12000

    def __init__(self):
        self.k8s = KubernetesConnection()
        self.k8s_connected = False

    async def handle_question(self, question: str) -> str:
        if not question.strip():
            raise BadRequestError("Question cannot be empty")

        if len(question) > self.MAX_PROMPT_CHARS:
            raise BadRequestError("The inputted prompt is too long.")

        try:
            if not self.k8s_connected:
                self.k8s_connected = self.k8s.connect()

            if self.k8s_connected:
                cluster_info = self.k8s.test_connection()
                return f"Connected to K8s cluster! Found {cluster_info['nodes']} nodes and {cluster_info['namespaces']} namespaces. Namespaces: {cluster_info['namespace_names']}"
            else:
                return "Failed to connect to Kubernetes cluster"

        except Exception:
            raise InternalServerError()