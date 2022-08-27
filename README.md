# NPWY-AUTO-YQTB

使用 GitHub Acition 进行西北工业大学自动疫情填报

![nwpu-auto-yqtb](https://socialify.git.ci/2ndelement/nwpu-auto-yqtb/image?description=1&descriptionEditable=%20GitHub%20Acition%20%E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E7%96%AB%E6%83%85%E5%A1%AB%E6%8A%A5&font=Bitter&issues=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

## 使用方式

- fork 本仓库

- 依次点击 Github 仓库 `Setting` => `Secrets`(侧边栏) => `Actions` => `New repository secret`

- 填写 `Name`: `config`

- 填写 `Value`: 仓库中 `config.json` 的示例

```json
[
  ["uname1","passwd1"],
  ["uname2","passwd2"]
]
```

- 点击 `Action` 启用 `自动疫情填报` 工作流即可

