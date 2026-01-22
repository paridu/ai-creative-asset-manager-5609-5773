module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    # Standard workers for API and Web
    general = {
      min_size     = 2
      max_size     = 10
      desired_size = 2
      instance_types = ["t3.medium"]
    }
    # GPU workers for AI inference (CLIP/Vision models)
    ai_inference = {
      min_size     = 1
      max_size     = 5
      desired_size = 1
      instance_types = ["g4dn.xlarge"]
      
      taints = [{
        key    = "workload"
        value  = "ai-inference"
        effect = "NO_SCHEDULE"
      }]
    }
  }

  # Enable OIDC for IAM Roles for Service Accounts
  enable_irsa = true
}