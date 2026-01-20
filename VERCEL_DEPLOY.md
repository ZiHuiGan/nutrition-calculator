# Vercel 部署完整指南

## ✅ 已完成的工作

1. ✅ **GitHub 仓库创建成功**
   - 仓库地址：https://github.com/ZiHuiGan/nutrition-calculator
   - 所有代码已推送
   - 主分支：`main`

2. ✅ **PWA 功能已配置**
   - manifest.json 已创建
   - 所有图标已生成（192x192, 512x512, 180x180, 32x32）
   - 社交分享 meta 标签已添加
   - 移动端优化已完成

3. ✅ **项目文件已就绪**
   - index.html（PWA 支持）
   - manifest.json
   - vercel.json（Vercel 配置）
   - icons/ 目录（所有图标）
   - README.md, DEPLOYMENT.md 等文档

## 🚀 部署到 Vercel（3 步完成）

### 步骤 1: 访问导入页面

**直接点击这个链接**（如果已登录 Vercel）：
```
https://vercel.com/new?import-project&repository=https://github.com/ZiHuiGan/nutrition-calculator
```

**或者**：
1. 访问 https://vercel.com/new
2. 如果没有登录，点击 "Login" → "Continue with GitHub"
3. 授权 Vercel 访问 GitHub

### 步骤 2: 导入仓库

1. 在 "Import Git Repository" 区域
2. 点击 "Continue with GitHub"（如果还没连接 GitHub）
3. 在仓库列表中找到 `ZiHuiGan/nutrition-calculator`
4. 点击仓库名称旁边的 "Import"

### 步骤 3: 配置并部署

Vercel 会自动检测配置，但请确认以下设置：

| 设置项 | 值 | 说明 |
|--------|-----|------|
| **Framework Preset** | `Other` | 静态网站，无框架 |
| **Root Directory** | `./` | 保持默认（根目录） |
| **Build Command** | （留空） | 静态网站无需构建 |
| **Output Directory** | （留空） | 保持默认 |
| **Install Command** | （留空） | 无需安装依赖 |

**然后**：
1. 点击 "Deploy" 按钮
2. 等待部署完成（约 1-2 分钟）
3. 部署完成后，会显示访问链接

**部署链接格式**：
- Production: `https://nutrition-calculator-xxxxx.vercel.app`
- 或者：`https://nutrition-calculator.vercel.app`

## 📝 部署后更新（重要！）

部署完成后，需要更新 `index.html` 中的社交分享链接：

### 快速更新脚本

在项目目录下运行（替换 `YOUR-DEPLOYMENT-URL` 为实际地址）：

```bash
cd /Users/gambby/Desktop/兴趣/CodeSpace/Nutrition

# 获取部署地址（从 Vercel 项目页面复制）
DEPLOY_URL="YOUR-DEPLOYMENT-URL"  # 例如：nutrition-calculator-xxxxx.vercel.app

# 更新 index.html
sed -i '' "s/your-app-url\.vercel\.app/${DEPLOY_URL}/g" index.html

# 提交并推送
git add index.html
git commit -m "Update social sharing URLs with deployment link"
git push

# Vercel 会自动重新部署（1-2 分钟）
```

### 手动更新

1. 打开 `index.html`
2. 找到第 21-33 行，替换 URL：
   ```html
   <!-- 将这些行中的 your-app-url.vercel.app 替换为实际部署地址 -->
   <meta property="og:url" content="https://你的实际地址.vercel.app">
   <meta property="og:image" content="https://你的实际地址.vercel.app/icons/icon-512.png">
   <meta name="twitter:image" content="https://你的实际地址.vercel.app/icons/icon-512.png">
   <meta itemprop="image" content="https://你的实际地址.vercel.app/icons/icon-512.png">
   ```
3. 保存文件
4. 提交并推送：
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs"
   git push
   ```

## ✅ 验证部署

部署完成后：

1. **访问部署链接**（从 Vercel 项目页面）
2. **测试功能**：
   - 计算营养需求
   - 选择食物组合
   - 查看结果

3. **测试 PWA**（手机）：
   - 在手机 Safari/Chrome 中打开链接
   - 点击分享 → "添加到主屏幕"
   - 在主屏幕上像 App 一样打开

4. **测试社交分享**：
   - 在微信/微博中分享链接
   - 检查预览卡片是否正确显示

## 🔄 自动部署设置

Vercel 默认启用自动部署：
- ✅ 每次 push 到 `main` 分支会自动部署
- ✅ 部署完成后，用户刷新页面即可看到更新
- ✅ 可以在项目设置中关闭自动部署（不推荐）

## 📊 查看部署状态

- **Vercel Dashboard**: https://vercel.com/dashboard
- **项目页面**: 点击项目名称可查看所有部署
- **部署日志**: 每个部署都可以查看详细日志

## 🎉 完成！

部署完成后，你的应用已经：
- ✅ 全球可访问（通过 Vercel CDN）
- ✅ HTTPS 自动启用
- ✅ 支持 PWA（可添加到主屏幕）
- ✅ 社交分享优化
- ✅ 自动部署（代码更新自动发布）

## 📖 相关文档

- [DEPLOYMENT.md](DEPLOYMENT.md) - 详细部署指南
- [DEPLOY_STATUS.md](DEPLOY_STATUS.md) - 当前部署状态
- [UPDATE_URLS.md](UPDATE_URLS.md) - 更新链接指南
- [README.md](README.md) - 项目使用说明
