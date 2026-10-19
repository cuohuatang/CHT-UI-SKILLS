# 03 · Theatre.js 动画编排 — 实战分册

> 开源项目：`theatre-js/theatre`。网页里的 AE + 时间轴：Studio 可视化调帧，Core 负责运行时播放。
> 适合产品演示、3D 展示、页面转场这类「出场顺序必须听指挥」的场合。
> 主入口与全局铁律见 `../SKILL.md`。

## 核心概念

| 概念 | 作用 | 类比 |
|---|---|---|
| **Project** | 顶层容器，持有 `state.json` | AE 工程 |
| **Sheet** | 一个场景 / 一条时间轴 | AE 合成 |
| **Sequence** | 播放头（含关键帧）| 时间轴 + 播放控制 |
| **Object** | 被动画的一组属性 | 选中图层组 |

**心智模型：** Theatre 不修改你的 DOM/Three 对象，只**产出数值**；你用 `onValuesChange` 把数值写到真正渲染的地方。因此它能驱动 DOM style、Three camera、CSS 变量、音频参数。

## 最小可运行模板（HTML/SVG，无需构建）

```html
<script type="module">
import 'https://cdn.jsdelivr.net/npm/@theatre/browser-bundles@0.5.0-insiders.88df1ef/dist/core-and-studio.js'
const { core, studio } = Theatre
studio.initialize()

const project = core.getProject('Landing Intro')
const sheet   = project.sheet('Hero')
const hero = sheet.object('Hero Title', {
  y: 0,
  opacity: core.types.number(1, { range: [0, 1] }),     // 约束范围，拖不出界
  scale: core.types.number(1, { nudgeMultiplier: 0.01 }),
})
hero.onValuesChange((v) => {
  const el = document.getElementById('title')
  el.style.transform = `translateY(${v.y}px) scale(${v.scale})`
  el.style.opacity = v.opacity
})
project.ready.then(() => sheet.sequence.play({ iterationCount: 1, range: [0, 4] }))
</script>
```

## 生产构建：三步剥离 Studio

1. Studio 面板左侧点项目名 → **Export to JSON** → 得到 `state.json`。
2. `getProject(name, { state: importedState })` 注入。
3. **移除 Studio 导入与 `studio.initialize()`**（CDN 换 `core-only.min.js`；bundler 用 `import.meta.env.DEV` 条件引入）。

```js
if (import.meta.env.DEV) {
  const { default: studio } = await import('@theatre/studio')
  studio.initialize()
}
import state from './state.json'
export const project = core.getProject('Landing Intro', { state })   // 生产只读 core
```

## React Three Fiber 集成

```jsx
import { Canvas } from '@react-three/fiber'
import { SheetProvider, editable } from '@theatre/r3f'
import { getProject } from '@theatre/core'
import studio from '@theatre/studio'
import extension from '@theatre/r3f/dist/extension'

studio.extend(extension)        // ⚠️ 必须在 initialize 之前
studio.initialize()

const sheet = getProject('Showcase').sheet('Main')
export default function Scene() {
  return (
    <Canvas camera={{ position: [5, 5, -5] }}>
      <SheetProvider sheet={sheet}>
        <editable.mesh theatreKey="Helmet">      {/* theatreKey = Studio 里的名字 */}
          <boxGeometry args={[1,1,1]} />
          <meshStandardMaterial color="orange" />
        </editable.mesh>
      </SheetProvider>
    </Canvas>
  )
}
```

```js
await project.ready
sheet.sequence.play({ iterationCount: Infinity, range: [0,6], direction: 'normal', rate: 1 })
sheet.sequence.position = 3   // 滚动驱动动画时非常有用
```

## Sequence 播放参数

| 参数 | 说明 |
|---|---|
| `range: [a,b]` | 播放区间（秒）|
| `iterationCount` | `1` / `Infinity` / 数字 |
| `direction` | `'normal'\|'reverse'\|'alternate'\|'alternateReverse'` |
| `rate` | 播放速率（`0.5` 慢放、`2` 快放）|
| `seq.position` `seq.playing` | 读/写播放头；是否播放中 |
| `seq.play()` `seq.pause()` | 播放 / 暂停 |

## 铁律

- Studio 只能存在于开发环境：生产包混入 Studio 会拖慢性能并暴露调试 UI。
- 导出 state 前清理多余关键帧：长期开发会积攒孤儿对象，state.json 越来越大。
- 永远 `await project.ready` 再 `sequence.play()`。
- 用 `types.number(v, {range})` 约束 Studio 拖拽范围（如 opacity 0–1）。
- 不要用它做每帧都变的交互式粒子：Theatre 是编排工具，连续反馈交回 spring/GSAP。
- `onValuesChange` 回调要极轻：每帧触发，不要内部做 `getBoundingClientRect`。
- 一个 Project 多 Sheet 比一条超长时间轴好维护。
- `prefers-reduced-motion`：跳过初始 sequence 直接呈现终态。
