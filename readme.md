# 环境配置

- 使用3.8以上的python版本，建议使用虚拟环境 

- 安装依赖包

  - `pip install -r requirements.txt` 

- 填写配置文件）

  - 修改配置文件可以选择需要用的翻译服务，具体参数可见[translators开源网址](https://github.com/UlionTse/translators)

```
[translation_service]
# 选择翻译服务
# 可选项：google, baidu, bing, youdao等
service = baidu
# 自动检测语言
from_lang = auto
# 目标语言，如中文zh,英文en,俄语ru
to_lang = zh

```

# 使用说明

执行main程序，选择pdf文件后，程序会自动创建两个文件夹，分别保存逐页提取的文本以及翻译后的文本。



