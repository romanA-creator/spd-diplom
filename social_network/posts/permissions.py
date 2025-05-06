from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

class IsOwnerOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    Разрешения на просмотр всех записей, изменения — только своему владельцу.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return obj.author == request.user