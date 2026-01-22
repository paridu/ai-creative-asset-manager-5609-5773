resource "aws_db_subnet_group" "postgres" {
  name       = "archive-ai-db-subnet"
  subnet_ids = module.vpc.private_subnets
}

resource "aws_db_instance" "metadata_db" {
  allocated_storage    = 100
  max_allocated_storage = 500
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t4g.medium"
  db_name              = "archiveai"
  username             = "admin"
  password             = var.db_password # Provided via TF_VAR
  db_subnet_group_name = aws_db_subnet_group.postgres.name
  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  skip_final_snapshot  = false
  multi_az             = true
  storage_encrypted    = true
}

resource "aws_security_group" "rds_sg" {
  name   = "archive-ai-rds-sg"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [module.eks.node_security_group_id]
  }
}