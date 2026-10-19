# 02 · CSS Doodle 图案生成 — 实战分册

> 开源项目：`css-doodle/css-doodle`。`<css-doodle>` Web Component，用类 CSS 小 DSL 生成几何图案与装饰纹理；
> 同一套语法还能写 SVG、画参数方程曲线，或编译成 GLSL 跑在 GPU 上。
> 主入口与全局铁律见 `../SKILL.md`。

## 最小可运行模板

```html
<script src="https://cdn.jsdelivr.net/npm/css-doodle@0.38.2/css-doodle.min.js"></script>
<css-doodle use="var(--a)" click-to-update seed="2026">
  :doodle { @grid: 12x12 / 100% 480px / #0b0e14; gap: 1px; overflow: hidden; }
  background: @pd(#ff8830, #d1b8a0, #aeced2, #cbdcdf);
  clip-path: polygon(@p(
    '0 0,100% 0,100% 100%', '0 0,100% 0,0 100%',
    '0 0,100% 100%,0 100%', '100% 0,100% 100%,0 100%'));
  transition: @r(1.2s) ease;
</css-doodle>
```

```bash
npm i css-doodle      # React/Vue 里作为自定义元素直接用，属性用 ref 调 JS API
```

## 语法速查

### 标签属性

| 属性 | 作用 |
|---|---|
| `grid="8x8"` | 行列数（也可在 `:doodle` 里 `@grid: 8x8`）|
| `seed="42"` | 随机种子，同种子结果一致（做「每天一张图」用日期当 seed）|
| `use="var(--a, --b)"` | 允许内部使用外部 CSS 变量，实现外部换色 |
| `click-to-update` | 点击图案自动重掷随机（挑图/demo 利器）|

### 核心 @-函数

| 函数 | 作用 | 示例 |
|---|---|---|
| `@grid: rxc / size` | 网格与画布尺寸 | `@grid: 16x9 / 100% auto` |
| `@place-cell: left\|center\|size(w,h)` | 单元格位置/大小 | `@place-cell: center; @size: 2 * @i` |
| `@size: expr` | 单元格尺寸 | `@size: calc(70% - @i*1.5%)` |
| `@p()/@pd()/@pn()` | 随机取值（可重复/不可重复/轮转）| `@p(#f00,#0f0)` `@pn(2,4,4,2)` |
| `@r(min,max)` / `@r(±10deg)` | 随机数（支持对称区间）| `rotate: @r(-28deg,28deg)` |
| `@i` `@n` `@row()` `@col()` `@even/@odd/@nth(3n)` | 序号/行列/奇偶 | `opacity: calc(@i/@n)` |
| `@shuffle()` | 打乱序列 | `background: @shuffle(#a,#b,#c)` |
| `@doodle()` | 嵌套子网格（分形）| — |
| `@plot.scatter(heart)` | 按形状方程散布点 | `@place: @plot.scatter(heart)` |
| `@shape(points,scale,x,y)` | 参数方程生成 `clip-path` | 见下方心形 |
| `@svg(...)` | CSS-like 语法写 SVG | `@svg(viewBox: -3 -3 6 6; ...)` |
| `@pattern(grid,shape,size,fill)` | 编译成 GLSL，GPU 渲染 | `@size: sin(3*log(dr)-2t-da)` |

### JS API

| 方法 | 用途 |
|---|---|
| `doodle.update([code])` | 重掷随机 / 替换代码重绘 |
| `doodle.export({scale})` | 导出 PNG（生成封面图）|
| `doodle.grid(rows,cols)` | 运行时改网格 |
| `doodle.seed(n)` | 运行时换种子 |

## 配方

**1）品牌三角纹理（对称、有序）**
```css
@grid: 10x10 / 360px;
background: @pd(#ff6d6d, #ffd868, #60569e);
clip-path: polygon(@p('0 0,100% 0,100% 100%', '0 0,100% 0,0 100%',
                      '0 0,100% 100%,0 100%', '100% 0,100% 100%,0 100%'));
```

**2）参数方程心形（`@shape`）**
```css
@grid: 1 / 100% auto (16/9) 1px; background: #e91e63;
clip-path: @shape(points: 1200; scale: .085 .08;
  -x: 16 * sin(t)^3;
  -y: 13*cos(t) - 5*cos(2t) - 2*cos(3t) - cos(4t));
```

**3）GPU shader 波纹（`@pattern`，动态背景但低端机慎全屏）**
```css
@grid: 1 / 100% auto (16/9);
@content: @pattern(grid: 48x27; shape: circle; size: sin(3*log(dr)-2t-da);
  fill: hsl(sin(dr/100 + 2t/100) .75 .65));
```

**4）命令行出图（批量封面）**
```bash
npm i -g css-doodle-cli   # cssd
cssd render code.css -x 10
```

## 铁律

- 装饰层不承载信息：doodle 内不放正文，需要文字就在外部叠一层 DOM。
- 图案之上叠文字必须加遮罩层（半透明渐变 / `backdrop-filter`），保 WCAG 对比度。
- 明确 `seed` 才有复现：想固定一张给 seed；想每次不同才用随机。
- 控制单元格数量：`30x30` 以上 DOM 上千，低端机卡；大面积背景优先 `@pattern`（GPU）或导出静态图复用。
- `prefers-reduced-motion`：`@pattern` 的 time 项在减弱动效偏好下应关闭。
- 首屏用静态/导出封面兜底，避免 JS 失败留白。
