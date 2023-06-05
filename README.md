# openai-chat

#### prompt

``` python
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


/**
 * 
 * 
 * 
 * 
 */


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

#### flow

``` python
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


/**
 * 
 * 
 * 
 * 
 */


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```

<!-- description -->

| Name | Type | Desc |
| :--- | :--- | :--- |
| require |
| | *model  | `string` |  |
| | *engine  | `string` | |
| | 
| prompt | `string` or `array<string>` | | |
| suffix | `string` | 返回结果的后缀 |
| max_tokens | `string` | |
| temperature | `number` | |
| top_p | `number` | |
| n | `number` | |
| stream | `boolean` | |
| |
| logprobs | `number` | |
| echo | `number` | |
| stop | `number` | |
| presence_penalty | `number` | |
| frequency_penalty | `number` | |
| best_of | `number` | |
| logit_bias | `number` | |
| user | `number` | |


#### completion.model

> 获取 model list

``` python
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


import os
import openai

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

# openai.organization = os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    completions = openai.Model.list()
    print(completions)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```


#### completion.engine

> 在 OpenAI API 中，model 和 engine 是互斥的参数，只能使用其中一个。
> 如果指定了 model 参数，则忽略 engine 
> 参数；如果没有指定 model 参数，则必须指定 engine 参数。

<!-- description -->

| version | Name | Desc |
| :--- | :--- | :--- |
| `v1` |
| | davinci |  全面性、功能强大的语言模型，可用于各种自然语言任务，包括文本生成、问题回答和语义搜索等 |
| | curie | 较小的语言模型，适用于需要较少计算资源的应用场景，例如智能回复和聊天机器人等 |
| | babbage | 更小的语言模型，适用于移动设备和嵌入式系统等资源受限的环境 |
| | ada  | 最小的语言模型，适用于资源非常受限的环境，例如 IoT 设备和传感器等。实验性引擎（可能不稳定）|
| `beta` |
| | davinci-codex | 面向编程和 AI 建模的语言模型，可用于代码自动生成、代码推理和代码补全等任务|
| | davinci-landscape | 面向地理空间数据分析和可视化的语言模型，可用于自然语言查询和图表生成等任务）|
