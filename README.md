# NPWY-AUTO-YQTB

使用 GitHub Acition 进行西北工业大学自动疫情填报

![nwpu-auto-yqtb](https://socialify.git.ci/2ndelement/nwpu-auto-yqtb/image?description=1&descriptionEditable=%20GitHub%20Acition%20%E8%A5%BF%E5%8C%97%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6%E8%87%AA%E5%8A%A8%E7%96%AB%E6%83%85%E5%A1%AB%E6%8A%A5&font=Bitter&issues=1&language=1&name=1&owner=1&stargazers=1&theme=Light)

## 使用方式

- fork 本仓库

- 依次点击 Github 仓库 `Settings` => `Secrets`(侧边栏) => `Actions` => `New repository secret`

- 填写 `Name`: `config`

- 填写 `Value`: 仓库中 [config.json](config.json) 的示例, **如果多个用户签到就填写多项列表,否则一项即可,不要重复填写同一个用户**

单人: 
```json
[
  ["202030xxx1","yourpassword"]
]
```
多人:
```json
[
  ["202030xxx1","yourpassword"],
  ["202030xxx2","hispassword"],
  ["202030xxx3","herpassword"]
]
```

- **❗重要❗** 最后点击 `Actions` => 选择`自动疫情填报` 工作流 => `Enable workflow`

- 推荐先手动运行一遍工作流查看是否能正确执行


## 启用消息推送（选用，不需要推送功能可以跳过）

### pushplus微信推送功能

用 [pushplus(推送加)](https://www.pushplus.plus/) 通过公众号推送结果:

- 登录pushplus官网后, 选择一对一推送页面, 按照网站的说明获取你的`token`.
 
- 复制该token，依次点击 Github 仓库 `Settings` => `Secrets`(侧边栏) => `Actions` => `New repository secret`

- 填写 `Name`: `pushplus`

- 填写 `Value`: 刚刚复制的token

## 提示

> 更改 [workflow yaml](.github/workflows/main.yml) 中 cron 项即可填报更改时间
>
> ``` yaml
> schedule:
>    - cron: '0 0 * * *' # 此时间为 'UTF时间', +8h 后为 '北京时间'
> ```
> 由于定时任务由Github调度, 实际执行时间可能延迟1-2h不定
> 更多可见 [github docs onschedule](https://docs.github.com/cn/actions/using-workflows/workflow-syntax-for-github-actions#onschedule)


## 声明
- 打卡可能会失败, 建议开启消息推送.
- 本项目仅提供参考, 因使用本项目导致的一切不良后果请使用者自行承担
