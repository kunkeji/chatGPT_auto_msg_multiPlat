function loadjQuery(url, callback) {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;

    // 当 script 加载完成后执行的回调函数
    script.onload = function() {
        if (typeof callback === 'function') {
            callback();
        }
    };
    // 处理加载错误
    script.onerror = function() {
        throw new Error('The script ' + url + ' is not accessible.');
    };

    // 将 script 元素添加到 head 中
    document.head.appendChild(script);
}
// 调用 loadjQuery 函数，加载 jQuery 并执行回调函数
loadjQuery('https://code.jquery.com/jquery-3.5.1.min.js', function() {
    !function () {
        $("#J_msg_list").append('<div class="J_msg imui-msg-system"><span>壳林AI已介入会话</span></div>')
        // $("#J_msgBtm")[0].remove();
        window.imsdk.invoke('im.uiutil.GetCurrentConversationID').then(function (e) {
            console.log("当前客户信息", e);
            window.imsdk.invoke('im.singlemsg.GetLocalHisMsg',{
                cid: {
                    ccode:e.result.ccode     //当前用户id
                },
                count: 20,                                             //获取条数       
                gohistory: 1                                           //是否获取历史消息
            }).then(function(e){
                console.log(e)
            })
        })
    }()
});

// 获取当前客服用户名window.imsdk.invoke('im.login.GetCurrentLoginID')
// 获取当前客户信息window.imsdk.invoke('im.uiutil.GetCurrentConversationID')
// 获取服务器时间window.imsdk.invoke('im.bizutil.GetIMSvrTime')

// im.singlemsg.GetNewMsg      //参数ccode:当前用户id      

// 注册用户消息监听 
// im.singlemsg.onPeerInputNotify                               //监听用户输入消息
// im.singlemsg.onReceiveNewMsg                                 //监听当前用户新消息
// im.uiutil.${dlgname}onConversationChange                     //监听切换用户事件
// window.imsdk.on('im.singlemsg.onReceiveNewMsg', (function(e) {
//         console.log("获取当前客户信息", e);
//     }
// ))

// 切换聊天对象
// window.imsdk.on('im.uiutil.${dlgname}onConversationChange'.replace(/\${dlgname}/g, ""), (function(t) {
//     console.log("切换聊天对象=================================================", t)}
// ))

// 根据用户id获取新消息列表
// window.imsdk.invoke('im.singlemsg.GetNewMsg',{
//     ccode: '2209327685704.1-3420774230.1#11001@cntaobao',                                         
// }).then(function(e){
//     console.log(e)
// })









