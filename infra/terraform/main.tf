resource "aws_instance" "app_server" {
    ami = "ami-053b0d53c279acc90"
    instance_type= "t2.micro"
    key_name = var.key_name
    vpc_security_group_ids = [aws_security_group.app_sg.id]


    user_data = <<-EOF
            #!/bin/bash
            apt-get update -y
            apt-get install -y docker.io
            systemctl start docker
            usermod -aG docker ubuntu
            EOF

  tags = {
    Name = "prod-server"
  }
}

resource "aws_security_group" "app_sg" {
  name        = "allow-flask-access"
  description = "Allow access to Flask app and SSH"
  
  ingress {
    description = "Allow HTTP requests to Flask app"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_key_pair" "mykeys" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}


