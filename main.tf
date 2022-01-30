provider "google" {
  project = var.project
  region  = var.location
}
# ---------------------------------------------------------------------------------------------------------------------
# DEPLOY A CLOUD RUN SERVICE
# ---------------------------------------------------------------------------------------------------------------------

resource "google_cloud_run_service" "service" {
  provider = google
  name     = var.service_name
  location = var.location

  template {
    metadata {

    }
    spec {
      containers {
        image = "us-docker.pkg.dev/cloudrun/container/hello"
        ports {
          container_port = 8000
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# ---------------------------------------------------------------------------------------------------------------------
# EXPOSE THE SERVICE PUBLICALLY
# ---------------------------------------------------------------------------------------------------------------------

resource "google_cloud_run_service_iam_member" "allUsers" {
  service  = google_cloud_run_service.service.name
  location = google_cloud_run_service.service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}

# ---------------------------------------------------------------------------------------------------------------------
# CREATE A CLOUD BUILD TRIGGER
# ---------------------------------------------------------------------------------------------------------------------

resource "google_cloudbuild_trigger" "cloudbuild" {
  provider = google
  github {
    owner = var.github_owner
    name  = var.github_repo
    push {
      branch = var.github_branch
    }
  }
  substitutions = {
    "_SERVICE_NAME" = var.service_name,
    "_DEPLOY_REGION" = var.location
    "_GCR_HOSTNAME" = "${var.gcr_region}.gcr.io"
  }
  name     = var.service_name
  filename = "cloudbuild.yaml"
}

locals {
  image_name = "${var.gcr_region}.gcr.io/${var.project}/${var.service_name}"
}
