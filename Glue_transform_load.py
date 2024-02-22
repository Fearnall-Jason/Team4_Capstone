import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1708543405168 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://semistructuredata"]},
    transformation_ctx="AmazonS3_node1708543405168",
)

# Script generated for node Change Schema
ChangeSchema_node1708543471726 = ApplyMapping.apply(
    frame=AmazonS3_node1708543405168,
    mappings=[
        ("job_id", "string", "job_id", "string"),
        ("agency", "string", "agency", "string"),
        ("posting_type", "string", "posting_type", "string"),
        ("number_of_positions", "string", "number_of_positions", "int"),
        ("business_title", "string", "business_title", "string"),
        ("civil_service_title", "string", "civil_service_title", "string"),
        ("level", "string", "level", "string"),
        (
            "full_time_part_time_indicator",
            "string",
            "full_time_part_time_indicator",
            "string",
        ),
        ("career_level", "string", "career_level", "string"),
        ("salary_range_from", "string", "salary_range_from", "decimal"),
        ("salary_range_to", "string", "salary_range_to", "decimal"),
        ("salary_frequency", "string", "salary_frequency", "string"),
        ("work_location", "string", "work_location", "string"),
        ("division_work_unit", "string", "division_work_unit", "string"),
        ("posting_date", "string", "posting_date", "date"),
        ("post_until", "string", "post_until", "string"),
    ],
    transformation_ctx="ChangeSchema_node1708543471726",
)

# Script generated for node Amazon Redshift
AmazonRedshift_node1708544284158 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1708543471726,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-637423487153-us-east-1/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.joblistings",
        "connectionName": "Redshift nyc listings connect",
        "preactions": "DROP TABLE IF EXISTS public.joblistings; CREATE TABLE IF NOT EXISTS public.joblistings (job_id VARCHAR, agency VARCHAR, posting_type VARCHAR, number_of_positions INTEGER, business_title VARCHAR, civil_service_title VARCHAR, level VARCHAR, full_time_part_time_indicator VARCHAR, career_level VARCHAR, salary_range_from DECIMAL, salary_range_to DECIMAL, salary_frequency VARCHAR, work_location VARCHAR, division_work_unit VARCHAR, posting_date DATE, post_until VARCHAR);",
    },
    transformation_ctx="AmazonRedshift_node1708544284158",
)

job.commit()