# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_39
settings:
  seed: 0
  time_unit: 4
  mode_cap: 32
  uncertainty: 2.0
  mode_factor_sigma: 0.15
  level_effect: 0.1
  efficiency_bounds:
  - 0.7
  - 1.4
  risk_classes:
  - - 0.5
    - 0.1
    - 0.3
  - - 0.35
    - 0.15
    - 0.6
  - - 0.15
    - 0.2
    - 1.2
  mode_spread_jitter: 0.3
  speed_risk_exponent: 3.0
  department_size: 6
  cross_department_share: 0.1
  dedication_levels:
  - 0.5
  - 0.75
  - 1.0
  dedication_weights:
  - 0.2
  - 0.3
  - 0.5
  safety_skill: true
  constraints: true
  reviewer: true
  extra_workers: true
  liaison: true
  rewire: true
  barred_share: 0.05
  incompatible_pairs_per_worker: 0.1
  review_task_share: 0.15
  quality_share: 0.15
  review_dedication:
  - 0.25
  - 0.5
  extra_share: 0.3
  extra_overhead: 0.1
  extra_floor: 0.75
  liaison_task_share: 0.1
  liaison_dedication:
  - 0.25
  - 0.5
  liaison_upper_spread: 2.0
  rewire_share: 0.3
  long_range_share: 0.3333333333333333
  dedication_variants: 3
  separate_quality_from: 12
  attempts_per_mode: 30
details:
  modes: 130
  tasks_at_cap: 0
  relaxed_constraints: 6
  rewired_edges: 6
  departments: 2
  quality:
  - worker_5
  - worker_8
  safety_skill: 3
  review_tasks: 3
  liaison_tasks: 3
  extra_tasks: 5
  barred_pairs: 8
  incompatible_pairs: 1
  edges: 59
