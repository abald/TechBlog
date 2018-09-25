# @copyright (c) 2018-2018 Andrew Baldin.
""" Collective TechBlog """

package_info = "Collective TechBlog"

try:
    from .version import version_info
except:
    major, minor = (0, 1)
    version_info = major, minor

author_info = (('Andrew Baldin',  'altkotm@gmail.com'),)

__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{} <{}>".format(*info) for info in author_info)