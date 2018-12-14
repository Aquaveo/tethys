************************
Tethys Platform Settings
************************

**Last Updated:** December 2018

Tethys Platform is built on the `Django web framework <https://www.djangoproject.com/>`_ or in other words it is a Django web application. The primary configuration file for a Django web application is the ``settings.py`` module (see `Django Settings <https://docs.djangoproject.com/en/2.1/topics/settings/>`_). The ``settings.py`` for Tethys Platform is located in the ``tethys_portal`` module. This document describes the each of the settings, many of which are native Django settings.


General Settings
++++++++++++++++

ADMINS
------

See: `ADMINS <https://docs.djangoproject.com/en/1.11/ref/settings/#admins>`_

ALLOWED_HOSTS
-------------

See: `ALLOWED_HOSTS <>`_

BYPASS_TETHYS_HOME_PAGE
-----------------------

DATABASES
---------

See: `DATABASES <>`_

DEBUG
-----

See: `DEBUG <>`_

INSTALLED_APPS
--------------

See: `INSTALLED_APPS <>`_

LOGGING
-------

See: `LOGGING <>`_

MIDDLEWARE_CLASSES
------------------

See: `MIDDLEWARE_CLASSES <>`_

REST_FRAMEWORK
--------------

See: `REST_FRAMEWORK <>`_

ROOT_URLCONF
------------

See: `ROOT_URLCONF <>`_

SECRET_KEY
----------

See: `SECRET_KEY <>`_

TEMPLATES
---------

See: `TEMPLATES <>`_

MESSAGE_TAGS
------------

See: `MESSAGE_TAGS <>`_

WSGI_APPLICATION
----------------

See: `WSGI_APPLICATION <>`_


Authentication Settings
+++++++++++++++++++++++

AUTHENTICATION_BACKENDS
-----------------------

See: `AUTHENTICATION_BACKENDS <>`_

AUTH_PASSWORD_VALIDATORS
------------------------

See: `AUTH_PASSWORD_VALIDATORS <>`_

ENABLE_OPEN_SIGNUP
------------------



Email Settings
++++++++++++++

DEFAULT_FROM_EMAIL
------------------

See: `DEFAULT_FROM_EMAIL <>`_

EMAIL_BACKEND
-------------

See: `EMAIL_BACKEND <>`_

EMAIL_HOST
----------

See: `EMAIL_HOST <>`_

EMAIL_HOST_PASSWORD
-------------------

See: `EMAIL_HOST_PASSWORD <>`_

EMAIL_HOST_USER
----------------

See: `EMAIL_HOST_USER <>`_

EMAIL_PORT
----------

See: `EMAIL_PORT <>`_

EMAIL_USE_TLS
-------------

See: `EMAIL_USE_TLS <>`_



Gravatar Settings
+++++++++++++++++

GRAVATAR_URL
------------

See: `GRAVATAR_URL <>`_

GRAVATAR_SECURE_URL
-------------------

See: `GRAVATAR_SECURE_URL <>`_

GRAVATAR_DEFAULT_SIZE
---------------------

See: `GRAVATAR_DEFAULT_SIZE <>`_

GRAVATAR_DEFAULT_IMAGE
----------------------

See: `GRAVATAR_DEFAULT_IMAGE <>`_

GRAVATAR_DEFAULT_RATING
-----------------------

See: `GRAVATAR_DEFAULT_RATING <>`_

GRAVATAR_DEFAULT_SECURE
-----------------------

See: `GRAVATAR_DEFAULT_SECURE <>`_



I18N and L10N
+++++++++++++

LANGUAGE_CODE
-------------

See: `LANGUAGE_CODE <>`_

TIME_ZONE
---------

See: `TIME_ZONE <>`_

USE_I18N
--------

See: `USE_I18N <>`_

USE_L10N
--------

See: `USE_L10N <>`_

USE_TZ
------

See: `USE_TZ <>`_



Session Security Settings
+++++++++++++++++++++++++

SESSION_EXPIRE_AT_BROWSER_CLOSE
-------------------------------

See: `SESSION_EXPIRE_AT_BROWSER_CLOSE <>`_

SESSION_SECURITY_WARN_AFTER
---------------------------

