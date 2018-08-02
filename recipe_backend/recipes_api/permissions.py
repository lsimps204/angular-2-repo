""" Custom permission class """
from rest_framework import permissions
import os

# Custom permission that allows unlimited access if not in the Docker container.
class AllowIfNotInDockerContainer(permissions.BasePermission):

    def has_permission(self, request, view):
        # If the request is a READ operation, grant access
        # Note: SAFE_METHODS is a tuple: ("GET", "OPTIONS", "HEAD")
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # If outside a container, grant access. If inside a countainer, ensure the user is not anonymous.
        outwith_container = os.environ.get('DOCKER_CONTAINER', None) is None
        if outwith_container:
            return True
        elif not outwith_container:
            return not request.user.is_anonymous