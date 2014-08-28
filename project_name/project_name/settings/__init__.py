from os import environ

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


+def load_environment_variables(envfile_path):
+    """
+    Load key-value pairs from an `autoenv`_-style env file (a.k.a. shell script) into the local environment.
+
+    .. _`autoenv`: https://github.com/kennethreitz/autoenv
+    """
+    try:
+        with open(envfile_path) as envfile:
+            lines = envfile.readlines()
+            for line in lines:
+                if 'export' in line:
+                    key, value = line[len('export '):].split('=', maxsplit=1)
+                    environ[key.strip()] = value.strip().strip('"')
+    except IOError:
+        msg = 'Could not load environment variables from "%s"' % envfile_path
+        raise ImproperlyConfigured(msg)
+
