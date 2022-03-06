# 介绍
一个远程控制舵机的方案
采用树莓派作为服务器端， 网页作为控制端。
网页通过点击按钮来发送Get请求，服务器端开启tornado web服务器监听http请求

# 依赖安装
```python
sudo pip install rpi.gpio
sudo pip install tornado
```
# 网页部署
1. 放在服务器上，使用nginx访问静态网页
2. 可集成到tornado，由tornado驱动网页 （未做）

# 使用
## 使用前修改以下文件
### 修改服务器端口号
`py/main.py` 修改 `app.listen(5601)`, 括号内为tornado服务器使用的端口号
`RemoteCom/index.js` 修改`const api_url = "http://xxxxxxxxxxxx"`, 引号内修改为 http://ip地址:服务器端口号， 如`http://192.168.0.0:5601`

### 修改树莓派的舵机GPIO口
`py/main.py` 修改 `rot = Rotation()`的第一个参数，为自己使用的GPIO的编号

## get请求格式
### 开启
`http://ip地址:端口号?ctrl=true`
### 关闭
`http://ip地址:端口号?ctrl=false`
# 运行
```bash
python main.py
```

