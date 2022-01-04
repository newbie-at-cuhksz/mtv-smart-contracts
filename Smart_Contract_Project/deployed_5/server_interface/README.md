# 如何使用接口

1. 将`server_interface`中的：

   * `deployed_XXX_server_interface`文件夹
   * `deployed_XXX_server_interface.py`

   拷贝到服务器`FISCO-BCOS-python-sdk`根目录下

   ```bash
   $ pwd
   /root/FISCO-BCOS-python-sdk
   $ ls
   bcos_solc.py               codegen.py              demo_mtv_get.py                 eth_account        hexbytes               README.md         tests
   bin                        console.py              demo_mtv_transaction.py         eth_hash           init_env.sh            README_SOLC.md    tools
   CHANGELOG                  console_utils           demo_perf.py                    eth_keys           LICENSE                release_note.txt  tox.ini
   Changelog.md               contracts               demo_transaction.py             eth_rlp            linux_python_setup.md  requirements.txt  utils
   ci                         CONTRIBUTING.md         deployed_4_server_interface     eth_typing         MANIFEST.in            rlp
   client                     cython_tassl_wrap       deployed_4_server_interface.py  eth_utils          __pycache__            sample
   client_config.py           demo_event_callback.py  Dockerfile                      event_callback.py  pytest.ini             setup.py
   client_config.py.template  demo_get.py             eth_abi                         gmssl              py_vesion_checker.py   solcjs
   ```

   

2. ```
   ################################################
   ########### Interface: LguToken.sol ############
   
   ...
   
   ################################################
   ```

   这部分代码为接口，只需要阅读function上方的注释

   

3. 运行

   ```bash
   python3.7 deployed_4_server_interface.py
   ```

   