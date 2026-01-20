# 部署状态

## ✅ 已完成

1. ✅ **GitHub 仓库已创建**
   - 仓库地址：https://github.com/ZiHuiGan/nutrition-calculator
   - 代码已推送
   - 所有 PWA 文件已提交

2. ✅ **PWA 配置完成**
   - manifest.json 已创建
   - 所有图标已生成
   - 社交分享标签已添加
   - 移动端优化已完成

3. ✅ **项目文件准备就绪**
   - index.html（PWA 支持）
   - manifest.json
   - icons/ 目录（所有图标）
   - README.md
   - .gitignore

## 🔄 待完成（需要在 Vercel 网站操作）

### 步骤 1: 登录 Vercel（如果还没登录）

1. 访问 https://vercel.com/login
2. 点击 "Continue with GitHub"
3. 授权 Vercel 访问 GitHub

### 步骤 2: 导入仓库部署

1. 登录后，访问 https://vercel.com/new
2. 点击 "Import Git Repository" 区域的 "Continue with GitHub"
3. 在仓库列表中找到 `ZiHuiGan/nutrition-calculator`
4. 点击仓库名称或 "Import"

### 步骤 3: 配置项目（通常自动完成）

Vercel 会自动检测配置，但请确认：
- **Framework Preset**: `Other` 或 `Static`
- **Root Directory**: `./` (根目录)
- **Build Command**: （留空，静态网站无需构建）
- **Output Directory**: `./` 或留空
- **Install Command**: （留空）

点击 "Deploy" 按钮

### 步骤 4: 等待部署完成

- 通常需要 1-2 分钟
- 可以看到实时部署日志
- 部署完成后会显示部署链接（如：`nutrition-calculator-xxxxx.vercel.app`）

### 步骤 5: 更新社交分享链接

部署完成后，需要更新 `index.html` 中的 URL：

1. **复制部署链接**（从 Vercel 项目页面）
   - 格式：`https://nutrition-calculator-xxxxx.vercel.app`

2. **更新 index.html**（第 22-35 行）
   
   将以下行中的 URL 替换为实际部署地址：
   ```html
   <meta property="og:url" content="你的实际部署地址">
   <meta property="og:image" content="你的实际部署地址/icons/icon-512.png">
   <meta name="twitter:image" content="你的实际部署地址/icons/icon-512.png">
   <meta itemprop="image" content="你的实际部署地址/icons/icon-512.png">
   ```

3. **提交并推送更新**
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs with deployment link"
   git push
   ```

4. **自动重新部署**
   - Vercel 会自动检测代码更新
   - 自动触发重新部署（1-2 分钟）

## 📝 快速命令参考

### 后续更新代码时：

```bash
cd /Users/gambby/Desktop/兴趣/CodeSpace/Nutrition

# 修改代码后
git add .
git commit -m "描述你的更改"
git push

# Vercel 会自动部署（约 1-2 分钟）
```

## 🔗 重要链接

- **GitHub 仓库**: https://github.com/ZiHuiGan/nutrition-calculator
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Vercel 新建项目**: https://vercel.com/new

## ⚠️ 注意事项

1. **部署链接**：部署完成后，记得更新 `index.html` 中的社交分享 URL
2. **自动部署**：确保 Vercel 项目中启用了自动部署（默认开启）
3. **HTTPS**：Vercel 自动提供 HTTPS，PWA 功能可以正常使用
