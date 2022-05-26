"""Sphinx extension that allows building versioned docs for self-hosting.

https://robpol86.github.io/sphinxcontrib-versioning
https://github.com/Robpol86/sphinxcontrib-versioning
https://pypi.python.org/pypi/sphinxcontrib-versioning
"""

from .sphinx_ import EventHandlers, SC_VERSIONING_VERSIONS, STATIC_DIR
from sphinxcontrib.versioning.lib import Config

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '2.2.1'

def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param sphinx.application.Sphinx app: Sphinx application object.

    :returns: Extension version.
    :rtype: dict
    """
    # Used internally. For rebuilding all pages when one or versions fail.
    app.add_config_value('sphinxcontrib_versioning_versions', SC_VERSIONING_VERSIONS, 'html')

    # Needed for banner.
    app.config.html_static_path.append(STATIC_DIR)
    try:
        app.add_css_file('banner.css')
    except AttributeError:
        # Old sphinx... get version?
        app.add_stylesheet('banner.css')

    # Tell Sphinx which config values can be set by the user.
    for name, default in Config():
        app.add_config_value('scv_{}'.format(name), default, 'html')

    # Event handlers.
    app.connect('builder-inited', EventHandlers.builder_inited)
    app.connect('env-updated', EventHandlers.env_updated)
    app.connect('html-page-context', EventHandlers.html_page_context)
    return dict(version=__version__)
