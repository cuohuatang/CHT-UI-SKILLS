# 06 · UI-UX Craft 设计工艺 — 实战分册

> 定位：把「设计得好看」变成「交付得规范」的工程手册。与侧重选风格的 `ui-ux-pro-max` 互补（它选方向，本分册落地规矩）。
> 主入口与全局铁律见 `../SKILL.md`。

## 标准交付物（四件套）

```
DESIGN.md              # 唯一真相源：token + 组件规格 + Do/Don't
tokens.css / theme.ts  # 可执行 token 层
components/<X>/states  # 每个组件的状态清单
QA-CHECKLIST.md        # 交付门禁
```

## Step 1 — Token 体系（铜后才能化瘀）

命名：`--{类别}-{用途}-{修饰}`（如 `--color-bg-surface`），**禁止** `--blue-2` 这种「不知用在哪」的名字。

```css
:root {
  --color-bg: #ffffff; --color-bg-subtle: #f7f8fa; --color-border: #e4e6eb;
  --color-text: #14161a; --color-text-muted: #6b7280;
  --color-accent: #2563eb; --color-accent-hover: #1d4ed8;
  --color-danger: #dc2626; --color-success: #16a34a;
  --space-1:4px; --space-2:8px; --space-3:12px; --space-4:16px;
  --space-5:24px; --space-6:32px; --space-7:48px; --space-8:64px;
  --radius-sm:6px; --radius-md:10px; --radius-lg:16px; --radius-full:999px;
  --shadow-sm: 0 1px 2px -1px rgb(0 0 0/.06);
  --shadow-md: 0 0 0 1px rgb(0 0 0/.06), 0 2px 4px -1px rgb(0 0 0/.06), 0 4px 8px -2px rgb(0 0 0/.04);
  --shadow-lg: 0 0 0 1px rgb(0 0 0/.08), 0 8px 16px -4px rgb(0 0 0/.10), 0 16px 32px -8px rgb(0 0 0/.08);
  --font-xs:12px; --font-sm:13px; --font-base:14px; --font-md:16px;
  --font-lg:20px; --font-xl:25px; --font-2xl:32px;
  --leading-tight:1.25; --leading-normal:1.6;
}
```

**暗色模式不要全局反色**：在 `[data-theme="dark"]` 重定义变量（不用 `filter: invert()`）。暗色下阴影几乎不读，改用 `0 0 0 1px rgb(255 255 255/.08)` 的 ring 表达层级。

## Step 2 — 组件状态矩阵（最影响「完成度」，易漏）

| 状态 | 必做 | 常见漏点 |
|---|---|---|
| `default` | 基础样式 | — |
| `hover` | 背景/边框微变，**不承载唯一信息** | 触屏无 hover，需另有 active 反馈 |
| `focus-visible` | `outline: 2px solid var(--color-accent); outline-offset: 2px` | 用 `:focus` 会残留环 |
| `active` | `transform: scale(.97)` 或背景加深 | 无按压反馈 |
| `disabled` | `opacity:.45; pointer-events:none;` + `aria-disabled` | 只改色没禁用事件 |
| `loading` | 占位 spinner/skeleton，**宽度不跳变** | 宽度塌陷抖动 |
| `error` | 红边框 + `aria-invalid` + 文案预留 | 文案挤动布局 |
| `selected` | 明确选中态（不只靠主色）| 只靠颜色（色盲不可读）|

数据类视图三态必须齐：**loading（骨架屏非全屏 spinner）/ empty（有插画+引导动作）/ error（可重试）**。

## Step 3 — 节律与对齐（让页面「像一个人做的」）

- 间距只用 token 8 个值，出现 `margin:13px` 应被拦下。
- 同心圆角：父子嵌套 `outer = inner + padding`，同圆角是「看起来不对」头号原因。
- 动态数字加 `font-variant-numeric: tabular-nums`（价格/计时/表格列），防跳动。
- 标题 `text-wrap: balance`，正文 `text-wrap: pretty`，消灭孤儿词。
- 触控热区 ≥ 44×44（WCAG），用伪元素扩展，热区不重叠。
- z-index 用 token 分层（`--z-dropdown:100; --z-modal:200; --z-toast:300`），禁 `z-index:9999`。

## Step 4 — 交付前 QA 门禁

**P0 阻断**：正文对比度 ≥ 4.5:1（大字/UI ≥ 3:1）；所有交互元素 `focus-visible` 键盘可达；图片有 alt、图标按钮有 `aria-label`；热区 ≥ 44×44 不重叠；数据视图 loading/empty/error 三态齐全；表单错误提示 + `aria-invalid`。

**P1 重要**：色值/间距/圆角/字号全来自 token，无魔法数字；每个组件 default/hover/active/selected/disabled 齐全；375/768/1440 三断点无横向滚动；动态数字 tabular-nums；`prefers-reduced-motion` 降级；暗色模式无刺眼纯白底黑字。

**P2 增强**：骨架屏形状接近真实内容；空状态带下一步动作；长文案/多语言不破版；打印或导出可用。

## 铁律

- 先 token 后组件：新组件先用到的颜色/间距确认在 token 表；不在就先加 token，不允许硬编码。
- 禁止「紫色保安」以外的魔法数字：间距/字号/圆角出现非 token 值即 bug。
- 状态不全不交付：缺 disabled/loading/error 等同未完成。
- hover 不能是唯一提示：键盘/触屏用户看不到 hover。
- 动态内容（图/数字/错误文案）必须预留空间，防 Layout 抖动。
- DESIGN.md 必须与代码同步，否则规范失效；建议把 QA 接到 lint 或 PR 模板。
- 规范是工具不是束缚：规范让界面变差时改规范并同步文档，而非绕过写死。
