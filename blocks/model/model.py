from block import Block

class Model(Block):
    def __init__(self, model_weights, incoming_blocks: list = [], outgoing_blocks: list = []):
        super().__init__(incoming_blocks, outgoing_blocks)
        self.model_weights = model_weights
    
    def update_model_weights(self, model_weights):
        self.model_weights = model_weights