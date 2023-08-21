import torch
import torch.nn as nn
import torch.nn.functional as F
# 单个input.shape = (seq_length, embed_dim)
# 不能接受batch 输入

class SelfAttention(nn.Module):
    def __init__(self, embed_dim):
        super(SelfAttention, self).__init__()
        self.embed_dim = embed_dim

        self.query = nn.Linear(embed_dim, embed_dim)
        self.key = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

        self.out = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        seq_length = x.size(0)

        # Compute queries, keys and values
        queries = self.query(x)
        keys = self.key(x)
        values = self.value(x)

        # Scaled dot-product attention
        attention_scores = torch.matmul(queries, keys.transpose(1, 0)) / (self.embed_dim ** 0.5)
        attention_weights = F.softmax(attention_scores, dim=-1)
        attention_output = torch.matmul(attention_weights, values)

        # Pass through final linear layer
        output = self.out(attention_output)

        return output
