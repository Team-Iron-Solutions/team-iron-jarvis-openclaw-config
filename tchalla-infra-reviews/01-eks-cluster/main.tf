# EKS Cluster Module — Team Iron Production
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.20"
    }
  }
  backend "s3" {
    bucket         = "team-iron-tfstate"
    key            = "prod/eks/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "team-iron-tfstate-lock"
  }
}

locals {
  cluster_name = "${var.project}-${var.environment}-eks"
  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
    Team        = "sre"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = local.cluster_name
  cluster_version = var.kubernetes_version

  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true

  # ⚠️ ISSUE: endpoint should be private-only in prod
  cluster_endpoint_public_access_cidrs = ["0.0.0.0/0"]

  eks_managed_node_groups = {
    general = {
      instance_types = var.node_instance_types
      min_size       = var.node_min_size
      max_size       = var.node_max_size
      desired_size   = var.node_desired_size

      # ⚠️ ISSUE: No max_unavailable_percentage set (update disruption risk)
      update_config = {
        max_unavailable = 1
      }

      labels = {
        role = "general"
      }

      block_device_mappings = {
        xvda = {
          device_name = "/dev/xvda"
          ebs = {
            # ⚠️ ISSUE: encrypted = false — must be true in production
            encrypted   = false
            volume_size = 50
            volume_type = "gp3"
            iops        = 3000
          }
        }
      }

      iam_role_additional_policies = {
        # ⚠️ ISSUE: Too permissive — should use fine-grained IRSA instead
        AmazonEC2FullAccess    = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
        AmazonS3FullAccess     = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
        CloudWatchFullAccess   = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
      }
    }

    spot = {
      instance_types = ["m5.xlarge", "m5a.xlarge", "m4.xlarge"]
      capacity_type  = "SPOT"
      min_size       = 0
      max_size       = 10
      desired_size   = 2

      labels = {
        role = "spot"
      }

      taints = {
        spot = {
          key    = "spot"
          value  = "true"
          effect = "NO_SCHEDULE"
        }
      }
    }
  }

  tags = local.common_tags
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "${local.cluster_name}-vpc"
  cidr = var.vpc_cidr

  azs             = data.aws_availability_zones.available.names
  private_subnets = var.private_subnet_cidrs
  public_subnets  = var.public_subnet_cidrs

  enable_nat_gateway   = true
  single_nat_gateway   = false
  enable_dns_hostnames = true

  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }
  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }

  tags = local.common_tags
}

data "aws_availability_zones" "available" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}
