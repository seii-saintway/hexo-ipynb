import os
import sys

from traitlets.config import Config
from nbconvert.exporters.html import HTMLExporter

class MyExporter(HTMLExporter):
    def __init__(self):
        super().__init__()
        self.template_paths = super().template_paths + [os.path.dirname(__file__)]

#     @property
#     def template_paths(self):
#         """
#         We want to inherit from HTML template, and have template under `./`
#         so append it to the search path.
#         """
#         return super().template_paths + [os.path.dirname(__file__)]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'hexo.tpl'

def main(ipynb_file):
    exporter = MyExporter()
    print(exporter.from_filename(ipynb_file)[0])

main(sys.argv[1])
