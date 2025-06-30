from block import Block
from exceptions import OutputOutgoingException

class Output(Block):
    def __init__(self, incoming_blocks, destination=None):
        super().__init__(incoming_blocks)
        self.outgoing_blocks = None
        self.destination = destination

    def add_outgoing_block(self, outgoing_block):
        raise OutputOutgoingException("Output blocks cannot have outgoing blocks")
    
    def add_destination(self, destination):
        self.destination = destination
    
    def fire_outputs(self):
        [self.destination(incoming_block.fire_outputs()) for incoming_block in self.incoming_blocks]