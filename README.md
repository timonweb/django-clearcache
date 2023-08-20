# Django ClearCache 🤠🧹💰 

![License](https://img.shields.io/pypi/l/django-clearcache)
![Django versions](https://img.shields.io/pypi/djversions/django-clearcache)
![Python versions](https://img.shields.io/pypi/pyversions/django-clearcache)

Allows you to clear Django cache via admin UI or manage.py command.

![demo](https://raw.githubusercontent.com/timonweb/django-clearcache/master/demo.gif)

## Installation

1. Install using PIP:

      ```
      pip install django-clearcache
      ```

2. Add **clearcache** to INSTALLED_APPS, make sure it's above `django.contrib.admin`:

      ```
      INSTALLED_APPS += [
          ...
          'clearcache',
          'django.contrib.admin',
          ...
      ]
      ```

3. Add url to the main **urls.py** right above root admin url:
   
       ```
       urlpatterns = [
           path('admin/clearcache/', include('clearcache.urls')),
           path('admin/', admin.site.urls),
       ]
       ```

4. Apply migrations:

   ```
   manage.py migrate [--database=<your_database>] [--settings=<your_settings>]
   ```

## Usage

### Via Django admin

Clearcache can be used by any user with permission ```clearcache.use_clearcache```, 
and obviously be any superuser (superusers have all permissions).

1. Go to `/admin/clearcache/`. If you are authorized, you should see a form with cache selector.
2. Pick a cache. Usually there's one default cache, but can be more.
3. Click the button, you're done!

Any user with access to the Admin interface (i.e. any user with `is_staff` privilege) 
will see a Clearcache section on the Admin homepage, if he is authorized, and can 
access Clearcache from there. 


### Via manage.py command

1. Run the following command to clear the default cache

      ```
      python manage.py clearcache
      ```

2. Run the command above with an additional parameter to clear non-default cache (if exists):

      ```
      python manage.py clearcache cache_name
      ```

## Follow me

1. Check my dev blog with Python and JavaScript tutorials at [https://timonweb.com](https://timonweb.com).
2. Follow me on Twitter [@timonweb](https://twitter.com/timonweb)
