# 部署指南

本指南将帮助你将营养计算器部署到云端，让全世界都能访问。

## 快速开始

### 步骤 1: 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角 "+" → "New repository"
3. 仓库名：`nutrition-calculator`（或你喜欢的名字）
4. 选择 Public（公开）
5. 不要初始化 README（我们已经有了）
6. 点击 "Create repository"

### 步骤 2: 初始化本地 Git 仓库

在项目目录下运行：

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

# 添加远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR-USERNAME/nutrition-calculator.git

# 推送到 GitHub
git push -u origin main
```

**注意：** 将 `YOUR-USERNAME` 替换为你的 GitHub 用户名。

### 步骤 3: 部署到云端

#### 选项 A: Zeabur（推荐，国内访问友好）

1. 访问 [zeabur.com](https://zeabur.com)
2. 使用 GitHub 账号登录
3. 点击 "New Project"
4. 点击 "Deploy Service"
5. 选择你的 GitHub 仓库 `nutrition-calculator`
6. Zeabur 会自动检测为静态网站
7. 点击 "Deploy"
8. 等待部署完成（约 1-2 分钟）
9. 获得部署链接（如：`nutrition-calculator-xxxxx.zeabur.app`）

**自动部署：**
- 每次你 push 代码到 GitHub，Zeabur 会自动重新部署
- 部署完成后，用户刷新页面即可看到更新

#### 选项 B: Vercel

1. 访问 [vercel.com](https://vercel.com)
2. 使用 GitHub 账号登录
3. 点击 "Add New..." → "Project"
4. 导入 GitHub 仓库 `nutrition-calculator`
5. 框架预设选择 "Other"
6. 根目录保持默认
7. 点击 "Deploy"
8. 等待部署完成
9. 获得部署链接（如：`nutrition-calculator.vercel.app`）

**更新社交分享链接：**

部署后，需要更新 `index.html` 中的社交分享 meta 标签：

1. 找到以下行（第 18-28 行左右）：
   ```html
   <meta property="og:url" content="https://your-app-url.vercel.app">
   <meta property="og:image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   ```

2. 将 `your-app-url.vercel.app` 替换为实际的 Vercel 部署地址

3. 提交并推送：
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs"
   git push
   ```

#### 选项 C: Cloudflare Pages

1. 访问 [dash.cloudflare.com](https://dash.cloudflare.com)
2. 登录账号（如果没有，注册免费账号）
3. 点击左侧菜单 "Workers & Pages"
4. 点击 "Create application" → "Pages" → "Connect to Git"
5. 选择 GitHub，授权并选择仓库
6. 配置构建设置：
   - Framework preset: None
   - Build command: （留空）
   - Build output directory: `/`（根目录）
7. 点击 "Save and Deploy"
8. 等待部署完成
9. 获得部署链接（如：`nutrition-calculator.pages.dev`）

### 步骤 4: 更新部署 URL

部署完成后，更新 `index.html` 中的社交分享链接：

1. 打开 `index.html`
2. 搜索 `your-app-url.vercel.app`（或对应的占位符）
3. 替换为实际的部署地址
4. 提交并推送更新

### 步骤 5: 测试部署

1. 在手机浏览器中打开部署链接
2. 测试所有功能
3. 尝试"添加到主屏幕"
4. 测试分享功能

## 后续更新

### 更新代码流程

```bash
# 1. 修改代码
# ... 在 Cursor 中修改 ...

# 2. 提交更改
git add .
git commit -m "描述你的更改"

# 3. 推送到 GitHub
git push

# 4. 自动部署（等待 1-2 分钟）
# 5. 用户刷新页面即可看到更新
```

## 启用 GitHub Issues（收集反馈）

1. 访问你的 GitHub 仓库
2. 点击 "Settings" 标签
3. 在左侧菜单找到 "Features"
4. 确保 "Issues" 已启用（默认开启）
5. 用户现在可以在仓库的 "Issues" 标签提交反馈

### 创建 Issue 模板（可选）

1. 在仓库根目录创建 `.github/ISSUE_TEMPLATE/` 目录
2. 创建模板文件（如 `bug_report.md`, `feature_request.md`）
3. 这将帮助用户更好地提交反馈

## 自定义域名（可选）

如果你有域名，可以绑定到部署平台：

### Zeabur
- 在项目设置中添加自定义域名
- 按照提示配置 DNS 记录

### Vercel
- 在项目设置 → Domains 中添加域名
- 按照提示配置 DNS

### Cloudflare Pages
- 在项目设置 → Custom domains 中添加域名
- 配置 DNS 记录

## 故障排除

### 部署失败

- 检查代码是否有语法错误
- 查看部署日志中的错误信息
- 确保所有必需文件都已提交到 Git

### 图标不显示

- 确保 `icons/` 目录已提交到 Git
- 检查 `manifest.json` 中的路径是否正确
- 检查浏览器控制台是否有 404 错误

### PWA 不工作

- 确保部署使用 HTTPS（所有部署平台都自动提供）
- 检查 `manifest.json` 是否存在且有效
- 使用浏览器开发者工具检查 PWA 清单

## 帮助

如遇问题，请：
1. 查看部署平台的文档
2. 在 GitHub Issues 中提问
3. 检查浏览器控制台错误信息
