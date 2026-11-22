# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_63
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
  modes: 142
  tasks_at_cap: 0
  relaxed_constraints: 7
  rewired_edges: 7
  departments: 1
  quality:
  - worker_3
  safety_skill: 2
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 4
  barred_pairs: 8
  incompatible_pairs: 1
  edges: 59
n_workers: 7
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 509
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
distributions:
  adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5:
    family: tabular
    probabilities:
      0: 1.0
  a991782053ccfc9187a2b502f2eda82e16e8bf22ab82600d0b53746004e26e54:
    family: pert
    a: 21.02911000236238
    b: 26.286387502952973
    c: 61.08128812192932
  2b00aca9d8f3c2c3ad040cbfe2bc103f1ad9b67760e9541a12dc2911fd780d70:
    family: pert
    a: 35.23951948939375
    b: 44.04939936174219
    c: 71.53937941001782
  c818adbb89442e8cb3858d55ca93dec7d1271e27561255d6477961a9c1f9cfd5:
    family: pert
    a: 52.39886325073002
    b: 65.49857906341252
    c: 95.12597138845533
  ad278ad94338a90d65c0f17579747e7e03407314755144fbf66ab4848033ba3c:
    family: pert
    a: 79.79437939439737
    b: 99.7429742429967
    c: 132.94778912354502
  7eb2c04242d14b3aac8a511f74762d77bbd3509bf32abacb3435f9e16f700124:
    family: pert
    a: 40.716756231312424
    b: 50.89594528914053
    c: 82.06957527903134
  3d6bde306adfc6245f93a980b2fa4bf2102f5eae45b03a6552a3250eda5af088:
    family: pert
    a: 26.13124060717594
    b: 32.66405075896992
    c: 62.36512760740485
  8aaa15c3f07a7b6671ebf586cba3a725f1e12ea57e53f32f43418f9343a298ad:
    family: pert
    a: 49.98962012086714
    b: 62.48702515108392
    c: 91.33734593674632
  e7340bca8e91a76d11895f4dc3d4a2fbddc44bd7f1f71cf2ce43584fba3743f7:
    family: pert
    a: 25.696630865770683
    b: 32.12078858221335
    c: 51.80862169966422
  535a15f5c1c6d7a362c6ea1029676f6684ecade4b3a95fec81d373cf9131f976:
    family: pert
    a: 8.628913699652886
    b: 12.327019570932695
    c: 19.267170522032387
  d71b0babd51f9d02175a72a508412de0e0611a81ad02154edcad27faf479e4f2:
    family: pert
    a: 6.286386733423333
    b: 8.980552476319048
    c: 29.622488293882018
  0b36fa87d0925137e1dd661142a5a1f3c44227532ccd23aa118c6c0ce6be3c5c:
    family: pert
    a: 6.605936090696085
    b: 9.437051558137265
    c: 22.207644403103824
  5c122c05094431899e264d73f583af24e7043685f60dca8b18f1987904d63d50:
    family: pert
    a: 5.645598313651322
    b: 8.065140448073318
    c: 18.794015320268585
  1d68497706565a8620e88f400a5331e5840d018b0992a4be8e22ea1075df0158:
    family: pert
    a: 3.6001795918867687
    b: 5.143113702695384
    c: 24.028464967585407
  3986093033eb85a692c86dbe9b087a466b1291bcd84b9302facc8d327c8e63e7:
    family: pert
    a: 31.597281277299356
    b: 45.138973253284796
    c: 225.694866266424
  af588117b02c97ba3c720c1b8a6e80437c8edafd56d726d269f4468c13cd4f80:
    family: pert
    a: 29.89008711475634
    b: 42.700124449651916
    c: 213.5006222482596
  3c65f29ff63928688909939d988bb115ac8a693d739f3521aa57ff5efadc0f9a:
    family: pert
    a: 34.01500000264579
    b: 48.59285714663685
    c: 242.96428573318425
  8c1170ee81c31586e700d9959a7a93b6c83a32ef9a464c11f6fced1d18b560b5:
    family: pert
    a: 12.654039767336549
    b: 15.817549709170684
    c: 26.281320419888157
  58fe8d0316b8e9713382e05fe8a5b018f241a9474a855fa622173f71bf06f3c4:
    family: pert
    a: 14.564749721424105
    b: 18.20593715178013
    c: 26.475001810415872
  bde9951e73db534147425531008af874918f0c20a55515d1ca7a8fde3c746a39:
    family: pert
    a: 11.882562961354344
    b: 14.853203701692928
    c: 26.385536971057878
  eea540cccdc0ebe007bdb14cefb39085294b5216a5c342ae6f63ed07e219f6dc:
    family: pert
    a: 15.108854412027998
    b: 18.886068015034997
    c: 30.14740785977752
  a6271d28a0d4612b9aa103714259a0a31d8f19ef7c790af5cfac6feb767f77f0:
    family: pert
    a: 11.228346295885293
    b: 14.035432869856615
    c: 21.706531228356717
  20ef1835a53ec7de431ce040f3614e627a41ff7c1ab68c216333135e6a400df5:
    family: pert
    a: 16.376059301427045
    b: 20.470074126783803
    c: 25.430986426899313
  f1a0fcbca75dceab501f68ff197da79a636ffe2a1242ffbce73ae1ae1f2618fb:
    family: pert
    a: 11.499662381913247
    b: 14.374577977391558
    c: 26.976040839564575
  e605b86de1995abf8a20187fdfd3d8a4844a781a9f4a10a31642310a9da8338d:
    family: pert
    a: 20.37506928768252
    b: 25.468836609603148
    c: 39.77763883530789
  518e83edf9330db20e9f4b4428c3f2247b2c525f4ea33b1c249e17960c370a5b:
    family: pert
    a: 12.587053626557
    b: 15.733817033196248
    c: 23.131669300094504
  b77357ce3ed142dafab9dee549390a6f1c863ea1e819d796824488a56daed4e8:
    family: pert
    a: 16.96584039682094
    b: 21.207300496026175
    c: 55.08453379349238
  831ee02a6454b28618427e56d4013e2040ed32388d8900fc1081c369e7dc49a9:
    family: pert
    a: 20.62519044552221
    b: 25.781488056902763
    c: 32.990728919582686
  31cc154ea107440b5dc34357e7fe44a3f78f9c8b77dab3923230a8794e40eef6:
    family: pert
    a: 20.119555837392838
    b: 25.149444796741047
    c: 41.16968287968084
  bc298e29e7becdacb3a25bc47c0bed25608e3991e4e598b75a84068e814b4ffa:
    family: pert
    a: 23.628889593004065
    b: 29.53611199125508
    c: 49.3117687284575
  22fb3bc32f935c65cf9f7ab10af7b1ca17db8b14107a1d55f0d7a617c3743209:
    family: pert
    a: 17.245355100392143
    b: 21.556693875490176
    c: 26.79031257700897
  c0541d16c2b8f7997fb95389fa2e78de13c8bb803ce5f796feb8df437687566d:
    family: pert
    a: 8.135867768992961
    b: 13.559779614988269
    c: 61.10524680641722
  c8325dda26170eed27e93b68d3da6e9637ada09e7d1f9d834bee3a79b4a552d4:
    family: pert
    a: 4.478305853070566
    b: 7.463843088450944
    c: 74.51338980420599
  489316aabf1e0f973a7c7a7baca7e6c20f9db98432051ab32c3861cdafa50841:
    family: pert
    a: 5.991917582222514
    b: 9.98652930370419
    c: 41.779829637324475
  de9933c5508ee976a46babc98694ebc97ad06bf763977151c48695903cae7609:
    family: pert
    a: 11.208680935173136
    b: 18.681134891955228
    c: 37.501171763942274
  6c0b9b6fbc799a73502b171b132bd6a452227e479ed630a085e555441f0bcff9:
    family: pert
    a: 5.6302454813098155
    b: 9.383742468849693
    c: 59.9823281963187
  3b5753afcf209e952aec3b6e1ca4ac804695c63f68bd06db334af179e0c2e41b:
    family: pert
    a: 12.708473194270862
    b: 21.180788657118104
    c: 37.278022056252276
  df52b710a6bd2f8ff849d0fe5292a59d89eb9e147c516df3db9b1a2a715f2e0b:
    family: pert
    a: 11.454029070154226
    b: 19.090048450257044
    c: 80.18741986501755
  8436a3d8c080134a46806ed3a99736a5947d9a6cab8998313e762ecc1d10a8ce:
    family: pert
    a: 21.986969793894417
    b: 36.644949656490695
    c: 104.7010890505245
  451ccf263b50d3f0411152c1205a23bbb59ff521037bdbe0181616b24ae46c2f:
    family: pert
    a: 10.670807521330014
    b: 17.78467920221669
    c: 46.55587751294939
  3d2048040dac17050aa1d11a8cf5c793eaed32ac97936e7745ef0d0be0128c8a:
    family: pert
    a: 20.0248814699404
    b: 28.606973528486286
    c: 44.276893526405864
  36dfd0a7cff73afd2089ac6ba7f364f6bb4a71e3cda66771d8dcacd2723326b1:
    family: pert
    a: 24.1289076624602
    b: 34.46986808922886
    c: 69.78532750317149
  b8fdb79ca25381df318753861f6b650dc7396a5974190589630fc883d9183c0a:
    family: pert
    a: 16.412535026890577
    b: 23.44647860984368
    c: 68.57952096095069
  b6af7a49869db5630eeca1c05eaad517f5ce744091abf0c7ba7efab91ab227c1:
    family: pert
    a: 9.28493096595257
    b: 13.26418709421796
    c: 81.33331185026802
  abbe3e55198497a35b7872aebc3d7da1e34e015ba71d88c3caa79c33607b6424:
    family: pert
    a: 7.25196919898296
    b: 9.0649614987287
    c: 14.00028872761171
  640bcbdeba539c190b0d71029cfb447d00e5ab1f121b3cbf5c7f30415344e2fc:
    family: pert
    a: 6.952340349513401
    b: 8.69042543689175
    c: 20.157650980475392
  0695563dc77ebdbc6d3e89044dd300e6aa8cee83e36e7715db505261fa8e0010:
    family: pert
    a: 7.846597997652257
    b: 9.80824749706532
    c: 15.4548018080375
  1b460bcb4aae0beb628435f9fe9e3aa155827e18eaba40f5e2debf6c80745302:
    family: pert
    a: 103.92096361139318
    b: 148.4585194448474
    c: 279.5177899040852
  34d31b2c9c2af76ab49f1b1f19c503e859388f3fa5305c9b2f4119896185ad6c:
    family: pert
    a: 40.19511873289047
    b: 57.421598189843536
    c: 178.63306173588296
  92aa028a3b6d8c2311aa1bac66b39f78d416bc28d91e0c10f755181b3c55384e:
    family: pert
    a: 10.573129014707867
    b: 15.104470021011238
    c: 38.668549084634414
  09c59caa2436ebfa1dd30d32b643d7734396ca965e0b3c75821b781bce8888e6:
    family: pert
    a: 13.718622193470825
    b: 19.598031704958323
    c: 36.60884999166921
  665802553101b4d9b8b967b89cccf36c628aa14ad37e2b39809defe176c7a5ac:
    family: pert
    a: 12.965522860558563
    b: 18.522175515083664
    c: 36.330683983022745
  2221728f186b7b24199d60941bf1e1bf4f3e78c3a30c9dae97d8c57d294aa8ce:
    family: pert
    a: 39.79479325939308
    b: 49.74349157424135
    c: 70.94801606795076
  7e85eaf0a7a574d7269c6307ec3b6d8a993a518ddaf9aad3a208adca17ed8c82:
    family: pert
    a: 49.007976618529526
    b: 61.2599707731619
    c: 92.54243628161412
  603ca2ea8cbd07e90fcf449c5c15d9809b6ea20998d99164be06b4fe67f412ec:
    family: pert
    a: 29.270613569259666
    b: 36.58826696157458
    c: 76.15356898095148
  e195e474550aca9d2e20ead576a4f3bd9bce0763b9041d407180375f68f7b42e:
    family: pert
    a: 41.36911191313944
    b: 51.7113898914243
    c: 82.1153686757862
  9f53301e59e13480593e862efb9cb4691eb1f7b75e5f8f8f59c5b97e2624fa70:
    family: pert
    a: 51.63218915328671
    b: 64.54023644160839
    c: 117.60228305580623
  67c343967ed7ed70a132740df8523a6d61eb49ed54f4569ac4973e47b3d1ca52:
    family: pert
    a: 34.473586906682456
    b: 43.09198363335307
    c: 66.2342085911797
  ec5c7b6e7baa2f482ace70fd56d0f838872d0e7e69fe876abe9e18f46a07c417:
    family: pert
    a: 60.37167072940439
    b: 75.46458841175549
    c: 93.75249586376636
  181093984dd1ebfb3ab981bf633b71214aa76ba709ae4013af2098a927f5724e:
    family: pert
    a: 32.83697191371132
    b: 41.04621489213915
    c: 72.25521888947836
  bdf4d3821b76ffb0bcd493ec7f4570dcd4e024e0dd81bfb798e3f895ec7daef9:
    family: pert
    a: 54.43483834170698
    b: 68.04354792713372
    c: 110.18139059999166
  a89cc0c6be4db784c428a12f30fea360ce7f5055fa1c2eed4ff1902d28d9458e:
    family: pert
    a: 32.036259145418704
    b: 40.045323931773375
    c: 66.2572318922507
  bdafb529ed4d6463e5fc3359a6a85b5f390220d209f60e0ac2853af44e3a729e:
    family: pert
    a: 39.577684087091086
    b: 49.47210510886386
    c: 64.76344981869397
  9546b231baf1e15b7f6e9def33cdf40582ae43276e02fd8b99ed98c7c847a62e:
    family: pert
    a: 50.69346404339304
    b: 63.3668300542413
    c: 94.03316124274517
  0bd4d5c19b573f85769c46f1c70504cf82cef65e8f0272e62aa3d37b41f4a8c6:
    family: pert
    a: 39.66539647128598
    b: 49.58174558910747
    c: 62.441287182193456
  d2a6b6b92bf0d3fd2594623abeebcfa41be664483cdd200d7cff6e889ff4472a:
    family: pert
    a: 17.964902428188324
    b: 25.66414632598332
    c: 110.68746062617396
  76368e7350b58c1d485df1de935d81c950f2c9a445827f9ae54df9fef93552e1:
    family: pert
    a: 19.72433091392589
    b: 28.177615591322702
    c: 64.27152392440298
  2478eb6d9a36d15a9962b8ca20de173cae36c93020000d0c738e4f01360e11a1:
    family: pert
    a: 28.889706135220518
    b: 41.271008764600744
    c: 131.0155618386968
  a959a2bc7b548508dfcf7a3576cc603a319033572c18e8719411b002bce79ce2:
    family: pert
    a: 28.47966515748727
    b: 40.68523593926753
    c: 82.2508977091773
  1b317638c9586419ff6ee0731dbcc1572eb822eabed33e655f82e7024819bfff:
    family: pert
    a: 20.190972375588714
    b: 28.844246250841024
    c: 77.70541092681758
  989a825eb336acb86b9e50aa4c031d5407226a4abc62ace05abeca64207bf445:
    family: pert
    a: 22.490401997818537
    b: 28.11300249727317
    c: 58.598264772721
  589298a02e61d448e2cc35bdac9306c637a651a193d328fddc40c06e25c7831e:
    family: pert
    a: 28.794164638614305
    b: 35.99270579826788
    c: 59.4085225083794
  2bcd8320513e70f7e7101c54a2b7c685b2e327cb89e69840bba3225f19e36619:
    family: pert
    a: 34.40467518449152
    b: 43.0058439806144
    c: 60.493944001336075
  7e38beec35538d5a30137fce1c7098c22bfeaaf0e84b334c0f3daaf91ec53cc6:
    family: pert
    a: 18.31890631295083
    b: 22.898632891188537
    c: 64.70717350781122
  17f4fcb208ed1bc7e57648e695bff374775cfa67d0398100ededde0f6d7a3306:
    family: pert
    a: 26.187285228172932
    b: 32.73410653521616
    c: 53.26294055200864
  4feb19d21f525ca827e29761b2cc985010424096a31f21ccc051dfc1cf39aa79:
    family: pert
    a: 24.866668427654904
    b: 31.08333553456863
    c: 50.53895802263941
  9f9ae789bd8d3bd3a170499b7951812ce96918a01b6de10c57b505585d27c9e9:
    family: pert
    a: 27.209466921909986
    b: 34.01183365238748
    c: 58.710382516466254
  23a84f23c4107862c0e9b858b6a7beca615fc8b66f712a590684129ab2403dd9:
    family: pert
    a: 18.714002220839422
    b: 26.73428888691346
    c: 43.97318459026326
  4a4872a0f1b99be03ccf39f0766939f6fca125aa9d8435f794d3421076185cd6:
    family: pert
    a: 13.525752132529753
    b: 19.322503046471077
    c: 42.84889417299353
  2f44d2aaf33998bd69a42991ff365f24089f078f66467dafb00312b053b389e7:
    family: pert
    a: 16.89774619863602
    b: 24.139637426622887
    c: 50.469954898619164
  5095f5a43d24e5c523b9f577f60973e8c8147478d809ef1535fa26ce632753f2:
    family: pert
    a: 17.35851512069068
    b: 24.79787874384383
    c: 46.821035674301584
  5e1f2d2298d870cb764f65a1cad75053dafa03e8959fe2497d738361a44cc3c5:
    family: pert
    a: 11.391555565183607
    b: 16.273650807405154
    c: 49.37924420515914
  26c6ae689a21bb3f9c33c5189e53a66822bc58efbe89efa174cd9f8f578e2db6:
    family: pert
    a: 13.317405985973304
    b: 19.024865694247577
    c: 39.50297563538448
  89ef6c6ea62dcb5f282fdb94fe38eb6c1a8f66dbb755c17df073144beb1df31b:
    family: pert
    a: 8.849513632278372
    b: 12.642162331826245
    c: 38.39247819781554
  fe73442a2191367add6bddb1de993fed90daf45578a39d95e429f19b6ae6d9c6:
    family: pert
    a: 17.588485169575144
    b: 25.12640738510735
    c: 43.80089948876199
  0d27cdf5e63e015c3a1b463fc25d6a817ef5d8ee00da00966d2c39c24a1472ad:
    family: pert
    a: 11.539344824187884
    b: 16.484778320268408
    c: 46.47415726391299
  da226b9548ef15b32fac0cd0c2b643ccb0546ba878c3742e0ef9c934fc6652ff:
    family: pert
    a: 11.284669844141161
    b: 16.12095692020166
    c: 39.20478201111078
  4290533e87ab027355ae91ae70b756d4e0c02bbd23d3fcd9a2964a187f5341dd:
    family: pert
    a: 12.995756306385386
    b: 18.565366151979124
    c: 36.345710995691555
  0c686777bce10b3b12cbc55a9af010beaa3563e1224446d2dacec9f26d45ca2c:
    family: pert
    a: 17.659708950419446
    b: 22.074636188024307
    c: 40.96652004218502
  ec179654bf5b0787ed7b7507df6670bf73034cf1193c48cb1059406889eaf921:
    family: pert
    a: 24.915131741972257
    b: 31.143914677465318
    c: 109.1013014000025
  71f5c5ac5181306853dae33d6a67151a456ba971640bd7c540e759b5f49bb2ea:
    family: pert
    a: 10.329978403126583
    b: 12.912473003908229
    c: 20.11933273781514
  2461e55a8bb4373aa369822adf7412fd09218ec827d93ca10c22cafc51fdaf84:
    family: pert
    a: 6.205227204053973
    b: 8.864610291505675
    c: 19.650034600454052
  65f86034b34a99c39e2e7da70843006073f4ce89e694a2d654bcb26ea58d4139:
    family: pert
    a: 8.369411699572172
    b: 11.956302427960248
    c: 19.889567665118552
  6fb990537b1cffd52f40b31e8f3a7af2149cd8ee85e76840e3d46341f32642be:
    family: pert
    a: 6.109269885995563
    b: 8.72752840856509
    c: 19.174286952256956
  34bd1dfc0c1e9b7d89131af40d7272c537bf55571a5e376253cfd11cdf6f83b6:
    family: pert
    a: 29.12796308524832
    b: 36.4099538565604
    c: 61.425151865678316
  c7fc88c1888bc1614228423044a100ef8de92b2b94efe64eb27737273096715d:
    family: pert
    a: 27.526066197327353
    b: 34.40758274665919
    c: 65.97943413641757
  9fc4e6ac3a31c13f1a295e6020ce0184d5307632737c85873b033439db6d257a:
    family: pert
    a: 32.198510218862495
    b: 40.248137773578115
    c: 69.88382794259063
  fc2df9f80534b689ab21e1f1094d9416c5de79e7078748518192cd16bde5cd02:
    family: pert
    a: 3.4477048442324056
    b: 4.925292634617723
    c: 8.754259165723532
  5da29dfe00f352d8e940d266274b8503f52f124841298c754cc8b84124dbe1c4:
    family: pert
    a: 18.18061057412868
    b: 22.725763217660848
    c: 113.62881608830423
  ce1985d492fde09135958df7cde18508e48485f0f19cb194471d1235b2049453:
    family: pert
    a: 21.188401320080736
    b: 26.485501650100918
    c: 132.4275082505046
  e4995853b7895de2f0ed33bbb963c7a544d10fc2024408e1876cf8c2d0bbc6a6:
    family: pert
    a: 17.356463097522717
    b: 28.927438495871193
    c: 97.20176365762542
  5e8ae0dadd014d745606637b99ddbd5bbe2b97264c7a7542ec3d0e8acab18a53:
    family: pert
    a: 16.40612468672928
    b: 27.3435411445488
    c: 71.64671230082821
  d0123c788a9fa677b8618d213c0f2e9d3371d3333fa81562086fba86e58f9d29:
    family: pert
    a: 18.998742588861422
    b: 31.664570981435702
    c: 86.74231321305797
  6b3eacdecb937bc18fee0239d8185806d20f9df6e8409767e6a80e64efa0fdc7:
    family: pert
    a: 20.23951340981681
    b: 33.73252234969468
    c: 88.05537742104421
  b01d6f200e9bedbf305e57be1c822f7c39a8afffe402f0ad77738ff3b95009e0:
    family: pert
    a: 14.027875108262096
    b: 23.379791847103494
    c: 103.5052505355957
  9cecc4b9cd694fb7aa6b0c49745c3933dbb3e74819528a0cac77d693186cc169:
    family: pert
    a: 13.608465471764147
    b: 22.68077578627358
    c: 94.15510294732427
  fec8fa2d15999f42543fd6a80b3e315770cda8539ff92e997979b8747060698c:
    family: pert
    a: 8.677797206238026
    b: 12.39685315176861
    c: 35.66207504152268
  f441069a7f9f105312bb507c595182b6604e992c44a706e7babd51c8bd550bdc:
    family: pert
    a: 9.517371562779235
    b: 13.596245089684622
    c: 21.76942694902996
  12f2671166fe12b0f2705c8f5a87ba7cb736653ecd37ed2581b6fcbd767c04ad:
    family: pert
    a: 7.45667352767815
    b: 10.65239075382593
    c: 31.232420320784158
  56282cf299e760c5161f3797de5b728078a442042197f1d0bf11a3063376746a:
    family: pert
    a: 13.921006782678411
    b: 19.887152546683446
    c: 54.43469192950856
  8331d21c22e4c3a31ab5ba0d220f42688ce5629bec2b6be8c70f2558627dc654:
    family: pert
    a: 14.932755146440158
    b: 21.33250735205737
    c: 33.24653834690486
  c168e56e4664305e5a2744136bbeeabb9b486ce7db4641f331fddd31c428f19b:
    family: pert
    a: 10.773467440160902
    b: 15.390667771658432
    c: 30.822664108608752
  68d1d7c1331815c6b21455e13c4c6f42947798f29b0bccd73fd7d041c3713426:
    family: pert
    a: 7.548462845168615
    b: 10.783518350240879
    c: 33.01569096304943
  e0b49f9bc68f61ac4080703afdc68457561f34bff63a73e2aa1b88e84fe72c90:
    family: pert
    a: 9.361676991476937
    b: 13.373824273538483
    c: 30.657396977742323
  a199a1f63d9d8f76a6bbb1803e53599b1b65522bf39e7c12d3d83ffec1e9fd65:
    family: pert
    a: 11.316432516016707
    b: 16.166332165738154
    c: 38.646877259087425
  b35afb763f53d331e31c5aa83373ebec9d67b6c49921757f313bb0a092a85fd9:
    family: pert
    a: 7.3101047927229805
    b: 10.443006846747116
    c: 34.58455832521175
  a2263ea3e4664b329e72f7cb0d3749bdadcd038ff52dfaf277ce254b177acccf:
    family: pert
    a: 17.27676338447452
    b: 24.68109054924932
    c: 51.95569820807848
  04dc9738c6e3c071d74843af8e62b1d9eac5796ca41536183d92a1d6a3750b44:
    family: pert
    a: 7.255357913263792
    b: 10.364797018948275
    c: 40.154111418266844
  39e8d997003a051cee2d345024f3281e99b4e3d7424a65d45db929f63aee8b30:
    family: pert
    a: 14.563561249991402
    b: 20.805087499987717
    c: 34.64810924872125
  d6480edeb832f35b23b56350344abaccd9814567afafc25b95c522f4ff487bc3:
    family: pert
    a: 9.832961373301337
    b: 14.047087676144768
    c: 29.366210050562017
  089cf4e76d8313d91f1bf21d0fa95674417321be0a328ae758c194d82413bdfc:
    family: pert
    a: 7.8113923162500125
    b: 11.159131880357162
    c: 28.459547092591933
  51428319f5c68584661c97f384645ea867defad8effd05f5c1d017932f66e5db:
    family: pert
    a: 12.45618644217565
    b: 17.79455206025093
    c: 39.96675714483302
  52e3b9f5be65a8a76efbbb659642856ead6a6135bb67e67bbd5d8a92ef529a06:
    family: pert
    a: 39.335133028116736
    b: 49.16891628514592
    c: 80.21357798432085
  563d27325bfdae5e09cd507151dd88a3885852f64f36f0c3896660eb26ab096a:
    family: pert
    a: 31.54795635725535
    b: 39.43494544656919
    c: 70.15048350395189
  349a20c4625e53090c51066074a773f8aa8fa25eecbae92a69527fca6666a8f0:
    family: pert
    a: 31.1882898793327
    b: 38.985362349165875
    c: 77.64391448061005
  17514bfabaa1b7b77332129c7102de76456301bd6bac35e288f59ffcee7a6204:
    family: pert
    a: 16.099117621136052
    b: 20.123897026420064
    c: 46.03730123884975
  6ec9ae7cb9dae877a2cb6a0814af74fde1a3f541f927654527d7ff1742df1510:
    family: pert
    a: 26.670298664498844
    b: 33.33787333062355
    c: 49.672165544989205
  af176e26f4bccd1d037c87cced8b0b93ced223d88d506fc713f538c53b09b98c:
    family: pert
    a: 29.97821176539648
    b: 37.4727647067456
    c: 51.40327071469002
  ee81e6df51ca8613a5d2a274a393ab74dbe1846ea45c81a51b35ace7d40a0a03:
    family: pert
    a: 39.89010481729383
    b: 49.86263102161728
    c: 68.77435805683585
  108978490219585c87ea2f45f9765cbaf048c15793441c34fd7c2bebe3faf31b:
    family: pert
    a: 14.723417292145294
    b: 18.404271615181617
    c: 92.02135807590808
  257c997e3fe84538fe14af7f40b91dc9eeeaa1d4958ea6e2fba3e8b698b1533d:
    family: pert
    a: 13.819542704591278
    b: 17.274428380739096
    c: 86.37214190369548
  adce76500edf67c29946a3a8cc23a36b67e908ce075a020374ddb4253454bde1:
    family: pert
    a: 13.915192363624946
    b: 17.39399045453118
    c: 86.9699522726559
  a0155d4d4396c291c4bcf1da05935bcc3d90112e94270aa732ec6d6bcdb5e7d3:
    family: pert
    a: 17.927098531270747
    b: 22.408873164088433
    c: 112.04436582044217
  f85188223545522beb756ec9821be585f4b5d8e61ae89c2b8c7859f31e2e1a4a:
    family: pert
    a: 12.602736595966293
    b: 15.753420744957866
    c: 78.76710372478934
  7bc92e5c8d4cea76e527ffe2d67635d3b96da5154d5b88d664c7a48539e455eb:
    family: pert
    a: 14.768323826599048
    b: 18.46040478324881
    c: 92.30202391624404
  0414f1607f5f019b958317fc3feea27124293e17032501b331cca19af908c604:
    family: pert
    a: 21.659149078517054
    b: 27.073936348146315
    c: 135.36968174073158
  476883742f8fb8cfd2d54bfc28444f4b2962d3b2a40d322e112c4b782ef3189d:
    family: pert
    a: 18.695038990070206
    b: 23.368798737587756
    c: 116.84399368793878
  987950f156f2d58580daff4a8e65584b580b36f2f0537b4674ddc6c0092f73d7:
    family: pert
    a: 13.583849310844094
    b: 16.979811638555116
    c: 84.89905819277558
  dda0acc12652737fd648842d465989a727b9c0725a6e6344337b80562089f48f:
    family: pert
    a: 17.37524158896708
    b: 21.719051986208846
    c: 108.59525993104424
  eb13e8d538d3a962803e94438d47c57d196c3da21d6fde21a66f9c04d9750a81:
    family: pert
    a: 19.125665706206586
    b: 23.907082132758234
    c: 119.53541066379117
  449e1e6d57afb3e8c0a27384bbd28ca600d2cbe4ba179ac8717aa582b668af2c:
    family: pert
    a: 13.494131434833774
    b: 16.867664293542216
    c: 84.33832146771108
  f70e2e59f958c59c25bb371157b097bebcfdba6c1fa744d21c0dd185b3b4f848:
    family: pert
    a: 9.89450874961003
    b: 12.368135937012536
    c: 19.175556514330374
  a121cd14617c36ef3a69b08ccd4f4451210fb304a9f6a162b483fa445a59ad4c:
    family: pert
    a: 10.020220118044547
    b: 16.700366863407577
    c: 56.8848039296095
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
      worker_1: 1.0
    distribution_hash: a991782053ccfc9187a2b502f2eda82e16e8bf22ab82600d0b53746004e26e54
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: 2b00aca9d8f3c2c3ad040cbfe2bc103f1ad9b67760e9541a12dc2911fd780d70
  - id: 3
    dedication:
      worker_6: 0.75
    distribution_hash: c818adbb89442e8cb3858d55ca93dec7d1271e27561255d6477961a9c1f9cfd5
  - id: 4
    dedication:
      worker_6: 0.5
    distribution_hash: ad278ad94338a90d65c0f17579747e7e03407314755144fbf66ab4848033ba3c
  - id: 5
    dedication:
      worker_2: 0.75
    distribution_hash: 7eb2c04242d14b3aac8a511f74762d77bbd3509bf32abacb3435f9e16f700124
  - id: 6
    dedication:
      worker_2: 1.0
    distribution_hash: 3d6bde306adfc6245f93a980b2fa4bf2102f5eae45b03a6552a3250eda5af088
  - id: 7
    dedication:
      worker_5: 0.5
    distribution_hash: 8aaa15c3f07a7b6671ebf586cba3a725f1e12ea57e53f32f43418f9343a298ad
  - id: 8
    dedication:
      worker_5: 1.0
    distribution_hash: e7340bca8e91a76d11895f4dc3d4a2fbddc44bd7f1f71cf2ce43584fba3743f7
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_6: 0.5
      worker_2: 1.0
    distribution_hash: 535a15f5c1c6d7a362c6ea1029676f6684ecade4b3a95fec81d373cf9131f976
  - id: 2
    dedication:
      worker_1: 0.5
      worker_6: 1.0
      worker_2: 1.0
    distribution_hash: d71b0babd51f9d02175a72a508412de0e0611a81ad02154edcad27faf479e4f2
  - id: 3
    dedication:
      worker_1: 0.75
      worker_6: 1.0
      worker_2: 1.0
    distribution_hash: 0b36fa87d0925137e1dd661142a5a1f3c44227532ccd23aa118c6c0ce6be3c5c
  - id: 4
    dedication:
      worker_5: 0.75
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 5c122c05094431899e264d73f583af24e7043685f60dca8b18f1987904d63d50
  - id: 5
    dedication:
      worker_5: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 1d68497706565a8620e88f400a5331e5840d018b0992a4be8e22ea1075df0158
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_4: 0.75
      worker_1: 1.0
      worker_3: 0.75
      worker_7: 0.5
    distribution_hash: 3986093033eb85a692c86dbe9b087a466b1291bcd84b9302facc8d327c8e63e7
  - id: 2
    dedication:
      worker_6: 1.0
      worker_4: 0.75
      worker_1: 0.75
      worker_3: 1.0
      worker_7: 0.25
    distribution_hash: af588117b02c97ba3c720c1b8a6e80437c8edafd56d726d269f4468c13cd4f80
  - id: 3
    dedication:
      worker_6: 1.0
      worker_4: 0.75
      worker_1: 0.75
      worker_3: 0.75
      worker_7: 0.5
    distribution_hash: 3c65f29ff63928688909939d988bb115ac8a693d739f3521aa57ff5efadc0f9a
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_5: 1.0
    distribution_hash: 8c1170ee81c31586e700d9959a7a93b6c83a32ef9a464c11f6fced1d18b560b5
  - id: 2
    dedication:
      worker_1: 0.75
      worker_5: 0.75
    distribution_hash: 58fe8d0316b8e9713382e05fe8a5b018f241a9474a855fa622173f71bf06f3c4
  - id: 3
    dedication:
      worker_1: 1.0
      worker_5: 0.75
    distribution_hash: bde9951e73db534147425531008af874918f0c20a55515d1ca7a8fde3c746a39
  - id: 4
    dedication:
      worker_2: 0.75
      worker_1: 0.75
    distribution_hash: eea540cccdc0ebe007bdb14cefb39085294b5216a5c342ae6f63ed07e219f6dc
  - id: 5
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: a6271d28a0d4612b9aa103714259a0a31d8f19ef7c790af5cfac6feb767f77f0
  - id: 6
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: 20ef1835a53ec7de431ce040f3614e627a41ff7c1ab68c216333135e6a400df5
  - id: 7
    dedication:
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: f1a0fcbca75dceab501f68ff197da79a636ffe2a1242ffbce73ae1ae1f2618fb
  - id: 8
    dedication:
      worker_6: 0.5
      worker_1: 0.75
    distribution_hash: e605b86de1995abf8a20187fdfd3d8a4844a781a9f4a10a31642310a9da8338d
  - id: 9
    dedication:
      worker_5: 1.0
      worker_2: 0.75
    distribution_hash: 518e83edf9330db20e9f4b4428c3f2247b2c525f4ea33b1c249e17960c370a5b
  - id: 10
    dedication:
      worker_5: 0.5
      worker_2: 0.5
    distribution_hash: b77357ce3ed142dafab9dee549390a6f1c863ea1e819d796824488a56daed4e8
  - id: 11
    dedication:
      worker_5: 0.5
      worker_2: 1.0
    distribution_hash: 831ee02a6454b28618427e56d4013e2040ed32388d8900fc1081c369e7dc49a9
  - id: 12
    dedication:
      worker_2: 0.75
      worker_6: 0.5
    distribution_hash: 31cc154ea107440b5dc34357e7fe44a3f78f9c8b77dab3923230a8794e40eef6
  - id: 13
    dedication:
      worker_2: 0.5
      worker_6: 0.5
    distribution_hash: bc298e29e7becdacb3a25bc47c0bed25608e3991e4e598b75a84068e814b4ffa
  - id: 14
    dedication:
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 22fb3bc32f935c65cf9f7ab10af7b1ca17db8b14107a1d55f0d7a617c3743209
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
    distribution_hash: c0541d16c2b8f7997fb95389fa2e78de13c8bb803ce5f796feb8df437687566d
  - id: 2
    dedication:
      worker_1: 1.0
    distribution_hash: c8325dda26170eed27e93b68d3da6e9637ada09e7d1f9d834bee3a79b4a552d4
  - id: 3
    dedication:
      worker_5: 1.0
    distribution_hash: 489316aabf1e0f973a7c7a7baca7e6c20f9db98432051ab32c3861cdafa50841
  - id: 4
    dedication:
      worker_5: 0.75
    distribution_hash: de9933c5508ee976a46babc98694ebc97ad06bf763977151c48695903cae7609
  - id: 5
    dedication:
      worker_2: 1.0
    distribution_hash: 6c0b9b6fbc799a73502b171b132bd6a452227e479ed630a085e555441f0bcff9
  - id: 6
    dedication:
      worker_2: 0.75
    distribution_hash: 3b5753afcf209e952aec3b6e1ca4ac804695c63f68bd06db334af179e0c2e41b
  - id: 7
    dedication:
      worker_6: 0.75
    distribution_hash: df52b710a6bd2f8ff849d0fe5292a59d89eb9e147c516df3db9b1a2a715f2e0b
  - id: 8
    dedication:
      worker_6: 0.5
    distribution_hash: 8436a3d8c080134a46806ed3a99736a5947d9a6cab8998313e762ecc1d10a8ce
  - id: 9
    dedication:
      worker_6: 1.0
    distribution_hash: 451ccf263b50d3f0411152c1205a23bbb59ff521037bdbe0181616b24ae46c2f
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
    distribution_hash: 3d2048040dac17050aa1d11a8cf5c793eaed32ac97936e7745ef0d0be0128c8a
  - id: 2
    dedication:
      worker_1: 1.0
    distribution_hash: 36dfd0a7cff73afd2089ac6ba7f364f6bb4a71e3cda66771d8dcacd2723326b1
  - id: 3
    dedication:
      worker_4: 1.0
    distribution_hash: b8fdb79ca25381df318753861f6b650dc7396a5974190589630fc883d9183c0a
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: b6af7a49869db5630eeca1c05eaad517f5ce744091abf0c7ba7efab91ab227c1
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_5: 1.0
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: abbe3e55198497a35b7872aebc3d7da1e34e015ba71d88c3caa79c33607b6424
  - id: 2
    dedication:
      worker_2: 1.0
      worker_5: 0.75
      worker_6: 0.5
      worker_1: 0.5
    distribution_hash: 640bcbdeba539c190b0d71029cfb447d00e5ab1f121b3cbf5c7f30415344e2fc
  - id: 3
    dedication:
      worker_2: 1.0
      worker_5: 0.5
      worker_6: 0.5
      worker_1: 1.0
    distribution_hash: 0695563dc77ebdbc6d3e89044dd300e6aa8cee83e36e7715db505261fa8e0010
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 1b460bcb4aae0beb628435f9fe9e3aa155827e18eaba40f5e2debf6c80745302
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 34d31b2c9c2af76ab49f1b1f19c503e859388f3fa5305c9b2f4119896185ad6c
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_6: 0.75
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 92aa028a3b6d8c2311aa1bac66b39f78d416bc28d91e0c10f755181b3c55384e
  - id: 2
    dedication:
      worker_1: 1.0
      worker_6: 0.5
      worker_4: 1.0
      worker_3: 0.75
    distribution_hash: 09c59caa2436ebfa1dd30d32b643d7734396ca965e0b3c75821b781bce8888e6
  - id: 3
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 665802553101b4d9b8b967b89cccf36c628aa14ad37e2b39809defe176c7a5ac
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_3: 0.5
    distribution_hash: 2221728f186b7b24199d60941bf1e1bf4f3e78c3a30c9dae97d8c57d294aa8ce
  - id: 2
    dedication:
      worker_6: 0.75
      worker_3: 0.5
    distribution_hash: 7e85eaf0a7a574d7269c6307ec3b6d8a993a518ddaf9aad3a208adca17ed8c82
  - id: 3
    dedication:
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: 603ca2ea8cbd07e90fcf449c5c15d9809b6ea20998d99164be06b4fe67f412ec
  - id: 4
    dedication:
      worker_1: 0.75
      worker_6: 0.75
    distribution_hash: e195e474550aca9d2e20ead576a4f3bd9bce0763b9041d407180375f68f7b42e
  - id: 5
    dedication:
      worker_4: 0.5
      worker_1: 0.75
    distribution_hash: 9f53301e59e13480593e862efb9cb4691eb1f7b75e5f8f8f59c5b97e2624fa70
  - id: 6
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 67c343967ed7ed70a132740df8523a6d61eb49ed54f4569ac4973e47b3d1ca52
  - id: 7
    dedication:
      worker_4: 0.75
      worker_1: 0.75
    distribution_hash: ec5c7b6e7baa2f482ace70fd56d0f838872d0e7e69fe876abe9e18f46a07c417
  - id: 8
    dedication:
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: 181093984dd1ebfb3ab981bf633b71214aa76ba709ae4013af2098a927f5724e
  - id: 9
    dedication:
      worker_3: 0.5
      worker_4: 0.75
    distribution_hash: bdf4d3821b76ffb0bcd493ec7f4570dcd4e024e0dd81bfb798e3f895ec7daef9
  - id: 10
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: a89cc0c6be4db784c428a12f30fea360ce7f5055fa1c2eed4ff1902d28d9458e
  - id: 11
    dedication:
      worker_1: 0.75
      worker_3: 1.0
    distribution_hash: bdafb529ed4d6463e5fc3359a6a85b5f390220d209f60e0ac2853af44e3a729e
  - id: 12
    dedication:
      worker_6: 0.75
      worker_4: 0.5
    distribution_hash: 9546b231baf1e15b7f6e9def33cdf40582ae43276e02fd8b99ed98c7c847a62e
  - id: 13
    dedication:
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: 0bd4d5c19b573f85769c46f1c70504cf82cef65e8f0272e62aa3d37b41f4a8c6
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.5
      worker_1: 0.75
      worker_3: 0.75
      worker_4: 1.0
    distribution_hash: d2a6b6b92bf0d3fd2594623abeebcfa41be664483cdd200d7cff6e889ff4472a
  - id: 2
    dedication:
      worker_6: 1.0
      worker_1: 1.0
      worker_3: 0.5
      worker_4: 1.0
    distribution_hash: 76368e7350b58c1d485df1de935d81c950f2c9a445827f9ae54df9fef93552e1
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_6: 0.5
      worker_4: 0.75
      worker_3: 0.75
    distribution_hash: 2478eb6d9a36d15a9962b8ca20de173cae36c93020000d0c738e4f01360e11a1
  - id: 2
    dedication:
      worker_1: 0.75
      worker_6: 1.0
      worker_4: 0.5
      worker_3: 1.0
    distribution_hash: a959a2bc7b548508dfcf7a3576cc603a319033572c18e8719411b002bce79ce2
  - id: 3
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 1b317638c9586419ff6ee0731dbcc1572eb822eabed33e655f82e7024819bfff
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 989a825eb336acb86b9e50aa4c031d5407226a4abc62ace05abeca64207bf445
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 589298a02e61d448e2cc35bdac9306c637a651a193d328fddc40c06e25c7831e
  - id: 2
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 2bcd8320513e70f7e7101c54a2b7c685b2e327cb89e69840bba3225f19e36619
  - id: 3
    dedication:
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 7e38beec35538d5a30137fce1c7098c22bfeaaf0e84b334c0f3daaf91ec53cc6
  - id: 4
    dedication:
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: 17f4fcb208ed1bc7e57648e695bff374775cfa67d0398100ededde0f6d7a3306
  - id: 5
    dedication:
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 4feb19d21f525ca827e29761b2cc985010424096a31f21ccc051dfc1cf39aa79
  - id: 6
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 9f9ae789bd8d3bd3a170499b7951812ce96918a01b6de10c57b505585d27c9e9
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_3: 0.75
    distribution_hash: 23a84f23c4107862c0e9b858b6a7beca615fc8b66f712a590684129ab2403dd9
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: 4a4872a0f1b99be03ccf39f0766939f6fca125aa9d8435f794d3421076185cd6
  - id: 3
    dedication:
      worker_6: 0.75
      worker_4: 0.5
      worker_1: 0.5
    distribution_hash: 2f44d2aaf33998bd69a42991ff365f24089f078f66467dafb00312b053b389e7
  - id: 4
    dedication:
      worker_6: 0.5
      worker_4: 0.75
      worker_1: 0.75
    distribution_hash: 5095f5a43d24e5c523b9f577f60973e8c8147478d809ef1535fa26ce632753f2
  - id: 5
    dedication:
      worker_6: 1.0
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: 5e1f2d2298d870cb764f65a1cad75053dafa03e8959fe2497d738361a44cc3c5
  - id: 6
    dedication:
      worker_6: 0.75
      worker_3: 0.75
      worker_4: 0.75
    distribution_hash: 26c6ae689a21bb3f9c33c5189e53a66822bc58efbe89efa174cd9f8f578e2db6
  - id: 7
    dedication:
      worker_6: 0.75
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 89ef6c6ea62dcb5f282fdb94fe38eb6c1a8f66dbb755c17df073144beb1df31b
  - id: 8
    dedication:
      worker_6: 0.75
      worker_3: 0.5
      worker_4: 0.75
    distribution_hash: fe73442a2191367add6bddb1de993fed90daf45578a39d95e429f19b6ae6d9c6
  - id: 9
    dedication:
      worker_3: 0.5
      worker_6: 1.0
      worker_1: 0.5
    distribution_hash: 0d27cdf5e63e015c3a1b463fc25d6a817ef5d8ee00da00966d2c39c24a1472ad
  - id: 10
    dedication:
      worker_3: 0.75
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: da226b9548ef15b32fac0cd0c2b643ccb0546ba878c3742e0ef9c934fc6652ff
  - id: 11
    dedication:
      worker_3: 0.75
      worker_6: 1.0
      worker_1: 0.75
    distribution_hash: 4290533e87ab027355ae91ae70b756d4e0c02bbd23d3fcd9a2964a187f5341dd
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: 0c686777bce10b3b12cbc55a9af010beaa3563e1224446d2dacec9f26d45ca2c
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: ec179654bf5b0787ed7b7507df6670bf73034cf1193c48cb1059406889eaf921
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 71f5c5ac5181306853dae33d6a67151a456ba971640bd7c540e759b5f49bb2ea
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_6: 0.5
      worker_5: 1.0
    distribution_hash: 2461e55a8bb4373aa369822adf7412fd09218ec827d93ca10c22cafc51fdaf84
  - id: 2
    dedication:
      worker_1: 0.5
      worker_2: 0.75
      worker_6: 1.0
      worker_5: 0.75
    distribution_hash: 65f86034b34a99c39e2e7da70843006073f4ce89e694a2d654bcb26ea58d4139
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_6: 1.0
      worker_5: 0.5
    distribution_hash: 6fb990537b1cffd52f40b31e8f3a7af2149cd8ee85e76840e3d46341f32642be
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: 34bd1dfc0c1e9b7d89131af40d7272c537bf55571a5e376253cfd11cdf6f83b6
  - id: 2
    dedication:
      worker_6: 1.0
      worker_3: 0.5
      worker_1: 0.75
    distribution_hash: c7fc88c1888bc1614228423044a100ef8de92b2b94efe64eb27737273096715d
  - id: 3
    dedication:
      worker_6: 0.75
      worker_3: 0.5
      worker_1: 0.75
    distribution_hash: 9fc4e6ac3a31c13f1a295e6020ce0184d5307632737c85873b033439db6d257a
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: fc2df9f80534b689ab21e1f1094d9416c5de79e7078748518192cd16bde5cd02
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 5da29dfe00f352d8e940d266274b8503f52f124841298c754cc8b84124dbe1c4
  - id: 2
    dedication:
      worker_6: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: ce1985d492fde09135958df7cde18508e48485f0f19cb194471d1235b2049453
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: e4995853b7895de2f0ed33bbb963c7a544d10fc2024408e1876cf8c2d0bbc6a6
  - id: 2
    dedication:
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 5e8ae0dadd014d745606637b99ddbd5bbe2b97264c7a7542ec3d0e8acab18a53
  - id: 3
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: d0123c788a9fa677b8618d213c0f2e9d3371d3333fa81562086fba86e58f9d29
  - id: 4
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 6b3eacdecb937bc18fee0239d8185806d20f9df6e8409767e6a80e64efa0fdc7
  - id: 5
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: b01d6f200e9bedbf305e57be1c822f7c39a8afffe402f0ad77738ff3b95009e0
  - id: 6
    dedication:
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 9cecc4b9cd694fb7aa6b0c49745c3933dbb3e74819528a0cac77d693186cc169
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: fec8fa2d15999f42543fd6a80b3e315770cda8539ff92e997979b8747060698c
  - id: 2
    dedication:
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: f441069a7f9f105312bb507c595182b6604e992c44a706e7babd51c8bd550bdc
  - id: 3
    dedication:
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 12f2671166fe12b0f2705c8f5a87ba7cb736653ecd37ed2581b6fcbd767c04ad
  - id: 4
    dedication:
      worker_3: 0.5
      worker_4: 0.5
    distribution_hash: 56282cf299e760c5161f3797de5b728078a442042197f1d0bf11a3063376746a
  - id: 5
    dedication:
      worker_3: 0.5
      worker_4: 1.0
    distribution_hash: 8331d21c22e4c3a31ab5ba0d220f42688ce5629bec2b6be8c70f2558627dc654
  - id: 6
    dedication:
      worker_4: 0.75
      worker_6: 1.0
    distribution_hash: c168e56e4664305e5a2744136bbeeabb9b486ce7db4641f331fddd31c428f19b
  - id: 7
    dedication:
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 68d1d7c1331815c6b21455e13c4c6f42947798f29b0bccd73fd7d041c3713426
  - id: 8
    dedication:
      worker_4: 1.0
      worker_6: 0.75
    distribution_hash: e0b49f9bc68f61ac4080703afdc68457561f34bff63a73e2aa1b88e84fe72c90
  - id: 9
    dedication:
      worker_6: 1.0
      worker_3: 0.5
    distribution_hash: a199a1f63d9d8f76a6bbb1803e53599b1b65522bf39e7c12d3d83ffec1e9fd65
  - id: 10
    dedication:
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: b35afb763f53d331e31c5aa83373ebec9d67b6c49921757f313bb0a092a85fd9
  - id: 11
    dedication:
      worker_6: 0.5
      worker_3: 0.5
    distribution_hash: a2263ea3e4664b329e72f7cb0d3749bdadcd038ff52dfaf277ce254b177acccf
  - id: 12
    dedication:
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: 04dc9738c6e3c071d74843af8e62b1d9eac5796ca41536183d92a1d6a3750b44
  - id: 13
    dedication:
      worker_1: 0.5
      worker_4: 0.75
    distribution_hash: 39e8d997003a051cee2d345024f3281e99b4e3d7424a65d45db929f63aee8b30
  - id: 14
    dedication:
      worker_1: 1.0
      worker_4: 0.75
    distribution_hash: d6480edeb832f35b23b56350344abaccd9814567afafc25b95c522f4ff487bc3
  - id: 15
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 089cf4e76d8313d91f1bf21d0fa95674417321be0a328ae758c194d82413bdfc
  - id: 16
    dedication:
      worker_1: 0.75
      worker_3: 0.5
    distribution_hash: 51428319f5c68584661c97f384645ea867defad8effd05f5c1d017932f66e5db
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_6: 1.0
      worker_1: 0.75
      worker_3: 0.5
    distribution_hash: 52e3b9f5be65a8a76efbbb659642856ead6a6135bb67e67bbd5d8a92ef529a06
  - id: 2
    dedication:
      worker_4: 0.75
      worker_6: 0.75
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: 563d27325bfdae5e09cd507151dd88a3885852f64f36f0c3896660eb26ab096a
  - id: 3
    dedication:
      worker_4: 0.75
      worker_6: 0.75
      worker_1: 0.5
      worker_3: 1.0
    distribution_hash: 349a20c4625e53090c51066074a773f8aa8fa25eecbae92a69527fca6666a8f0
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: 17514bfabaa1b7b77332129c7102de76456301bd6bac35e288f59ffcee7a6204
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
      worker_6: 0.75
    distribution_hash: 6ec9ae7cb9dae877a2cb6a0814af74fde1a3f541f927654527d7ff1742df1510
  - id: 2
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: af176e26f4bccd1d037c87cced8b0b93ced223d88d506fc713f538c53b09b98c
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 0.75
      worker_3: 0.5
      worker_6: 0.5
    distribution_hash: ee81e6df51ca8613a5d2a274a393ab74dbe1846ea45c81a51b35ace7d40a0a03
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_6: 0.75
      worker_3: 0.75
      worker_7: 0.25
    distribution_hash: 108978490219585c87ea2f45f9765cbaf048c15793441c34fd7c2bebe3faf31b
  - id: 2
    dedication:
      worker_1: 1.0
      worker_6: 0.75
      worker_3: 1.0
      worker_7: 0.25
    distribution_hash: 257c997e3fe84538fe14af7f40b91dc9eeeaa1d4958ea6e2fba3e8b698b1533d
  - id: 3
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_3: 0.75
      worker_7: 0.5
    distribution_hash: adce76500edf67c29946a3a8cc23a36b67e908ce075a020374ddb4253454bde1
  - id: 4
    dedication:
      worker_4: 0.5
      worker_3: 0.75
      worker_6: 0.75
      worker_7: 0.25
    distribution_hash: a0155d4d4396c291c4bcf1da05935bcc3d90112e94270aa732ec6d6bcdb5e7d3
  - id: 5
    dedication:
      worker_4: 0.5
      worker_3: 1.0
      worker_6: 0.75
      worker_7: 0.5
    distribution_hash: f85188223545522beb756ec9821be585f4b5d8e61ae89c2b8c7859f31e2e1a4a
  - id: 6
    dedication:
      worker_4: 0.5
      worker_3: 1.0
      worker_6: 0.5
      worker_7: 0.25
    distribution_hash: 7bc92e5c8d4cea76e527ffe2d67635d3b96da5154d5b88d664c7a48539e455eb
  - id: 7
    dedication:
      worker_1: 0.5
      worker_3: 0.5
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 0414f1607f5f019b958317fc3feea27124293e17032501b331cca19af908c604
  - id: 8
    dedication:
      worker_1: 0.5
      worker_3: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 476883742f8fb8cfd2d54bfc28444f4b2962d3b2a40d322e112c4b782ef3189d
  - id: 9
    dedication:
      worker_1: 0.75
      worker_3: 0.75
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 987950f156f2d58580daff4a8e65584b580b36f2f0537b4674ddc6c0092f73d7
  - id: 10
    dedication:
      worker_6: 0.5
      worker_4: 1.0
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: dda0acc12652737fd648842d465989a727b9c0725a6e6344337b80562089f48f
  - id: 11
    dedication:
      worker_6: 0.75
      worker_4: 0.75
      worker_1: 0.5
      worker_7: 0.5
    distribution_hash: eb13e8d538d3a962803e94438d47c57d196c3da21d6fde21a66f9c04d9750a81
  - id: 12
    dedication:
      worker_6: 1.0
      worker_4: 0.75
      worker_1: 0.75
      worker_7: 0.25
    distribution_hash: 449e1e6d57afb3e8c0a27384bbd28ca600d2cbe4ba179ac8717aa582b668af2c
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: f70e2e59f958c59c25bb371157b097bebcfdba6c1fa744d21c0dd185b3b4f848
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: a121cd14617c36ef3a69b08ccd4f4451210fb304a9f6a162b483fa445a59ad4c
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
  - task_7
