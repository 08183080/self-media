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
**微信公众号标题格式要求：**
- ❌ 不使用 emoji（如 🚀 ✨ 💡 ✅ ❌ 等）
- ❌ 不使用竖线 `|` 作为分隔符
- ❌ 不使用其他特殊符号
- ✅ 使用破折号 `-` 或冒号 `：` 作为分隔符
- ✅ 推荐格式：「主标题：副标题」或「主标题 - 副标题」

**Examples:**
- ❌ Wrong: `🚀 Claude Code：让 AI 成为你的编程搭档 | 最佳实践全攻略`
- ✅ Correct: `Claude Code：让 AI 成为你的编程搭档 - 最佳实践全攻略`

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

## Important Notes

1. **Always check title format** before publishing - no emoji, no pipe symbol
2. **API credentials** are in `.baoyu-skills/.env` and excluded from git
3. **Cover images** are required for WeChat API publishing
4. **Drafts** should be moved to `published/` after successful publication
5. **Comment settings** default: closed, fans-only (configurable in EXTEND.md)
