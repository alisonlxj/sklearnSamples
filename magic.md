
## 01 执行Shell命令
#### eg:
    !ls
    !pwd
    !echo "Hello World"
    print(!ls)
    type(!pwd)


## 02 magic command

### 2.1 basic
- %qtconsole :->        启动和当前笔记本相同内核的 qtconsole
- %connect_info :->     当前笔记本链接信息


### 2.2 Line Magic
- %alias :->            定义别名
- %automagic :->        设置输入魔术命令时是否键入%前缀, on(1)/off(0)
- %bookmark :->         管理IPython的书签系统
- %env :->              设置环境变量(无需重启)
- %lsmagic :->          列出当前可用的魔术命令
- %magic :->            显示魔术命令的帮助
- %matplotlib :->       设置matplotlib的工作方式
- %pdb :->              控制pdb交互式调试器的自动调用


### 2.3 Print
- %pdef :->             打印任何可调用对象信息
- %pdoc :->             打印对象的docstring
- %pinfo :->            


### 2.4 Run
- %reset :->
- %time :->             执行Python语句或表达式的时间
- %who_ls :->           列出全局变量







