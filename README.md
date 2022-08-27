# NPWY-AUTO-YQTB

使用 GitHub Acition 进行西北工业大学自动疫情填报

![nwpu-auto-yqtb](https://socialify.git.ci/2ndelement/nwpu-auto-yqtb/image?description=1&descriptionEditable=%20GitHub%20Acition%20%E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E7%96%AB%E6%83%85%E5%A1%AB%E6%8A%A5&font=Bitter&issues=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

## 使用方式

- fork 本仓库

- 依次点击 Github 仓库 `Settings` => `Secrets`(侧边栏) => `Actions` => `New repository secret`

- 填写 `Name`: `config`

- 填写 `Value`: 仓库中 [config.json](config.json) 的示例, **如果多个用户签到就填写多项列表,否则一项即可,不要重复填写同一个用户**

```json
[
  ["uname1","passwd1"],
  ["uname2","passwd2"]
]
```

- ❗**最后点击 `Actions` 启用 `自动疫情填报` 工作流**❗
> fork 之后的定时工作流是默认关闭的! 一定要手动启用一下！

## 提示

> 更改 [workflow yaml](.github/workflows/main.yml) 中 cron 项即可填报更改时间
> ``` yaml
> schedule:
>    - cron: '0 0 * * *' # 此时间为 'UTF时间', +8h 后为 '北京时间'
> ```
> 更多可见 [github docs onschedule](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)
