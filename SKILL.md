---
name: CHT-UI-SKILLS
display_name: "CHT 前端视觉与动效技能集"
display_name_en: "CHT UI Skills"
description: "一站式前端视觉与动效技能集，融合 12 大能力：p5.js 创意编码、CSS Doodle 图案生成、Theatre.js 时间轴编排、React Spring 物理动画、Inure 精致微交互、UI-UX Craft 设计规范工艺、React PostFX 后期特效、Chakra UI 组件系统、oil-ui 界面设计/改版/评审、draw-ui 设计稿生成与截图还原、m3e-canvas 可拖拽 UI 设计，以及 superpowers 开发方法论（头脑风暴/计划/TDD/调试/验证/评审）。按任务路由到对应分册。"
description_zh: "CHT-UI-SKILLS：前端视觉/动效/设计/工程全家桶——创意编码、生成图案、动画编排、物理动画、微交互、设计规范、后期特效、组件系统、界面设计评审、设计稿生成还原、可拖拽 UI 设计、开发方法论（TDD/计划/验证/评审）"
description_en: "CHT-UI-SKILLS: a frontend visual & motion toolkit covering p5.js, css-doodle, Theatre.js, React Spring, Inure micro-interactions, UI/UX craft, React PostFX, Chakra UI, oil-ui design/review, draw-ui design-to-code, m3e-canvas draggable UI design, and superpowers dev methodology."
category: frontend
version: 1.1.1
author: cuohuatang
tags:
  - frontend
  - visual
  - animation
  - motion
  - generative-art
  - design-system
  - ui
  - creative-coding
  - m3e
  - canvas
  - prototype
  - draggable
  - development
  - tdd
  - methodology
allowed-tools: Read,Write,Bash
---

# CHT-UI-SKILLS —— 前端视觉与动效技能集

> 把 12 个前端视觉/动效/设计/工程能力**嫁接成一个技能包**。每个能力都是对应知名开源项目的实战工艺指南，
> 本文件是**总入口与路由**，具体 API、模板、配方都在 `references/` 分册里（渐进披露，按需读取）。

## 一、12 大能力一览

| # | 能力 | 开源来源 | 一句话 |
|---|------|----------|--------|
| 1 | **p5.js 创意编码** | `processing/p5.js` | 交互式 Canvas 视觉、粒子背景、生成艺术 |
| 2 | **CSS Doodle 图案** | `css-doodle/css-doodle` | 类 CSS 小 DSL 生成几何纹理 / SVG / GPU shader |
| 3 | **Theatre.js 编排** | `theatre-js/theatre` | 网页里的 AE：时间轴 + 关键帧，编排出场顺序 |
| 4 | **React Spring 物理动画** | `pmndrs/react-spring` | 弹簧物理弹性，手势跟随与列表进出 |
| 5 | **Inure 精致微交互** | `Hamza417/Inure`（参考样本） | 参考拆解 + 复刻「小操作也舒服」的 UI 动效 |
| 6 | **UI-UX Craft 设计工艺** | 设计规范方法论 | token + 组件状态矩阵 + 交付 QA 门禁 |
| 7 | **React PostFX 后期特效** | `pmndrs/react-postprocessing` | R3F 场景的 Bloom/景深/暗角/glitch 等后期 |
| 8 | **Chakra UI 组件系统** | `chakra-ui/chakra-ui` | 开箱即用、支持主题定制的 React 组件库 |
| 9 | **oil-ui 界面设计/改版/评审** | `oil-oil/oil-ui` | 先定设计北极星，多风格同屏对比、按真实截图打磨视觉层级；只做设计判断 |
| 10 | **draw-ui 设计稿生成/还原** | `oil-oil/draw-ui` | 生成 UI 设计稿（图片），并还原为 HTML/CSS/小程序；与 oil-ui 互补 |
| 11 | **m3e-canvas 可拖拽 UI 设计** | `lnkiai/m3e-canvas` | AI 生成 Material 3 设计 JSON → 分享链接 → 侧边栏/浏览器拖改 → 导出 vibe-coding 提示词 |
| 12 | **superpowers 开发方法论** | `obra/superpowers` | 给 AI 编程代理的完整开发方法论：头脑风暴 → 计划 → TDD → 子代理执行 → 调试 → 验证 → 评审 |