n_workers: 12
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 488
deadline_reference_dedication: full
schema_version: 2
n_dedication_levels: 4
```

# Data

```yaml
workers:
- id: worker_1
- id: worker_2
- id: worker_3
- id: worker_4
- id: worker_5
- id: worker_6
- id: worker_7
- id: worker_8
- id: worker_9
- id: worker_10
- id: worker_11
- id: worker_12
distributions:
  adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5:
    family: tabular
    probabilities:
      0: 1.0
  e4e7b9dd4c356e17e59e07035266877fb4aa946b2bb8e4f613458301ba276497:
    family: pert
    a: 42.335381533422755
    b: 52.91922691677844
    c: 87.48681402173135
  e78f4d3f45ab568eb25780afdf8235b5ebf095360f88eed49a4a7c4ad2350ef7:
    family: pert
    a: 29.109314317273743
    b: 36.38664289659218
    c: 48.331137861954915
  e40a325bdf99d383490db7565f2ba537799ff08cdf25ab0e61b953209a8424af:
    family: pert
    a: 23.128717769165803
    b: 28.910897211457254
    c: 41.73079814102385
  978b78a08618f9e03c59d834d83e8b2cc6dff7bce31a2afac988750a8a1d5596:
    family: pert
    a: 40.91141446461145
    b: 51.1392680807643
    c: 87.3867345062391
  f99253ad755396a2b293c495c6c6c3ad53b1132c5bf8bb131dd42732f933f260:
    family: pert
    a: 23.63045478470262
    b: 29.538068480878277
    c: 51.554661652267534
  6e67e21c41cf7b4f804fa469ffb87a5e21083e4ab06f1cbeb301abca97ec7375:
    family: pert
    a: 22.188296673707583
    b: 36.98049445617931
    c: 136.07640340049642
  c6a929224052ef37d8f5033e0c91f4e3d4a3d074ff2453a44d028f13175fb4f6:
    family: pert
    a: 24.51006665709095
    b: 40.85011109515158
    c: 68.92128368796492
  a195f0b8c68aa3941c687d149bf774a3d13c1bc796f33fb4d544b28cb5dc4ba0:
    family: pert
    a: 16.510833569180797
    b: 27.518055948634665
    c: 74.51985003151789
  54738f64504384186870848a96b4f4fd6ec17ff16428a6b2c370ece8a7a7a07c:
    family: pert
    a: 14.254984877281268
    b: 23.758308128802113
    c: 114.94232584801144
  c3269e81ec8079ebb2f557907df55fa3439ca791eb7d88da9c7c26427e68c341:
    family: pert
    a: 12.475008296049058
    b: 20.791680493415097
    c: 101.36472615562666
  b145aae61c5bc33efef7d18b87ab37708ff71f5176cffdb5e7319903c096aabd:
    family: pert
    a: 16.89868209974556
    b: 28.1644701662426
    c: 92.73345938578777
  ac17a54537e6581fd1d9f77098d1c660789cf9e1ca37a89d20df92545cc32a4f:
    family: pert
    a: 28.93280650661302
    b: 48.221344177688366
    c: 175.61077992890068
  db2fd8de6fe1bdf5321333c51f44aee3d570a3b3830fbf823501fd239f384613:
    family: pert
    a: 15.19168719880171
    b: 25.319478664669518
    c: 185.9648537650136
  60c0131f49bcb10127bef47cdb6400bd19a8a7f80b257dd5e8e49fc7dc638a00:
    family: pert
    a: 23.494642444144613
    b: 39.15773740690769
    c: 133.29026514545654
  a846348b718561eb1575655ede5ba88be7471476a8969a31e7f67a0cd8a735a0:
    family: pert
    a: 15.640763197690484
    b: 26.067938662817475
    c: 116.06629645795995
  721683f0fcb2ea86c861cb251089eec648fe2d98e43707df6148860a17206e66:
    family: pert
    a: 22.59240163145733
    b: 37.65400271909555
    c: 122.67936817315358
  6514c0d69aa1192e45fdf85eb9b4a031f9dda1bf71261ab75acd37a5c51c9d84:
    family: pert
    a: 14.824329621439496
    b: 24.707216035732493
    c: 96.87963337498255
  06fe0564f6a82c6b5252fb0cc9c5a8326f402205f3b6a270523b04ea250aa311:
    family: pert
    a: 17.78649034918195
    b: 29.644150581969917
    c: 97.70238369479864
  fee7d7ed496bd96874b83239ed4695e26368ef4e67ee6d341e9a5235f29d9320:
    family: pert
    a: 15.646853352214281
    b: 26.078088920357136
    c: 113.52104165656414
  8846a28a91876635227b846bc26d93dd39fd6032962182379f3c406dcb1852ac:
    family: pert
    a: 15.319379084944234
    b: 19.149223856180292
    c: 30.56842127248504
  13f7b7c18d4745fc81f1d6f9ff7a81f37b2437dba81ebb2362bbdf6f3da290fd:
    family: pert
    a: 32.193412300783116
    b: 53.65568716797186
    c: 213.9522563814708
  f6cba9975f06ed29731cdf873fd7a6f0097ce95323565f4723a4e136efd0e588:
    family: pert
    a: 102.75011987142099
    b: 171.25019978570165
    c: 299.8565414202657
  e3e0a712fb07f6bf7fbe2661e80602ef458a43f9f62b586ea00037d7346e6337:
    family: pert
    a: 27.791803893563554
    b: 39.70257699080508
    c: 93.49510857655292
  cb24e56d9dbd684e24bd82fb70ae8c2069ad4e7b83c536c5914113fd7827eb4c:
    family: pert
    a: 22.142219987555965
    b: 31.631742839365668
    c: 71.3518204130976
  14d48de10f4896f843d6c4ac926ac16f1edda9814eab21f1d4608fbcb3f6e9cc:
    family: pert
    a: 23.982650396161347
    b: 34.26092913737335
    c: 57.877056139094165
  901a2ceacade974f4649760472214ad566938fdfd22b396b849751d6752da24b:
    family: pert
    a: 18.05821851736724
    b: 25.797455024810343
    c: 144.31331774465016
  c7469ede63a788dd6610a2daafa2f4f778351ebb57ba04be50ef500c2c722282:
    family: pert
    a: 32.42763784824643
    b: 46.325196926066326
    c: 109.13743392840148
  15996406bf8995c45becf332bf3cbd77a9f09ea94342dbf10fd053b0b61e53dd:
    family: pert
    a: 20.655334431870195
    b: 29.507620616957425
    c: 59.058897936005636
  8233332c0cda8846765bbdef42093f5cf6b8efd93fac5d6bcab6656828c7eac4:
    family: pert
    a: 25.05344942874224
    b: 35.790642041060345
    c: 102.64954397158748
  ebff23f2b215c413dda1c051415ee06c489b26ecbc62ff1242b18f6223a8e9ec:
    family: pert
    a: 31.881133703742414
    b: 45.54447671963202
    c: 81.40817439193029
  01efd4bb40ea4abe0daf1526ed8ce0db2ab7cc5c23084064deb71fecaca13b6d:
    family: pert
    a: 31.00495637112097
    b: 44.2927948158871
    c: 72.5557610109116
  e3ed918c307d914764b3b1b4f96b7b40e43dace0f21254b210eef70d4977ef18:
    family: pert
    a: 24.04554741511553
    b: 34.350782021593616
    c: 97.8931150710041
  641f1b89f1d2b157da3e98237656f2242e24bc3b94589435591451faa50bec7c:
    family: pert
    a: 20.101099490332448
    b: 28.715856414760644
    c: 62.092287352937966
  f3a126e2d5aad60f30389bb1070a3a3119800af1a7cb19b9b15be8f845b2f3f4:
    family: pert
    a: 21.824036862195317
    b: 31.177195517421882
    c: 68.15347857632962
  3d2436e50a10e7101227adedcdd281f220acfcf96a1a7d1b86ed5cda5cb4ffc0:
    family: pert
    a: 34.536028754495895
    b: 49.33718393499414
    c: 72.7742686011425
  3a753870234fd879a6021bce2d84344a35eaf92b57cf2f2da9295309d3bd84fb:
    family: pert
    a: 33.247644764158444
    b: 47.49663537736921
    c: 117.14439846976951
  67f89f24a1cf62a181e04ce7007ab32419f0c5d60e19419b5c889c19d6899d7c:
    family: pert
    a: 37.13140013075413
    b: 53.044857329648764
    c: 109.38804194434267
  c819982d948f0fbbe9777fc099955d30988cc45acb98d731d3a13493cd243814:
    family: pert
    a: 37.13941011404822
    b: 53.05630016292603
    c: 79.64579384666463
  6bcb166adf2d2c66b8f5ec0d3d28849addc3ea859fdd45c443d2cb3f8ecba1a7:
    family: pert
    a: 27.747375986653193
    b: 39.639108552361705
    c: 82.48490294682176
  6ad80ae8d974b9232600cf6345ad5a462dcdc0b675816c1787f704ebc7fa1a49:
    family: pert
    a: 48.659618129584416
    b: 60.82452266198052
    c: 83.3749283481097
  c097d9781ffa967f8580c4880bc423d8aeca9b9fc23cd49adc887d824994cae0:
    family: pert
    a: 35.82916478897276
    b: 44.78645598621595
    c: 75.40591293742283
  7871363d5ddf998f564f6de4f745a168db9ea91977b75d24bad9e3b13071e8be:
    family: pert
    a: 38.1167816969759
    b: 47.64597712121987
    c: 67.84197511075756
  ffd478b9c5b5f3644fddc6ac453d8bb1cb9eeac4ef1d9edb373d8056442c547e:
    family: pert
    a: 42.91774749980261
    b: 53.64718437475326
    c: 81.5365155085317
  ea22b5040040f43020e8b69fbfbcf50269698829f8b7b3af158b5a9c75dfdb2b:
    family: pert
    a: 57.39651257269776
    b: 71.7456407158722
    c: 89.85014495096999
  8e6a056f90d85fb777dc0dc777578c81ae1ad0eb355222a4f46c8a124c585dd1:
    family: pert
    a: 38.5057838469579
    b: 48.13222980869737
    c: 78.28094411639371
  b726e7582424a4c0457b3263d2cb39a5403828b69d3bf548765ffabe22c0467a:
    family: pert
    a: 31.466166615519587
    b: 39.33270826939948
    c: 69.93140064568045
  e019bb39f8f69468394af0f316005645956b9a19e54394cc58174733737fbb0b:
    family: pert
    a: 41.654551148576104
    b: 52.06818893572013
    c: 76.0964279711104
  d24f961710610bce04d5ef937b33528d1390839513e220c925e8b64f07aa5fa2:
    family: pert
    a: 33.34772935675719
    b: 41.68466169594649
    c: 70.17445170665556
  a4dfa36c37ce88cec14c6ec11733ba45b7f03d5c443a1031546ba6b8814ea504:
    family: pert
    a: 74.00748645790924
    b: 92.50935807238655
    c: 121.06469827480434
  e7e038888ef6695c9b56eeb61f5649eb1154e4dde5a3275b5d7d39abc65b35eb:
    family: pert
    a: 28.60823091152097
    b: 35.76028863940121
    c: 55.78890879082439
  95a91a27bdeca8ae00aa84e991e59fe0ea6f18cb977040e78d122be6eef65e38:
    family: pert
    a: 35.085366302782234
    b: 43.85670787847779
    c: 67.18999666346971
  dcc1d39142155f02c8658d6bacd21e6f82c35b47454f684fdbf757448086f2d9:
    family: pert
    a: 37.217240227724
    b: 46.521550284655
    c: 74.39833637032552
  673797b144f7d4c8b6afa73f326b429cc9f5e7944a3c05617bd4417224f0bbcc:
    family: pert
    a: 69.4981260410306
    b: 86.87265755128826
    c: 127.64554694852167
  911e9df2af80ca482d04eefeb5b623b8d6b28203cca6ccded9373b2dcc043160:
    family: pert
    a: 33.99286523269677
    b: 42.491081540870965
    c: 66.25617465294846
  47f292d72b4d8ce0a2eac3bea0259f18534e9784ff2c4850530a33ee7b17e43a:
    family: pert
    a: 34.40824234974159
    b: 49.15463192820228
    c: 138.9863007124075
  d64df7605ab23c30e7f623cca4f7e5d9179bc4bf51d6f96f1e50a6a28aeba92c:
    family: pert
    a: 81.10407213214211
    b: 115.86296018877445
    c: 264.56730339014194
  2b07f01f6fb64584160a63e0e69b2ead25f0c6ea95e16243c827ba20190be266:
    family: pert
    a: 12.001448843017704
    b: 17.14492691859672
    c: 39.99961274951667
  0394bbd2f72541d8862a44ea7bcf7bf2430921bd12ea88c6f0aa217f82d36151:
    family: pert
    a: 21.162913041110848
    b: 35.27152173518475
    c: 178.4950937520234
  8bf77439dd9ed81e9a06ba562013de1c539f9c7f2a526405973fffd919dcc14b:
    family: pert
    a: 20.975654937204588
    b: 34.95942489534098
    c: 176.78320087657426
  4b665fbb77c729ebc12f6c027c5bfe0acc0dbe48a94eb983c664d6f94ff6beab:
    family: pert
    a: 31.406247596062165
    b: 52.34374599343695
    c: 170.16486220566966
  d2b07d4970b116525dba08e42463a6965cf19aaf2ecfbecd1f7ad0f77abfbc32:
    family: pert
    a: 26.350051700269184
    b: 32.93756462533648
    c: 52.862237908857104
  d2bac5e6bd29bad1129584eaf656f9da462874ac6dec3da8a991e8598842c37e:
    family: pert
    a: 25.64389640363856
    b: 32.0548705045482
    c: 51.53489678634562
  a301e23236789b6cdac8572db417537e71e85fc6738a814673058ea5010786fa:
    family: pert
    a: 21.5019271527322
    b: 26.87740894091525
    c: 37.91138636065409
  83e30a3b9854862bd7ecac03d3493ed390bb2cc646081feb747b1666075c6284:
    family: pert
    a: 23.50052619954503
    b: 29.375657749431284
    c: 62.36707503908317
  795e646eba0213d9803e4b949b96e8b2f571c5e127ee9fd17afbc559a2011b05:
    family: pert
    a: 35.93884065850061
    b: 44.92355082312576
    c: 66.12245219592589
  6d95c8feffa6024c42a9c3cf27ec4b920afc17ea36c7ce39566798e06ffa1211:
    family: pert
    a: 33.91802724141028
    b: 48.454324630586115
    c: 125.10959730968293
  7a23bf25fc905d53a8b44a4c0695b33acd77d2fff58edd2af79fc3fcaefd07da:
    family: pert
    a: 26.409659521928017
    b: 37.72808503132574
    c: 88.18139799892316
  85df270842b4edd1899f266e363e49e95227350f84b082574e093179d1405570:
    family: pert
    a: 23.460767225822362
    b: 33.51538175117481
    c: 66.0164352660465
  cf0b25ba1fd8ddff0d26e8b74629afa17d69d3eeef8299fab5087eaabf6f5d34:
    family: pert
    a: 47.81994789494709
    b: 59.77493486868386
    c: 76.97546427962993
  d480173b73317eae571e1c7a57ed02fa90d4b73dcc0e48dd4d75562da2f5ee30:
    family: pert
    a: 31.10537862011094
    b: 38.881723275138675
    c: 69.07551207119795
  dc32133d045141397c077ad137f709e303419aa825da9b5eb240e5ead7f46c0e:
    family: pert
    a: 40.35550329445838
    b: 50.44437911807297
    c: 65.87501640715288
  50e980f3c4b6fe052c6efca21f42548ac134459de384806c2ec7e68971326334:
    family: pert
    a: 7.362646494063761
    b: 10.518066420091088
    c: 15.221926632473123
  ed9c401105d7db1cdd6d5a9c2a184e53d9bb043d5cc9837a4f75baea84e62c85:
    family: pert
    a: 10.698951193461575
    b: 15.284215990659392
    c: 39.92519215525796
  9c49e572f74da224e4354ee232e62695bff414f0e72f9dfc0165de56d51e9f3d:
    family: pert
    a: 18.87958569305151
    b: 26.970836704359304
    c: 37.174709050476864
  def281e7725a3f3163a92d773103cc2b69e60e502de3d0c9455dd6ed7c53e25b:
    family: pert
    a: 36.83644742209887
    b: 52.62349631728411
    c: 118.39681899517002
  7225b72d14bd62ef3ed54ffce256cb7506ab2b9fb2d8a27c046c422007c9ed9e:
    family: pert
    a: 38.09145689455898
    b: 54.41636699222712
    c: 155.66040243061835
  09543b5fa5c465dd87de2d5e7a99751bfb6f9809a759f002bef29a634d22b2d6:
    family: pert
    a: 27.323392337346437
    b: 39.033417624780625
    c: 95.8728372633179
  54b89c6a6c01a59b3cbbb8dba570b44adad486c12f7b76b595334387fd584294:
    family: pert
    a: 37.40866047714581
    b: 46.76082559643226
    c: 233.8041279821613
  f9a25063ddda09b3e20488569fb541ffceb4c34a54c4f5efd0e906fa6b6d8235:
    family: pert
    a: 35.372602052229944
    b: 44.215752565287424
    c: 221.07876282643713
  67d7cbc44f3c04a3d6630ff181e6ff81bda1ff3d4fbdd491e72bc3dcfcd0f591:
    family: pert
    a: 37.3524789498345
    b: 46.69059868729312
    c: 233.4529934364656
  18627ef6525c71504e7c39060ff82f8596bdd81360d7104028cc6bbafb8c38ea:
    family: pert
    a: 24.962101000461008
    b: 31.20262625057626
    c: 43.02826482584573
  aafa3cb92126de0e0e53e3c2319f4c2f5a8f4c63bb0d0ae0f4a0fee92abab0fb:
    family: pert
    a: 20.320883940201558
    b: 25.401104925251946
    c: 42.489619254330805
  da75dd46f50c1cc1bec40200148fe4cad2522e715d165a3ebe7d2bd59af95c9b:
    family: pert
    a: 24.20248050931575
    b: 30.25310063664468
    c: 44.437823142774285
  de7ddb819f82fa01f810e31cc9c285fd728698c99f5f37e86961d9e60a15b876:
    family: pert
    a: 7.975593542821136
    b: 11.393705061173053
    c: 58.98842429754729
  3ae1e35dbad4e6158694b261e97b893695b8b2959d61cefd57f62495786d46c4:
    family: pert
    a: 13.514136083765337
    b: 19.30590869109334
    c: 32.53592085095295
  2bcd940ea689914ffa403a9109677954fdd640687f8fdf2c16d2f720d5f1a078:
    family: pert
    a: 11.740192292739776
    b: 16.77170327534254
    c: 30.01822659984654
  b9df88c5c70bcd05b09f9ece45faa964a5b4642b6e80f5f825231c01e3a4561d:
    family: pert
    a: 13.299669049252884
    b: 18.999527213218407
    c: 32.4170698068719
  6f66e08fdeade02c178674a43f98cc1bdf68e00507594363e4e89e8fb338201b:
    family: pert
    a: 9.792516683073433
    b: 13.989309547247762
    c: 39.171934947552984
  881a644d6522a0228874e939f174a7aa58bbe091fd93f6360cc52dde4cba8e83:
    family: pert
    a: 12.542942795445331
    b: 17.918489707779045
    c: 31.1423275461071
  b3ea0daa8b557067a7bad0f58840004490014d30615469c14f4740bb95a35cb9:
    family: pert
    a: 6.048364913855351
    b: 7.560456142319188
    c: 13.947264559345639
  9bb735acd4be9d2b6c28a23b0ce0fb6461551526c6da03c2ca59965f4c629bd8:
    family: pert
    a: 5.857245691180621
    b: 7.321557113975776
    c: 15.259339448008319
  35448eeede1291fc51bc00b529778c4f32de8d40acb48e1094c72dd607d113d0:
    family: pert
    a: 7.738960687706854
    b: 9.673700859633566
    c: 12.462097687966834
  c2a1b17d3082264468e4a117ea6367f1318d7a635545576edde36ea53f0ce2c5:
    family: pert
    a: 4.763127996322054
    b: 7.9385466605367565
    c: 28.501329089350616
  ab9f3ddc4005434c7d7453e3f3fe41f1fdcdd2a6af54b112a91cc50bed1d8655:
    family: pert
    a: 11.403189114675861
    b: 14.253986393344826
    c: 27.98678040018759
  f4370edbeafc41fae706e651dc1dd6fd99f8389417dec7807a0404630dfeeb84:
    family: pert
    a: 13.142306054233671
    b: 16.42788256779209
    c: 25.99871010071941
  a78fbc061703b0adc1692cc20dd4e6229b5b522ffaa190ed94546f2d9a967fc8:
    family: pert
    a: 15.190590046600793
    b: 18.98823755825099
    c: 29.30262628089322
  e254b6a8f60bbe3275b74ca1f7117400e5b587e1e75d41ad1b6f35f930475d0d:
    family: pert
    a: 25.36282437259028
    b: 31.703530465737845
    c: 45.22815385220847
  2327d3a530ca0a5340005c79db00ecb4eeb5c47b130a41b3a10b45f492f871c7:
    family: pert
    a: 20.802428031382355
    b: 26.003035039227942
    c: 42.0369747380226
  cbfe9ecf389b162cc680a9dbf98af765690ecf095c6cede4175926d5366d4156:
    family: pert
    a: 14.264888500541534
    b: 17.831110625676917
    c: 38.89873750471852
  c9ec675f98e2a29378539a07adda47cc4f34bcad5c3795f4be42cf818efa2ac3:
    family: pert
    a: 13.636791603260331
    b: 19.481130861800473
    c: 39.42144310364192
  95fa0332bf766936e3e31a75c9e8ef2c927daebc37a13c01cc35bacd9333eaa0:
    family: pert
    a: 29.66094407015265
    b: 37.07618008769081
    c: 59.86017815508429
  ef9ff31103ff191bbaf8a4508d9e94a25f47d9caf937fba0c534a036f1ffd22c:
    family: pert
    a: 14.808162392466611
    b: 18.510202990583263
    c: 33.67749957740442
  6b1993d2cb4cb257222bf4e4afafed59c9a5d0f7b1dd9af99d1231ab781cab41:
    family: pert
    a: 14.695448108747366
    b: 18.369310135934207
    c: 38.183332648566584
  f59aceef51173f63d5dd36ed100fadce8f845578ddc387e714d886ad7efc57b2:
    family: pert
    a: 6.223272018155943
    b: 7.779090022694929
    c: 13.045402472476903
  c5c906cc28153dfa33657bead7e41455a6927bbb465236db0fa4212d650e76cf:
    family: pert
    a: 5.139377756871568
    b: 6.42422219608946
    c: 14.665217938981483
  a73cf3cc43842ab3d3a60437b8da30bd867ada4c2ff6e65947eac9cc7fa0505a:
    family: pert
    a: 7.535891141539096
    b: 9.41986392692387
    c: 19.161541630953444
  b14c90a666518cdbdce7c7289acd94ea5a4d42acedd68d0eb715127ec5234363:
    family: pert
    a: 8.907090317825643
    b: 11.133862897282054
    c: 17.266845018800534
  cc23618d3fd626212c9d86904879655f6d9d55e4f3dda79f55dc59bed8634eed:
    family: pert
    a: 7.472496803538033
    b: 9.340621004422541
    c: 14.777477618690025
  75c71f7ff726e3a00ae0cba4d1676b09034599bd6aa22d24576663de4ffa37a1:
    family: pert
    a: 6.4866199824958315
    b: 8.10827497811979
    c: 18.906169316631914
  da69d3cb7a9978280fca0f9e9ad2ca67276c6a8640549c747a7b1feb9c778697:
    family: pert
    a: 8.045487911544345
    b: 10.05685988943043
    c: 12.465284011792944
  0919872b7ce2a63eec2c34c3ff1d0b2b9183093894c37656a20cbbcd0068af84:
    family: pert
    a: 9.900444058568526
    b: 12.375555073210657
    c: 17.61266163927912
  05a21dc666cde9262a47b723f6c2f5458540b1d39886290a220d216518b388f1:
    family: pert
    a: 9.29901832530811
    b: 11.623772906635137
    c: 24.607965291152006
  e80ae0168e20bfbed0b9324bc97461a70634774f845c6736e323cea9494b2f2c:
    family: pert
    a: 6.929818740187184
    b: 8.662273425233979
    c: 12.523686453103572
  e0a7fff6228df6966e36e7391066c9ab02ae8ad04f478d910fe3915cdcb79ec0:
    family: pert
    a: 7.718766820756108
    b: 9.648458525945134
    c: 18.12666676329557
  4170c5074dacb7a082fe3fbffdf0463dff17baf8b4f43123d124478b359781fd:
    family: pert
    a: 6.207607166721019
    b: 7.759508958401272
    c: 12.580329025281635
  9f14751fe568334b34a5bac047c3bb97c5660e39e2bbbfda874f5f4f9d85efb4:
    family: pert
    a: 11.529811335238229
    b: 14.412264169047784
    c: 17.7057485117244
  fde46962a835a50b84cc8060c0f55951c24c015f9438d2efef45162ed4ec7cc3:
    family: pert
    a: 7.2656207420057655
    b: 9.082025927507207
    c: 13.166591305648396
  765dfe4a5f91b4e53c71e1975ecb976d65362e4b61c07d9cb4f851003ac081a0:
    family: pert
    a: 11.652796900167552
    b: 14.565996125209438
    c: 72.82998062604719
  2847126570d24dd06343195d80f5d1a8979147e7aada3e3d2b7d7dabd73ec205:
    family: pert
    a: 6.9490314726952604
    b: 8.686289340869076
    c: 43.431446704345376
  57089e4b809f24f9493cda6b436fc0246d48eb32fcf587ebb74edc8e51c4713a:
    family: pert
    a: 7.921642681606809
    b: 9.90205335200851
    c: 49.51026676004255
  5570fab0196889f162936f50b31c105f4bc167e54bdc0e2fc254f7921bce0555:
    family: pert
    a: 7.011200373637646
    b: 10.016000533768066
    c: 17.65582204368406
  ebd7c79ca81827e446591bd13a6c312306208dd192b70765e13d7ec530f901f9:
    family: pert
    a: 17.63999936564913
    b: 22.04999920706141
    c: 110.24999603530705
  35a441b0227ec4638e4f748f61895f1e06797fcb8a79a9ecb7a60d19cb71818e:
    family: pert
    a: 18.64530290262567
    b: 23.306628628282088
    c: 116.53314314141043
  09abc9a1ee202f63a8144f7a81314a59fe184512850fd2dfa2b88647a666b547:
    family: pert
    a: 15.113107657369765
    b: 18.891384571712205
    c: 94.45692285856103
  f4c0cf072e9bbc4c4385e567bf389e426f7d2e9c0ad1165311aac8436968261b:
    family: pert
    a: 16.73500367271939
    b: 20.918754590899237
    c: 104.59377295449619
  509b7bf016700a7a7ccbd714549902a39759e696580d61ecf234dd0eaf3a3a24:
    family: pert
    a: 11.652383003571952
    b: 14.56547875446494
    c: 72.8273937723247
  5a6461be06934c6736247006f09c85953a1e605972fb1223f2c75249141dd17b:
    family: pert
    a: 26.868024870073988
    b: 33.58503108759248
    c: 167.92515543796242
  f72532454cacc658b315823c9c56ece3f9c475e5b8bc4b73061ccb8f281ee20a:
    family: pert
    a: 20.997232917565455
    b: 29.99604702509351
    c: 77.25279562327307
  6d79d483ffc661485aceeffde5fb5f215cfa008d13eb885d69cb5a29b3b59638:
    family: pert
    a: 28.116071046269354
    b: 40.1658157803848
    c: 57.23101430770628
  3bb41699127c53c93d9ad15fee1fb6fc0cffc7f6a6c55f53e4930072046628a6:
    family: pert
    a: 23.888968421708164
    b: 34.12709774529738
    c: 58.57335491189999
