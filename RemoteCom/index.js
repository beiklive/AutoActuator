checkbox = document.getElementsByName("ckbx-square-1")
function send(){
    // if(checkbox.checked){
    //     alert("checkbox is checked");
    // }
    const api_url = "http://xxxxxxxxxxxx"
    const type = "/ctrl";
    //获取checkbox状态
    flag = $("input[type='checkbox']").is(':checked') 
    console.log(flag)
    send_data = { "flag": flag };
    //发送get请求
    $.get(api_url + type, send_data, function (data, status) {});
} 