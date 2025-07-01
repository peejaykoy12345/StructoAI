import torch.nn as nn

class DocNet(nn.Module):
    def __init__(self, input_dim=100, output_dim=3):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64)
            nn.ReLU()
            nn.Linear(64, output_dim) 
        )
    def forward(self, x):
        return self.model(x)
    
    def fit(self, epochs):
        

    