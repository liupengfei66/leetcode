import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadSelfAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super(MultiHeadSelfAttention, self).__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.query = nn.Linear(embed_dim, embed_dim)
        self.key = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

        self.out = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        seq_length = x.size(0)

        # Split into multiple heads
        queries = self.query(x).view(seq_length, self.num_heads, self.head_dim)
        keys = self.key(x).view(seq_length, self.num_heads, self.head_dim)
        values = self.value(x).view(seq_length, self.num_heads, self.head_dim)

        # Scaled dot-product attention
        keys = keys.permute(1, 2, 0)  # Transpose keys for multiplication
        attention_scores = torch.matmul(queries, keys) / (self.head_dim ** 0.5)
        attention_weights = F.softmax(attention_scores, dim=-1)
        attention_output = torch.matmul(attention_weights, values.permute(1, 0, 2))
        attention_output = attention_output.permute(1, 0, 2).contiguous().view(seq_length, self.embed_dim)

        # Pass through final linear layer
        output = self.out(attention_output)

        return output
