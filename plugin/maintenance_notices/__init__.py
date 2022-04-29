"""maintenance_notices Plugin Initilization."""

from nautobot.extras.plugins import PluginConfig

try:
    from importlib import metadata
except ImportError: 
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

class MaintenanceNoticesConfig(PluginConfig):
    """Plugin configuration for the maintenance_notices plugin."""

    name = "maintenance_notices"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "Maintenance Notices"  # Human-friendly name for the plugin.
    base_url = "maintenance_notices"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    
    #This is refrenced in views.py to set the default duration with the SETTINGS.get
    #However it's being overridden by the PLUGINS_CONFIG in nautobot_config.py
    default_settings = {"default_duration": 120,}  # A dictionary of configuration parameters and their default values.
    caching_config = {}  # Plugin-specific cache configuration.
    version = __version__
    description='A scrap work plugin to learn stuff'
    author='Daniel Himes'


config = MaintenanceNoticesConfig