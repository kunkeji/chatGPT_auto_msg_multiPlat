# "壳林"智能客服开源项目
## 1. 项目介绍
    这个项目是智能客服开源项目，目前主要功能有：
    1. 智能客服
       这个功能是通过结合FastGPT接口实现对用户问题的自动回答，通过FastGPT的知识库可以实现大部分问题的自动回答。
       目前，这个功能已经上线了，并且正在不断优化中。
    2. 关键词匹配
       除了调用FastGPT接口进行智能问答外，还可以通过关键词匹配的方式对用户的问题进行自动回答。使用的是fuzzywuzzy库
    3. 目前存在问题


       # **在获取用户信息时采用的是对整个输入框进行全选复制，然后通过正则表达式进行匹配，这种方式存在一定的局限性。目前这个是问题是最大的问题**

## 2. 项目架构
    略
## 3. 项目部署
    
## 4. 项目演示
## 5. 项目交流