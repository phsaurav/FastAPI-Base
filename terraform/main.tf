# Check existing tag to avoid modifying existing resources on current tag change
# data "aws_vpc" "existing_tags" {
#   filter {
#     name   = "tag:Project"
#     values = [var.project]
#   }
#   filter {
#     name   = "tag:Environment"
#     values = [var.environment]
#   }
# }
#

locals {
  # existing_tags = data.aws_vpc.existing_tags.tags

  tags = {
    Project     = var.project
    # CreatedBy   = lookup(local.existing_tags, "CreatedBy", var.createdby)
    CreatedBy = var.createdby
    Environment = var.environment
    TFWorkspace = terraform.workspace
  }
}

# * VPC Module
module "vpc" {
  source                 = "./modules/vpc"
  vpc_name               = var.vpc_name
  vpc_cidr               = var.vpc_cidr
  vpc_private_subnets    = var.vpc_private_subnets
  vpc_public_subnets     = var.vpc_public_subnets
  enable_nat_gateway     = var.enable_nat_gateway
  vpc_tags               = local.tags
}

module "ecr"{
  source                 = "./modules/ecr"
  repo_name = "dhaka-celsius"
}