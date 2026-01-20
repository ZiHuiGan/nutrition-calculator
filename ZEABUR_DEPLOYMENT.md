# Zeabur 部署完整指南

## 你需要提供的信息

### 必需信息

1. **GitHub 账号**
   - 如果没有账号：访问 https://github.com 注册（免费）
   - 需要邮箱地址即可注册

2. **GitHub 仓库**
   - 你需要先在 GitHub 创建一个仓库
   - 仓库名建议：`nutrition-calculator` 或你喜欢的名字
   - 必须设置为 Public（公开）以便部署

### 可选信息

3. **项目名称**（可选）
   - Zeabur 会自动使用 GitHub 仓库名
   - 部署后可以在设置中修改

4. **自定义域名**（可选，后续可添加）
   - 如果有域名，可以绑定
   - 暂时不需要，可以先用免费的 `.zeabur.app` 域名

---

## 完整部署步骤

### 步骤 1: 创建 GitHub 仓库

1. **登录 GitHub**
   - 访问 https://github.com
   - 登录你的账号（或注册新账号）

2. **创建新仓库**
   - 点击右上角 "+" → "New repository"
   - Repository name: `nutrition-calculator`（或你喜欢的名字）
   - Description（可选）: "减脂期营养计算器 PWA"
   - 选择 **Public**（必须公开才能免费部署）
   - **不要**勾选 "Add a README file"（我们已经有了）
   - 点击 "Create repository"

3. **记录仓库 URL**
   - 创建后，GitHub 会显示仓库 URL
   - 格式：`https://github.com/YOUR-USERNAME/nutrition-calculator.git`
   - 记住这个 URL，下一步会用到

### 步骤 2: 推送代码到 GitHub

在项目目录下运行以下命令（**替换 YOUR-USERNAME 为你的 GitHub 用户名**）：

```bash
cd /Users/gambby/Desktop/兴趣/CodeSpace/Nutrition

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit: Nutrition Calculator PWA"

# 设置主分支
git branch -M main

# 添加远程仓库（替换 YOUR-USERNAME）
git remote add origin https://github.com/YOUR-USERNAME/nutrition-calculator.git

# 推送到 GitHub
git push -u origin main
```

**如果提示输入用户名和密码：**
- 用户名：你的 GitHub 用户名
- 密码：使用 **Personal Access Token**（不是 GitHub 密码）
  - 生成 Token：GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
  - 勾选 `repo` 权限
  - 复制生成的 token 作为密码使用

### 步骤 3: 在 Zeabur 部署

1. **访问 Zeabur**
   - 访问 https://zeabur.com
   - 点击右上角 "Sign In" 或 "Get Started"

2. **使用 GitHub 登录**
   - 点击 "Continue with GitHub"
   - 授权 Zeabur 访问你的 GitHub 账号
   - 选择需要授权的权限范围（选择仓库访问权限即可）

3. **创建项目**
   - 登录后，点击 "New Project"
   - 输入项目名称（可选，如：Nutrition Calculator）
   - 点击 "Create"

4. **部署服务**
   - 在项目页面，点击 "Deploy Service" 或 "+"
   - 选择 "Deploy from GitHub"
   - 从列表中选择你的仓库 `nutrition-calculator`
   - 点击 "Deploy"

5. **等待部署**
   - Zeabur 会自动检测项目类型（静态网站）
   - 自动配置构建设置
   - 等待部署完成（通常 1-2 分钟）
   - 可以看到部署进度和日志

6. **获得部署链接**
   - 部署完成后，会显示访问链接
   - 格式：`nutrition-calculator-xxxxx.zeabur.app`
   - 点击链接即可访问你的应用

### 步骤 4: 更新社交分享链接（重要）

部署完成后，需要更新 `index.html` 中的社交分享 URL：

1. **获取实际部署地址**
   - 从 Zeabur 项目页面复制部署链接
   - 格式：`https://nutrition-calculator-xxxxx.zeabur.app`

2. **更新 index.html**
   ```bash
   # 在 Cursor 中打开 index.html
   # 找到以下行（大约第 22-35 行）：
   ```

   需要替换的 URL：
   ```html
   <meta property="og:url" content="https://your-app-url.vercel.app">
   <meta property="og:image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   <meta name="twitter:image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   <meta itemprop="image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   ```

   替换为：
   ```html
   <meta property="og:url" content="https://nutrition-calculator-xxxxx.zeabur.app">
   <meta property="og:image" content="https://nutrition-calculator-xxxxx.zeabur.app/icons/icon-512.png">
   <meta name="twitter:image" content="https://nutrition-calculator-xxxxx.zeabur.app/icons/icon-512.png">
   <meta itemprop="image" content="https://nutrition-calculator-xxxxx.zeabur.app/icons/icon-512.png">
   ```

3. **提交更新**
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs with Zeabur deployment link"
   git push
   ```

4. **自动重新部署**
   - Zeabur 会自动检测到代码更新
   - 自动触发重新部署（1-2 分钟）
   - 更新后社交分享会显示正确的预览

---

## 自动部署设置（默认已启用）

Zeabur 默认会在以下情况自动重新部署：

- ✅ 你推送代码到 GitHub 的 main 分支
- ✅ 你可以手动点击 "Redeploy" 按钮
- ✅ 部署设置中的自动部署默认开启

**关闭自动部署（不推荐）：**
- 项目设置 → Service → Settings → 关闭 "Auto Deploy"

---

## 费用说明

- ✅ **完全免费**：Zeabur 对个人项目提供免费额度
- ✅ 免费额度足够运行这个静态网站项目
- ✅ 不需要绑定信用卡

---

## 常见问题

### Q: 需要绑定信用卡吗？
A: 不需要。Zeabur 免费额度足够这个项目使用。

### Q: 部署需要多长时间？
A: 通常 1-2 分钟。首次部署可能需要稍长一些。

### Q: 可以绑定自定义域名吗？
A: 可以。部署后在项目设置 → Domains 中添加域名，并配置 DNS。

### Q: 如何查看部署日志？
A: 在 Zeabur 项目页面，点击服务名称，可以看到部署日志和实时日志。

### Q: 部署失败怎么办？
A: 
1. 查看部署日志中的错误信息
2. 确保所有文件都已提交到 GitHub
3. 检查 `.gitignore` 是否排除了必需文件
4. 在 GitHub Issues 或 Zeabur 文档中查找解决方案

### Q: 如何删除部署？
A: 在 Zeabur 项目页面，点击服务设置 → Delete Service

---

## 下一步

部署成功后：

1. ✅ 测试应用功能
2. ✅ 在手机浏览器测试 PWA（添加到主屏幕）
3. ✅ 测试社交分享功能
4. ✅ 分享链接给用户收集反馈
5. ✅ 通过 GitHub Issues 收集反馈

---

## 需要帮助？

- 📖 Zeabur 文档：https://zeabur.com/docs
- 💬 GitHub Issues：在你的仓库中提问
- 🔍 查看部署日志：在 Zeabur 项目页面查看详细日志
