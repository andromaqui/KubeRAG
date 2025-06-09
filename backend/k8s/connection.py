from typing import Optional, Dict, Any
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import logging

logger = logging.getLogger(__name__)


class KubernetesConnection:

    def __init__(self, kubeconfig_path: Optional[str] = None):
        self.kubeconfig_path = kubeconfig_path
        self.v1 = None
        self.apps_v1 = None
        self.batch_v1 = None
        self.connected = False

    def connect(self) -> bool:
        try:
            if self.kubeconfig_path:
                config.load_kube_config(config_file=self.kubeconfig_path)
            else:
                config.load_kube_config()  # Uses ~/.kube/config (minikube)

            self._initialize_clients()
            self.connected = True
            logger.info("✅ Connected to Kubernetes cluster")
            return True

        except Exception as e:
            logger.error(f"❌ Connection failed: {e}")
            return False

    def _initialize_clients(self):
        self.v1 = client.CoreV1Api()
        self.apps_v1 = client.AppsV1Api()
        self.batch_v1 = client.BatchV1Api()

    def test_connection(self) -> Dict[str, Any]:
        if not self.connected:
            return {"status": "disconnected", "error": "Not connected to cluster"}

        try:
            nodes = self.v1.list_node()
            namespaces = self.v1.list_namespace()

            return {
                "status": "connected",
                "nodes": len(nodes.items),
                "namespaces": len(namespaces.items),
                "node_names": [node.metadata.name for node in nodes.items],
                "namespace_names": [ns.metadata.name for ns in namespaces.items]
            }

        except ApiException as e:
            return {"status": "error", "error": f"API Error: {e.status} - {e.reason}"}
        except Exception as e:
            return {"status": "error", "error": str(e)}