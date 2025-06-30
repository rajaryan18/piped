from uuid import uuid4
from exceptions import OutputNotAvailableException

class Block():
    def __init__(self, incoming_blocks: list = [], outgoing_blocks: list = []):
        self.block_id = uuid4()
        self.incoming_blocks = incoming_blocks
        self.outgoing_blocks = outgoing_blocks
    
    def add_incoming_block(self, incoming_block):
        self.incoming_blocks.append(incoming_block)
    
    def add_outgoing_block(self, outgoing_block):
        self.outgoing_blocks.append(outgoing_block)
    
    def get_incoming_blocks(self):
        return self.incoming_blocks
    
    def get_outgoing_blocks(self):
        return self.outgoing_blocks
    
    def trigger_inputs(self):
        inputs = []
        for incoming_block in self.incoming_blocks:
            try:
                inputs.append(incoming_block.fire_outputs())
            except OutputNotAvailableException:
                print(f"[ERROR] Incoming data failed from Block ID: {incoming_block.block_id}")
                raise OutputNotAvailableException
            except OverflowError:
                print(f"[ERROR] Incoming data ended from Block ID: {incoming_block.block_id}")
                raise OverflowError
    
    def fire_outputs(self):
        pass