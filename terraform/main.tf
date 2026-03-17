terraform {

  required_providers {

    docker = {
      source = "kreuzwerker/docker"
    }

  }

}

provider "docker" {}

resource "docker_network" "devops_network" {
  name = "devops_network"
}