## 二、什么时候用 / 不要用

**用：** 用户在做前端视觉、UI、动效、组件系统相关任务时，无论要「生成图案」「做粒子背景」
「编排转场」「加弹性反馈」「复刻精致动效」「定设计规范」「加 3D 后期」「搭组件库」，都用本技能路由。
若要做**整站/整页的界面设计、改版、风格探索或多方案对比、独立视觉评审**，路由到 `oil-ui/SKILL.md`（第 9 项）。
若要做**UI 设计稿（图片）生成、截图/参考图精准还原成 HTML/CSS/小程序**，路由到 `draw-ui/SKILL.md`（第 10 项）。
若要做**可拖拽/可交互的 UI 原型**（AI 直出设计、边看边改、导出 vibe-coding 提示词），路由到 `m3e-canvas/SKILL.md`（第 11 项）。
若要把设计交付物变成**工程化、已验证的代码**（需求收敛/计划/TDD/调试/验证/评审），路由到 `superpowers/SKILL.md`（第 12 项）。

**不用：** 纯后端、纯业务逻辑、与视觉/交互无关的任务无需激活。若只是静态样式微调（颜色/间距），
可走 `ui-ux-craft` 分册的 token 规范；若需要选整体设计风格方向，与 `ui-ux-pro-max` 互补（它选方向，本技能落地）。

## 三、能力选择决策树

| 你想做 | 读这个分册 |
|---|---|
| 互动海报 / 粒子背景 / 鼠标交互 / 数据艺术 / 导出 GIF | `references/01-p5js.md` |
| 几何背景纹理 / 装饰图案 / 参数方程图形 / 品牌纹理 | `references/02-css-doodle.md` |
| 多元素精确时序 / 产品演示 / 3D 运镜 / 页面转场 | `references/03-theatrejs.md` |
| 按钮弹性反馈 / 拖拽跟随 / 列表进出 / 连锁编排 | `references/04-react-spring.md` |
| 复刻「高级感」微交互 / 有参考录屏想拆解实现 | `references/05-inure.md` |
| 统一按钮字号间距 / 补齐 loading·empty·error 状态 / 设计规范 | `references/06-ui-ux-craft.md` |
| 3D 产品展示加 Bloom·景深·暗角·glitch | `references/07-react-postfx.md` |
| 用现成组件库搭界面 / 主题定制 / v3 system | `references/08-chakra-ui.md` |
| 整站/整页设计、改版、多风格对比、截图还原、独立视觉评审 | `oil-ui/SKILL.md`（含自带的 references/、scripts/、assets/） |
| UI 设计稿（图片）生成、截图还原成 HTML/CSS/小程序、参考图精准复刻 | `draw-ui/SKILL.md`（含自带的 references/、scripts/、assets/、evals/） |
| 可拖拽/可交互的 UI 原型、AI 直出设计、边看边改、vibe-coding 提示词 | `m3e-canvas/SKILL.md`（含自带的 scripts/、references/） |
| 开发方法论、需求收敛、计划、TDD、调试、完成前验证、代码评审、子代理驱动 | `superpowers/SKILL.md`（含自带的 skills/，15 个组合式技能） |

**组合模式（常见）：** Theatre.js 编排转场 + React Spring 做交互反馈 + React PostFX 做画面；
UI-UX Craft 定 token 与状态规范作为其它所有能力的统一底座。

## 四、全局铁律（跨所有子能力）

