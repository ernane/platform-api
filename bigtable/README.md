# Bigtable

## Data Modeling - Overview

![bigtable-overview](https://github.com/ernane/platform-api/blob/develop/assets/images/bigtable-overview.png?raw=true)

## Data Modeling - Proposal

![bigtable-table](https://github.com/ernane/platform-api/blob/develop/assets/images/bigtable-table.png?raw=true)

## Hands On

Table, Column family and Instance were pre-provisioned with terraform.

### List tables

```bash
$ cbt ls
platform-api-score
```

### Inspect table **platform-api-score**

```bash
$ cbt ls platform-api-score
Family Name             GC Policy
-----------             ---------
comportamento           <never>
financeiro              <never>
```

### Inserting Records Column_family: financeiro

```bash
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 financeiro:score01=0.0715
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 financeiro:score02=0.0459
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 financeiro:score03=0.0359
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 financeiro:score01=0.0747
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 financeiro:score01=0.0768
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 financeiro:score01=0.0778
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 financeiro:score02=0.0461
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 financeiro:score03=0.0415
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 financeiro:score02=0.0466
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 financeiro:score02=0.0478
```

### Reading Records

```bash
$ cbt read platform-api-score
----------------------------------------
customerid#1001#empresa#banco#202201
  financeiro:score01                       @ 2022/01/30-18:05:55.477000
    "0.0768"
  financeiro:score01                       @ 2022/01/30-18:05:47.142000
    "0.0747"
  financeiro:score01                       @ 2022/01/30-18:05:24.050000
    "0.0715"
  financeiro:score02                       @ 2022/01/30-18:05:32.998000
    "0.0459"
  financeiro:score03                       @ 2022/01/30-18:05:40.202000
    "0.0359"
----------------------------------------
customerid#1001#empresa#banco#202202
  financeiro:score01                       @ 2022/01/30-18:06:04.282000
    "0.0778"
  financeiro:score02                       @ 2022/01/30-18:06:36.347000
    "0.0478"
  financeiro:score02                       @ 2022/01/30-18:06:28.890000
    "0.0466"
  financeiro:score02                       @ 2022/01/30-18:06:14.017000
    "0.0461"
  financeiro:score03                       @ 2022/01/30-18:06:21.051000
    "0.0415"
```

### Inserting Records Column_family: comportamento

```bash
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 comportamento:score01=666
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 comportamento:score02=632
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 comportamento:score03=655
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 comportamento:score01=668
$ cbt set platform-api-score customerid#1001#empresa#banco#202201 comportamento:score01=669
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 comportamento:score01=699
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 comportamento:score02=644
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 comportamento:score03=666
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 comportamento:score02=688
$ cbt set platform-api-score customerid#1001#empresa#banco#202202 comportamento:score02=701
```

### Reading Records

```bash
$ cbt read platform-api-score
----------------------------------------
customerid#1001#empresa#banco#202201
  comportamento:score01                    @ 2022/01/30-18:12:46.504000
    "669"
  comportamento:score01                    @ 2022/01/30-18:12:39.604000
    "668"
  comportamento:score01                    @ 2022/01/30-18:12:11.881000
    "666"
  comportamento:score02                    @ 2022/01/30-18:12:22.359000
    "632"
  comportamento:score03                    @ 2022/01/30-18:12:32.055000
    "655"
  financeiro:score01                       @ 2022/01/30-18:05:55.477000
    "0.0768"
  financeiro:score01                       @ 2022/01/30-18:05:47.142000
    "0.0747"
  financeiro:score01                       @ 2022/01/30-18:05:24.050000
    "0.0715"
  financeiro:score02                       @ 2022/01/30-18:05:32.998000
    "0.0459"
  financeiro:score03                       @ 2022/01/30-18:05:40.202000
    "0.0359"
----------------------------------------
customerid#1001#empresa#banco#202202
  comportamento:score01                    @ 2022/01/30-18:12:53.751000
    "699"
  comportamento:score02                    @ 2022/01/30-18:13:19.639000
    "701"
  comportamento:score02                    @ 2022/01/30-18:13:13.792000
    "688"
  comportamento:score02                    @ 2022/01/30-18:13:01.198000
    "644"
  comportamento:score03                    @ 2022/01/30-18:13:07.296000
    "666"
  financeiro:score01                       @ 2022/01/30-18:06:04.282000
    "0.0778"
  financeiro:score02                       @ 2022/01/30-18:06:36.347000
    "0.0478"
  financeiro:score02                       @ 2022/01/30-18:06:28.890000
    "0.0466"
  financeiro:score02                       @ 2022/01/30-18:06:14.017000
    "0.0461"
  financeiro:score03                       @ 2022/01/30-18:06:21.051000
    "0.0415"
```
