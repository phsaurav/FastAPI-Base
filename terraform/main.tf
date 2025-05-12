# Check existing tag to avoid modifying existing resources on current tag change
data "aws_vpc" "existing_tags" {
  filter {
    name   = "tag:Project"
    values = [var.project]
  }
  filter {
    name   = "tag:Environment"
    values = [var.environment]
  }
}

# Provider configuration for WAF
provider "aws" {
  alias  = "us-east-1"
  region = "us-east-1"
}

locals {
  existing_tags = data.aws_vpc.existing_tags.tags

  tags = {
    Project     = var.project
    CreatedBy   = lookup(local.existing_tags, "CreatedBy", var.createdby)
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
  agw_name               = var.agw_name
  stage_name             = var.stage_name
  hosted_zone_name       = var.hosted_zone_name
  domain_name            = var.domain_name
  domain_certificate_arn = var.domain_certificate_arn
  alb_listeners_arn      = module.asg.http_listener_arn
  enable_nat_gateway     = var.enable_nat_gateway
  vpc_tags               = local.tags
}
