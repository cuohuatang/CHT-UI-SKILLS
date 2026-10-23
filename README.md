# CHT-UI-SKILLS

一站式前端视觉与动效技能集，融合 15 大能力，并内置一条「审美打底 → 出方案矩阵 → 出稿（静态稿 / 可拖改原型）→ 生成可运行代码（快速 / 工程模式）→ 完成前验证 → 实测验收」的编排工作流。

## 工作流（内置）

```
frontend-design 定审美立场 + taste-skill/garden-skills 供方向素材（避开 AI 默认陷阱）
   ↓
oil-ui + 8 大分册 → 出「风格 × 技术」方案矩阵（默认 6-9 版）放在对比页让你挑
   ↓ 闸门确认分支
分支甲：draw-ui → 出静态精细设计稿
分支乙：m3e-canvas → 出可拖改原型（AI 直出，边看边改）
   ↓
第三步：生成可运行代码
   快速模式：v0.dev Chat / Builder.io 生成代码
   工程模式：superpowers 驱动（计划 → TDD → 子代理执行 → 验证 → 评审）
   ↓
第四步：完成前验证（跑测试/构建，附验证证据）
   ↓
你手动接进项目、git 提交、部署
```

## 15 大能力

| # | 能力 | 开源来源 | 一句话 |
|---|------|----------|--------|
| 1 | p5.js 创意编码 | `processing/p5.js` | 交互式 Canvas 视觉、粒子背景、生成艺术 |
| 2 | CSS Doodle 图案 | `css-doodle/css-doodle` | 类 CSS 小 DSL 生成几何纹理 / SVG / GPU shader |
| 3 | Theatre.js 编排 | `theatre-js/theatre` | 网页里的 AE：时间轴 + 关键帧，编排出场顺序 |
| 4 | React Spring 物理动画 | `pmndrs/react-spring` | 弹簧物理弹性，手势跟随与列表进出 |
| 5 | Inure 精致微交互 | `Hamza417/Inure`（参考样本） | 参考拆解 + 复刻「小操作也舒服」的 UI 动效 |
| 6 | UI-UX Craft 设计工艺 | 设计规范方法论 | token + 组件状态矩阵 + 交付 QA 门禁 |
| 7 | React PostFX 后期特效 | `pmndrs/react-postprocessing` | R3F 场景的 Bloom/景深/暗角/glitch 等后期 |
| 8 | Chakra UI 组件系统 | `chakra-ui/chakra-ui` | 开箱即用、支持主题定制的 React 组件库 |
| 9 | oil-ui 界面设计/改版/评审 | `oil-oil/oil-ui` | 先定设计北极星，多风格同屏对比、按真实截图打磨视觉层级 |
| 10 | draw-ui 设计稿生成/还原 | `oil-oil/draw-ui` | 生成 UI 设计稿（图片），并还原为 HTML/CSS/小程序 |
| 11 | m3e-canvas 可拖拽 UI 设计 | `lnkiai/m3e-canvas` | AI 生成 Material 3 设计 JSON → 分享链接 → 侧边栏/浏览器拖改 → 导出 vibe-coding 提示词 |
| 12 | superpowers 开发方法论 | `obra/superpowers` | 给 AI 编程代理的完整开发方法论：头脑风暴 → 计划 → TDD → 子代理执行 → 调试 → 验证 → 评审 |
| 13 | frontend-design 设计哲学 | `anthropics/skills` | Anthropic 官方设计宪法：像设计工作室主设那样思考，避开 5 大 AI 默认陷阱，两遍流程 |
| 14 | taste-skill 研究方向引擎 | `Leonxlnx/taste-skill` | 从 247 个策展站提炼：脚本发牌 20 方向、反 slop 房规、真实浏览器 inspect、截图 look-and-fix |
| 15 | garden-skills 风格配方库 | `ConardLi/garden-skills` | web-design-engineer 25 种风格配方 + 设计工程师全流程；另含视频演示/图像生成/文章排版等 6 技能 |

## 安装

把本目录整体放到 `~/.codebuddy/skills/CHT-UI-SKILLS/`（目录名必须严格等于 `SKILL.md` 的 `name` 字段），对所有对话与项目生效。

```bash
git clone https://github.com/cuohuatang/CHT-UI-SKILLS.git ~/.codebuddy/skills/CHT-UI-SKILLS
```

## 结构

```
CHT-UI-SKILLS/
├── SKILL.md                 # 总入口与路由（含内置工作流第七节）
├── README.md                # 本文件
├── CHANGELOG.md             # 版本迭代记录
├── references/01–08.md      # 前 8 项能力分册
├── oil-ui/                  # 第 9 项：oil-ui 完整技能
├── draw-ui/                 # 第 10 项：draw-ui 完整技能
├── m3e-canvas/              # 第 11 项：m3e-canvas 可拖拽 UI 设计（SKILL.md + scripts/ + references/）
├── superpowers/             # 第 12 项：superpowers 开发方法论（SKILL.md + skills/ 15 个组合式技能）
├── frontend-design/         # 第 13 项：Anthropic 官方设计哲学（SKILL.md）
├── taste-skill/             # 第 14 项：研究方向引擎（SKILL.md + library/ + references/ + scripts/）
└── garden-skills/           # 第 15 项：风格配方库 + 6 技能（skills/ + README + LICENSE）
```
