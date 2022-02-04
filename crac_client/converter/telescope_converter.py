
from crac_protobuf.telescope_pb2 import (
    TelescopeStatus,
    TelescopeSpeed
)
from crac_client.gui_constants import GuiLabel


class TelescopeConverter:
    def convert(self, response, g_ui):
        if response.sync:
            g_ui.update_status_sync(GuiLabel.TELESCOPE_SYNC_ON, text_color="#2c2825", background_color="green")
            g_ui.update_button_sync(disabled=True)
        else:
            g_ui.update_status_sync(GuiLabel.TELESCOPE_SYNC_OFF, text_color="red", background_color="white")
            g_ui.update_button_sync(disabled=False)
        
        if response.speed == TelescopeSpeed.DEFAULT:
            g_ui.update_status_tracking(GuiLabel.TELESCOPE_TRACKING_OFF, text_color="red", background_color="white")
            g_ui.update_status_slewing(GuiLabel.TELESCOPE_SLEWING_OFF, text_color="red", background_color="white")
        elif response.speed == TelescopeSpeed.TRACKING:
            g_ui.update_status_tracking(GuiLabel.TELESCOPE_TRACKING_ON, text_color="#2c2825", background_color="green")
            g_ui.update_status_slewing(GuiLabel.TELESCOPE_SLEWING_OFF, text_color="red", background_color="white")
        elif response.speed == TelescopeSpeed.CENTERING:
            g_ui.update_status_tracking(GuiLabel.TELESCOPE_TRACKING_OFF, text_color="red", background_color="white")
            g_ui.update_status_slewing(GuiLabel.TELESCOPE_SLEWING_OFF, text_color="red", background_color="white")
        elif response.speed == TelescopeSpeed.SLEWING:
            g_ui.update_status_tracking(GuiLabel.TELESCOPE_TRACKING_OFF, text_color="red", background_color="white")
            g_ui.update_status_slewing(GuiLabel.TELESCOPE_SLEWING_ON, text_color="#2c2825", background_color="green")
        
        if response.status == TelescopeStatus.PARKED:
            pass
        elif response.status == TelescopeStatus.FLATTER:
            pass
        elif response.status == TelescopeStatus.SECURE:
            pass
        elif response.status == TelescopeStatus.NORTHEAST:
            pass
        elif response.status == TelescopeStatus.EAST:
            pass
        elif response.status == TelescopeStatus.SOUTHEAST:
            pass
        elif response.status == TelescopeStatus.SOUTHWEST:
            pass
        elif response.status == TelescopeStatus.WEST:
            pass
        elif response.status == TelescopeStatus.NORTHWEST:
            pass
        elif response.status == TelescopeStatus.LOST:
            pass
        elif response.status == TelescopeStatus.ERROR:
            pass
