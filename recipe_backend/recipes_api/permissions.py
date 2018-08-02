""" Custom permission class """
from rest_framework import permissions
import os

# Custom permission that allows unlimited access if not in the Docker container
class AllowIfNotInDockerContainer(permissions.BasePermission):
    def has_permission(self, request, view):
        return os.environ.get('DOCKER_CONTAINER', None) is None