# 与龙邂逅 - 自媒体内容库

微信公众号「与龙邂逅」的文章创作与发布管理仓库。

## 📁 目录结构

```
self-media/
├── .baoyu-skills/              # 技能配置
│   ├── .env                    # API credentials（不提交）
│   ├── baoyu-post-to-wechat/   # 微信发布配置
│   └── baoyu-cover-image/      # 封面图生成配置
├── articles/                   # 文章目录
│   ├── drafts/                # 📝 草稿
│   └── published/             # ✅ 已发布
│       └── YYYY-MM-DD-title/  # 文章目录（按日期-标题命名）
│           ├── article.md     # 原始 Markdown
│           ├── article.html   # 生成的 HTML
│           ├── cover.png      # 封面图
│           └── prompts/       # 生成提示
├── assets/                     # 公共资源
│   ├── images/                # 图片素材
│   ├── covers/                # 封面模板
│   └── templates/             # 文章模板
├── scripts/                    # 自定义脚本
└── CLAUDE.md                   # Claude Code 工作指南
```

## 🚀 快速开始

### 1. 创建新文章

在 `articles/drafts/` 创建新的 Markdown 文件：

```bash
# 使用模板
cp assets/templates/article-template.md articles/drafts/my-new-article.md
```

### 2. 发布文章

使用 Claude Code 的 baoyu-post-to-wechat 技能：

```bash
# 方式一：直接调用技能
/baoyu-post-to-wechat articles/drafts/my-article.md

# 方式二：使用 Claude Code 对话
"帮我发布 articles/drafts/my-article.md 到微信公众号"
```

### 3. 文章归档

发布后，将文章移动到 `articles/published/` 并按日期命名：

```bash
mv articles/drafts/my-article.md articles/published/2026-02-19-my-article/article.md
```

## 📝 文章规范

### 标题格式要求

**⚠️ 微信公众号标题限制：**
- ❌ 不使用 emoji（如 🚀 ✨ 💡）
- ❌ 不使用竖线 `|` 作为分隔符
- ✅ 使用破折号 `-` 或冒号 `：`
- ✅ 推荐格式：「主标题：副标题」或「主标题 - 副标题」

**示例：**
```
✅ Claude Code：让 AI 成为你的编程搭档 - 最佳实践全攻略
❌ 🚀 Claude Code：让 AI 成为你的编程搭档 | 最佳实践全攻略
```

### Markdown 格式建议

- 使用 YAML frontmatter 设置元数据（标题、作者、摘要）
- H2 (##) 作为主要章节标题
- 适当使用粗体、列表、代码块增强可读性
- 图片放在文章同目录的 `images/` 子文件夹

## ⚙️ 配置信息

### 公众号信息
- **名称**：与龙邂逅
- **默认作者**：谢苹果
- **主题**：simple（简洁主题）
- **评论设置**：关闭，仅粉丝可评论

### API 配置
- API credentials 存储在 `.baoyu-skills/.env`（不提交到 git）
- 发布方式：API（需要 IP 白名单）
- 草稿管理：https://mp.weixin.qq.com

## 🛠️ 常用命令

```bash
# 创建新文章
cp assets/templates/article-template.md articles/drafts/new-article.md

# 发布到微信
/baoyu-post-to-wechat articles/drafts/new-article.md

# 生成封面图
/baoyu-cover-image --title "文章标题" --aspect 16:9

# 格式化 Markdown
/baoyu-format-markdown articles/drafts/new-article.md

# 提交更改
git add .
git commit -m "Add new article: [title]"
git push
```

## 📊 已发布文章

| 日期 | 标题 | 状态 |
|------|------|------|
| 2026-02-19 | Claude Code：让 AI 成为你的编程搭档 - 最佳实践全攻略 | ✅ 已发布 |

## 📖 相关资源

- [微信公众号后台](https://mp.weixin.qq.com)
- [Claude Code 文档](https://docs.anthropic.com/claude/docs)
- [baoyu-skills GitHub](https://github.com/JimLiu/baoyu-skills)

---

**作者**：谢苹果
**更新日期**：2026-02-19
