from exceptions import InputIncomingException
from block import Block

class Input(Block):
    def __init__(self, outgoing_blocks):
        super().__init__(outgoing_blocks)
        # Input block cannot have incoming blocks
        self.incoming_blocks = None
    
    def add_incoming_block(self, incoming_block):
        raise InputIncomingException("Input blocks cannot have incoming blocks")

    def set_input(self, source):
        self.source = source
    
    def get_element(self):
        return self.source