1. **只动 `transform` 与 `opacity`**（颜色插值在动画库里安全）。动 `width/height/margin/top/left` 触发 layout，掉帧。
2. **`prefers-reduced-motion` 必须处理**：减弱动效偏好下保留 opacity/color 过渡，去掉位移与缩放；交互类直接呈现终态。
3. **装饰性视觉不承载信息**：图案/粒子/特效层不要放正文；其上叠文字必须有遮罩层保对比度（WCAG ≥ 4.5:1）。
4. **触控热区 ≥ 44×44px**（WCAG），可见控件更小要用伪元素扩，且热区不重叠。
5. **性能预算**：移动端动效要实机验证；粒子数按面积自适应，postprocessing 高开销效果按设备降级。
6. **状态全覆盖**：任何交互组件至少具备 default / hover / active / focus-visible / disabled；数据视图必备 loading / empty / error。
7. **代码与文档同步**：设计 token 与规范改动须同步 `references/06-ui-ux-craft.md` 的约定，避免规范失效。
8. **善用官方文档为准**：下方分册给出经过核验的 API 与版本要点，但库会迭代，落地前以官方文档/当前版本为准。
9. **TDD 不可跳过**（superpowers）：写任何实现代码前先写测试，且必须亲眼看过测试失败（红）再写实现到通过（绿）。
10. **计划先行**（superpowers）：需求未收敛不进实现；计划未确认不动手；不 YAGNI/DRY 双标——不做多余的东西，重复代码必须抽象。
11. **完成前验证**（superpowers）：声称"完成"前，必须运行验证（测试/构建/检查）并给出证据，不得口头宣称完成。

## 五、分册索引（触发词 → 文件）

| 分册 | 触发词 |
|---|---|
| `01-p5js.md` | p5.js、Processing、sketch、粒子、流场、柏林噪声、生成艺术、互动背景 |
| `02-css-doodle.md` | css-doodle、CSS 图案、生成背景、几何纹理、@grid、@shape、@pattern |
| `03-theatrejs.md` | Theatre.js、时间轴、关键帧、编排动画、cinematic camera、转场 sequence |
| `04-react-spring.md` | react-spring、弹性动画、物理动画、spring animation、回弹、拖拽跟随 |
| `05-inure.md` | Inure、微交互、精致动效、操作反馈、菜单展开、页面切换、交互质感 |
| `06-ui-ux-craft.md` | 设计规范、按钮统一、字号间距、加载/空/错状态、UI 工艺、DESIGN.md、token |
| `07-react-postfx.md` | postprocessing、后期特效、bloom、景深、暗角、glitch、扫描线、R3F 特效 |
| `08-chakra-ui.md` | Chakra UI、组件系统、主题定制、chakra v3、recipe、design system |
| `oil-ui/SKILL.md` | oil-ui、界面设计、改版、风格探索、多方案对比、截图还原、视觉评审、设计北极星、design direction |
| `draw-ui/SKILL.md` | draw-ui、UI 设计稿、生成设计图、截图还原、HTML 还原、小程序、参考图复刻、design mockup、reconstruction |
| `m3e-canvas/SKILL.md` | m3e、M3E Canvas、可拖拽设计、可交互原型、Material 3 画布、AI 直出设计、边看边改、vibe-coding、分享链接、#docz |
| `superpowers/SKILL.md` | superpowers、开发方法论、需求收敛、计划、TDD、测试驱动、调试、完成前验证、代码评审、子代理驱动、worktree |

## 六、与其它技能的关系

