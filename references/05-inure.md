# 05 · Inure 精致微交互 — 实战分册

> 参考项目：`Hamza417/Inure`（开源 Android 应用管理器，自定义界面与动画）。
> **关键认知：** Inure 本身不是前端库，它是「动效教科书」。本分册教你怎么从任意参考（录屏 / Inure / 竞品）中拆解动效，再用自己的技术栈（Web / React / RN / Flutter）复刻。
> 主入口与全局铁律见 `../SKILL.md`。

## 标准工作流：参考 → 拆解 → 复刻

### 第 1 步：读成「动效规格表」（不要凭印象）

| 交互 | 触发 | 时长 | 曲线 | 动的属性 | 顺序/stagger | 备注 |
|---|---|---|---|---|---|---|
| 菜单展开 | 点击图标 | 220ms | cubic-bezier(.2,.9,.2,1) | height+opacity | 子项延迟 30ms 递增 | 图标旋转 90° |
| 弹窗出现 | 点击按钮 | 180ms | spring(t280,f26) | scale .95→1 + opacity | — | 背后模糊遮罩 |
| 页面切换 | 路由变化 | 320ms | ease-in-out | translateX + opacity | 旧页先出 100ms | 共享元素同步位移 |

**估算时长/曲线（无源文件时）：** 逐帧看录屏（播放器 `,`/`.` 逐帧）数起止帧 ÷ 30/60fps = 时长。先快后慢 = ease-out；起手延迟 = ease-in-out；到达后回弹 = spring/overshoot。

### 第 2 步：拆出四类 Inure 式细节（缺一不可）

1. **层级错位 (stagger)**：一组元素按 20–60ms 递增依次出现，而非整体进出。
2. **共享元素 (shared element)**：点击卡片「变成」新页面 —— 几何连续性，而非淡入淡出。
3. **状态全覆盖**：同一控件必有 default/hover/focus-visible/active/disabled/loading，缺一个就糙。
4. **物理回弹而非线性**：1–2 次微超冲（overshoot），>2 次就廉价。

## 可直接复用的片段

### 1) 错位入场（stagger）
```jsx
{items.map((it, i) => (
  <animated.li key={it.id} style={useSpring({
    from: { opacity: 0, transform: 'translateY(12px)' },
    to:   { opacity: 1, transform: 'translateY(0px)' },
    delay: 40 + i * 45, config: { tension: 260, friction: 26 },
  })}>{it.label}</animated.li>
))}
```

纯 CSS：
```css
.item { opacity: 0; transform: translateY(12px); animation: rise 380ms cubic-bezier(.2,.9,.2,1) forwards; }
@keyframes rise { to { opacity: 1; transform: none; } }
.item:nth-child(1){ animation-delay: 40ms } .item:nth-child(2){ animation-delay: 85ms }
```

### 2) 菜单展开（高度 + 内容错位）
```jsx
const { height, opacity } = useSpring({ height: open ? 'auto' : 0, opacity: open ? 1 : 0,
  config: { tension: 300, friction: 30 } })
return <animated.div style={{ overflow: 'hidden', opacity, height }}>{children}</animated.div>
```

### 3) 按压反馈 + 焦点环（一次性补齐所有状态）
```css
.btn { transition: transform 120ms cubic-bezier(.2,.9,.2,1), box-shadow 160ms ease, background-color 160ms ease; }
.btn:hover { transform: translateY(-1px); filter: brightness(1.06); }
.btn:active { transform: scale(.975); }
.btn:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
.btn:disabled { opacity: .45; pointer-events: none; }
.btn[data-loading] { color: transparent; }
```

### 4) 共享元素转场（View Transitions API）
```jsx
const t = document.startViewTransition
if (t && !reducedMotion) t(() => setState(nextPage))
```
```css
.card { view-transition-name: hero-card; }
::view-transition-old(hero-card), ::view-transition-new(hero-card) {
  animation-duration: 320ms; animation-timing-function: cubic-bezier(.2,.9,.2,1); }
```

## 手感字典（照抄即可）

| 场景 | 时长 | 曲线 |
|---|---|---|
| 按钮按压 | 100–160ms | ease-out |
| Tooltip/Popover | 125–200ms | ease-out |
| 下拉菜单 | 150–250ms | cubic-bezier(.2,.9,.2,1) |
| 抽屉/Modal | 200–500ms | spring 或 ease-out |
| 页面/路由转场 | 260–400ms | cubic-bezier(.77,0,.175,1) |
| 列表 stagger 间隔 | 30–80ms | — |
| 出现不要从 scale(0) | 起始 scale(.95)+opacity 0 | — |

## 铁律

- UI 动效 < 300ms；超过 300ms 拆分缓动。
- 离场比入场快且更轻（出场 < 200ms），遵循「用户想马上看到结果」。
- 重复操作（一天点 100 次）不要动画，否则显得慢。
- `transform-origin` 要对：菜单从触发按钮展开，popover 从触发器一侧长出。
- 只动 transform / opacity；菜单展开用 `height: auto` spring 或 `grid-template-rows: 0fr→1fr`。
- `prefers-reduced-motion` 降级，保留 opacity/color 过渡、去掉位移与缩放。
- 不要整体抖动（jelly）：overshoot 一次即可；多 spring 争抢同一属性是抖动主因。
- 参考不等于照抄实现：Inure 是 Kotlin/XML 写的，你要的是它的时间感与顺序感。
