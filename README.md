# fortirss

Fortinet機器の脆弱性情報を取得して下記を出力します。

* タイトル
* 掲載日
* 詳細URL
* 対象バージョン

### サンプル

```python
> python .\fortirss.py

    --- No. 1 ---
    Titile: XSS vulnerability in FortiClientEMS
    Date: Mon, 23 Sep 2019 07:13:10 +0000
    Link: https://fortiguard.com/psirt/FG-IR-19-072
    Affected Ver:
        Affected Products
        FortiClientEMS version 6.2.0 and below.



    --- No. 2 ---
    Titile: IPMI network LAN interface failover operational risk
    Date: Tue, 17 Sep 2019 09:54:20 +0000
    Link: https://fortiguard.com/psirt/FG-IR-17-195
    Affected Ver:
        Affected Products

        FortiAnalyzer models:

        FAZ-400E, FAZ-1000E, FAZ-2000E, FAZ-3000F, FAZ-3500F, FAZ-3700F

        FortiManager models:

        FMG-300E, FMG-400E, FMG-2000E, FMG-3000F

        Other models and Fortinet products are confirmed to not have a default Failover setting.




    --- No. 3 ---
    Titile: HTTP/2 Multiple DoS Attacks (VU#605641)
    Date: Tue, 03 Sep 2019 14:41:11 +0000
    Link: https://fortiguard.com/psirt/FG-IR-19-225
    Affected Ver:
        Affected Products

        The following products have been confirmed to NOT be vulnerable to any of the above:

        FortiOS
        FortiAP
        FortiSwitch
        FortiAnalyzer
        FortiWeb
        FortiManager
        FortiMail


...


```


