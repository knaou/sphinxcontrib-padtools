import os
import subprocess
import pkg_resources
from hashlib import sha1
from docutils.parsers.rst import directives
from sphinx.errors import SphinxError
from sphinxcontrib.imagehelper import (
    ImageConverter, add_image_type, generate_image_directive, generate_figure_directive
)
from sphinx.util import logging

logger = logging.getLogger(__name__)

class PadToolsCmd(object):
    def __init__(self, app):
        self._padtools_jar_path = app.config.padtools_jar_path
        
    def convert(self, filename, to):
        if self._padtools_jar_path is None:
            logger.warning('padtools.jar not found. set padtools_jar_path in conf.py')
            return False

        command_args = ['java', '-Djava.awt.headless=true', '-jar', self._padtools_jar_path, '--', '-o', to, filename]
        exitcode = subprocess.call(command_args, cwd=os.path.dirname(self._padtools_jar_path))
        if exitcode != 0:
            logger.warning('Fail to convert (exitcode: %s)' % exitcode)
            return False
        return True

class PadToolsImageConverter(ImageConverter):
    def get_filename_for(self, node):
        hashed = sha1((node['uri']).encode('utf-8')).hexdigest()
        return "padtools-%s.png" % hashed

    def convert(self, node, filename, to):
        return PadToolsCmd(self.app).convert(filename, to)


def setup(app):
    app.add_config_value('padtools_jar_path', None, 'html')

    add_image_type(app, 'padtools', 'spd', PadToolsImageConverter)
    app.add_directive('padtools-image', generate_image_directive('padtools'))
    app.add_directive('padtools-figure', generate_figure_directive('padtools'))
    
    return {
        'version': pkg_resources.require('sphinxcontrib-padtools')[0].version,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
