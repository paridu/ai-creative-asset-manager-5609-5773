output "eks_cluster_endpoint" {
  value = module.eks.cluster_endpoint
}

output "s3_bucket_name" {
  value = aws_s3_bucket.assets.id
}

output "db_endpoint" {
  value = aws_db_instance.metadata_db.endpoint
}

output "sqs_queue_url" {
  value = aws_sqs_queue.ingestion_queue.id
}