- `oil-ui`（第 9 项）：负责**界面设计、改版、风格探索、多方案对比与独立视觉评审**，自带完整的设计方法与截图工具；是 CHT-UI-SKILLS 里「设计判断」这一层的主体。它与本集其它 8 项（落地实现）配合：oil-ui 定方向/出评审结论 → 其余分册负责把设计**落地**成可运行代码与组件。
- `draw-ui`（第 10 项）：负责**生成 UI 设计稿（图片）并把截图/参考图精准还原为 HTML/CSS/小程序**，是「设计稿生成 + 还原成代码」这一层。它与 oil-ui 互补——draw-ui 自己也会在探索视觉方向时推荐 oil-ui，二者常串联：draw-ui 出图/还原 → oil-ui 做方向打磨与评审；对已有界面的小幅改造则直接用 draw-ui 的还原路径。
- `m3e-canvas`（第 11 项）：负责**可拖拽/可交互的 UI 原型**——AI 按 M3E 协议生成设计 JSON，压缩进分享链接，用户在豆包侧边栏或浏览器画布里直接拖改，改完导出 vibe-coding 提示词喂给 AI 代码生成。与 draw-ui 互补：draw-ui 出**静态精细稿**，m3e-canvas 出**可拖改原型**；在内置工作流第二步作为分支乙（见第七节）。
- `superpowers`（第 12 项）：负责**开发方法论**——需求收敛（brainstorming）、实现计划（writing-plans）、测试驱动开发（test-driven-development）、子代理驱动执行（subagent-driven-development）、系统化调试（systematic-debugging）、完成前验证（verification-before-completion）、代码评审（requesting/receiving-code-review）。是「工程实现」这一层：CHT-UI-SKILLS 的设计/视觉能力负责"做出什么"，superpowers 负责"怎么工程化交付"；在内置工作流第一步（需求模糊时）与第三步（工程模式）对接（见第七节）。
- `ui-ux-pro-max`：负责选「风格方向」（风格/配色/字体）；本技能负责把方向**落地**成可运行代码与规范。
- `frontend-design`（Anthropic 设计宪法）、`web-design-guidelines`（可访问性审计）：可在交付前做质量复核。
- 本技能是「实践工艺 + 工程方法论」层，与它们构成「方向选择 → 设计判断(oil-ui) → 设计稿生成/还原(draw-ui) 或 可拖改原型(m3e-canvas) → 规范制定 → 工程化实现(superpowers) → 可访问性审计」的前端质量闭环。

## 七、内置工作流：出方案矩阵 → 出稿（静态稿 / 可拖改原型）→ 生成可运行代码（快速 / 工程模式）

> 适用：用户说"做个界面 / 设计个页面 / 想看看几种风格"，但**还没定方向**，需要先看方案、再出正式稿、最后还要能跑起来的代码。
> 这条流水线把「方向（oil-ui）× 技术气质（8 大分册）× 交互形态（draw-ui 静态稿 / m3e-canvas 可拖改原型）」组合成**方案矩阵**，
> 第一步后设一道人工确认闸门，第二步按用户偏好走**分支甲（静态精细稿）或分支乙（可拖改原型）**，第三步进入代码生成
> （**快速模式**或接 superpowers 的**工程模式**），第四步完成前验证（superpowers 铁律）。

**整体流向：**

