import cv2
from input import Input
from exceptions import OutputNotAvailableException

class VideoInput(Input):
    def __init__(self, source, outgoing_blocks):
        super().__init__(outgoing_blocks=outgoing_blocks)
        self.source = self.set_input(source)
        self.outputs = None
    
    def set_input(self, source):
        return cv2.VideoCapture(source)

    def get_element(self):
        ret, img = self.source.read()
        if not ret:
            raise OverflowError("Video Stream Ended or encountered an error")
        self.outputs = img

    def fire_outputs(self):
        if self.outputs is not None:
            return self.outputs
        raise OutputNotAvailableException("Output from this block is not available")

    def run(self):
        try:
            return self.get_element()
        except OverflowError as error:
            print(f"[ERROR] {error}")
            return None