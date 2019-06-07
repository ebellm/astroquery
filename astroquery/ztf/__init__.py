# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
ZTF service.
-------------------------

:author: Eric C. Bellm (ecbellm@uw.edu)
"""

# Make the URL of the server, timeout and other items configurable
# See <http://docs.astropy.org/en/latest/config/index.html#developer-usage>
# for docs and examples on how to do this
# Below is a common use case
from astropy import config as _config


class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astroquery.ztf`.
    """
    server = _config.ConfigItem(
        ['https://irsa.ipac.caltech.edu/ibe/search/ztf/products/',],
        'Root query URL.')

    lightcurve_server = _config.ConfigItem(
        ['https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves',],
        'Root query URL.')

    timeout = _config.ConfigItem(
        300,
        'Time limit for connecting to IRSA ZTF server.')

    pedantic = _config.ConfigItem(
        False,
        'If True, raise an error when the result violates the spec, '
        'otherwise issue warning(s).')


conf = Conf()

# Now import your public class
# Should probably have the same name as your module
from .core import Ztf, ZtfClass

__all__ = ['Ztf', 'ZtfClass',
           'Conf', 'conf',
           ]