```
[用户提需求]
   │
   ▼
【第一步 · 出方案矩阵（多维组合）】
   · 需求模糊 → 先触发 superpowers/brainstorming 收敛出 spec（接口①）
   · oil-ui 定调性：认品类 / 拆标杆 / 写 N 套（默认 3）风格方向
   · 8 大分册定技术气质：p5 粒子 / CSS Doodle 图案 / Theatre 叙事 / Spring 弹性 / Inure 微交互 / Chakra 组件 / PostFX 后期 / Craft 规范
   · 交互形态：静态稿（draw-ui）或 可拖改原型（m3e-canvas）
   → 组合成「风格 × 技术 × 形态」候选集（默认 6–9 版，可要求十几版）
   → 做成首屏对比页交给用户挑
   │
   ▼
★ 第一步收尾闸门（必须询问）★
   "方向已定 ✅ 第二步走哪个分支？
     分支甲：draw-ui 出【静态精细设计稿】
     分支乙：m3e-canvas 出【可拖改原型】（AI 直出设计，边看边改）
     也可只停在设计说明 / 直接做可运行实现。"
   │  ← 等用户确认，未确认不进第二步
   ▼
【第二步 · 按分支出稿】
   分支甲（draw-ui）：以选定方向卡为视觉基线，生成精细视觉稿，可还原 HTML/CSS/小程序
   分支乙（m3e-canvas）：按 M3E 协议生成设计 JSON → 分享链接 → 侧边栏/浏览器拖改
   │
   ▼
【第三步 · 生成可运行代码（双模式）】
   快速模式（原）：设计稿/prompt → v0.dev Chat / Builder.io → React/Next 代码 → 人工接项目
   工程模式（superpowers，接口②）：设计定稿 → writing-plans → test-driven-development
       → subagent-driven-development → verification-before-completion → code-review
       → 交付已验证的工程化代码
   │
   ▼
【第四步 · 完成前验证（接口③，superpowers 铁律）】
   声称完成前：跑测试 / 构建 / 检查，附验证证据；有未通过项不得宣称完成
   │
   ▼
【你手动接进项目 → git 提交 → 部署】
```

### 第一步：出方案矩阵（多维组合）

1. **需求模糊时先收敛（接口①）**：用户需求不清晰（"做个好一点的界面"），先读 `superpowers/skills/brainstorming/SKILL.md`，用头脑风暴法问出真实目标、约束与验收标准，输出一句话 spec 后再进入方案矩阵。
2. 按 `oil-ui/SKILL.md` 的「1. 探索并收敛方向」：认品类、拆标杆、定调性，先写出 **N 套（默认 3）风格不同的方向**。
3. **叠加技术气质维度**：从 8 大分册中选 1–2 种与本设计匹配的技术路线（如「p5 粒子背景 + 科技感」「Chakra 组件化 + 工具效率」「Inure 微交互 + 高级感」），把「风格 × 技术」组合成候选集。
4. 每套用三四行简述：给人什么感觉、首屏长什么样、字体与色彩、主视觉靠什么、用什么技术实现；附上推荐哪套及理由。
5. 用户要看实图 → 按 oil-ui 的「风格对比页」把候选集做成真实首屏放进对比页（含 `sheet` 总览图）交给用户挑；**这一轮到此结束**，不自动往下走。
6. **第一步收尾闸门（强制询问，不可跳过）**：用户挑定后，必须主动询问——
   > 已定方向 ✅。第二步走哪个分支？**分支甲：draw-ui 出静态精细稿**（完整页面/长页精修视觉稿）；**分支乙：m3e-canvas 出可拖改原型**（AI 直出、边看边改）；也可以只停在设计说明，或直接做可运行实现。
   - 用户确认分支 → 进入对应第二步路径；
   - 用户选"只做设计说明 / 直接可运行实现" → 按对应分册收尾，**不强行调用 draw-ui / m3e-canvas**。

### 第二步·分支甲：出详细设计稿（draw-ui）

1. 把第一步选定的**方向卡作为视觉基线**，读 `draw-ui/SKILL.md` 的「新设计或风格探索」路径。
2. 按 `references/ui-design.md` 组织提示词、生成并检查；若是完整长页，再读 `references/full-page.md` 分段生成。
3. 交付：设计稿图片 + 简短实现说明；如需继续还原成 HTML/CSS/微信小程序，按 draw-ui 的还原路径（software-reconstruction / html-reconstruction）走。

### 第二步·分支乙：出可拖改原型（m3e-canvas）

1. 读 `m3e-canvas/SKILL.md`：按 M3E 协议把选定方向生成设计 JSON（含 frames 屏幕 + groups 部件，默认手机 412×892）。
2. 运行 `m3e-canvas/scripts/make_link.py` 把 JSON 压缩成分享链接（`#docz=` 形式，整个设计都在链接里）。
3. 交付**双模式**（用户自选、可随时切换）：模式 A 把链接贴进豆包侧边栏直接拖改；模式 B 浏览器/客户端点开拖改。
4. 用户拖改完成后，在画布右上角「提示词」按钮导出 vibe-coding prompt（可编辑、可保存单屏 PNG）。

