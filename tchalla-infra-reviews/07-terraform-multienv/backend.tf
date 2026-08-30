# Multi-Environment Terraform State Management
# Environments: dev, staging, prod
# Workspaces: terraform workspace select {env}

terraform {
  required_version = ">= 1.5.0"

  # ⚠️ ISSUE: Backend config is hardcoded — should use partial config + -backend-config flag
  backend "s3" {
    bucket = "team-iron-tfstate"
    key    = "global/terraform.tfstate"   # ⚠️ ISSUE: key doesn't vary per workspace
    region = "us-east-1"

    # ⚠️ ISSUE: State encryption not configured — should enable encrypt = true
    # encrypt = true
    # kms_key_id = "arn:aws:kms:..."

    # ⚠️ ISSUE: DynamoDB locking disabled for dev env (workspace-conditional missing)
    dynamodb_table = "team-iron-tfstate-lock"
  }
}

# Workspace-based environment config
locals {
  env_config = {
    dev = {
      vpc_cidr            = "10.10.0.0/16"
      eks_instance_types  = ["t3.medium"]
      node_min_size       = 1
      node_max_size       = 3
      node_desired_size   = 1
      db_instance_class   = "db.t3.micro"
      multi_az            = false
      # ⚠️ ISSUE: Dev env shares same S3 bucket as prod for backups
      backup_bucket       = "team-iron-backups"
    }
    staging = {
      vpc_cidr            = "10.20.0.0/16"
      eks_instance_types  = ["t3.large"]
      node_min_size       = 2
      node_max_size       = 5
      node_desired_size   = 2
      db_instance_class   = "db.t3.medium"
      multi_az            = true
      backup_bucket       = "team-iron-backups"
    }
    prod = {
      vpc_cidr            = "10.30.0.0/16"
      eks_instance_types  = ["m5.xlarge"]
      node_min_size       = 3
      node_max_size       = 20
      node_desired_size   = 5
      db_instance_class   = "db.r6g.xlarge"
      multi_az            = true
      backup_bucket       = "team-iron-backups"
    }
  }

  # Current environment from workspace name
  current_env    = terraform.workspace
  current_config = local.env_config[local.current_env]
}

# ⚠️ ISSUE: No remote state data source for cross-stack references
# Should use: data "terraform_remote_state" "vpc" { ... }

# ⚠️ ISSUE: Workspace isolation — all envs read same backend key
# Production Recommendation: Use separate S3 prefixes per environment:
# s3://team-iron-tfstate/dev/terraform.tfstate
# s3://team-iron-tfstate/staging/terraform.tfstate
# s3://team-iron-tfstate/prod/terraform.tfstate

output "environment" {
  value       = local.current_env
  description = "Current deployment environment"
}

output "env_config" {
  value       = local.current_config
  description = "Active environment configuration"
  sensitive   = false
}
