from diagrams import Cluster,Diagram
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.group import NS
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.podconfig import ConfigMap

with Diagram("XPTO product diagram - K8S", filename="xpto_product_diagram-k8s"):
    with Cluster("Namespace_Xpto"):
        NS("namespace X")
        local   = Ingress("internal.xpto") >> Service("svc")
        private = Ingress("private.xpto") >> Service ("svc")
        local >> [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")] << ReplicaSet("rs") << ConfigMap("cm") << Deployment("dp") << HPA("hpa")
        private >> [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")] << ReplicaSet("rs") << ConfigMap("cm") << Deployment("dp") << HPA("hpa")
        