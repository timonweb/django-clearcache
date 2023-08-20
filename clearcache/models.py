from django.db.models import Model


class CustomPermissions(Model):
    """
    This model just defines custom permissions, without a corresponding table in the database.
    """
    class Meta:
        managed = False  # No database table creation or deletion operations will be performed for this model.
        default_permissions = ()  # disable "add", "change", "delete" and "view" default permissions for this model.
        permissions = (
            ('use_clearcache',
             "Can see clearcache UI in Admin, and use the 'clearcache_admin' view."),
        )
