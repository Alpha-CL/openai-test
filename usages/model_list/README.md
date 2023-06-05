#### model list

``` python
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

{
  "data": [
    {
      "created": 1677532384,                    # Unix 时间戳，表示该模型对象创建的时间
      "id": "whisper-1",                        # 该模型对象的唯一标识符
      "object": "model",                        # 描述了该对象是 OpenAI 平台上的一个模型对象
      "owned_by": "openai-internal",            # 标记该对象的所有者，本例中为 OpenAI
      "parent": null,                           # 描述哪个模型是该模型对象的父亲，null 表示该模型没有父亲模型
      "permission": [                           # 包含一个或多个模型访问权限的数组。描述使用该模型对象的人员可以做的事情
        {
          "allow_create_engine": false,                 # 是否允许创建模型引擎。如果为 false，则不能创建模型引擎
          "allow_fine_tuning": false,                   # 是否允许微调模型。如果为 false，则不能微调模型
          "allow_logprobs": true,                       # 是否允许返回对数概率值。如果为 true，则可以返回对数概率值
          "allow_sampling": true,                       # 是否允许对模型进行采样。如果为 true，则可以对模型进行采样
          "allow_search_indices": false,                # 是否允许搜索索引。如果为 false，则不能搜索索引
          "allow_view": true,                           # 是否允许查看模型。如果为 true，则可以查看模型
          "created": 1683912666,                        # 模型权限创建的时间戳
          "group": null,                                # 模型权限所属的组。如果不存在，则为 null
          "id": "modelperm-KlsZlfft3Gma8pI6A8rTnyjs",   # 模型权限 ID
          "is_blocking": false,                         # 是否在进行模型查询时进行阻塞。如果为 false，则不会进行阻塞
          "object": "model_permission",                 # 对象类型，表明这是一个模型权限对象
          "organization": "*"                           # 模型权限所属的组织。如果没有特定组织，则为 "*"
        }
      ],
      "root": "whisper-1"                       # 标记该对象模型的根模型，本例中为" text-babbage:001"
    },
    ...
  ]
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
```
