# myapp/mongoadmin.py

# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin

# Import your custom models
from .models import Post

# Subclass MongoAdmin and add a customization
class PostAdmin(MongoAdmin):

    # Searches on the title field. Displayed in the DocumentListView.
    search_fields = ('title',)

    # provide following fields for view in the DocumentListView
    list_fields = ('title', "published", "pub_date")

    def has_view_permission(self, request):
        """ Can view this object """
        return (request.user.is_authenticated and request.user.is_active) or True

# Instantiate the PostAdmin subclass
# Then attach PostAdmin to your model
Post.mongoadmin = PostAdmin()
