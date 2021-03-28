terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_iam_role" "iam_lambda_username_checker" {
  name = "iam_lambda_username_checker"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "username_checker" {
  function_name = "username_checker_test"
  role          = aws_iam_role.iam_lambda_username_checker.arn

  source_code_hash = filebase64sha256("deployment_package.zip")
  filename         = "deployment_package.zip"
  runtime          = "python3.8"
  handler          = "lambda_function.lambda_handler"
  timeout          = 600

}

resource "aws_cloudwatch_event_rule" "every_hour" {
  name                = "every_hour"
  description         = "Fires every hour"
  schedule_expression = "rate(1 hour)"
}

resource "aws_cloudwatch_event_target" "username_check_every_hour" {
  rule      = aws_cloudwatch_event_rule.every_hour.name
  target_id = "username_checker"
  arn       = aws_lambda_function.username_checker.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_username_checker" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.username_checker.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_hour.arn
}