tasks:
- id: task_1
  milestone: true
  modes:
  - id: 1
    dedication: {}
    distribution_hash: adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5
- id: task_2
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_11: 0.5
    distribution_hash: e4e7b9dd4c356e17e59e07035266877fb4aa946b2bb8e4f613458301ba276497
  - id: 2
    dedication:
      worker_11: 1.0
    distribution_hash: e78f4d3f45ab568eb25780afdf8235b5ebf095360f88eed49a4a7c4ad2350ef7
  - id: 3
    dedication:
      worker_3: 1.0
    distribution_hash: e40a325bdf99d383490db7565f2ba537799ff08cdf25ab0e61b953209a8424af
  - id: 4
    dedication:
      worker_3: 0.5
    distribution_hash: 978b78a08618f9e03c59d834d83e8b2cc6dff7bce31a2afac988750a8a1d5596
  - id: 5
    dedication:
      worker_10: 0.75
    distribution_hash: f99253ad755396a2b293c495c6c6c3ad53b1132c5bf8bb131dd42732f933f260
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 0.5
      worker_6: 0.75
    distribution_hash: 6e67e21c41cf7b4f804fa469ffb87a5e21083e4ab06f1cbeb301abca97ec7375
  - id: 2
    dedication:
      worker_7: 1.0
      worker_6: 0.75
    distribution_hash: c6a929224052ef37d8f5033e0c91f4e3d4a3d074ff2453a44d028f13175fb4f6
  - id: 3
    dedication:
      worker_7: 1.0
      worker_6: 1.0
    distribution_hash: a195f0b8c68aa3941c687d149bf774a3d13c1bc796f33fb4d544b28cb5dc4ba0
  - id: 4
    dedication:
      worker_2: 0.75
      worker_5: 1.0
    distribution_hash: 54738f64504384186870848a96b4f4fd6ec17ff16428a6b2c370ece8a7a7a07c
  - id: 5
    dedication:
      worker_2: 1.0
      worker_5: 1.0
    distribution_hash: c3269e81ec8079ebb2f557907df55fa3439ca791eb7d88da9c7c26427e68c341
  - id: 6
    dedication:
      worker_7: 1.0
      worker_2: 0.75
    distribution_hash: b145aae61c5bc33efef7d18b87ab37708ff71f5176cffdb5e7319903c096aabd
  - id: 7
    dedication:
      worker_7: 0.5
      worker_2: 0.5
    distribution_hash: ac17a54537e6581fd1d9f77098d1c660789cf9e1ca37a89d20df92545cc32a4f
  - id: 8
    dedication:
      worker_7: 1.0
      worker_5: 0.5
    distribution_hash: db2fd8de6fe1bdf5321333c51f44aee3d570a3b3830fbf823501fd239f384613
  - id: 9
    dedication:
      worker_7: 0.75
      worker_5: 0.75
    distribution_hash: 60c0131f49bcb10127bef47cdb6400bd19a8a7f80b257dd5e8e49fc7dc638a00
  - id: 10
    dedication:
      worker_5: 1.0
      worker_6: 0.75
    distribution_hash: a846348b718561eb1575655ede5ba88be7471476a8969a31e7f67a0cd8a735a0
  - id: 11
    dedication:
      worker_5: 1.0
      worker_6: 0.5
    distribution_hash: 721683f0fcb2ea86c861cb251089eec648fe2d98e43707df6148860a17206e66
  - id: 12
    dedication:
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 6514c0d69aa1192e45fdf85eb9b4a031f9dda1bf71261ab75acd37a5c51c9d84
  - id: 13
    dedication:
      worker_6: 1.0
      worker_2: 0.5
    distribution_hash: 06fe0564f6a82c6b5252fb0cc9c5a8326f402205f3b6a270523b04ea250aa311
  - id: 14
    dedication:
      worker_6: 0.5
      worker_2: 1.0
    distribution_hash: fee7d7ed496bd96874b83239ed4695e26368ef4e67ee6d341e9a5235f29d9320
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_1: 1.0
      worker_10: 1.0
      worker_7: 1.0
    distribution_hash: 8846a28a91876635227b846bc26d93dd39fd6032962182379f3c406dcb1852ac
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
    distribution_hash: 13f7b7c18d4745fc81f1d6f9ff7a81f37b2437dba81ebb2362bbdf6f3da290fd
  - id: 2
    dedication:
      worker_5: 0.25
    distribution_hash: f6cba9975f06ed29731cdf873fd7a6f0097ce95323565f4723a4e136efd0e588
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_10: 0.75
    distribution_hash: e3e0a712fb07f6bf7fbe2661e80602ef458a43f9f62b586ea00037d7346e6337
  - id: 2
    dedication:
      worker_1: 0.75
      worker_10: 1.0
    distribution_hash: cb24e56d9dbd684e24bd82fb70ae8c2069ad4e7b83c536c5914113fd7827eb4c
  - id: 3
    dedication:
      worker_8: 1.0
      worker_4: 0.75
    distribution_hash: 14d48de10f4896f843d6c4ac926ac16f1edda9814eab21f1d4608fbcb3f6e9cc
  - id: 4
    dedication:
      worker_8: 1.0
      worker_4: 0.5
    distribution_hash: 901a2ceacade974f4649760472214ad566938fdfd22b396b849751d6752da24b
  - id: 5
    dedication:
      worker_8: 0.75
      worker_4: 0.5
    distribution_hash: c7469ede63a788dd6610a2daafa2f4f778351ebb57ba04be50ef500c2c722282
  - id: 6
    dedication:
      worker_10: 0.75
      worker_8: 1.0
    distribution_hash: 15996406bf8995c45becf332bf3cbd77a9f09ea94342dbf10fd053b0b61e53dd
  - id: 7
    dedication:
      worker_10: 0.75
      worker_8: 0.5
    distribution_hash: 8233332c0cda8846765bbdef42093f5cf6b8efd93fac5d6bcab6656828c7eac4
  - id: 8
    dedication:
      worker_8: 0.75
      worker_1: 0.75
    distribution_hash: ebff23f2b215c413dda1c051415ee06c489b26ecbc62ff1242b18f6223a8e9ec
  - id: 9
    dedication:
      worker_8: 0.75
      worker_1: 1.0
    distribution_hash: 01efd4bb40ea4abe0daf1526ed8ce0db2ab7cc5c23084064deb71fecaca13b6d
  - id: 10
    dedication:
      worker_8: 1.0
      worker_1: 0.75
    distribution_hash: e3ed918c307d914764b3b1b4f96b7b40e43dace0f21254b210eef70d4977ef18
  - id: 11
    dedication:
      worker_4: 0.75
      worker_10: 1.0
    distribution_hash: 641f1b89f1d2b157da3e98237656f2242e24bc3b94589435591451faa50bec7c
  - id: 12
    dedication:
      worker_4: 1.0
      worker_10: 0.75
    distribution_hash: f3a126e2d5aad60f30389bb1070a3a3119800af1a7cb19b9b15be8f845b2f3f4
  - id: 13
    dedication:
      worker_4: 0.5
      worker_10: 0.75
    distribution_hash: 3d2436e50a10e7101227adedcdd281f220acfcf96a1a7d1b86ed5cda5cb4ffc0
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_10: 1.0
      worker_8: 0.75
    distribution_hash: 3a753870234fd879a6021bce2d84344a35eaf92b57cf2f2da9295309d3bd84fb
  - id: 2
    dedication:
      worker_1: 0.75
      worker_10: 1.0
      worker_8: 1.0
    distribution_hash: 67f89f24a1cf62a181e04ce7007ab32419f0c5d60e19419b5c889c19d6899d7c
  - id: 3
    dedication:
      worker_10: 0.75
      worker_4: 1.0
      worker_8: 1.0
    distribution_hash: c819982d948f0fbbe9777fc099955d30988cc45acb98d731d3a13493cd243814
  - id: 4
    dedication:
      worker_10: 1.0
      worker_4: 1.0
      worker_8: 0.75
    distribution_hash: 6bcb166adf2d2c66b8f5ec0d3d28849addc3ea859fdd45c443d2cb3f8ecba1a7
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_11: 0.75
    distribution_hash: 6ad80ae8d974b9232600cf6345ad5a462dcdc0b675816c1787f704ebc7fa1a49
  - id: 2
    dedication:
      worker_3: 1.0
      worker_11: 0.75
    distribution_hash: c097d9781ffa967f8580c4880bc423d8aeca9b9fc23cd49adc887d824994cae0
  - id: 3
    dedication:
      worker_3: 0.75
      worker_11: 1.0
    distribution_hash: 7871363d5ddf998f564f6de4f745a168db9ea91977b75d24bad9e3b13071e8be
  - id: 4
    dedication:
      worker_3: 0.75
      worker_10: 0.75
    distribution_hash: ffd478b9c5b5f3644fddc6ac453d8bb1cb9eeac4ef1d9edb373d8056442c547e
  - id: 5
    dedication:
      worker_3: 0.5
      worker_10: 0.75
    distribution_hash: ea22b5040040f43020e8b69fbfbcf50269698829f8b7b3af158b5a9c75dfdb2b
  - id: 6
    dedication:
      worker_3: 1.0
      worker_9: 0.75
    distribution_hash: 8e6a056f90d85fb777dc0dc777578c81ae1ad0eb355222a4f46c8a124c585dd1
  - id: 7
    dedication:
      worker_3: 1.0
      worker_9: 1.0
    distribution_hash: b726e7582424a4c0457b3263d2cb39a5403828b69d3bf548765ffabe22c0467a
  - id: 8
    dedication:
      worker_3: 0.75
      worker_9: 1.0
    distribution_hash: e019bb39f8f69468394af0f316005645956b9a19e54394cc58174733737fbb0b
  - id: 9
    dedication:
      worker_11: 1.0
      worker_9: 1.0
    distribution_hash: d24f961710610bce04d5ef937b33528d1390839513e220c925e8b64f07aa5fa2
  - id: 10
    dedication:
      worker_11: 0.5
      worker_9: 0.5
    distribution_hash: a4dfa36c37ce88cec14c6ec11733ba45b7f03d5c443a1031546ba6b8814ea504
  - id: 11
    dedication:
      worker_11: 1.0
      worker_10: 1.0
    distribution_hash: e7e038888ef6695c9b56eeb61f5649eb1154e4dde5a3275b5d7d39abc65b35eb
  - id: 12
    dedication:
      worker_11: 1.0
      worker_10: 0.75
    distribution_hash: 95a91a27bdeca8ae00aa84e991e59fe0ea6f18cb977040e78d122be6eef65e38
  - id: 13
    dedication:
      worker_11: 0.5
      worker_10: 1.0
    distribution_hash: dcc1d39142155f02c8658d6bacd21e6f82c35b47454f684fdbf757448086f2d9
  - id: 14
    dedication:
      worker_10: 0.5
      worker_9: 0.5
    distribution_hash: 673797b144f7d4c8b6afa73f326b429cc9f5e7944a3c05617bd4417224f0bbcc
  - id: 15
    dedication:
      worker_10: 1.0
      worker_9: 1.0
    distribution_hash: 911e9df2af80ca482d04eefeb5b623b8d6b28203cca6ccded9373b2dcc043160
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 0.5
    distribution_hash: 47f292d72b4d8ce0a2eac3bea0259f18534e9784ff2c4850530a33ee7b17e43a
  - id: 2
    dedication:
      worker_8: 0.25
    distribution_hash: d64df7605ab23c30e7f623cca4f7e5d9179bc4bf51d6f96f1e50a6a28aeba92c
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_6: 1.0
      worker_10: 1.0
    distribution_hash: 2b07f01f6fb64584160a63e0e69b2ead25f0c6ea95e16243c827ba20190be266
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 1.0
      worker_11: 1.0
      worker_9: 0.5
      worker_3: 0.75
    distribution_hash: 0394bbd2f72541d8862a44ea7bcf7bf2430921bd12ea88c6f0aa217f82d36151
  - id: 2
    dedication:
      worker_10: 0.75
      worker_11: 0.5
      worker_9: 0.75
      worker_3: 1.0
    distribution_hash: 8bf77439dd9ed81e9a06ba562013de1c539f9c7f2a526405973fffd919dcc14b
  - id: 3
    dedication:
      worker_10: 0.75
      worker_11: 0.5
      worker_9: 0.5
      worker_3: 1.0
    distribution_hash: 4b665fbb77c729ebc12f6c027c5bfe0acc0dbe48a94eb983c664d6f94ff6beab
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 0.75
      worker_1: 0.75
    distribution_hash: d2b07d4970b116525dba08e42463a6965cf19aaf2ecfbecd1f7ad0f77abfbc32
  - id: 2
    dedication:
      worker_10: 1.0
      worker_1: 0.5
    distribution_hash: d2bac5e6bd29bad1129584eaf656f9da462874ac6dec3da8a991e8598842c37e
  - id: 3
    dedication:
      worker_10: 1.0
      worker_4: 1.0
    distribution_hash: a301e23236789b6cdac8572db417537e71e85fc6738a814673058ea5010786fa
  - id: 4
    dedication:
      worker_10: 0.5
      worker_4: 1.0
    distribution_hash: 83e30a3b9854862bd7ecac03d3493ed390bb2cc646081feb747b1666075c6284
  - id: 5
    dedication:
      worker_10: 0.5
      worker_4: 0.75
    distribution_hash: 795e646eba0213d9803e4b949b96e8b2f571c5e127ee9fd17afbc559a2011b05
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 0.5
      worker_11: 0.75
      worker_3: 0.5
      worker_9: 0.5
    distribution_hash: 6d95c8feffa6024c42a9c3cf27ec4b920afc17ea36c7ce39566798e06ffa1211
  - id: 2
    dedication:
      worker_10: 1.0
      worker_11: 1.0
      worker_3: 1.0
      worker_9: 0.5
    distribution_hash: 7a23bf25fc905d53a8b44a4c0695b33acd77d2fff58edd2af79fc3fcaefd07da
  - id: 3
    dedication:
      worker_10: 1.0
      worker_11: 1.0
      worker_3: 0.75
      worker_9: 1.0
    distribution_hash: 85df270842b4edd1899f266e363e49e95227350f84b082574e093179d1405570
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_5: 1.0
      worker_6: 0.5
      worker_2: 0.5
    distribution_hash: cf0b25ba1fd8ddff0d26e8b74629afa17d69d3eeef8299fab5087eaabf6f5d34
  - id: 2
    dedication:
      worker_7: 0.5
      worker_5: 0.75
      worker_6: 1.0
      worker_2: 1.0
    distribution_hash: d480173b73317eae571e1c7a57ed02fa90d4b73dcc0e48dd4d75562da2f5ee30
  - id: 3
    dedication:
      worker_7: 1.0
      worker_5: 1.0
      worker_6: 0.5
      worker_2: 1.0
    distribution_hash: dc32133d045141397c077ad137f709e303419aa825da9b5eb240e5ead7f46c0e
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 0.5
    distribution_hash: 50e980f3c4b6fe052c6efca21f42548ac134459de384806c2ec7e68971326334
  - id: 2
    dedication:
      worker_8: 0.25
    distribution_hash: ed9c401105d7db1cdd6d5a9c2a184e53d9bb043d5cc9837a4f75baea84e62c85
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_10: 1.0
      worker_6: 1.0
      worker_7: 1.0
    distribution_hash: 9c49e572f74da224e4354ee232e62695bff414f0e72f9dfc0165de56d51e9f3d
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 0.5
      worker_4: 1.0
      worker_10: 0.75
      worker_1: 1.0
    distribution_hash: def281e7725a3f3163a92d773103cc2b69e60e502de3d0c9455dd6ed7c53e25b
  - id: 2
    dedication:
      worker_8: 0.75
      worker_4: 0.5
      worker_10: 0.5
      worker_1: 1.0
    distribution_hash: 7225b72d14bd62ef3ed54ffce256cb7506ab2b9fb2d8a27c046c422007c9ed9e
  - id: 3
    dedication:
      worker_8: 1.0
      worker_4: 1.0
      worker_10: 0.75
      worker_1: 0.75
    distribution_hash: 09543b5fa5c465dd87de2d5e7a99751bfb6f9809a759f002bef29a634d22b2d6
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_11: 1.0
      worker_9: 0.75
      worker_10: 0.5
      worker_3: 1.0
      worker_12: 0.25
    distribution_hash: 54b89c6a6c01a59b3cbbb8dba570b44adad486c12f7b76b595334387fd584294
  - id: 2
    dedication:
      worker_11: 0.75
      worker_9: 0.5
      worker_10: 0.5
      worker_3: 0.75
      worker_12: 0.25
    distribution_hash: f9a25063ddda09b3e20488569fb541ffceb4c34a54c4f5efd0e906fa6b6d8235
  - id: 3
    dedication:
      worker_11: 0.5
      worker_9: 0.5
      worker_10: 0.75
      worker_3: 1.0
      worker_12: 0.25
    distribution_hash: 67d7cbc44f3c04a3d6630ff181e6ff81bda1ff3d4fbdd491e72bc3dcfcd0f591
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 1.0
      worker_6: 1.0
    distribution_hash: 18627ef6525c71504e7c39060ff82f8596bdd81360d7104028cc6bbafb8c38ea
  - id: 2
    dedication:
      worker_6: 1.0
      worker_7: 1.0
    distribution_hash: aafa3cb92126de0e0e53e3c2319f4c2f5a8f4c63bb0d0ae0f4a0fee92abab0fb
  - id: 3
    dedication:
      worker_10: 1.0
      worker_7: 1.0
    distribution_hash: da75dd46f50c1cc1bec40200148fe4cad2522e715d165a3ebe7d2bd59af95c9b
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_10: 1.0
    distribution_hash: de7ddb819f82fa01f810e31cc9c285fd728698c99f5f37e86961d9e60a15b876
  - id: 2
    dedication:
      worker_10: 1.0
      worker_7: 1.0
    distribution_hash: 3ae1e35dbad4e6158694b261e97b893695b8b2959d61cefd57f62495786d46c4
  - id: 3
    dedication:
      worker_6: 1.0
      worker_7: 1.0
    distribution_hash: 2bcd940ea689914ffa403a9109677954fdd640687f8fdf2c16d2f720d5f1a078
  - id: 4
    dedication:
      worker_1: 1.0
      worker_7: 1.0
    distribution_hash: b9df88c5c70bcd05b09f9ece45faa964a5b4642b6e80f5f825231c01e3a4561d
  - id: 5
    dedication:
      worker_1: 1.0
      worker_10: 1.0
    distribution_hash: 6f66e08fdeade02c178674a43f98cc1bdf68e00507594363e4e89e8fb338201b
  - id: 6
    dedication:
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: 881a644d6522a0228874e939f174a7aa58bbe091fd93f6360cc52dde4cba8e83
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 0.75
      worker_4: 1.0
      worker_8: 1.0
      worker_1: 0.75
    distribution_hash: b3ea0daa8b557067a7bad0f58840004490014d30615469c14f4740bb95a35cb9
  - id: 2
    dedication:
      worker_10: 0.75
      worker_4: 1.0
      worker_8: 1.0
      worker_1: 0.5
    distribution_hash: 9bb735acd4be9d2b6c28a23b0ce0fb6461551526c6da03c2ca59965f4c629bd8
  - id: 3
    dedication:
      worker_10: 1.0
      worker_4: 0.75
      worker_8: 1.0
      worker_1: 1.0
    distribution_hash: 35448eeede1291fc51bc00b529778c4f32de8d40acb48e1094c72dd607d113d0
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_6: 1.0
      worker_1: 1.0
      worker_10: 1.0
    distribution_hash: c2a1b17d3082264468e4a117ea6367f1318d7a635545576edde36ea53f0ce2c5
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_8: 1.0
      worker_10: 1.0
    distribution_hash: ab9f3ddc4005434c7d7453e3f3fe41f1fdcdd2a6af54b112a91cc50bed1d8655
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_8: 0.75
      worker_10: 1.0
    distribution_hash: f4370edbeafc41fae706e651dc1dd6fd99f8389417dec7807a0404630dfeeb84
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_8: 1.0
      worker_10: 0.75
    distribution_hash: a78fbc061703b0adc1692cc20dd4e6229b5b522ffaa190ed94546f2d9a967fc8
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 0.5
      worker_11: 0.75
      worker_9: 0.75
      worker_3: 1.0
    distribution_hash: e254b6a8f60bbe3275b74ca1f7117400e5b587e1e75d41ad1b6f35f930475d0d
  - id: 2
    dedication:
      worker_10: 0.75
      worker_11: 1.0
      worker_9: 0.75
      worker_3: 0.5
    distribution_hash: 2327d3a530ca0a5340005c79db00ecb4eeb5c47b130a41b3a10b45f492f871c7
  - id: 3
    dedication:
      worker_10: 1.0
      worker_11: 1.0
      worker_9: 0.75
      worker_3: 0.75
    distribution_hash: cbfe9ecf389b162cc680a9dbf98af765690ecf095c6cede4175926d5366d4156
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 1.0
      worker_6: 1.0
      worker_1: 1.0
      worker_7: 1.0
    distribution_hash: c9ec675f98e2a29378539a07adda47cc4f34bcad5c3795f4be42cf818efa2ac3
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
      worker_6: 0.5
      worker_2: 0.5
      worker_7: 0.5
    distribution_hash: 95fa0332bf766936e3e31a75c9e8ef2c927daebc37a13c01cc35bacd9333eaa0
  - id: 2
    dedication:
      worker_5: 1.0
      worker_6: 1.0
      worker_2: 1.0
      worker_7: 0.75
    distribution_hash: ef9ff31103ff191bbaf8a4508d9e94a25f47d9caf937fba0c534a036f1ffd22c
  - id: 3
    dedication:
      worker_5: 1.0
      worker_6: 0.75
      worker_2: 1.0
      worker_7: 1.0
    distribution_hash: 6b1993d2cb4cb257222bf4e4afafed59c9a5d0f7b1dd9af99d1231ab781cab41
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_11: 1.0
      worker_9: 1.0
    distribution_hash: f59aceef51173f63d5dd36ed100fadce8f845578ddc387e714d886ad7efc57b2
  - id: 2
    dedication:
      worker_3: 1.0
      worker_11: 1.0
    distribution_hash: c5c906cc28153dfa33657bead7e41455a6927bbb465236db0fa4212d650e76cf
  - id: 3
    dedication:
      worker_3: 1.0
      worker_11: 0.5
    distribution_hash: a73cf3cc43842ab3d3a60437b8da30bd867ada4c2ff6e65947eac9cc7fa0505a
  - id: 4
    dedication:
      worker_9: 1.0
      worker_10: 0.5
    distribution_hash: b14c90a666518cdbdce7c7289acd94ea5a4d42acedd68d0eb715127ec5234363
  - id: 5
    dedication:
      worker_9: 0.5
      worker_10: 1.0
    distribution_hash: cc23618d3fd626212c9d86904879655f6d9d55e4f3dda79f55dc59bed8634eed
  - id: 6
    dedication:
      worker_9: 0.75
      worker_10: 0.75
    distribution_hash: 75c71f7ff726e3a00ae0cba4d1676b09034599bd6aa22d24576663de4ffa37a1
  - id: 7
    dedication:
      worker_3: 1.0
      worker_9: 1.0
    distribution_hash: da69d3cb7a9978280fca0f9e9ad2ca67276c6a8640549c747a7b1feb9c778697
  - id: 8
    dedication:
      worker_3: 1.0
      worker_9: 0.5
    distribution_hash: 0919872b7ce2a63eec2c34c3ff1d0b2b9183093894c37656a20cbbcd0068af84
  - id: 9
    dedication:
      worker_10: 0.5
      worker_11: 0.5
    distribution_hash: 05a21dc666cde9262a47b723f6c2f5458540b1d39886290a220d216518b388f1
  - id: 10
    dedication:
      worker_10: 0.75
      worker_11: 1.0
    distribution_hash: e80ae0168e20bfbed0b9324bc97461a70634774f845c6736e323cea9494b2f2c
  - id: 11
    dedication:
      worker_10: 0.75
      worker_11: 0.75
    distribution_hash: e0a7fff6228df6966e36e7391066c9ab02ae8ad04f478d910fe3915cdcb79ec0
  - id: 12
    dedication:
      worker_3: 1.0
      worker_10: 1.0
    distribution_hash: 4170c5074dacb7a082fe3fbffdf0463dff17baf8b4f43123d124478b359781fd
  - id: 13
    dedication:
      worker_3: 1.0
      worker_10: 0.5
    distribution_hash: 9f14751fe568334b34a5bac047c3bb97c5660e39e2bbbfda874f5f4f9d85efb4
  - id: 14
    dedication:
      worker_3: 0.75
      worker_10: 1.0
    distribution_hash: fde46962a835a50b84cc8060c0f55951c24c015f9438d2efef45162ed4ec7cc3
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_8: 0.75
      worker_1: 0.5
      worker_10: 1.0
      worker_12: 0.25
    distribution_hash: 765dfe4a5f91b4e53c71e1975ecb976d65362e4b61c07d9cb4f851003ac081a0
  - id: 2
    dedication:
      worker_4: 1.0
      worker_8: 0.75
      worker_1: 0.75
      worker_10: 0.75
      worker_12: 0.25
    distribution_hash: 2847126570d24dd06343195d80f5d1a8979147e7aada3e3d2b7d7dabd73ec205
  - id: 3
    dedication:
      worker_4: 0.5
      worker_8: 0.5
      worker_1: 1.0
      worker_10: 1.0
      worker_12: 0.5
    distribution_hash: 57089e4b809f24f9493cda6b436fc0246d48eb32fcf587ebb74edc8e51c4713a
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_10: 1.0
      worker_1: 1.0
      worker_6: 1.0
      worker_7: 1.0
    distribution_hash: 5570fab0196889f162936f50b31c105f4bc167e54bdc0e2fc254f7921bce0555
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_10: 1.0
      worker_8: 0.75
      worker_12: 0.25
    distribution_hash: ebd7c79ca81827e446591bd13a6c312306208dd192b70765e13d7ec530f901f9
  - id: 2
    dedication:
      worker_1: 0.5
      worker_10: 0.5
      worker_8: 1.0
      worker_12: 0.5
    distribution_hash: 35a441b0227ec4638e4f748f61895f1e06797fcb8a79a9ecb7a60d19cb71818e
  - id: 3
    dedication:
      worker_1: 0.5
      worker_10: 1.0
      worker_8: 1.0
      worker_12: 0.5
    distribution_hash: 09abc9a1ee202f63a8144f7a81314a59fe184512850fd2dfa2b88647a666b547
  - id: 4
    dedication:
      worker_8: 0.75
      worker_10: 1.0
      worker_4: 1.0
      worker_12: 0.5
    distribution_hash: f4c0cf072e9bbc4c4385e567bf389e426f7d2e9c0ad1165311aac8436968261b
  - id: 5
    dedication:
      worker_8: 1.0
      worker_10: 1.0
      worker_4: 1.0
      worker_12: 0.25
    distribution_hash: 509b7bf016700a7a7ccbd714549902a39759e696580d61ecf234dd0eaf3a3a24
  - id: 6
    dedication:
      worker_8: 1.0
      worker_10: 0.5
      worker_4: 0.5
      worker_12: 0.5
    distribution_hash: 5a6461be06934c6736247006f09c85953a1e605972fb1223f2c75249141dd17b
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_7: 0.5
      worker_5: 0.75
    distribution_hash: f72532454cacc658b315823c9c56ece3f9c475e5b8bc4b73061ccb8f281ee20a
  - id: 2
    dedication:
      worker_2: 1.0
      worker_7: 0.75
      worker_5: 0.5
    distribution_hash: 6d79d483ffc661485aceeffde5fb5f215cfa008d13eb885d69cb5a29b3b59638
  - id: 3
    dedication:
      worker_2: 0.75
      worker_7: 1.0
      worker_5: 0.75
    distribution_hash: 3bb41699127c53c93d9ad15fee1fb6fc0cffc7f6a6c55f53e4930072046628a6
