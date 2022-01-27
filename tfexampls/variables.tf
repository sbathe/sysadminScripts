variable "iam_role_name" {
}

variable "allowed_assume_from_principal" {
}

variable "iam_role_policy_name" {
	default = "service_policy"
}

variable "iam_role_policy" {
	default = ""
}

variable "assume_role_policy_document" {
  default = "default"
}

