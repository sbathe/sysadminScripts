data "aws_iam_policy_document" "assume_role_policy_document" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "AWS"
      identifiers = [var.allowed_assume_from_principal]
    }
  }
}

locals {
  assume_role_policy = var.assume_role_policy_document != "default" ? var.assume_role_policy_document : data.assume_role_policy_document.json
}

resource "aws_iam_role" "role" {
	name = "${var.iam_role_name}"
  assume_role_policy = jsonencode("${var.assume_role_policy}")
}

resource "aws_iam_role_policy" "policy" {
	count = "${length(var.iam_role_policy) > 0 ? 1 : 0}"
	name = "${var.iam_role_policy_name}"
	role = "${aws_iam_role.role.name}"
	policy = "${var.iam_role_policy}"
}