- id: task_32
  milestone: true
  modes:
  - id: 1
    dedication: {}
    distribution_hash: adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5
tpg_edges:
- - task_1
  - task_2
- - task_1
  - task_3
- - task_1
  - task_4
- - task_1
  - task_5
- - task_1
  - task_6
- - task_1
  - task_8
- - task_1
  - task_9
- - task_1
  - task_10
- - task_1
  - task_12
- - task_1
  - task_22
- - task_1
  - task_23
- - task_1
  - task_24
- - task_1
  - task_25
- - task_1
  - task_26
- - task_1
  - task_27
- - task_1
  - task_28
- - task_1
  - task_29
- - task_1
  - task_30
- - task_1
  - task_31
- - task_2
  - task_7
- - task_2
  - task_13
- - task_2
  - task_16
- - task_2
  - task_20
- - task_2
  - task_21
- - task_3
  - task_13
- - task_3
  - task_16
- - task_3
  - task_19
- - task_4
  - task_11
- - task_4
  - task_15
- - task_5
  - task_15
- - task_6
  - task_18
- - task_7
  - task_11
- - task_8
  - task_17
- - task_9
  - task_13
- - task_10
  - task_14
- - task_23
  - task_16
- - task_5
  - task_13
- - task_4
  - task_14
- - task_4
  - task_7
- - task_28
  - task_17
- - task_11
  - task_32
- - task_12
  - task_32
- - task_13
  - task_32
- - task_14
  - task_32
- - task_15
  - task_32
- - task_16
  - task_32
- - task_17
  - task_32
- - task_18
  - task_32
- - task_19
  - task_32
- - task_20
  - task_32
- - task_21
  - task_32
- - task_22
  - task_32
- - task_24
  - task_32
- - task_25
  - task_32
- - task_26
  - task_32
- - task_27
  - task_32
- - task_29
  - task_32
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 610
validation:
  project_key: c664918ee169469476483cbc168b7b72baf5f61658b49302af1b195b781a81b0
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 73 days; worst-case serial bound: 1904 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
