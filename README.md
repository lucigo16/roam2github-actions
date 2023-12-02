# roam2github-actions

2023-12-2 新增：

1. 支持配置多个Roam Graph
    - `ROAM_GRAPH` 的value值，Roam Graph的名称。对于多个Graph，添加单独的行（或用逗号分隔）
2. github actions 改为 1天自动备份一次

备注：推荐创建的仓库名为 `roam_backup`，否则需要修改脚本中的`cd /home/runner/work/roam_backup/roam_backup` 路径

参考：https://github.com/JimmyLv/roam2github-actions

---

How to start: https://github.com/everruler12/roam2github

> Added image backup script. 增加了图片备份脚本

![image](https://user-images.githubusercontent.com/4997466/112108490-37857280-8beb-11eb-8743-9544594a69b2.png)
