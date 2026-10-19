# 08 · Chakra UI 组件系统 — 实战分册

> 开源项目：`chakra-ui/chakra-ui`。现代 React 组件库，开箱即用、支持主题定制（语义 token + recipe）。
> 本分册以 **v3（当前主流）** 为准，并标注 v2 关键差异。
> 主入口与全局铁律见 `../SKILL.md`。

## 安装与 Provider（v3）

```bash
npm i @chakra-ui/react @emotion/react
# 可选：下载官方 snippets（Button/Dialog 等组件源码到 components/ui，便于自定义）
npx @chakra-ui/cli snippet add
```

```tsx
// app/providers.tsx —— v3 用 defaultSystem，不再手写 extendTheme
'use client'
import { ChakraProvider, defaultSystem } from '@chakra-ui/react'

export function Providers({ children }: { children: React.ReactNode }) {
  return <ChakraProvider value={defaultSystem}>{children}</ChakraProvider>
}
```

```tsx
// 暗色模式：搭配 next-themes
import { ChakraProvider, defaultSystem } from '@chakra-ui/react'
import { ThemeProvider, useTheme } from 'next-themes'
import { ColorModeProvider } from '@/components/ui/color-mode'

export function Providers({ children }) {
  return (
    <ThemeProvider attribute="class" disableTransitionOnChange>
      <ChakraProvider value={defaultSystem}>
        <ColorModeProvider>{children}</ColorModeProvider>
      </ChakraProvider>
    </ThemeProvider>
  )
}
```

## 常用写法

### chakra factory（就地样式，首选）
```tsx
import { chakra, Stack, Button } from '@chakra-ui/react'

const Box = chakra('div', {
  base: { rounded: 'lg', bg: 'bg.subtle', p: '4', _hover: { bg: 'bg.emphasized' } },
})

<Stack direction="row" gap="3">
  <Button colorPalette="blue" variant="solid">保存</Button>
  <Button colorPalette="gray" variant="outline">取消</Button>
</Stack>
```

### 语义 token 是 v3 的核心
取值走语义名而非裸色值：`bg.subtle` / `bg.emphasized` / `fg.default` / `fg.muted` / `border.default` / `colorPalette`。暗色模式自动切换，无需手写两套。

### 状态全覆盖（与 `06-ui-ux-craft` 一致）
Chakra 组件自带 hover/active/focus-visible/disabled 样式；自定义组件用伪类补：`_hover` `_active` `_focusVisible` `_disabled` `_loading`。

## 主题定制（v3）

```tsx
// theme.ts —— v3 用 createSystem + defineConfig，废弃 extendTheme
import { createSystem, defineConfig, defineRecipe } from '@chakra-ui/react'

const config = defineConfig({
  theme: {
    tokens: {
      colors: {
        brand: { value: '#2563eb' },
      },
    },
    recipes: {
      button: defineRecipe({
        base: { borderRadius: 'lg' },
        variants: { tone: { loud: { bg: 'brand' } } },
      }),
    },
  },
})
export const system = createSystem(defaultConfig, config)
// <ChakraProvider value={system}>
```

`defineSlotRecipe` / `sva`（slot recipe + variant）用于多部位组件（Dialog、Tabs）。

## v2 → v3 关键差异

| 项 | v2 | v3 |
|---|---|---|
| Provider | `<ChakraProvider theme={extendTheme()}>` | `<ChakraProvider value={defaultSystem\|system}>` |
| 主题扩展 | `extendTheme` | `createSystem(defaultConfig, defineConfig({theme}))` |
| 颜色 | 裸色值 `blue.500` | 语义 token `colorPalette` / `bg.*` / `fg.*` |
| 样式写法 | `<Box bg="blue.500">` | `<Box bg="bg.subtle">` 或 `chakra()` factory |
| 组件来源 | 主包直接导出 | 核心组件仍导出；复杂组件推荐用 CLI snippets 落地源码 |
| 事件回调 | `onClick` 等属性直传 | 部分组件改为 `onValueChange` 等命名（见文档）|

## 铁律

- v3 用 `defaultSystem` 起步，**不要再用 `extendTheme`**（已废弃，类型不兼容）。
- 一律走语义 token（`bg.*` `fg.*` `border.*` `colorPalette`），保证暗色模式与主题切换零成本。
- 自定义组件优先 `chakra()` factory + `defineRecipe`，不要在业务里堆内联样式对象。
- **状态全覆盖**：自定义交互组件必须补 `_hover/_active/_focusVisible/_disabled`；数据视图用 Skeleton/EmptyState 等内置组件补齐 loading/empty/error。
- 间距/圆角/字号用 theme 的 spacing/radii/fontSizes，`p="4"` 而非 `p="17px"`（统一节律，呼应 `06-ui-ux-craft`）。
- 触控热区 ≥ 44×44；图标按钮必须有 `aria-label`。
- `prefers-reduced-motion`：Chakra 的 motion 组件已部分内置降级，自定义动画仍需自行校验。
- 升级 v2→v3 是大版本迁移（provider、token、事件命名全变），不要混用两套写法。
- 以官方文档/当前版本为准：库迭代快，落地前核对 `chakra-ui.com` 当前 API。
