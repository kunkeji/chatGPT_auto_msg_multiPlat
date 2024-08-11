# 壳林智能客服

<p align="center">
<a href="https://kunkeji.com" target="_blank">壳林智能客服项目</a>
</p>

## 项目介绍

这个项目是智能客服开源项目，目前主要功能有：
1. 智能客服
    这个功能是通过结合FastGPT接口实现对用户问题的自动回答，通过FastGPT的知识库可以实现大部分问题的自动回答。目前，这个功能已经上线了，并且正在不断优化中。
2. 关键词匹配
       除了调用FastGPT接口进行智能问答外，还可以通过关键词匹配的方式对用户的问题进行自动回答。使用的是fuzzywuzzy库，该库可以匹配字符串的相似度。
3. 支持平台
    目前千牛已经完全适配，即使获取聊天记录的方式不正确，但是依然可以。其次就是拼多多

## 注意：
这是目前这个项目遇到的唯一的技术难点
在获取用户信息时采用的是对整个输入框进行全选复制，然后通过正则表达式进行匹配，这种方式存在一定的局限性。目前这个是问题是最大的问题
我想通过hook，或者通过拦截WebSocket的方式获取聊天信息，但是我不会这个技术，希望有大佬能够指导一下我。
或者通过 Chromium 动态脚本注入的方式也行，理论上这些方法都是可以的，希望有这方技术的大佬可以为项目贡献代码。

## 2. 项目架构
**略**
## 3. 项目部署
1. 安装依赖
```python
pip install -r requirements.txt 
```
2. 启动项目
```python
python app.py
```
## 4. 项目演示
<video width="960" height="540" controls>
  <source src="https://www.kunkeji.com/video/%E5%A3%B3%E6%9E%97%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## 5. 项目交流
微信：kunkeji2021