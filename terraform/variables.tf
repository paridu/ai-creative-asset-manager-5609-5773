variable "aws_region" {
  default = "us-east-1"
}

variable "environment" {
  default = "production"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "cluster_name" {
  default = "archive-ai-cluster"
}

variable "asset_bucket_name" {
  default = "archive-ai-assets-prod"
}