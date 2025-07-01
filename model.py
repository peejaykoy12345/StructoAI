import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

class DocNet(nn.Module):
    def __init__(self, input_dim=100, output_dim=3):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, output_dim) 
        )
    def forward(self, x):
        return self.model(x)
    
    def fit(self, train_loader, epochs):
        optimizer = torch.optim.Adam(self.parameters(), lr=0.001)
        criterion = nn.CrossEntropyLoss()

        for epoch in range(epochs):
            for x, y in train_loader:
                optimizer.zero_grad()
                y_pred = self.model(x)
                loss = criterion(y_pred, y)
                loss.backward()
                optimizer.step()

    