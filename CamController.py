import pylablib as pll
pll.par["devices/dlls/sisofgrab"] = "C:\Program Files\SiliconSoftware\Runtime5.7\bin"
from pylablib.devices import SiliconSoftware as SiSo

class CamController():
    def __init__(self):
        self.cam = SiSo.SiliconSoftwareCamera(0, "FullAreaGray8_HS")
        
    
    def get_frame(self):
        '''get a single fram'''
        frame = self.cam.snap()
        return frame
    
    def get_frames(self, num):
        '''get num sequential frames'''
        frames = self.cam.grab(num)
        return frames
    
    def close(self):
        '''close connection to cam'''
        self.cam.close()
    
    # automatically close cam connection when garbage collected
    def __del__(self):
        self.close()

