# 07 · React PostFX 后期特效 — 实战分册

> 基于 `pmndrs/react-postprocessing`（`postprocessing` 的 R3F 封装）。
> 原理：场景渲到离屏 buffer 后做全屏像素级加工，一次十几个效果组合也只合并成一条 EffectPass，比 three/examples 的 pass 链式更省。
> 主入口与全局铁律见 `../SKILL.md`。

## 安装与最小模板

```bash
npm i three @react-three/fiber @react-three/drei @react-three/postprocessing
```

```jsx
import { Canvas } from '@react-three/fiber'
import { EffectComposer, Bloom, DepthOfField, Vignette, Noise } from '@react-three/postprocessing'

export default function App() {
  return (
    <Canvas gl={{ antialias: false }} camera={{ position: [0, 0, 5] }}>
      <ambientLight intensity={0.6} />
      <ProductMesh />
      <EffectComposer disableNormalPass multisampling={0}>
        <DepthOfField focusDistance={0.02} focalLength={0.05} bokehScale={2.4} height={480} />
        <Bloom intensity={0.6} luminanceThreshold={0.75} luminanceSmoothing={0.9} mipmapBlur />
        <Noise opacity={0.025} />
        <Vignette eskil={false} offset={0.12} darkness={1.05} />
      </EffectComposer>
    </Canvas>
  )
}
```

> ⚠️ `gl={{ antialias: false }}`：用了后期链路就别再开 MSAA，改由 `multisampling={n}` 控制，否则双倍开销。
> ⚠️ 没用到法线通道时用 `disableNormalPass`，省一次全屏渲染。

## Effect 速查表

| 组件 | 作用 | 关键 props | 性能 |
|---|---|---|---|
| `Bloom` | 发光溢出 | `intensity` `luminanceThreshold` `luminanceSmoothing` `mipmapBlur` | 中 |
| `DepthOfField` | 景深/虚化 | `focusDistance` `focalLength` `bokehScale` `height` | 高（降 height）|
| `Vignette` | 暗角 | `offset` `darkness` `eskil` | 极低 |
| `Noise` | 颗粒/胶片 | `opacity` `premultiply` | 极低 |
| `Scanline` | 扫描线 | `density` `opacity` | 极低 |
| `ChromaticAberration` | 色散 | `offset:[x,y]` `radialModulation` | 中 |
| `Glitch` | 故障风 | `delay` `duration` `strength` `mode` | 中（建议短暂触发）|
| `ToneMapping` | HDR 色调映射 | `mode: ToneMappingMode.ACES_FILMIC` | 低 |
| `SelectiveBloom` | 只让部分物体发光 | `lights` `selection` | 中高 |
| `N8AO` / `SSAO` | 环境光遮蔽（第三方）| `aoRadius` `intensity` / `samples` `radius` | 高 |
| `SMAA` | 抗锯齿（替代 MSAA）| — | 低 |
| `Pixelation` | 像素质化 | `granularity` | 极低 |

**叠加顺序原则**：校正类在前（ToneMapping）→ 场景感（DOF、AO）→ 发光（Bloom）→ 氛围/风格化（Noise、Scanline、Vignette）。

## Selective Bloom（最常被问到）

```jsx
import { EffectComposer, SelectiveBloom } from '@react-three/postprocessing'
import { useRef } from 'react'
function Scene() {
  const logoRef = useRef()
  return (<>
    <mesh ref={logoRef}>…</mesh>
    <mesh>…其他物体…</mesh>
    <EffectComposer autoClear={false}>
      <SelectiveBloom selection={[logoRef]} intensity={2} luminanceThreshold={0.2} mipmapBlur />
    </EffectComposer>
  </>)
}
```

## 动态交互：随状态改变特效

```jsx
const [zoom, setZoom] = useState(false)
<EffectComposer>
  <DepthOfField target={[0,0,0]} focalLength={zoom ? 0.02 : 0.08} bokehScale={zoom ? 5 : 2} height={480} />
</EffectComposer>
```
频繁变更 pass 会重建 shader：用 `react-spring` 驱动**数值**而非频繁挂载/卸载 `<Effect>`。

## 铁律

- 性能预算优先：移动端最多 2–3 个效果（通常 `Bloom + Vignette + SMAA`），DOF/SSAO/N8AO 这类高开销按设备降级或只在桌面开。
- 用 `multisampling={0}` + `<SMAA/>` 取代 MSAA，通常更省钱且边缘更干净。
- `Bloom`/`DOF` 的 `height` 是质量旋钮：降到 240–360 大幅省费。
- 改动 `multisampling` / `enableNormalPass` 会重建整条 composer，应在初始化决定而非频繁切换。
- 调参顺序：先只放 `Bloom` 看基础观感，再依次叠加，避免一次上满导致性能与观感都难定位。
- `transparent` 物体与 DOF/SSAO 常打架：对含透明材质的场景，先用 SelectiveBloom 等局部效果替代全屏 AO。
- `prefers-reduced-motion` 涉及动效类（如持续 Glitch、自动景深呼吸）时关闭或降强度。
- 注意 ColorManagement：启用后期后亮度可能偏移，配合 `ToneMapping` 与 `gl={{ toneMapping: NoToneMapping }}` 由 composer 统一接管色调映射。
