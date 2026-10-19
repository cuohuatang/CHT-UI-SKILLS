# CHT-UI-SKILLS

一站式前端视觉与动效技能集，融合 10 大能力，并内置一条「定方向 → 出详细设计稿 → 生成可运行代码」的编排工作流。

## 工作流（内置）

```
oil-ui     → 定设计方向，出 3 套方案放在对比页让你挑
draw-ui    → 挑中后出详细设计稿
   ↓
交给 v0.dev Chat / Builder.io → 生成可运行代码
   ↓
你手动接进项目、git 提交、部署
```

## 10 大能力

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
├── references/01–08.md      # 前 8 项能力分册
├── oil-ui/                  # 第 9 项：oil-ui 完整技能
└── draw-ui/                 # 第 10 项：draw-ui 完整技能
```
