class Cup:
    def __init__(self,size :int,quantity :int):
        self.size = size
        self.quantity = quantity
        
    def fill(self,quantity :int) -> None:
        if self.quantity + quantity <= self.size:
            self.quantity += quantity
            
    def status(self) -> int | float: #returns int OR float
        return self.size  - self.quantity
    
    
        
        
