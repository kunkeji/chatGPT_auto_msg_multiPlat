!function () {
    if (!window.__JDY) {
        window.__JDY = !0;
        var d = [5e4]
            , e = ["9.0.0.1N"];
        Date.prototype.format = function (e) {
            var o = {
                "M+": this.getMonth() + 1,
                "d+": this.getDate(),
                "h+": this.getHours(),
                "m+": this.getMinutes(),
                "s+": this.getSeconds(),
                "q+": Math.floor((this.getMonth() + 3) / 3),
                S: this.getMilliseconds()
            };
            for (var n in /(y+)/.test(e) && (e = e.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length))),
                o)
                new RegExp("(" + n + ")").test(e) && (e = e.replace(RegExp.$1, 1 == RegExp.$1.length ? o[n] : ("00" + o[n]).substr(("" + o[n]).length)));
            return e
        }
            ;
        var n, t, o = (t = !(n = []),
            document.addEventListener ? (document.addEventListener("DOMContentLoaded", s, !1),
                document.addEventListener("readystatechange", s, !1),
                window.addEventListener("load", s, !1)) : document.attachEvent && (document.attachEvent("onreadystatechange", s),
                    window.attachEvent("onload", s)),
            function (e) {
                t ? e.call(document) : n.push(e)
            }
        ), i = null, a = {
            isReady: function () {
                return !!r()
            },
            getVersion: function (e, o) {
                o = o || function () { }
                    ;
                var n = r();
                return !!n && (n.application.invoke({
                    cmd: "getVersion",
                    param: {},
                    success: e,
                    error: o
                }),
                    !0)
            },
            getSDKVersion: function (e, o) {
                o = o || function () { }
                    ;
                var n = r();
                return !!n && (n.application.invoke({
                    cmd: "getSDKVersion",
                    param: {},
                    success: e,
                    error: o
                }),
                    !0)
            },
            getLoginUser: function (e, o) {
                o = o || function () { }
                    ;
                var n = r();
                return !!n && (n.application.invoke({
                    cmd: "getLoginuser",
                    param: {},
                    success: e,
                    error: o
                }),
                    !0)
            },
            getQN: r
        };
        o(function () {
            g("1.1.0", e),
                g("READY", {
                    TASK_CACHE: TASK_CACHE
                });
            try {
                document.getElementById("ydkr").remove()
            } catch (e) { }
            try {
                document.getElementById("ydk1").remove()
            } catch (e) { }
            try {
                document.getElementById("ydk").remove()
            } catch (e) { }
            try {
                document.getElementById("ydks").remove()
            } catch (e) { }
            var i = null
                , s = null
                , r = null;
            function c(e, o, n) {
                if (r != o) {
                    if (r = o,
                        n && 0 != n.length)
                        for (var t = 0; t < n.length; t++)
                            if (0 == n[t].type) {
                                var i = parseInt(n[t].time);
                                if (10 == (i + "").length && (i *= 1e3),
                                    !(6e5 <= Date.now() - i))
                                    try {
                                        e.send(JSON.stringify({
                                            type: "message",
                                            msg: n[t]
                                        }))
                                    } catch (e) { }
                            }
                } else
                    console.log(o, n)
            }
            f(function (e) {
                return u("getVersion", {
                    count: e
                }),
                    a.getVersion(function (e) {
                        l("getVersion", e),
                            e.version,
                            f(function (e) {
                                return u("getSDKVersion", {
                                    count: e
                                }),
                                    a.getSDKVersion(function (e) {
                                        l("getSDKVersion", e),
                                            e.version,
                                            f(function (e) {
                                                return u("getLoginUser", {
                                                    count: e
                                                }),
                                                    a.getLoginUser(function (e) {
                                                        l("getLoginUser", [e, s = e.sub_user_nick || e.user_nick]),
                                                            i = y(s),
                                                            f(function () {
                                                                return !(!window.imsdk2 || !window.imsdk) && (window.imsdk.on("im.singlemsg.onReceiveNewMsg", function (e) {
                                                                    imsdk2.getLocalHistoryMsg({
                                                                        cid: {
                                                                            ccode: e[0].ccode
                                                                        },
                                                                        count: 2,
                                                                        gohistory: 1
                                                                    }, "single").then(function (e) {
                                                                        
                                                                        if (l("imsdk2.getLocalHistoryMsg", e),0 < e.msgs.length) {
                                                                            l("imsdk2.getLocalHistoryMsg", e.msgs.length);
                                                                            var o = e.msgs.length - 1
                                                                                , n = e.msgs[o];
                                                                            switch (l("imsdk2.getLocalHistoryMsg.last", n),
                                                                            n.templateId) {
                                                                                case 503:
                                                                                    l("imsdk2.getLocalHistoryMsg", 503);
                                                                                    for (var t = o; 0 <= t; t--)
                                                                                        if (l("imsdk2.getLocalHistoryMsg", e.msgs[t], e.msgs[t].fromid.nick),
                                                                                            l("imsdk2.getLocalHistoryMsg", s, e.msgs[t].fromid.nick),
                                                                                            l("imsdk2.getLocalHistoryMsg", e.msgs[t].fromid.nick),
                                                                                            s != e.msgs[t].fromid.nick && 101 == e.msgs[t].templateId) {
                                                                                            c(i, e.msgs[t].mcode.messageId, [{
                                                                                                type: 0,
                                                                                                templateId: 503,
                                                                                                time: e.msgs[t].sendTime,
                                                                                                nick: e.msgs[t].fromid.nick,
                                                                                                message: e.msgs[t].originalData.text,
                                                                                                shop: s
                                                                                            }]);
                                                                                            console.log("Message  (503):", e.msgs[o].originalData);
                                                                                        }
                                                                                    break;
                                                                                case 101:  //文本消息
                                                                                    l("imsdk2.getLocalHistoryMsg", 101),
                                                                                        s != e.msgs[o].fromid.nick && c(i, e.msgs[o].mcode.messageId, [{
                                                                                            type: 0,
                                                                                            templateId: e.msgs[o].templateId,
                                                                                            time: e.msgs[o].sendTime,
                                                                                            nick: e.msgs[o].fromid.nick,
                                                                                            message: e.msgs[o].originalData.text,
                                                                                            shop: s
                                                                                        }]);
                                                                                    break;
                                                                                case 102:  //图片消息
                                                                                    l("imsdk2.getLocalHistoryMsg", 102),
                                                                                        s != e.msgs[o].fromid.nick && c(i, e.msgs[o].mcode.messageId, [{
                                                                                            type: 0,
                                                                                            templateId: e.msgs[o].templateId,
                                                                                            time: e.msgs[o].sendTime,
                                                                                            nick: e.msgs[o].fromid.nick,
                                                                                            message: e.msgs[o].originalData.url,
                                                                                            shop: s
                                                                                        }]);
                                                                                    break;
                                                                                case 104:  //语音消息
                                                                                    l("imsdk2.getLocalHistoryMsg", 104),
                                                                                        s != e.msgs[o].fromid.nick && c(i, e.msgs[o].mcode.messageId, [{
                                                                                            type: 0,
                                                                                            templateId: e.msgs[o].templateId,
                                                                                            time: e.msgs[o].sendTime,
                                                                                            nick: e.msgs[o].fromid.nick,
                                                                                            message: e.msgs[o].ext.bizDataExt.audio_text,
                                                                                            url: e.msgs[o].originalData.url,
                                                                                            shop: s
                                                                                        }]);

                                                                                    break;
                                                                                default:
                                                                                    l("imsdk2.getLocalHistoryMsg", "other"),
                                                                                        s != e.msgs[o].fromid.nick && c(i, e.msgs[o].mcode.messageId, [{
                                                                                            type: 0,
                                                                                            templateId: e.msgs[o].templateId,
                                                                                            time: e.msgs[o].sendTime,
                                                                                            nick: e.msgs[o].fromid.nick,
                                                                                            message: "未知消息",
                                                                                            data: e.msgs[o].originalData,
                                                                                            shop: s
                                                                                        }])

                                                                                        
                                                                            }
                                                                        }
                                                                    }).catch(function (e) {
                                                                        m("imsdk2.getLocalHistoryMsg", e)
                                                                    })
                                                                }),!0)
                                                            
                                                            })
                                                    }, function () {
                                                        m("getLoginUser")
                                                    })
                                            })
                                    }, function () {
                                        m("getVersion")
                                    })
                            })
                    }, function () {
                        m("getVersion")
                    })
            })
        })
    }
    function g(e, o) {

    }
    function u(e, o) {

    }
    function l(e, o) {

    }
    function m(e, o) {

    }
    function f(n, t, i, s, r) {
        t = t || 1e3,
            i = i || 0,
            s = s || function () { }
            ,
            r = r || function (e) { }
            ;
        var c = 0
            , d = 0;
        !function e() {
            if (0 < i && i < d + 1)
                r(1);
            else {
                var o = n(++d);
                c && (clearTimeout(c),
                    c = 0),
                    o ? s() : c = setTimeout(e, t)
            }
        }()
    }
    function s(e) {
        if (!t && ("onreadystatechange" !== e.type || "complete" === document.readyState)) {
            for (var o = 0; o < n.length; o++)
                n[o].call(document);
            t = !0,
                n = null
        }
    }
    function r() {
        return i || (i = function () {
            if (!window.workbench)
                return null;
            window.YDK_TASK_CACHE || (window.YDK_TASK_CACHE = []);
            window.YDK_NOTIFY_FUNC || (window.YDK_NOTIFY_FUNC = {});
            var e = {
                application: {
                    invoke: function (e) {
                        var o = {
                            id: workbench.createSequenceId(),
                            cmd: e.cmd,
                            param: e.param,
                            onSuccess: e.success,
                            onError: e.error
                        };
                        window.YDK_TASK_CACHE[o.id] = o,
                            workbench.application.invoke(o.id, e.cmd, JSON.stringify(e.param))
                    }
                },
                event: {
                    regEvent: function (e) {
                        window.event_regConfigs[e.eventId] = e,
                            window.YDK_NOTIFY_FUNC[e.eventId] = e.notify,
                            workbench.regEvent(workbench.createSequenceId(), e.eventId)
                    }
                }
            };
            return window.YDK_ori_OnInvokeNotify = window.onInvokeNotify,
                window.onInvokeNotify = function (e, o, n) {
                    if (g("window.onInvokeNotify", {
                        sid: e,
                        status: o,
                        rsp: n
                    }),
                        e) {
                        var t = YDK_TASK_CACHE[e];
                        if (void 0 !== t) {
                            try {
                                n = JSON.parse(n)
                            } catch (e) { }
                            0 === o ? "function" == typeof t.onSuccess && t.onSuccess(n) : "function" == typeof t.onError && t.onError(n)
                        }
                        "function" == typeof window.YDK_ori_OnInvokeNotify && window.YDK_ori_OnInvokeNotify(e, o, n)
                    }
                }
                ,
                window.YDK_oriOnEventNotify = window.onEventNotify,
                window.onEventNotify = function (e, o, n, t, i) {
                    var s;
                    switch (g("window.onEventNotify", {
                        sid: e,
                        eventId: o,
                        rsp: t,
                        o: i
                    }),
                    "function" == typeof window.YDK_oriOnEventNotify && window.YDK_oriOnEventNotify(e, o, n, t, i),
                    window.event_regConfigs && window.event_regConfigs[o] && (s = window.event_regConfigs[o]),
                    n) {
                        case 0:
                            s && s.success && "function" == typeof s.success && s.success(o),
                                s && delete window.event_regConfigs[o];
                            break;
                        case 1:
                            s && s.error && "function" == typeof s.error && s.error(t, o),
                                s && delete event_regConfigs[o];
                            break;
                        case 2:
                            "function" == typeof window.YDK_NOTIFY_FUNC[o] && window.YDK_NOTIFY_FUNC[o](t, o)
                    }
                }
                ,
                e
        }())
    }
    function y(e) {
        var n = 0
            , t = null
            , i = 0
            , s = e;
        function r(e) {
            if (t && 1 == t.readyState)
                try {
                    t.send(e)
                } catch (e) { }
        }
        var c = {
            timeout: 1e4,
            timeoutObj: null,
            serverTimeoutObj: null,
            reset: function () {
                return clearTimeout(this.timeoutObj),
                    clearTimeout(this.serverTimeoutObj),
                    this.timeoutObj = this.serverTimeoutObj = null,
                    this
            },
            start: function () {
                var e = this;
                this.timeoutObj = setTimeout(function () {
                    r("{type:'beat'}"),
                        e.serverTimeoutObj = setTimeout(function () {
                            t.close(),
                                t = null
                        }, e.timeout)
                }, this.timeout)
            }
        };

        return function o() {
            var e;
            n >= d.length && (n = 0),
                port = d[n],
                n++,
                e = "ws://127.0.0.1:" + port + "?seller=" + encodeURIComponent(s),
                (t = "WebSocket" in window ? new WebSocket(e) : "MozWebSocket" in window ? new MozWebSocket(e) : null).onopen = function () {
                    // SystemMessage('消息监听连接成功','msg');
                    n--,
                        c.reset().start(),
                        0 != i && (clearTimeout(i),
                            i = 0)
                }
                ,
                t.onclose = function (e) {
                    //SystemMessage('消息监听连接断开','msg');
                    0 != i && (clearTimeout(i),
                        i = 0),
                        i = setTimeout(o, 1e3)
                }
                ,
                t.onmessage = function (e) {
                    c.reset().start();
                    //var msg = e.data;

                    //如果你想在 WebSocket 收到消息时调用 sendmsg 函数，你可以将 sendmsg 调用放在匿名函数内部的 t.onmessage 事件处理程序中
                    //发送消息																															
                    function sendmsg(msg) {
                        console.log(msg.nick, msg.uid, msg.text);

                        openAndVerifyWindow(msg.nick, msg.uid, msg.text)
                            .then(result => {
                                var results = true;
                                t.send(JSON.stringify({
                                    type: 'sendmsgs',
                                    status: results,
                                }));
                            })
                            .catch(error => {
                                var results = false;
                                t.send(JSON.stringify({
                                    type: 'sendmsgs',
                                    status: results,
                                }));
                            });
                    }


                    function getEvaluationResult(t) {
                        // 获取当前13位时间戳（毫秒级）
                        const currentTimeStamp = Date.now();

                        // 获取消息列表中最新一条消息的属性
                        const lastMessage = window._vs.msgList[window._vs.msgList.length - 1];
                        const lastSendTime = lastMessage.originBanamaMessage.sendTime;
                        const lastSenderNick = lastMessage.originBanamaMessage.fromid.nick;
                        const msgId = lastMessage.clientId;

                        // 获取登录用户的昵称
                        const loginIDNick = window._vs.loginID.nick;

                        // 获取conversationID的相关属性
                        const conversationNick = window._vs.conversationID.nick;
                        const conversationTargetId = window._vs.conversationID.targetId;

                        // 检查条件2：最新消息发送者昵称是否与登录用户昵称相同
                        const condition2Result = lastSenderNick === loginIDNick;

                        // 计算现行时间戳与lastSendTime的差值
                        const timeDifference = currentTimeStamp - lastSendTime;

                        // 构建JSON对象
                        const evaluationResult = {
                            type: 'evaluationResult', // 添加"type"属性
                            condition2Result: condition2Result,
                            msgId: msgId,
                            currentTimeStamp: currentTimeStamp,
                            lastSendTime: lastSendTime,
                            timeDifference: timeDifference,
                            loginIDNick: loginIDNick,
                            conversationNick: conversationNick,
                            conversationTargetId: conversationTargetId
                        };

                        // 将JSON对象封装在立即解决的Promise中，并在then中发送消息
                        return Promise.resolve(evaluationResult).then((result) => {
                            t.send(JSON.stringify({
                                type: result.type,
                                status: true, // 或根据实际情况设置status值
                                data: result
                            }));
                        });
                    }

                    try {
                        var o = JSON.parse(e.data);
                        if (o.type == 'chat_records') {
                            t.send(JSON.stringify({
                                type: 'chat_records',
                                msg: document.body.innerText,
                            }));
                        } else if (o.type == 'sendmsgs') {
                            sendmsg(o); // 将 sendmsg 调用放在这里
                        } else if (o.type == 'evaluationResult') { // 修复了此处的语法错误
                            getEvaluationResult(t).then(() => {
                                // 处理解析后的数据...
                            });
                        } // 移除了此处多余的右大括号
                    } catch (error) {
                        // 空的catch块，不处理任何错误
                    }
                }
        }(),
        {
            send: function (e) {
                r(e)
            },
            log: function (e) {
                var o;
                o = {
                    type: "log",
                    message: e
                },
                    r(JSON.stringify(o))
            }
        }
    }
}();
alert('配置成功，关闭此窗口')