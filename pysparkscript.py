from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('Partition JSON file')
sc = SparkContext(conf=conf)

# Set up the input and output paths
input_path = 'gs://cs512_group2/yelp_academic_dataset_user.json'
output_path = 'gs://cs512_group2/user_chunks/user'

# Load the JSON file as an RDD
json_rdd = sc.textFile(input_path)

# Partition the RDD into 20 parts
partitioned_rdd = json_rdd.repartition(20)

# Save each partition to a separate file in the output path
partitioned_rdd.saveAsTextFile(output_path)
