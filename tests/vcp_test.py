
# Core Python imports.
import os
import sys
import threading




#   00000000 3a02c000 784646000000003a02c000784646005a5a5a
# b'00000014 3a02c000 0100020000000000000000000a000000500202000100a5a5a5a5'
# 973258752



# Modify path so we can include the version of cruntils in this directory
# instead of relying on the user having it installed.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import our package.
import cruntils

# class CVcpManagerObject(cruntils.Obj.CActiveObject):
#     def __init__(self, name):

#         # Call base init.
#         super().__init__(name)

#     def Start(self):

#         # Open the hardware serial port connection and connect.
#         self.Vcp = cruntils.serial.Vcp("COM3")
#         self.Vcp.Open()

#         # Put the hardware into auto-update mode (so we don't have to poll it).
#         self.Vcp.SetAutoUpdate(True, True)

#         # Now keep checking the serial port for updates and send them out to
#         # the network port.
#         while True:

#             # Check for latest hardware state.
#             self.Vcp.Read()

#             # Put latest state into message and send.


msg = cruntils.fw.MVcpRadioStatus()
print(msg.Serialise().hex())


