variable "project" {
  description = "The project ID where all resources will be launched."
  type        = string
}

variable "location" {
  description = "The location (region or zone) to deploy the Cloud Run services. Note: Be sure to pick a region that supports Cloud Run."
  type        = string
  default = "us-central1"
}

variable "gcr_region" {
  description = "Name of the GCP region where the GCR registry is located. e.g: 'us' or 'eu'."
  type        = string
  default = "us"
}

variable "service_name" {
  description = "The name of the Cloud Run service to deploy."
  type        = string
  default     = "sample-docker-service"
}
variable "github_owner" {
    description = "The name of the github owner. e.g: 'motianjun4' for 'github.com/motianjun4'."
    type = string
}

variable "github_repo" {
    description = "Name of the repository. For example: The name for https://github.com/googlecloudplatform/cloud-builders is 'cloud-builders'."
    type = string
}

variable "github_branch" {
    description = "Regex of branches to match to deploy the build trigger. e.g: 'master'."
    type = string
    default = "master"
}