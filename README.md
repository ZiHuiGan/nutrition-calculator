# 减脂期营养计算器

一个基于网页的减脂期营养计算工具，支持计算每日碳水、蛋白质需求，并提供食物搭配建议。

## 🌐 在线访问

**🔗 访问地址**：https://nutrition-calculator-pwa.vercel.app

- 📱 **PWA 支持**：可添加到手机主屏幕，像原生 App 一样使用
- ✨ **移动端优化**：已针对 iPhone 15 Pro Max 及主流手机优化
- 🎨 **响应式设计**：自动适配不同屏幕尺寸

## 功能特性

- 📊 根据身高、体重、性别自动计算营养配额
- 🍽️ 支持多种训练方案（早饭后练、午饭前练等）
- 🥗 食物数据库，包含常见碳水和蛋白质食物
- 📱 PWA 支持，可添加到手机主屏幕
- 💪 支持多种食物组合，自定义每餐搭配
- 📈 实时计算营养值，显示与目标对比
- 🎯 优化的移动端交互体验

## 使用方法

### 网页版

1. 访问：https://nutrition-calculator-pwa.vercel.app
2. 选择训练日类型（力训日/休息日）
3. 选择训练方案
4. 输入性别、身高、体重
5. 点击"计算营养需求"
6. 查看结果并选择食物搭配

### 添加到手机主屏幕（PWA）

**iPhone:**
1. 在 Safari 中打开网页
2. 点击底部分享按钮
3. 选择"添加到主屏幕"
4. 自定义名称后点击"添加"

**Android:**
1. 在 Chrome 中打开网页
2. 点击右上角菜单
3. 选择"添加到主屏幕"
4. 确认添加

详细步骤请参考 [MOBILE_APP_GUIDE.md](MOBILE_APP_GUIDE.md)

## 部署指南

### 方案一：使用 Zeabur（推荐，国内访问友好）

1. **创建 GitHub 仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Nutrition Calculator PWA"
   git branch -M main
   git remote add origin https://github.com/your-username/nutrition-calculator.git
   git push -u origin main
   ```

2. **部署到 Zeabur**
   - 访问 [zeabur.com](https://zeabur.com)
   - 使用 GitHub 账号登录
   - 点击 "New Project" → "Deploy Service"
   - 选择你的 GitHub 仓库
   - Zeabur 会自动识别并部署
   - 获得部署链接（如：`your-app.zeabur.app`）

3. **自动部署**
   - 每次 push 代码到 GitHub，Zeabur 会自动部署
   - 部署完成后，用户刷新页面即可看到更新

### 方案二：使用 Vercel

1. **创建 GitHub 仓库**（同上）

2. **部署到 Vercel**
   - 访问 [vercel.com](https://vercel.com)
   - 使用 GitHub 账号登录
   - 点击 "New Project"
   - 导入 GitHub 仓库
   - 框架选择 "Other" 或 "Static"
   - 点击 "Deploy"
   - 获得部署链接（如：`your-app.vercel.app`）

3. **更新社交分享链接**
   - 部署后，编辑 `index.html` 中的社交分享 meta 标签
   - 将 `your-app-url.vercel.app` 替换为实际部署地址
   - 提交并推送更新

### 方案三：使用 Cloudflare Pages

1. **创建 GitHub 仓库**（同上）

2. **部署到 Cloudflare Pages**
   - 访问 [dash.cloudflare.com](https://dash.cloudflare.com)
   - 进入 Pages → "Create a project"
   - 连接 GitHub 仓库
   - 配置构建设置（直接部署，无需构建命令）
   - 点击 "Save and Deploy"
   - 获得部署链接（如：`your-app.pages.dev`）

## 本地开发

### 启动本地服务器

```bash
# 使用 Python（推荐）
python3 -m http.server 8000

# 然后在浏览器打开
open http://localhost:8000
```

### 生成图标

如果修改了图标 SVG，重新生成 PNG 图标：

```bash
# 确保已安装 Pillow
pip3 install Pillow

# 运行生成脚本
python3 generate_icons.py
```

## 反馈与问题

### 提交反馈

我们欢迎所有反馈！请通过以下方式：

1. **GitHub Issues**（推荐）
   - 访问仓库的 [Issues 页面](https://github.com/your-username/nutrition-calculator/issues)
   - 点击 "New Issue"
   - 选择问题类型：
     - 🐛 Bug 报告
     - 💡 功能建议
     - 📝 使用问题
     - ❓ 其他

2. **提交 Issue 模板**

   **Bug 报告：**
   - 描述问题
   - 复现步骤
   - 预期行为
   - 实际行为
   - 设备/浏览器信息

   **功能建议：**
   - 功能描述
   - 使用场景
   - 预期效果

## 技术栈

- 纯 HTML/CSS/JavaScript（无框架）
- PWA（Progressive Web App）
- 响应式设计
- 移动端优化

## 文件结构

```
Nutrition/
├── index.html              # 主应用文件
├── manifest.json           # PWA 清单文件
├── generate_icons.py       # 图标生成脚本
├── .gitignore             # Git 忽略文件
├── README.md              # 本文件
├── icons/                 # 图标目录
│   ├── icon.svg
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── apple-touch-icon.png
│   └── favicon.ico
└── [其他数据文件]
```

## 更新日志

### v1.1.0 (最新)
- ✅ 针对 iPhone 15 Pro Max 优化移动端交互体验
- ✅ 更大的触摸目标（48-52px）
- ✅ 优化的间距和布局
- ✅ 防止 iOS 自动缩放
- ✅ 流畅的滚动体验
- ✅ 更新社交分享链接

### v1.0.0
- ✅ 初始版本发布
- ✅ 支持营养需求计算
- ✅ 食物数据库
- ✅ 多种食物组合功能
- ✅ PWA 支持
- ✅ 移动端优化

## 许可证

本项目采用 MIT 许可证。

## 贡献

欢迎提交 Pull Request！

## 支持

如有问题或建议，请通过 GitHub Issues 联系我们。

---

**注意：** 请将本文档中的 `your-username` 和 `nutrition-calculator` 替换为你的实际 GitHub 用户名和仓库名。
