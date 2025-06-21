variable "aws_region" {
    description = "The AWS region where resources will be created"
}


variable "key_name" {
  description = "The name of the EC2 key pair to use for SSH"
}

variable "public_key_path" {
  description = "The local file path to the public key for EC2 login"
}
