import torch
import torch.nn as nn
import torch.optim as optim

# 逻辑回归模型
class LogisticRegression(nn.Module):
    def __init__(self, input_dim):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

# 生成模拟数据
torch.manual_seed(42)
X = torch.cat((torch.randn(50, 2) - 2, torch.randn(50, 2) + 2), dim=0)
Y = torch.cat((torch.zeros(50, 1), torch.ones(50, 1)), dim=0)

# 设置超参数
input_dim = X.shape[1]
learning_rate = 0.01
epochs = 1000

# 创建模型
model = LogisticRegression(input_dim)
criterion = nn.BCELoss() # 二元交叉熵损失
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# 训练模型
for epoch in range(epochs):
    # 前向传播
    predictions = model(X)
    loss = criterion(predictions, Y)

    # 反向传播和优化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}')

# 打印学习到的权重和偏置
print(f'Learned Weights: {model.linear.weight}')
print(f'Learned Bias: {model.linear.bias}')
