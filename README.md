<h1 align="center">DS160填写工具</h1>

## 更新
2024/01/15 更新等待模式为显式等待（护照信息页处理暂时保留隐式等待，显式等待会报错，原因暂时未知），以及对应文档更新
2024/02/15 填写的数据来源转移至JSON
           除最后一页外，取消保存处理（一定提高速度，可能降低稳定性）
2024/02/27 新增更改json值的图形化flask工具       

## 介绍

不多说，看标题应该能猜出来了吧

## 效果

填表OK，上传照片OK，总耗时<5min（可能根据填表数据不同或Pause_Time设定而异）

## 常见问题和对应

本地测试成功率较高，但不是100%，目前已知以下原因：
1. 网络卡了
2. 该网站本身问题（著名的超时窗口等）
3. 验证码错误
4. 简单逻辑错误（填的资料里父亲比你还小，调用下拉菜单时指定了一个不存在的值等）
5. 照片不合规，或者指定路径错误

目前已知应对方法，请根据情况选择：
1. 换个好的网（较小可能：追加新的等待处理语句试试）
2. 联系网站管理员（如果你认为可行的话），或者等待对应的错误处理模块（虽然我也不知道什么时候能完成），或者自己制作
3. 不用多说了吧（过程中刷新验证码图片操作OK）
4. 不用多说了吧
5. 不用多说了吧

## 注意事项

请牢记工具里print出来的值

## 最后补充

本工具包含从登录到上传照片过程，后续review等流程不在本工具范围内，请在该工具运行完成后仔细核对所填信息再提交