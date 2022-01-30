output "url" {
  description = "The URL where the Cloud Run Service can be accessed."
  value       = google_cloud_run_service.service.status[0].url
}

output "trigger_id" {
  description = "The unique identifier for the Cloud Build trigger."
  value       = google_cloudbuild_trigger.cloudbuild.trigger_id
}

output "triggers_url"{
    description = "Goto cloud build triggers"
    value = "https://console.cloud.google.com/cloud-build/triggers?project=${var.project}"
}