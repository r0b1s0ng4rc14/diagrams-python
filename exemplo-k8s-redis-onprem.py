from calendar import c
from turtle import color
from diagrams import Cluster,Diagram, Edge
from diagrams.onprem.inmemory import Redis
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.group import NS
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.podconfig import ConfigMap

with Diagram("XPTO product diagram - K8S", filename="xpto_product_diagram-k8s-redis-OP"):
    
    with Cluster("K8S ⚓"):
        local   = Ingress("internal.xpto") >> Service("svc")
        pods = [Pod("pod1"),
                Pod("pod2"),
                Pod("pod3")]
        pods << ReplicaSet("rs") << ConfigMap("cm") << Deployment("dp") << HPA("hpa")    

    with Cluster("Redis 🔥 "):
        redis = Redis("Main Server")
        redis >> Edge(color="red", style="dashed") >> [Redis("Replica-2"), Redis("Replica-1")]
    
    
    local >> pods
    pods >> Edge(color="darkgreen", style="bold") >> redis    





