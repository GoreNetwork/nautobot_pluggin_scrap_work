"""Navigation Items to add to Nautobot for maintenance_notices."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

"""
menu_items = (
    PluginMenuItem(
        link='plugins:maintenance_notices:model',  # A reverse compatible link to follow.
        link_text = 'Sample Text',  # Text to display to user.
        permissions = [],  # Optional: List of permissions required to display this link.
        buttons = (  # Optional: Iterable of PluginMenuButton instances to display.
            PluginMenuButton(
                'plugins:maintenance_notices:model',  # A reverse compatible link to follow.
                'Sample Text',  # Text to display to user.
                'mdi mdi-help-circle',  # Button icon CSS Classes (Currently supports Material Design Icons.)
                ButtonColorChoices.BLUE,  # Optional: Color for the button.,
                permissions = []  # Optional: List of permissions required to display this button.
            )
        )
    )
)
"""
add_maintenancenotice_button = PluginMenuButton(
    link='plugins:maintenance_notices:maintenancenotice_add',
    title='Add a new maintenance notice',
    icon_class='mdi mdi-plus-thick',
    color=ButtonColorChoices.GREEN,
    # This would limit who can see the buttion to if they have access
    # permissions=['maintenance_notices.add_maintenancenotice'],
)

menu_items = (
    PluginMenuItem(
        link='plugins:maintenance_notices:maintenancenotice_list', #Refrences urls.py "name" in the url
        link_text='Maintenance Notices',
        buttons=[add_maintenancenotice_button],
        #This would hide the Maintenance Noticication plugin if they didn't have access to it.
        # permissions=['maintenance_notices.view_maintenancenotice'],
    ),
    PluginMenuItem(
        link='plugins:maintenance_notices:maintenancenotice_active_list',
        link_text='Active Maintenance Notices',
        # permissions=['maintenance_notices.view_maintenancenotice'],
        buttons=[add_maintenancenotice_button],
    ),
) 