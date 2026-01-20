# 立即部署到 Vercel - 快速指南

## ✅ 准备工作已完成

- ✅ GitHub 仓库已创建：https://github.com/ZiHuiGan/nutrition-calculator
- ✅ 代码已推送
- ✅ PWA 配置完成
- ✅ 所有文件已准备就绪

## 🚀 部署步骤（3 分钟完成）

### 方式 1: 通过导入页面（推荐）

1. **直接访问这个链接**（如果已登录 Vercel）：
   ```
   https://vercel.com/new?import-project&repository=https://github.com/ZiHuiGan/nutrition-calculator
   ```

2. **或者访问**：
   - https://vercel.com/new
   - 点击 "Import Git Repository"
   - 点击 "Continue with GitHub"（如果还没连接）
   - 搜索 `nutrition-calculator` 或 `ZiHuiGan/nutrition-calculator`
   - 点击仓库名称

3. **配置项目**（通常自动检测）：
   - Framework Preset: `Other`
   - Root Directory: `./` (保持默认)
   - Build Command: （留空）
   - Output Directory: （留空）
   - Install Command: （留空）

4. **点击 "Deploy"**

5. **等待部署完成**（约 1-2 分钟）

6. **获得部署链接**（如：`nutrition-calculator-xxxxx.vercel.app`）

### 方式 2: 通过项目页面

1. 访问 https://vercel.com/dashboard
2. 点击 "Add New..." → "Project"
3. 搜索 `nutrition-calculator`
4. 点击仓库名称
5. 点击 "Deploy"

## 📝 部署后需要做的

### 更新社交分享链接

部署完成后，你会获得一个链接，例如：
- `https://nutrition-calculator-xxxxx.vercel.app`

**更新 index.html**：

1. 打开 `index.html`
2. 找到以下行（第 21-33 行），替换 `your-app-url.vercel.app`：
   ```html
   <meta property="og:url" content="https://nutrition-calculator-xxxxx.vercel.app">
   <meta property="og:image" content="https://nutrition-calculator-xxxxx.vercel.app/icons/icon-512.png">
   <meta name="twitter:image" content="https://nutrition-calculator-xxxxx.vercel.app/icons/icon-512.png">
   <meta itemprop="image" content="https://nutrition-calculator-xxxxx.vercel.app/icons/icon-512.png">
   ```

3. 提交并推送更新：
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs"
   git push
   ```

4. Vercel 会自动重新部署（约 1-2 分钟）

## ✨ 完成！

部署完成后，你可以：
- 📱 在手机浏览器中访问链接
- ➕ 添加到主屏幕（像 App 一样使用）
- 🔗 分享链接到社交平台
- 📊 通过 GitHub Issues 收集反馈

## 🔄 后续更新

每次修改代码后，只需：
```bash
git add .
git commit -m "描述更改"
git push
```

Vercel 会自动重新部署，用户刷新页面即可看到更新。
