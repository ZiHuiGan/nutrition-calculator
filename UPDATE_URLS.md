# 部署后更新社交分享链接

## 部署完成后需要做的

部署到 Vercel 后，你会获得一个部署链接，例如：
- `https://nutrition-calculator-xxxxx.vercel.app`

需要将这个链接更新到 `index.html` 文件中。

## 快速更新方法

### 方法 1: 手动替换（推荐）

1. 打开 `index.html`
2. 找到以下行（大约第 22-35 行）：
   ```html
   <meta property="og:url" content="https://your-app-url.vercel.app">
   <meta property="og:image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   <meta name="twitter:image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   <meta itemprop="image" content="https://your-app-url.vercel.app/icons/icon-512.png">
   ```

3. 将所有 `your-app-url.vercel.app` 替换为你的实际部署地址

4. 保存文件，然后运行：
   ```bash
   git add index.html
   git commit -m "Update social sharing URLs"
   git push
   ```

### 方法 2: 使用命令行快速替换

```bash
cd /Users/gambby/Desktop/兴趣/CodeSpace/Nutrition

# 替换 YOUR-ACTUAL-URL 为你的实际部署地址
sed -i '' 's/your-app-url\.vercel\.app/YOUR-ACTUAL-URL/g' index.html

# 提交并推送
git add index.html
git commit -m "Update social sharing URLs with deployment link"
git push
```

## 如何获取部署地址

1. 访问 https://vercel.com/dashboard
2. 找到你的项目 `nutrition-calculator`
3. 点击项目名称
4. 在项目页面可以看到：
   - Production URL（生产环境地址）
   - 或者 Deployment URL（部署地址）

复制这个 URL，然后更新到 `index.html` 中。

## 验证更新

更新后，等待 Vercel 自动重新部署（1-2 分钟），然后：
1. 访问部署链接
2. 在社交平台（微信、微博等）分享链接
3. 检查分享预览是否正确显示
