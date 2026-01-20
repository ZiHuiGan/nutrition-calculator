# 快速开始指南

## 已完成的准备工作

✅ PWA manifest.json 文件已创建  
✅ 应用图标已生成（所有必需尺寸）  
✅ 社交分享 meta 标签已添加  
✅ 移动端样式已优化  
✅ .gitignore 文件已创建  
✅ README.md 文档已创建  
✅ 部署指南已创建

## 下一步操作

### 1. 初始化 Git 仓库并推送到 GitHub

```bash
cd /Users/gambby/Desktop/兴趣/CodeSpace/Nutrition

# 初始化 Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Nutrition Calculator PWA"

# 设置主分支
git branch -M main

# 添加远程仓库（替换 YOUR-USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR-USERNAME/nutrition-calculator.git

# 推送到 GitHub
git push -u origin main
```

### 2. 部署到云端（选择其中一个）

#### 选项 A: Zeabur（推荐，国内访问友好）

1. 访问 https://zeabur.com
2. 使用 GitHub 账号登录
3. 点击 "New Project" → "Deploy Service"
4. 选择你的 GitHub 仓库
5. 等待自动部署（1-2 分钟）
6. 获得部署链接

#### 选项 B: Vercel

1. 访问 https://vercel.com
2. 使用 GitHub 账号登录
3. 点击 "Add New..." → "Project"
4. 导入 GitHub 仓库
5. 框架选择 "Other"
6. 点击 "Deploy"
7. 获得部署链接

### 3. 更新社交分享链接

部署后，编辑 `index.html`，将以下位置的 URL 替换为实际部署地址：

- 第 22 行：`og:url`
- 第 24 行：`og:image`
- 第 30 行：`twitter:image`
- 第 35 行：`itemprop="image"`

然后提交并推送更新。

### 4. 测试

- 在手机浏览器中打开部署链接
- 测试"添加到主屏幕"功能
- 测试分享功能
- 测试所有计算功能

## 完整文档

- 📖 详细使用说明：查看 [README.md](README.md)
- 🚀 部署指南：查看 [DEPLOYMENT.md](DEPLOYMENT.md)

## 需要帮助？

如有问题，请查看：
1. README.md 中的故障排除部分
2. DEPLOYMENT.md 中的详细部署说明
3. 在 GitHub Issues 中提问
