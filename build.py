from pybuilder.core import use_plugin, init, Project

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")


name = "home-api"
default_task = "publish"


@init
def set_properties(project):
    """

    :type project: Project
    """
    project.depends_on_requirements("requirements.txt")
    pass
