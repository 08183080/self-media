# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the self-media content repository for 微信公众号「与龙邂逅」. Content is created, formatted, and published using Claude Code with baoyu-skills.

### Directory Structure
```
self-media/
├── articles/
│   ├── drafts/              # Work-in-progress articles
│   └── published/           # Published articles (archived by date)
│       └── YYYY-MM-DD-title/
│           ├── article.md   # Original Markdown
│           ├── article.html # Generated HTML
│           ├── cover.png    # Cover image
│           └── prompts/     # Generation prompts
├── assets/
│   ├── images/             # Shared image assets
│   ├── covers/             # Cover templates
│   └── templates/          # Article templates
├── scripts/                # Custom scripts
└── .baoyu-skills/          # Skills configuration (not committed to git)
```

## WeChat Official Account Publishing

### Configuration
- **Account**: 与龙邂逅
- **Default Author**: 谢苹果
- **Theme**: simple (简洁主题)
- **Publishing Method**: API (requires IP whitelist)
- **Comment Settings**: Closed, fans-only

### Title Format Rules ⚠️ CRITICAL
**微信公众号标题格式：`【关键词】自媒体爆款风格标题`**
- ✅ 格式：`【xxx】yyy`，xxx 是文章核心关键词，yyy 是吸引点击的爆款标题
- ❌ 不使用 emoji（如 🚀 ✨ 💡 ✅ ❌ 等）
- ❌ 不使用竖线 `|`
- ❌ 不使用其他特殊符号

**Examples:**
- ✅ Correct: `【AI智能体】卡帕西一句话点醒所有产品经理`
- ✅ Correct: `【Claude Code】官方最佳实践，看完少走三年弯路`
- ❌ Wrong: `🚀 Claude Code：让 AI 成为你的编程搭档 | 最佳实践全攻略`

### Article Workflow

**1. Create New Article**
```bash
# Copy template to drafts
cp assets/templates/article-template.md articles/drafts/my-new-article.md
```

**2. Edit Content**
- Write in Markdown format
- Use YAML frontmatter for metadata (title, author, summary)
- Follow title format rules (no emoji, no pipe symbol)
- Place images in `articles/drafts/images/` if needed

**3. Publish to WeChat**
```bash
# Use the baoyu-post-to-wechat skill
/baoyu-post-to-wechat articles/drafts/my-new-article.md
```

The skill will:
- Convert Markdown to HTML (simple theme)
- Generate/use cover image
- Upload to WeChat draft box via API
- Apply author, comment settings from config

**4. Archive Published Article**
After publishing, move to published directory:
```bash
# Create dated directory
mkdir -p articles/published/2026-02-19-article-slug

# Move files
mv articles/drafts/my-new-article.md articles/published/2026-02-19-article-slug/article.md
# HTML and cover will be generated in the dated directory
```

**5. Update README**
Add entry to published articles table in README.md

## Development Commands

### Publishing
```bash
# Publish article (auto-converts and uploads)
/baoyu-post-to-wechat articles/drafts/article.md

# Manual conversion (if needed)
/baoyu-markdown-to-html article.md --theme simple

# Manual upload (after HTML generation)
npx -y bun <skill-path>/scripts/wechat-api.ts article.html \
  --author "谢苹果" \
  --title "标题" \
  --summary "摘要" \
  --cover cover.png
```

### Content Creation
```bash
# Format Markdown (CJK spacing, emphasis fixes)
/baoyu-format-markdown article.md

# Generate cover image
/baoyu-cover-image --title "标题" --aspect 16:9
```

### Git Operations
```bash
# Add new article
git add articles/published/2026-02-19-article-slug/
git commit -m "Add article: [title]"
git push

# Note: .baoyu-skills/.env is excluded via .gitignore
```

## Architecture

### Skills Configuration
Configuration files stored in `.baoyu-skills/` (project-level):
- `baoyu-post-to-wechat/EXTEND.md` - Publishing preferences & title rules
- `baoyu-cover-image/EXTEND.md` - Cover image generation settings
- `.env` - API credentials (NOT committed to git)

### API Credentials
Required for WeChat API publishing:
- `WECHAT_APP_ID` - From mp.weixin.qq.com → 开发 → 基本配置
- `WECHAT_APP_SECRET` - Same location
- IP whitelist must include current IP address

### File Naming Convention
Published articles use date-slug format:
- Format: `YYYY-MM-DD-article-slug/`
- Example: `2026-02-19-claude-code-best-practices/`
- Slug: 2-5 words, lowercase, hyphens, English preferred

## Writing Style（文风规则）⚠️ CRITICAL

所有文章必须模仿作者「谢苹果」的个人文风，核心特征如下：

### 思维方式
- **游戏化隐喻**
- **第一性原理**：从根本处追问，不停留在表面现象，一刀切到底层逻辑

### 句式节奏
- **短句为主，长短交替**：不堆砌从句，用句号而非逗号断句，制造呼吸感
- **收束有力**：段落结尾用格言式金句收束
- **古文白话混搭**：偶尔用古典句式嵌入现代语境，形成文言白话的张力

### 表达态度
- **笃定但不说教**
- **狂喜代替焦虑**：面对未知不恐惧，而是兴奋
- **去中心化视角**：强调"每个人的"而非精英叙事，强调个体行动力

### 结构手法
- **先抛出观点或隐喻，再层层展开**，最后用一两句话收束全篇
- **善用类比和具象场景**
- **个人体验穿插论证**：用自己或朋友的真实故事锚定观点，不空谈

### 禁忌
- ❌ 不写空洞的鸡汤套话
- ❌ 不用"让我们一起xxx"之类的公众号八股句式
- ❌ 不堆砌专业术语炫技，术语出现时必须用大白话或隐喻翻译
- ❌ 不写面面俱到的百科式文章，宁可一刀见骨


## Important Notes

1. **Always check title format** before publishing - no emoji, no pipe symbol
2. **API credentials** are in `.baoyu-skills/.env` and excluded from git
3. **Cover images** are required for WeChat API publishing
4. **Drafts** should be moved to `published/` after successful publication
5. **Comment settings** default: closed, fans-only (configurable in EXTEND.md)
