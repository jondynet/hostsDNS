# hostsDNS
一个DNS服务端，先解析hosts文件里的域名，如果没有再去公网解析，方便使用hosts

设置hosts可以方便我们突破一些限制，同样也增加了被中间人攻击的风险，请慎用！

这个项目来自于我的一个关于代理服务器的群，网友想同步他谷歌浏览器的收藏夹，然而大部分免费代理服务器是不能有效帮助他们翻墙的。
在零成本和对隐私没那么敏感的情况下，我推荐他修改hosts来实现，毕竟有这么多前辈收集整理了能用hosts，
通过修改hosts很容易的就解决网友PC端的问题，那么如何在手机端也能用呢，手机可没有PC这么容易修改hosts。

于是就有个这个脚本，一个DNS服务端，当域名查询来的时候，首先判断hosts里有没有，如果有返回解析为hosts里的IP，
如果没有，去公网dns里查询并返回相应记录。

启动服务

```
$ sudo python hostsDNS.py
```

hosts 文件来自github关注量最高的[https://github.com/racaljk/hosts](https://github.com/racaljk/hosts)

```
$ curl -O https://raw.githubusercontent.com/racaljk/hosts/master/hosts
```

