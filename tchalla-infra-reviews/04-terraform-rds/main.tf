# Terraform RDS PostgreSQL Multi-AZ — Team Iron Production
resource "aws_db_subnet_group" "main" {
  name        = "${var.project}-${var.environment}-db-subnet"
  subnet_ids  = var.private_subnet_ids
  description = "RDS subnet group for ${var.project} ${var.environment}"
  tags        = local.common_tags
}

resource "aws_security_group" "rds" {
  name        = "${var.project}-${var.environment}-rds-sg"
  description = "Security group for RDS PostgreSQL"
  vpc_id      = var.vpc_id

  ingress {
    description = "PostgreSQL from EKS nodes"
    from_port   = 5432
    to_port     = 5432
    # ⚠️ ISSUE: Too broad — should restrict to EKS node security group only
    cidr_blocks = ["10.0.0.0/8"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.common_tags
}

resource "aws_db_instance" "main" {
  identifier = "${var.project}-${var.environment}-postgres"

  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = var.db_instance_class
  allocated_storage    = var.db_allocated_storage
  max_allocated_storage = var.db_max_allocated_storage
  storage_type         = "gp3"
  storage_encrypted    = true
  kms_key_id          = aws_kms_key.rds.arn

  db_name  = var.db_name
  username = var.db_username
  password = var.db_password  # ⚠️ ISSUE: Should use aws_secretsmanager_secret_version

  multi_az               = var.environment == "prod" ? true : false
  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  backup_retention_period = var.backup_retention_days
  backup_window          = "03:00-04:00"
  maintenance_window     = "Mon:04:00-Mon:05:00"

  performance_insights_enabled    = true
  performance_insights_retention_period = 7

  monitoring_interval = 60
  monitoring_role_arn = aws_iam_role.rds_monitoring.arn

  # ⚠️ ISSUE: deletion_protection = false in production is dangerous
  deletion_protection = false

  # ⚠️ ISSUE: No final_snapshot_identifier — data loss risk on destroy
  skip_final_snapshot = true

  parameter_group_name = aws_db_parameter_group.main.name

  tags = local.common_tags
}

resource "aws_db_parameter_group" "main" {
  family = "postgres15"
  name   = "${var.project}-${var.environment}-pg15-params"

  parameter {
    name  = "log_connections"
    value = "1"
  }
  parameter {
    name  = "log_disconnections"
    value = "1"
  }
  parameter {
    name  = "log_statement"
    value = "ddl"
  }
  parameter {
    name  = "shared_preload_libraries"
    value = "pg_stat_statements"
  }

  tags = local.common_tags
}

resource "aws_kms_key" "rds" {
  description             = "KMS key for RDS encryption - ${var.project} ${var.environment}"
  deletion_window_in_days = 7
  enable_key_rotation     = true
  tags                    = local.common_tags
}