### 第三步：生成可运行代码（快速 / 工程模式）

**快速模式（默认，人工收口）：**
1. 把第二步产出的**详细设计稿（图片/截图）**或 m3e prompt 作为视觉基准，交给 **v0.dev Chat** 或 **Builder.io**（或用户的 AI 编码工具），生成 React / Next.js 等可运行前端代码。
2. 在工具内迭代到结构、视觉接近设计稿；导出代码。
3. **你（或主 Agent 协助）手动**把生成的代码接进现有项目、跑通、`git commit`、部署。这一步是人工收口，不在 Skill 自动范围内。

**工程模式（superpowers 驱动，接口②）：**
适用：用户要求"工程化交付 / 带测试 / 质量保障"，或代码要长期维护、多人协作。
1. 读 `superpowers/SKILL.md`，从 `skills/writing-plans/SKILL.md` 开始：把设计定稿 + 需求 spec 写成可执行实现计划（任务拆解、验收标准）。
2. 按 `skills/test-driven-development/SKILL.md` 执行真·红绿 TDD：先写测试看失败（红）→ 写最小实现到通过（绿）。
3. 任务量大时按 `skills/subagent-driven-development/SKILL.md` 拆给子代理并行驱动，各任务独立验证。
4. 完成后按 `skills/verification-before-completion/SKILL.md` 全面验证；复杂功能走 `skills/requesting-code-review/SKILL.md` + `skills/receiving-code-review/SKILL.md` 收评审意见并消化。
5. 交付：可运行代码 + 测试通过证据 + 实现说明；代码接入与部署仍由你手动收口。

**分支乙衔接**：m3e 路线用户改完原型导出 prompt 后，**先呈现 prompt，询问用户**是走快速模式（直接喂 AI 编码工具）还是工程模式（superpowers 驱动带 TDD/验证）；未获指令前不自动执行。

### 第四步：完成前验证（接口③，superpowers 铁律）

1. **声称"完成"前**：必须运行最小验证集——测试（vitest/jest/对应测试框架）、构建（tsc/build）、检查（lint/typecheck），把命令输出作为**验证证据**附在交付说明里。
2. 有未通过项：不得宣称完成，修复后重跑直至通过；无法自动化验证的（视觉还原度等），明确列出人工核对项。
3. 验证范围与结果、仍存在的缺口，随交付说明一起给出。

### 关键约定

- **下游闭环**：第一步后闸门确认 → 第二步按分支出稿（静态稿或可拖改原型）→ 第三步双模式出可运行代码 → 第四步完成前验证；最终由你手动接入项目、git 提交与部署，Skill 产出止于"可运行代码已生成且通过验证"。
- **严格顺序**：方向未定不进第二步；第二步不重新发散风格，只把已锁定的方向做成稿/原型。
- **闸门不能省**：第一步后必须询问分支选择；第三步工程模式必须先呈现计划/测试方案征得用户同意再执行，避免"替用户默认决策"。
- **分支可切换**：选定静态稿后想改可拖改原型（或反之），回到闸门重新选分支即可；已产出的稿/原型保留，以最新选择为准。
- **可回退**：选定方向后想换另一套，回到第一步对比页再选；已生成的稿/原型以最新选定的方向为准。
- **快速/工程模式可切换**：工程模式生成的代码结构与快速模式一致时可互转；默认快速，用户要求质量保障才切工程模式。
- **与其它能力衔接**：进了第二步需要真实前端实现时，再路由到 `references/08-chakra-ui.md`（组件）或 `references/07-react-postfx.md`（3D 后期）等落地分册；需要开发方法论支持时路由到 `superpowers/skills/`。
