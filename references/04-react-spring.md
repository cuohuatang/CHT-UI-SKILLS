# 04 · React Spring 物理动画 — 实战分册

> 开源项目：`pmndrs/react-spring`。基于弹簧物理模型的动画库，由「质量/张力/摩擦」决定弹性手感，比 CSS ease-out 更有生命感。
> 主入口与全局铁律见 `../SKILL.md`。

## 安装与最小模板

```bash
npm i @react-spring/web      # Web 目标；RN 项目用 @react-spring/native
```

```jsx
import { useSpring, animated, config } from '@react-spring/web'

export function Card() {
  const [pressed, setPressed] = React.useState(false)
  const { xys } = useSpring({ xys: pressed ? [1, 1.03, 14] : [0, 1, 4], config: config.wobbly })
  const tiltX  = xys.to([0, 1], [-8, 8])
  const scale  = xys.to(s => s[1])
  const shadow = xys.to(sy => `0 ${sy}px ${sy*3}px rgba(0,0,0,.18)`)
  return (
    <animated.div onPointerDown={() => setPressed(true)} onPointerUp={() => setPressed(false)}
      style={{ scale, rotateX: tiltX, boxShadow: shadow }} className="card" />
  )
}
```

## Hooks 速查

| Hook | 用途 | 场景 |
|---|---|---|
| `useSpring` | 单动画值 → style 对象 | 悬停、按压、显隐 |
| `useSprings(n, fn)` | 一组独立 spring | 卡片网格分别触发 |
| `useTrail(n, props)` | 前一个驱动后一个，连锁迟到 | 导航项依次出现 |
| `useTransition(items, props)` | **列表挂载/卸载**动画 | todo 增删、路由切换 |
| `useChain(...refs)` | 按顺序串起多条 spring | 复杂入场序列 |
| `useSpringValue` | 单可变值（命令式）| 与手势库配合 |
| `useSpringRef` | 给 spring 一个 ref 以便 `useChain` / `.start()` | 编排控制 |

```jsx
const api = useSpringRef()
const springs = useSprings(3, i => ({ ref: api, from: { o: 0 }, to: { o: 1 } }))
useChain([api], [0], 500)   // 延迟 500ms 启动
```

## 弹簧调参速查

```js
import { config } from '@react-spring/web'
config.default    // mass:1 tension:170 friction:26 —— 万能默认
config.gentle     // tension:120 friction:14 —— 柔和缓慢
config.wobbly     // tension:180 friction:12 —— 明显回弹
config.stiff      // tension:210 friction:20 —— 干脆
config.slow       // tension:280 friction:60 —— 沉稳慢镜
config.molasses   // tension:280 friction:120 —— 几乎不过冲
```

| 想要的手感 | 调整方向 |
|---|---|
| 更 bouncy | ↑ `tension` 或 ↓ `friction` |
| 更快响应 | ↓ `mass` 或 ↑ `tension` |
| 完全不过冲 | `friction` 高 + `clamp: true` |
| 固定时长 | `{ duration: 300 }` 替代物理参数（退化为缓动）|

经验值：UI 微交互（<300ms）用 `{ tension: 300, friction: 30 }`；抽屉/大面板用 `{ tension: 220, friction: 28, mass: 1.2 }`。回弹次数最多 1–2 次。

## 常用配置

```jsx
useSpring({
  from: { opacity: 0, y: 24 }, to: { opacity: 1, y: 0 },
  delay: 120, config: { mass: 1, tension: 280, friction: 26 },
  onChange: ({ value }) => {}, onRest: () => {},
  immediate: false, reset: true,
})
```
`spring.to(v => ...)` 做任何转换；多值组合 `to([a,b], (a,b)=>...)`；颜色插值直接写 `background: colorSpring` 即可。

## 铁律

- 列表动画必须给稳定 `keys`：`useTransition(items, { keys: it => it.id })`，否则重排会串味。
- 只动 `transform` 和 `opacity`；`<animated.div>` 只包裹需要的那一层，别铺满整棵子树。
- 同一属性不要被多个 spring 争抢，否则会抖动/闪回。
- `prefers-reduced-motion` 必须处理：
```jsx
import { Globals } from '@react-spring/web'
Globals.assign({ skipAnimation: window.matchMedia('(prefers-reduced-motion: reduce)').matches })
```
- `useTransition` 的 `enter/exit/leave` 三段写全，否则删除项会硬切。
- 手势跟随用 `api.start({ x: e.clientX, immediate: true })`，松手再换回物理回弹。
- 多次快速切换交互不要依赖累计 offset，应依赖目标 state，避免叠加抖动。
