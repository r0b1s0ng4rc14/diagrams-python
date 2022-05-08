from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB,Route53
from diagrams.aws.database import RDSPostgresqlInstance,ElasticacheForRedis

with Diagram("XPTO product diagram - AWS", filename="xpto_product_diagram-aws",):
    dns = Route53("DNS")
    lb  = ELB("LoadBanlancer")

    with Cluster("Instances:"):
        inst_group = [EC2("Server-1"),
                      EC2("Server-2"),
                      EC2("Server-3")]
    
    with Cluster("Databases:"):
        db_primary = RDSPostgresqlInstance("DB_Master")
        db_primary - [RDSPostgresqlInstance("DB_Slave-RO")]

    with Cluster("Redis:"):
        mem_cache = ElasticacheForRedis("Redis-M")
        mem_cache  >> [ElasticacheForRedis("Redis-M1"),
                     ElasticacheForRedis("Redis-S1"),
                     ElasticacheForRedis("Redis-S2"),
                     ElasticacheForRedis("Redis-S3")]                 

    dns >> lb >> inst_group
    inst_group >> db_primary
    inst_group >> mem_cache