# Kigurumi IP Brand Kit - AI Agent 使用指南 (HOW-TO-USE)

你好，AI 助手！如果你被要求基于本项目的 Kigurumi IP 生成新的 Icon、插图或进行衍生设计，请**务必严格遵循**本指南中的说明与规则。这能保证生成出来的视觉风格始终保持“绝对居中对称”、“极简”以及“特征统一”。

## 1. 核心垫图的使用 (Base Reference)
为了让 AI 生图工具更好地理解手部动作和物品位置，请**根据用户需求在 `assets/` 目录下智能挑选最匹配的已有设计作为垫图**。
- 如果用户只需要纯粹的基础形象，或者需要的动作难以归类，请使用 `assets/00_Base_Reference.jpg`。
- 如果用户需要“手持物品”的 Icon，请优先在已有的库中（例如 `01_Icon_Tools.jpg`, `07_Icon_Dev.jpg`, `08_Icon_Finance.jpg` 等）挑选一个**手部姿势最接近**的图片作为核心特征垫图 (Image Prompt / ControlNet Reference)。
利用已有的构图和动作参考可以极大提高出图的稳定性和成功率。

## 2. Prompt 书写标准结构 (The Prompt Template)
请参考 `reference/` 目录下的 `.md` 文件（如 `01_Icon_Tools_Prompt.md` 等）。
所有新的 Prompt 必须严格遵循以下 **8个模块化段落**。除 `Background` 和 `Subject` 外，其余段落必须保持一字不差的绝对一致。

```text
Create one complete full-bleed 1:1 square image.
Reference the provided image for the character's core design (blonde twin tails WITH DISTINCT PINK GRADIENT TIPS, red eyes, a tiny clean mouth, cream cardigan, blue bow tie).
Background: [根据应用场景替换为纯色，例如: fill the entire square with solid gently muted tech blue.]
Subject: place one extremely simplified, cute, endearing girl IP character perfectly centered and upright, emerging from the bottom edge. To represent a [你的应用主题] app, she is holding [替换为手持物品，如: a large, pure geometric wrench].
Crucial details: She MUST have a tiny, perfectly clean mouth. The twin tails MUST have visible pink gradient tips. The red eyes MUST be perfect, clean ovals.
Complexity: use only 4–7 large basic shapes. Remove every nonessential line, detail, texture, and decoration. Keep the character readable at 32 × 32 as an app icon.
Color behavior: organize the colors into broad purposeful masses (blonde hair, pink tips, cream cardigan, dark blue bow tie, red eyes).
Composition: perfectly centered at the bottom, filling about 85% of the square.
Style: make simplification, cuteness, and lovable baby-like appeal the strongest qualities. Ultra-clean graphic treatment. Extremely subtle neo-skeuomorphic depth.
Constraints: Use no text or watermark. Include no extra scenery. Keep the background completely solid and uniform.
```

## 3. 修改变量指南 (Variables to Change)
当用户提出新需求（例如为“天气应用”、“游戏应用”做图标）时，你**只允许修改以下两处**：
- **Background**: 改为符合主题颜色的纯色。例如 `solid gently muted night sky blue` 或 `solid soft pastel green`。
- **Subject**: 保留前置句式（`place one... emerging from the bottom edge.`），仅修改 `To represent a [...] app, she is holding [...]` 部分。确保设定的手持物体是“极简的”、“纯几何形状的 (pure geometric)”。

## 4. 绝对禁止的行为 (Strict Constraints)
- **禁止添加文字/水印**：图标必须纯净。
- **禁止添加多余背景元素**：背景必须是绝对纯色（solid and uniform），不允许有渐变云彩、星空纹理等复杂背景环境。
- **背景色 Ban 位（色彩防粘连）**：严禁将背景色设定为与角色本体相近的暖色系（如暖橘色、浅黄色、淡粉色、米白色）。背景必须使用对比色或深色，以保证角色轮廓的清晰。
- **禁止修改核心特征**：必须保留奶黄渐变粉色的双马尾（无杂乱发丝）、纯红无高光无睫毛的竖椭圆眼、极小的嘴巴、暖米白针织衫、深藏青领结。
- **禁止过度复杂化**：必须遵循 4-7 个大基础形状的约束，保证在 32x32 分辨率下的可读性（盲盒/软黏土/极简图标质感）。

## 5. 建议给用户的回答/工作流
当用户要求你为某个新项目设计 Kigurumi IP Icon 时，你应该：
1. 询问/确认新应用的**主题**和**主色调**。
2. 分析并从 `assets/` 目录下挑选一张**动作或结构最接近**的已有图片作为垫图推荐给用户。
3. 决定 `Background` 和 `Subject` 的替换词。
4. 按照第 2 节的模板直接输出一段完整的英文 Prompt。
5. 提醒用户使用你推荐的那张图片作为垫图，并在生图工具（如 Midjourney）中适当调高垫图权重（如 `--iw 1.5`）。