See: `SESSION_SECURITY_WARN_AFTER <>`_

SESSION_SECURITY_EXPIRE_AFTER
-----------------------------

See: `SESSION_SECURITY_EXPIRE_AFTER <>`_



Social Authentication Settings
++++++++++++++++++++++++++++++

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS
------------------------------------

See: `SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS <>`_

SOCIAL_AUTH_LOGIN_ERROR_URL
---------------------------

See: `SOCIAL_AUTH_LOGIN_ERROR_URL <>`_

SOCIAL_AUTH_LOGIN_REDIRECT_URL
------------------------------

See: `SOCIAL_AUTH_LOGIN_REDIRECT_URL <>`_

SOCIAL_AUTH_SLUGIFY_USERNAMES
-----------------------------

See: `SOCIAL_AUTH_SLUGIFY_USERNAMES <>`_

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
-----------------------------

See: `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY <>`_

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
--------------------------------

See: `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET <>`_

SOCIAL_AUTH_FACEBOOK_KEY
------------------------

See: `SOCIAL_AUTH_FACEBOOK_KEY <>`_

SOCIAL_AUTH_FACEBOOK_SCOPE
--------------------------

See: `SOCIAL_AUTH_FACEBOOK_SCOPE <>`_

SOCIAL_AUTH_FACEBOOK_SECRET
---------------------------

See: `SOCIAL_AUTH_FACEBOOK_SECRET <>`_

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY
-------------------------------

See: `SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY <>`_

SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET
----------------------------------

See: `SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET <>`_

SOCIAL_AUTH_HYDROSHARE_KEY
--------------------------

See: `SOCIAL_AUTH_HYDROSHARE_KEY <>`_

SOCIAL_AUTH_HYDROSHARE_SECRET
-----------------------------

See: `SOCIAL_AUTH_HYDROSHARE_SECRET <>`_



Static Files and Workspace Settings
+++++++++++++++++++++++++++++++++++

STATIC_URL
----------

See: `STATIC_URL <>`_

STATICFILES_DIRS
----------------

See: `STATICFILES_DIRS <>`_

STATICFILES_FINDERS
-------------------

See: `STATICFILES_FINDERS <>`_

STATIC_ROOT
-----------

See: `STATIC_ROOT <>`_

TETHYS_WORKSPACES_ROOT
----------------------

See: `TETHYS_WORKSPACES_ROOT <>`_



Terms and Conditions Settings
+++++++++++++++++++++++++++++

ACCEPT_TERMS_PATH
-----------------

See: `ACCEPT_TERMS_PATH <>`_

TERMS_EXCLUDE_URL_PREFIX_LIST
-----------------------------

See: `TERMS_EXCLUDE_URL_PREFIX_LIST <>`_

TERMS_EXCLUDE_URL_LIST
----------------------

See: `TERMS_EXCLUDE_URL_LIST <>`_

TERMS_BASE_TEMPLATE
-------------------

See: `TERMS_BASE_TEMPLATE <>`_




Django Guardian Settings
++++++++++++++++++++++++

`Django Guardian <https://django-guardian.readthedocs.io/en/stable/overview.html>`_ provides permissions on an object level in Django. Tethys uses it to provide permissions specific to an app. In general, you should not change these settings unless you know what you are doing.

.. warning::

    Do not change these settings unless you know what you are doing.

ANONYMOUS_USER_ID
-----------------

See: `ANONYMOUS_USER_ID <>`_

GUARDIAN_RAISE_403
------------------

See: `GUARDIAN_RAISE_403 <https://django-guardian.readthedocs.io/en/stable/configuration.html#guardian-raise-403>`_

GUARDIAN_RENDER_403
-------------------

See: `GUARDIAN_RENDER_403 <https://django-guardian.readthedocs.io/en/stable/configuration.html#guardian-render-403>`_

GUARDIAN_TEMPLATE_403
---------------------

See: `GUARDIAN_TEMPLATE_403 <https://django-guardian.readthedocs.io/en/stable/configuration.html#guardian-template-403>`_

ANONYMOUS_USER_NAME
-------------------

See: `ANONYMOUS_USER_NAME <https://django-guardian.readthedocs.io/en/stable/configuration.html#anonymous-user-name>`_