- - task_1
  - task_8
- - task_1
  - task_9
- - task_1
  - task_10
- - task_1
  - task_11
- - task_1
  - task_12
- - task_1
  - task_13
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
- - task_2
  - task_15
- - task_2
  - task_25
- - task_3
  - task_17
- - task_3
  - task_18
- - task_3
  - task_20
- - task_4
  - task_20
- - task_4
  - task_24
- - task_5
  - task_15
- - task_5
  - task_19
- - task_5
  - task_23
- - task_6
  - task_14
- - task_7
  - task_21
- - task_8
  - task_14
- - task_9
  - task_14
- - task_10
  - task_18
- - task_11
  - task_16
- - task_12
  - task_22
- - task_13
  - task_15
- - task_5
  - task_18
- - task_9
  - task_23
- - task_3
  - task_25
- - task_10
  - task_21
- - task_5
  - task_22
- - task_6
  - task_31
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
- - task_23
  - task_32
- - task_24
  - task_32
- - task_25
  - task_32
- - task_26
  - task_32
- - task_27
  - task_32
- - task_28
  - task_32
- - task_29
  - task_32
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 636
validation:
  project_key: 2e37ba6ebf2e373d8fe54df45751a66467142e0799623cd6a8adbf419e1a1df2
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 69 days; worst-case serial bound: 1741 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
