from mongonaut.sites import MongoAdmin

from .models import Post

class PostAdmin(MongoAdmin):

    # Searches on the title field. Displayed in the DocumentListView.
    search_fields = ('title', 'tags')

    # provide following fields for view in the DocumentListView
    list_fields = ('title', "author",)

    def has_view_permission(self, request):
        """ Can view this object """
        return (request.user.is_authenticated and request.user.is_active)

# Instantiate the PostAdmin subclass
# Then attach PostAdmin to your model
Post.mongoadmin = PostAdmin()

