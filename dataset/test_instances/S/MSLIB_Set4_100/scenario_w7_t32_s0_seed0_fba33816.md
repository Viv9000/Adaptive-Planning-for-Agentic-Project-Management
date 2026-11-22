# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_100
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
  relaxed_constraints: 8
  modes: 150
  tasks_at_cap: 0
  rewired_edges: 3
  departments: 1
  quality:
  - worker_1
  safety_skill: 0
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 5
  barred_pairs: 4
  incompatible_pairs: 1
  edges: 54
n_workers: 7
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 602
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
  33eba4b10b86150f3c46ab60dfee2ff6d0458e493e55940c6c238d5f8c31b5db:
    family: pert
    a: 37.30056715895305
    b: 46.62570894869131
    c: 233.12854474345656
  499869445125c22ced4a0077825ac068396cc9fd2db6bb0cad2a5237cca68ba5:
    family: pert
    a: 36.15915977554315
    b: 45.19894971942894
    c: 225.99474859714468
  0656dae03a9e54a71885a269ceb2e380ada6b5a0c46c6422a6d21e606461bab7:
    family: pert
    a: 29.662823337011346
    b: 37.07852917126418
    c: 185.39264585632088
  d399a53ea778b5eb085445ba9ef229189b99135b3efe73a48d0d34e786af4acf:
    family: pert
    a: 4.820032299115056
    b: 8.03338716519176
    c: 21.60932870338265
  99608dfc579f2143b37af7bac06d21da2c5ac511b77d1b74c8fd90a3952ffa7e:
    family: pert
    a: 11.91935884559227
    b: 19.86559807598712
    c: 40.25775260350509
  a1493792ae4c0548258906e944686837490a0202e086fb5eb293995f268e29c3:
    family: pert
    a: 7.61771822863601
    b: 10.882454612337158
    c: 33.24754862678093
  8ed8bc00299d2a5d64364686b70b12dedf788c5236c5ab1ff1421dfd1d934c0d:
    family: pert
    a: 7.736292536766239
    b: 11.051846481094628
    c: 24.020831499213394
  162e8a71b5f973bb7be0d45b0b6cdf046b61ca676f32b432d5c538fe323c7da1:
    family: pert
    a: 9.792700916186757
    b: 13.989572737409652
    c: 28.981807613709318
  815a0e54f23a3b81783953ca0cdb64fea7f803c97ef098282ed66858c7455f8c:
    family: pert
    a: 9.111174358421101
    b: 13.015963369173003
    c: 29.058081718305107
  7f44b62b4099c9679f9e3d30f992a96560b831c7e2a41671388e00665dc0c054:
    family: pert
    a: 7.976477148133157
    b: 11.39496735447594
    c: 24.73427910665277
  cc426a2f2f3f251659199823fb31d21241c04222744c886f96f619cb21a4dea2:
    family: pert
    a: 5.611613100206022
    b: 8.016590143151461
    c: 19.63014224999329
  ebe497e84d109a77595cd237422d2838e133f5c647476bc6af1794fb963aa713:
    family: pert
    a: 9.249313767428172
    b: 13.213305382040245
    c: 22.042971676729344
  ec5a968d87f0ea902a7cdbe4b679d7dbb684fc6653b7b4fc7193b6dcc2f0b581:
    family: pert
    a: 19.003490483546013
    b: 23.754363104432514
    c: 39.28815139240889
  cfcc5e44d3cec6b2dae4b61fd23d1ffb97730c00970e0b905d88bf98667d04fb:
    family: pert
    a: 14.038490567574854
    b: 17.548113209468568
    c: 26.86574682718079
  79092a7596e319c8fdc0dc6929c831b5e136433c8fe634c1483942bf16f21bfc:
    family: pert
    a: 15.402909577419308
    b: 19.253636971774135
    c: 33.25466256994258
  14fdc7bae62f44cdede475ba150cfc3ed027cb18b01c817a599f49ffd76238c0:
    family: pert
    a: 17.460451724484642
    b: 21.825564655605802
    c: 29.82841840324154
  721be1b385d13ef831d8e6ad4f4c5aa2981b8cb5360b94c6ae05732d1719e08e:
    family: pert
    a: 16.387010110630907
    b: 20.48376263828863
    c: 35.463710161179264
  9b568b34120bba0a51ede278f930488b98ca72ccf8b233020d2d386bba5be9a8:
    family: pert
    a: 12.66095765627328
    b: 15.8261970703416
    c: 31.54872665390743
  8a93be50a39b87476c8db30afb4274443ce85ce409b250421da4f61de7e9bfee:
    family: pert
    a: 20.022121769695612
    b: 25.027652212119513
    c: 35.80498887300284
  832e11ef60220d54c36f2d1438fcf8baff27d5a003da71c39be34bfdebad4d97:
    family: pert
    a: 13.186449118706461
    b: 16.483061398383075
    c: 33.3248489826725
  7cc76d7e602d376144f858547bf6ed994d1c3820830fceaf6041c554def3f02f:
    family: pert
    a: 20.55454829366845
    b: 25.69318536708556
    c: 43.552857795057875
  d992213058bc625a3a5318e3e0b512a4cc365b0413a0f4e0dae76e0c12568361:
    family: pert
    a: 33.815885329468465
    b: 48.308407613526384
    c: 89.40609577254459
  b39fb8ba91e3adb9c5311b82e030cc27a9e5c93eec974e02d8da9b9632ae156e:
    family: pert
    a: 27.343562016300762
    b: 39.06223145185823
    c: 105.99166771193738
  5b3ea112d6beba98f6aa760268e62bf0239888485e277ee4d1f045a1fe2d21b8:
    family: pert
    a: 36.526877528792284
    b: 52.18125361256041
    c: 137.19865891858012
  9bb3fb2494289cb8b4631f7007a903c9b9752a81257f95ee3d041806ba4111cd:
    family: pert
    a: 40.370878054895535
    b: 57.67268293556505
    c: 121.4014036414219
  b676a466566c0c1ca88673f703f8d7a19dd3e61c697f3cfd21a49f4a10c3b9bf:
    family: pert
    a: 37.62202845159493
    b: 53.745754930849905
    c: 111.911357438192
  e253d6a0172571f919b937e01c163d2cceb9bf31e6150bd7df618f9322b4ba93:
    family: pert
    a: 17.56172516840839
    b: 25.08817881201199
    c: 41.93001897354859
  1db42bfb9704e53e88295c127769663fb65da756bd9c2d203d5bf3b6d6503b72:
    family: pert
    a: 10.352957036371283
    b: 14.789938623387549
    c: 47.060855560054094
  6be6e62dc8ce5b563dd6c4985644681de71d13abefc68eb315ddd77cbbf63bf9:
    family: pert
    a: 13.245358647987759
    b: 18.9219409256968
    c: 53.00467360793824
  f2c8bec63904b5e04308b2c993cfe150c40c3a84a70905dce01aaeae8e1c1f2d:
    family: pert
    a: 16.162892876945417
    b: 23.089846967064883
    c: 40.34939878305453
  64da9e300bacdfcaaf0d89eab889ef69a1bb764d37df0ed36b4eca9c3609da81:
    family: pert
    a: 13.808956225459282
    b: 19.72708032208469
    c: 32.35987557314608
  7ef528d60d54a0f17ed1ef46474956bea0d9578477e3b4b9611dd55db2b3a0cd:
    family: pert
    a: 13.001985449262781
    b: 18.57426492751826
    c: 32.513929199840035
  a0c3d8b4424cbdd245207fdf1ceef852cb30549e0a199d1d2eabbeec30df3a20:
    family: pert
    a: 21.754917310801336
    b: 27.19364663850167
    c: 41.009656896715256
  327f9f3c7510dced3d4eb24bcf29e79328d79afc17f25e6c64c6d8ee80700aec:
    family: pert
    a: 33.0607970848368
    b: 41.325996356046
    c: 82.08153198429457
  7d743bf64c2a9dd1f74c2e33681dc1ac7c52683a7c65b2aba4db71824bacdb86:
    family: pert
    a: 12.6256141652771
    b: 15.782017706596374
    c: 26.559444421110655
  9a0ef74b30814b4ef3fffe3b8407c3c43d2128a67d787537469d1590bf2f38a7:
    family: pert
    a: 7.144177861591922
    b: 11.906963102653204
    c: 42.07127143233754
  d5d7aba550c4b7f9765cab9e39219dc9a0bd73fb09a582fc731da7434ed241b5:
    family: pert
    a: 5.060339861704994
    b: 8.433899769508324
    c: 35.064951848353
  ed5c0fad568901481d4ab056a713312b442ddf1b99f62bad45248e6661ce3334:
    family: pert
    a: 5.269046412209043
    b: 8.781744020348405
    c: 22.147725399195316
  41c00102581a0a27e0d755f9ec15eb1afec5dba8969282bafce21d232791f49e:
    family: pert
    a: 38.96815948731947
    b: 55.66879926759924
    c: 91.49673356429695
  e64d5bf44d539f152788ee5ff89e834a6b81f426ac039b95299b89436fb2b54c:
    family: pert
    a: 32.58243149093553
    b: 46.546330701336466
    c: 76.8283150683343
  7c847a293a7bf743ed3d170e61336e856bdf3b5e5c86e26bd0151502eb0b0fb4:
    family: pert
    a: 26.328219355478364
    b: 37.611741936397664
    c: 115.14413084812773
  d4b3ef89c4e218e062891a07971e35120495b61dea9f923a19b2b73867669eae:
    family: pert
    a: 10.565391734451211
    b: 17.608986224085353
    c: 52.49829743066161
  f7b39e3f2b9698e5a183e04c01bb135ade2d5717e58bebd078e6f4f7ad8408fb:
    family: pert
    a: 8.965543197904735
    b: 14.94257199650789
    c: 52.03310254634753
  03ffaae63f1ebbd67a672ed563db728c060decb017a3e2e90b268a301461ca0d:
    family: pert
    a: 6.097548288596638
    b: 10.162580480994396
    c: 66.24380147840621
  5e3f59ee3a31f8c357b5311c93407ae6e31be7973016d24f973183b6fa882715:
    family: pert
    a: 8.726353739097995
    b: 14.543922898496659
    c: 62.464030899209746
  5f5f25a81209144a43dcb7415951b534b008bf172d65241645ee45fe8ed6dcda:
    family: pert
    a: 10.049168001343272
    b: 16.74861333557212
    c: 54.65596231262317
  8e918473c16e11f338af45891f9ddc0b01abefa798356e111785246d8a0010ac:
    family: pert
    a: 14.792392093808985
    b: 24.653986823014975
    c: 43.843957647597016
  9dcee7dd2ca612314eccf591b4acfeaa164ff377b566283e2cd0ce18e45b144f:
    family: pert
    a: 2.7776492213028674
    b: 3.9680703161469535
    c: 8.531124408150617
  f73467514cf0e02547f2fe7baf52e5b6b1b521ed805a00db56362642594ee07a:
    family: pert
    a: 3.0624183422839177
    b: 4.374883346119883
    c: 8.393023769268664
  ef5d818cd47d1629ca9b2932365cb8fca491b79edfe747043f4c980453280d99:
    family: pert
    a: 2.4553500559184323
    b: 3.507642937026332
    c: 9.292284959490267
  15e93f4a91ca10e04cdd1eeb46919632c739cc25a2841789f7a5b7aaa0eda7a5:
    family: pert
    a: 3.137360026714989
    b: 4.481942895307127
    c: 10.748389784492053
  abdb2def867bcc327bf61b5b9a35ab7a64c17c9262c976cda67b8af4bbcd2a26:
    family: pert
    a: 11.591564967115062
    b: 16.55937852445009
    c: 49.66187764140793
  c094740746cbc3a4688afa840325d3dbd691ec24bc1852b7e1e9c565d4030f82:
    family: pert
    a: 12.917585821971697
    b: 21.529309703286163
    c: 85.61179341353072
  06e31cdcf8adf10ec9ceec63acf7f2d596d7e9f0425857ac8cfef140f3713507:
    family: pert
    a: 13.322205160183694
    b: 22.203675266972823
    c: 75.78433960102839
  e16b24a013342b6bdd285c8b52e0eeed0bc8f4a2ebeaac47d0e4becbffdb3b1b:
    family: pert
    a: 6.4515790130239585
    b: 8.064473766279947
    c: 12.557115907722318
  7fdb48e4e2c8cfd73c453899c3bb98f8c8b3ad382a991a9c544a52ebacf61e17:
    family: pert
    a: 20.50930723447773
    b: 25.636634043097164
    c: 32.28375205660555
  b45b84f7bd37845bb88eebd9764e4f5f4c822a467d95b4b7439febd988a1826d:
    family: pert
    a: 29.953709262294378
    b: 37.44213657786797
    c: 54.17574329541358
  7688c9c009ea4ef3e97b63ff8146f6b756fff8ffd79de1b64cdf3983c2e30567:
    family: pert
    a: 13.466122581725381
    b: 16.832653227156726
    c: 29.164374214166614
  f45af4a62824239e049ad61f0f61a576c5a3a2e2af6915283d9e0a2257e812f9:
    family: pert
    a: 24.34438274748058
    b: 30.430478434350725
    c: 38.388942557316554
  a0dd10d31f9ac50b8552aee1b699659012e9813a37943b70bc55a400658f09d7:
    family: pert
    a: 31.364283344213597
    b: 39.205354180266994
    c: 56.4092526722125
  d4b10d4275f136bd0bf2e61c0e5419e3516824e297b498a59a47c5ed43ffc066:
    family: pert
    a: 21.062283668205836
    b: 26.327854585257295
    c: 42.31656310872296
  07bc99665477cc291ebce2cd94113d0d832184f7dc9168901dbbefc811d311b6:
    family: pert
    a: 22.64750491229902
    b: 28.309381140373773
    c: 46.64589663848807
  beb83833fa15195be52899d77bb199496ae038b2f6c4b2ac296781d5067d4a97:
    family: pert
    a: 20.52076614280964
    b: 25.65095767851205
    c: 36.72037154829498
  eff9e446981f97efc31fd487b0221cc2657d75dc3304b1979938cd2abbe537c5:
    family: pert
    a: 13.554660875983732
    b: 16.943326094979664
    c: 27.094398496700848
  20b3ca7b41d72077d18235c075d7648119dea364b285f1d00c2ae15de8869fcc:
    family: pert
    a: 14.764134338574317
    b: 18.455167923217896
    c: 33.72982656631748
  14b328e344a2424f3e9535cad124e1382af7c682954a0cadc9a4af73f78a6807:
    family: pert
    a: 12.281168354110465
    b: 15.35146044263808
    c: 38.357786991825435
  adb193a7a2b81588a3eaf3f346c474a02104e9050e95af8421c8c410621d790c:
    family: pert
    a: 23.208276455862567
    b: 29.010345569828207
    c: 42.57261036134753
  5a4c2d255ca0a2c59ef6fe5547a7f43ee40fcc9eb6fea422709a4c584de50613:
    family: pert
    a: 34.15053203937233
    b: 42.688165049215414
    c: 213.44082524607705
  f84d44263443a9b34fd2cfe03cbaa90a515be367f8493ae221727d7c09b1b760:
    family: pert
    a: 25.83771335353529
    b: 32.29714169191911
    c: 161.48570845959554
  bfb9002edba07b5aae32537340a0c615aacf4b5372acf5aefad622fe4053e69d:
    family: pert
    a: 24.147506994197713
    b: 30.184383742747137
    c: 150.9219187137357
  f7f2bd1b4db7c76bf71e879ea123f9616c01a055e847ecddffb3e4aaf52b2ffb:
    family: pert
    a: 16.625647521880463
    b: 20.78205940235058
    c: 37.81489727942316
  7ce661b97bf22c0be0215c0869e7233a28c1c8926d36c85a54dbabc5e95b515b:
    family: pert
    a: 25.39242246010808
    b: 31.740528075135096
    c: 44.56526059003354
  4375f0ecdb7514e0ac87d33c834759901d2a6d274af570fd0073b21a0f038130:
    family: pert
    a: 13.873199106969402
    b: 17.34149888371175
    c: 33.30116966220042
  dc788362a069b14e65889ed39357defe4f9478e75459a67c928e06079b2c4a77:
    family: pert
    a: 19.519582486805096
    b: 24.39947810850637
    c: 37.07507489334196
  b505b3402342a2123dc0322488ecba1a831006bc9c9d1d2e69cf5e75b8d3f309:
    family: pert
    a: 12.830688267027964
    b: 16.038360333784954
    c: 30.194999414134536
  bbc58db3fbd3c45c951c949136af5f0e7d36d6cf277ed5766143c15f859cb78f:
    family: pert
    a: 25.241739036509593
    b: 31.55217379563699
    c: 45.72766919501923
  9586189e2ff8f39c8b5633ba400adf7ea308545f2c6cf57f32dbe2bca2833a39:
    family: pert
    a: 17.678088983306033
    b: 22.09761122913254
    c: 37.49540331625938
  6828b192ca7cf12a73f2ca723e8ab30e67aceda71e56141b9fe19b20b32acee6:
    family: pert
    a: 12.014955611745087
    b: 15.018694514681357
    c: 25.67926276019716
  62b239df6812b141617d6f60bf0213c6b7f3dc59bb665e1eedac167980a43154:
    family: pert
    a: 13.510489092700713
    b: 16.88811136587589
    c: 25.460404891338506
  ba8dafb3d0ae96d026a108aedff4ee8d7bca067a2b6837ffd0728f9a951cbbf0:
    family: pert
    a: 14.38163335735632
    b: 17.977041696695398
    c: 35.395445474888135
  17b62974ca43a8cc5ec9759dc53c5c68d3e429787b96f9f863f73e60e34e78d5:
    family: pert
    a: 25.09774488634273
    b: 31.372181107928412
    c: 49.588164974764766
  fbcf109a47a98743e5e2572a3505faa33bf7f999fc8330fe4bc2f89466c6ca0e:
    family: pert
    a: 16.091772145041283
    b: 20.1147151813016
    c: 39.384736042941384
  dafdc0fd6f7b3f6f9e68e6eb20b83ddc76ac2c604edbc388f445b81558303a32:
    family: pert
    a: 17.50339541618181
    b: 21.87924427022726
    c: 59.58403510182174
  3f803206a163485b150638399958558e74e13ec39f5b994427e7dbcea46588c5:
    family: pert
    a: 12.516623893372113
    b: 15.64577986671514
    c: 25.268868432392438
  6b05bded75fd9679156ffb6a32e5a2995270ce8081e5eaf8e94e6dfb4bc37f8b:
    family: pert
    a: 13.76248775051023
    b: 17.203109688137786
    c: 25.057968418624867
  282e39567de3f12445f27bcf241f34ba9bf3f4e276ea48e27b771c7d966664d1:
    family: pert
    a: 13.850880463358095
    b: 17.31360057919762
    c: 29.053846231004716
  87911578900cb3d8026b3da7c8b6aa27bdb0a3546e7f83cfe66d8d7aaf35f2b2:
    family: pert
    a: 22.597228368806896
    b: 28.246535461008616
    c: 36.48075618382566
  2373e3d70c8c81813648ecc84804d029f98eec3ba51838ae7921c4e8852827e9:
    family: pert
    a: 29.329125636776094
    b: 36.661407045970115
    c: 52.002573984713386
  34b5ec0c2a9d337b153022912b20fbb116999da705dea928d880e8ea017bcb3e:
    family: pert
    a: 13.848782408860703
    b: 17.31097801107588
    c: 51.12108247181762
  d31ebf5695803e61949936037be62205e6f77e6baf94ba3da90c88759ec9f785:
    family: pert
    a: 17.54524816193872
    b: 21.931560202423398
    c: 34.7841146612331
  91c1b67041887e3260a6240bf45fa7fff756c936bb4bacb3b554b8f690d3760a:
    family: pert
    a: 14.484082576764491
    b: 18.105103220955613
    c: 32.760621446663244
  f79f15781f4aee61d274740884d11c3a84213771b84f5b2400a8c0d3561c4625:
    family: pert
    a: 23.3135990585135
    b: 29.141998823141872
    c: 48.057095139681984
  33d636d28113c4352961b6590ce21ba6923581ae09e88cd1665914233008ab40:
    family: pert
    a: 18.389793657763445
    b: 22.987242072204307
    c: 39.49829692559522
  9056c4d9dc7c8226fdcf280eced68e5c4e5361a5f2d517faf81b75c2e18c6619:
    family: pert
    a: 13.141542523882803
    b: 16.426928154853503
    c: 26.072112162203908
  d3c4fe951f13cb672e912d87fe3c93d18f0f466e82d45c0e1ce8fb43b6cb9baf:
    family: pert
    a: 14.528808044271981
    b: 18.161010055339975
    c: 22.621161117965908
  8b67437f4dbe8974c447d0a5bba1a6df471d20013c33649d155bc856eb30fbd5:
    family: pert
    a: 31.096155559669437
    b: 44.423079370956344
    c: 75.49261426299631
  a78e978b94790bb65efbcd9a686961f1b7eed686ef25ccfe75994667507f9875:
    family: pert
    a: 29.28475004729045
    b: 41.835357210414934
    c: 75.11945328593745
  33cf684b10cb6de0d5a13399252913a29ad39b458ed87bab799a3df6616d4790:
    family: pert
    a: 29.810978487017323
    b: 42.587112124310465
    c: 93.9708155637109
  95ac8670ded34f6e3ce2807ee05ca15c2db17af781bdb7506a4227a8341f8e66:
    family: pert
    a: 22.27844946959157
    b: 31.82635638513082
    c: 61.51989104753064
  9f5b9ddada57a72fc2e72d9f98f754875164f47925d57752a5b6ec9127bd3e84:
    family: pert
    a: 28.45493987695077
    b: 40.649914109929675
    c: 71.86636971702987
  3a14965006cb7bb487fd04d4b52149ebbb1042dfe51d4f4fdade8266354d69f7:
    family: pert
    a: 20.54324159328224
    b: 29.347487990403202
    c: 59.48945151081547
  68737ddea44bd04c829ec8916c2fa80cb9b5b37af2e6d8f6b49eac78d2f127ba:
    family: pert
    a: 28.907752787222822
    b: 41.296789696032604
    c: 83.51112226547127
  db962db6afd204ad819090ab8622d97411b76de566ea500cc0d9e16d611b595e:
    family: pert
    a: 19.89600801087583
    b: 28.42286858696547
    c: 57.53583175183778
  ae71a09ed369459c020c52f994a7ad617b4306f857dc2073d0f88404540407b5:
    family: pert
    a: 21.851897159357783
    b: 31.216995941939693
    c: 86.05493178874788
  742755e5ffdcb8c361ccd812b87e79c51663f93d4e20b461a7a8cd205dc61cfa:
    family: pert
    a: 21.74103202395315
    b: 31.05861717707593
    c: 52.010632391162076
  d6e8c0776a8a2e1f33b27334a55659454d89bd90ebb8a6dcd93ac586f785e87a:
    family: pert
    a: 27.57733607615911
    b: 39.39619439451302
    c: 88.80014916335328
  81fe20ce99d6d4011a18774df9d882953dec9d809befefea1692bc2f33b3ffbe:
    family: pert
    a: 22.997228607944763
    b: 32.853183725635375
    c: 90.12231415638557
  f8aba8f0455cf345251667076911ada16ebaad23359642158638e4dff39c6e4b:
    family: pert
    a: 20.5599963533659
    b: 29.371423361951287
    c: 60.01179190976902
  c73f9c06f2886a913585d02ebd9ca4d93cacc3a52264efba4d728fa6e4057903:
    family: pert
    a: 2.792038323372603
    b: 3.490047904215754
    c: 9.338174993863305
  5eca47196f855a8d85affc9a55f3846e004c98bcf7482c7e234750f7860dfa7c:
    family: pert
    a: 3.867792360964762
    b: 4.834740451205953
    c: 6.596038379923472
  a37f63d6e299173ce6ef3ba72f5a3cf8d84a71568984652536c4e446ef43d427:
    family: pert
    a: 5.812243249917693
    b: 7.265304062397116
    c: 9.470858421297772
  6f79cfd4ce4de66910a01096f0806c03386a64849b3caf9d29bf5b590adf7a79:
    family: pert
    a: 7.378019310252354
    b: 12.29669885042059
    c: 28.903295945462393
  f1df208f70835c08bcc62655c37fd28206c128fc38578f2594111ceed7fd3aba:
    family: pert
    a: 5.79775035912671
    b: 9.662917265211185
    c: 38.02828686938868
  0165cc4dfb93dcd17534da38d21784cfe70b8e1c7f893ccb0ca42c88d6bbd41b:
    family: pert
    a: 9.685777512104274
    b: 16.14296252017379
    c: 56.21138429006748
  ee61542958da6ef81a009798f91e84da27db010c2c535ed76f588d4d2b814b67:
    family: pert
    a: 6.725941683509116
    b: 11.209902805848527
    c: 28.296251823021812
  39c2dff767bb659910d3be04484ddbf40b7647813c28597839647fcb4d124ad8:
    family: pert
    a: 7.453876321338725
    b: 12.423127202231209
    c: 46.04367090871376
  d77179e4bc670d420c54c58d179aa1c6e9287c63900edd526a5482aa06fe540f:
    family: pert
    a: 6.676285202999811
    b: 11.127142004999685
    c: 33.11913898984734
  116a1234d1586c0c0e96bdc5cfce3a80f1bb498846f00b3667193eaeab6e9bb2:
    family: pert
    a: 36.074314504665374
    b: 51.534735006664825
    c: 93.36304988488683
  cfeaefe45475c0d9572ba21b086a8a3a4fb4a317b8e12af7b80b0e7ff3a931ba:
    family: pert
    a: 32.38942159102153
    b: 46.2706022728879
    c: 85.74495584653192
  23d35bce3b5b302c39650bf4dfabdfb20d14edefea1199044748b807bfc312e2:
    family: pert
    a: 47.75792109422808
    b: 68.22560156318298
    c: 109.76524111712538
  25effe9c280508a98bf205775ac464824402d361f4bc8e8a8d0c2cc362b51508:
    family: pert
    a: 6.114105764484611
    b: 7.642632205605763
    c: 11.669452174243293
  1a3df1664567fc5304f249d7c9e63671e726cd3d9da8feba309f4218466a8bee:
    family: pert
    a: 9.722491047733783
    b: 12.153113809667229
    c: 21.63589439331707
  0985bb6119e5161995052c816c7d5aee7ac1e5265350302124692f88cb22782d:
    family: pert
    a: 10.521377850234646
    b: 13.151722312793307
    c: 24.132862828649184
  9d0c2afb12acefece5172e2fe880ad0bcc31af03bf685a56ba39aee6ee9f825d:
    family: pert
    a: 9.78692761683029
    b: 12.233659521037863
    c: 22.19420271367102
  ead14cbce5d2ecf9e767e33d49483e81c7a05110eb80d4cb3c67d84cdfec9e1f:
    family: pert
    a: 40.4088964000457
    b: 50.51112050005712
    c: 60.96849379136061
  c4ec1984a24e5ff34090e3a248c2618bf5d6d98f3c64ed984c279d05fc22b73d:
    family: pert
    a: 53.013666771893
    b: 66.26708346486625
    c: 114.0274363142582
  ead31076bd347d92a000d86fcd75b2633ae71e71dd742f4267c030b9446b3535:
    family: pert
    a: 24.970794076805223
    b: 31.213492596006528
    c: 43.76645168598023
  4c76b1d5195107ae0f9b1cbb6fc27eb40c59c3dbce969ad8436272293c865a4a:
    family: pert
    a: 29.480572162614067
    b: 36.85071520326758
    c: 56.786106516298425
  39e815bb9051df631b6b24da3569d7ad0a0822415ae10c40f0786d0bdc532146:
    family: pert
    a: 30.58061026085453
    b: 38.22576282606816
    c: 65.65327777068765
  5bb079268db7e441f5441b5315c2e1e689c86b93575a817144e55aba579c6bd6:
    family: pert
    a: 34.96773101161313
    b: 43.709663764516414
    c: 63.14421707716887
  1889c3d19064fd9ad0ea4d52bd6973d72f4e2956a018b3d361404bd64f92f03b:
    family: pert
    a: 39.6008516299547
    b: 49.50106453744337
    c: 79.42861717987098
  ea483ef46ddd7d0a79096325523d9d49915dc9e3cf5f968ac5b8dc86600a0217:
    family: pert
    a: 21.632970023532728
    b: 27.04121252941591
    c: 38.37622977305077
  745ea7d99fa3a8ab5604d5f95befeb827b9d2e094ad9ae6737f57fd746ec4c4f:
    family: pert
    a: 24.83288798209542
    b: 35.47555426013632
    c: 86.52988397807796
  1776d50a5ac6d96e5874d33a2e27576fe4ff981e29b28ea1b9f02c7d1d82a391:
    family: pert
    a: 12.143499739239157
    b: 17.347856770341654
    c: 59.66553538265016
  caa43c4d84fc0ef0609eaa54baa23b3e244a3bc6c185e726313fc1a4d915f6a2:
    family: pert
    a: 14.99305472243754
    b: 21.4186496034822
    c: 33.855418753207566
  d3149c9ac90be8b74bbffec8d1ffb490ab438e51b69936a680ca79eb4f773181:
    family: pert
    a: 12.428742298890464
    b: 17.755346141272092
    c: 47.58366191091585
  45999ed1e5f989aee94aebfd82a4b949aa269923befb00953f6989d30336df43:
    family: pert
    a: 14.296642793096773
    b: 20.423775418709678
    c: 41.575319271098046
  82e518f4e0e17aef2a50109bbca93d5ff5f20240c59a9f4500bb04a79a79b388:
    family: pert
    a: 12.803409925683178
    b: 18.29058560811883
    c: 29.091388318378765
  3c631272844174b75968de6c83ddb0c0e7ace2a60395a35dc6ad87a752f80528:
    family: pert
    a: 20.626382283835124
    b: 29.46626040547875
    c: 52.49057160066509
  d31545cc31238db8fb7f90b5c48ab337929891b232eeb7858ca9ca37efe2d290:
    family: pert
    a: 13.127093867826071
    b: 18.75299123975153
    c: 53.13418324125605
  8dd75d84daf9b64b8b034be67801f97f0d47e27117e69c6fa999212280412a96:
    family: pert
    a: 9.859985597424613
    b: 14.085693710606591
    c: 56.52670111989205
  9182a3569be949e56a3733a6fc9f0fbf6d37fc33448a4967bed8af9b5dd1d6ff:
    family: pert
    a: 21.848778598159154
    b: 31.212540854513076
    c: 58.81096478432763
  3b8f9db9ea8a11350b659b5c760b74f8fe550018aa5f19f32017f875167de604:
    family: pert
    a: 16.60375756224318
    b: 23.719653660347404
    c: 52.51210398034257
  2337becc2a277f682fd0478da4fa748626b6363c1d5a280f5fe13dcc2586e2b9:
    family: pert
    a: 9.779535012569644
    b: 13.97076430367092
    c: 39.37926054958257
  22d6b27d1e91f71f85aa41407d24bb45c3b7428f36fb29c141d0e983a0f94675:
    family: pert
    a: 13.60361978334099
    b: 19.433742547629986
    c: 31.86817413001557
  5a5838ea60234c92114591b5f04331e7c499510fbf18ef0b309cfb72974595eb:
    family: pert
    a: 17.30327421940684
    b: 24.7189631705812
    c: 43.30269591145895
  d63a52b2d4daa845faaa1df696a765b8c16a29d77f0c4f5ceaad59ef83590cbf:
    family: pert
    a: 11.45436960155308
    b: 16.363385145075828
    c: 34.12764049901688
  c79b84d915cb3983e646f6864179fa51c38ba16bcba33761e413a0918696efe1:
    family: pert
    a: 10.423324913727438
    b: 14.890464162467769
    c: 41.8310250593598
  416784e0320648be00a53881b954b34778e61e7950be1086bec4d65b34c89f5e:
    family: pert
    a: 45.422993967728914
    b: 56.77874245966114
    c: 283.8937122983057
  e33d0c7659501c8c2886748dae792fd76d4bc30d4734c1763d88078efddfa5f9:
    family: pert
    a: 123.64979066217138
    b: 154.56223832771423
    c: 772.8111916385711
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
      worker_4: 1.0
      worker_1: 0.75
      worker_5: 1.0
      worker_2: 0.75
      worker_7: 0.5
    distribution_hash: 33eba4b10b86150f3c46ab60dfee2ff6d0458e493e55940c6c238d5f8c31b5db
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 0.75
      worker_5: 0.75
      worker_2: 1.0
      worker_7: 0.5
    distribution_hash: 499869445125c22ced4a0077825ac068396cc9fd2db6bb0cad2a5237cca68ba5
  - id: 3
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_5: 1.0
      worker_2: 1.0
      worker_7: 0.25
    distribution_hash: 0656dae03a9e54a71885a269ceb2e380ada6b5a0c46c6422a6d21e606461bab7
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
    distribution_hash: d399a53ea778b5eb085445ba9ef229189b99135b3efe73a48d0d34e786af4acf
  - id: 2
    dedication:
      worker_1: 0.25
    distribution_hash: 99608dfc579f2143b37af7bac06d21da2c5ac511b77d1b74c8fd90a3952ffa7e
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: a1493792ae4c0548258906e944686837490a0202e086fb5eb293995f268e29c3
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 8ed8bc00299d2a5d64364686b70b12dedf788c5236c5ab1ff1421dfd1d934c0d
  - id: 3
    dedication:
      worker_6: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 162e8a71b5f973bb7be0d45b0b6cdf046b61ca676f32b432d5c538fe323c7da1
  - id: 4
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 815a0e54f23a3b81783953ca0cdb64fea7f803c97ef098282ed66858c7455f8c
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_2: 1.0
      worker_5: 0.75
      worker_1: 0.5
    distribution_hash: 7f44b62b4099c9679f9e3d30f992a96560b831c7e2a41671388e00665dc0c054
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 0.75
      worker_5: 0.75
      worker_1: 1.0
    distribution_hash: cc426a2f2f3f251659199823fb31d21241c04222744c886f96f619cb21a4dea2
  - id: 3
    dedication:
      worker_4: 1.0
      worker_2: 0.5
      worker_5: 0.5
      worker_1: 0.75
    distribution_hash: ebe497e84d109a77595cd237422d2838e133f5c647476bc6af1794fb963aa713
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: ec5a968d87f0ea902a7cdbe4b679d7dbb684fc6653b7b4fc7193b6dcc2f0b581
  - id: 2
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: cfcc5e44d3cec6b2dae4b61fd23d1ffb97730c00970e0b905d88bf98667d04fb
  - id: 3
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 79092a7596e319c8fdc0dc6929c831b5e136433c8fe634c1483942bf16f21bfc
  - id: 4
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 14fdc7bae62f44cdede475ba150cfc3ed027cb18b01c817a599f49ffd76238c0
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 721be1b385d13ef831d8e6ad4f4c5aa2981b8cb5360b94c6ae05732d1719e08e
  - id: 6
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 9b568b34120bba0a51ede278f930488b98ca72ccf8b233020d2d386bba5be9a8
  - id: 7
    dedication:
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: 8a93be50a39b87476c8db30afb4274443ce85ce409b250421da4f61de7e9bfee
  - id: 8
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 832e11ef60220d54c36f2d1438fcf8baff27d5a003da71c39be34bfdebad4d97
  - id: 9
    dedication:
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 7cc76d7e602d376144f858547bf6ed994d1c3820830fceaf6041c554def3f02f
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_5: 1.0
    distribution_hash: d992213058bc625a3a5318e3e0b512a4cc365b0413a0f4e0dae76e0c12568361
  - id: 2
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_5: 0.75
    distribution_hash: b39fb8ba91e3adb9c5311b82e030cc27a9e5c93eec974e02d8da9b9632ae156e
  - id: 3
    dedication:
      worker_2: 1.0
      worker_1: 0.75
      worker_4: 0.5
    distribution_hash: 5b3ea112d6beba98f6aa760268e62bf0239888485e277ee4d1f045a1fe2d21b8
  - id: 4
    dedication:
      worker_2: 1.0
      worker_1: 0.5
      worker_4: 0.75
    distribution_hash: 9bb3fb2494289cb8b4631f7007a903c9b9752a81257f95ee3d041806ba4111cd
  - id: 5
    dedication:
      worker_2: 0.5
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: b676a466566c0c1ca88673f703f8d7a19dd3e61c697f3cfd21a49f4a10c3b9bf
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: e253d6a0172571f919b937e01c163d2cceb9bf31e6150bd7df618f9322b4ba93
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: 1db42bfb9704e53e88295c127769663fb65da756bd9c2d203d5bf3b6d6503b72
  - id: 3
    dedication:
      worker_4: 0.5
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 6be6e62dc8ce5b563dd6c4985644681de71d13abefc68eb315ddd77cbbf63bf9
  - id: 4
    dedication:
      worker_1: 0.5
      worker_5: 1.0
      worker_2: 1.0
    distribution_hash: f2c8bec63904b5e04308b2c993cfe150c40c3a84a70905dce01aaeae8e1c1f2d
  - id: 5
    dedication:
      worker_1: 1.0
      worker_5: 0.75
      worker_2: 1.0
    distribution_hash: 64da9e300bacdfcaaf0d89eab889ef69a1bb764d37df0ed36b4eca9c3609da81
  - id: 6
    dedication:
      worker_1: 1.0
      worker_5: 1.0
      worker_2: 0.75
    distribution_hash: 7ef528d60d54a0f17ed1ef46474956bea0d9578477e3b4b9611dd55db2b3a0cd
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
    distribution_hash: a0c3d8b4424cbdd245207fdf1ceef852cb30549e0a199d1d2eabbeec30df3a20
  - id: 2
    dedication:
      worker_1: 0.25
    distribution_hash: 327f9f3c7510dced3d4eb24bcf29e79328d79afc17f25e6c64c6d8ee80700aec
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_1: 1.0
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 7d743bf64c2a9dd1f74c2e33681dc1ac7c52683a7c65b2aba4db71824bacdb86
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_5: 0.5
      worker_1: 1.0
      worker_6: 0.5
    distribution_hash: 9a0ef74b30814b4ef3fffe3b8407c3c43d2128a67d787537469d1590bf2f38a7
  - id: 2
    dedication:
      worker_3: 1.0
      worker_5: 0.75
      worker_1: 1.0
      worker_6: 0.75
    distribution_hash: d5d7aba550c4b7f9765cab9e39219dc9a0bd73fb09a582fc731da7434ed241b5
  - id: 3
    dedication:
      worker_3: 1.0
      worker_5: 1.0
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: ed5c0fad568901481d4ab056a713312b442ddf1b99f62bad45248e6661ce3334
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
      worker_5: 0.75
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 41c00102581a0a27e0d755f9ec15eb1afec5dba8969282bafce21d232791f49e
  - id: 2
    dedication:
      worker_2: 1.0
      worker_5: 1.0
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: e64d5bf44d539f152788ee5ff89e834a6b81f426ac039b95299b89436fb2b54c
  - id: 3
    dedication:
      worker_2: 1.0
      worker_5: 0.75
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: 7c847a293a7bf743ed3d170e61336e856bdf3b5e5c86e26bd0151502eb0b0fb4
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: d4b3ef89c4e218e062891a07971e35120495b61dea9f923a19b2b73867669eae
  - id: 2
    dedication:
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: f7b39e3f2b9698e5a183e04c01bb135ade2d5717e58bebd078e6f4f7ad8408fb
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 03ffaae63f1ebbd67a672ed563db728c060decb017a3e2e90b268a301461ca0d
  - id: 4
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 5e3f59ee3a31f8c357b5311c93407ae6e31be7973016d24f973183b6fa882715
  - id: 5
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 5f5f25a81209144a43dcb7415951b534b008bf172d65241645ee45fe8ed6dcda
  - id: 6
    dedication:
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 8e918473c16e11f338af45891f9ddc0b01abefa798356e111785246d8a0010ac
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 9dcee7dd2ca612314eccf591b4acfeaa164ff377b566283e2cd0ce18e45b144f
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: f73467514cf0e02547f2fe7baf52e5b6b1b521ed805a00db56362642594ee07a
  - id: 3
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: ef5d818cd47d1629ca9b2932365cb8fca491b79edfe747043f4c980453280d99
  - id: 4
    dedication:
      worker_6: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 15e93f4a91ca10e04cdd1eeb46919632c739cc25a2841789f7a5b7aaa0eda7a5
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: abdb2def867bcc327bf61b5b9a35ab7a64c17c9262c976cda67b8af4bbcd2a26
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_5: 1.0
      worker_2: 1.0
    distribution_hash: c094740746cbc3a4688afa840325d3dbd691ec24bc1852b7e1e9c565d4030f82
  - id: 2
    dedication:
      worker_1: 1.0
      worker_5: 0.75
      worker_2: 0.75
    distribution_hash: 06e31cdcf8adf10ec9ceec63acf7f2d596d7e9f0425857ac8cfef140f3713507
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: e16b24a013342b6bdd285c8b52e0eeed0bc8f4a2ebeaac47d0e4becbffdb3b1b
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: 7fdb48e4e2c8cfd73c453899c3bb98f8c8b3ad382a991a9c544a52ebacf61e17
  - id: 2
    dedication:
      worker_5: 0.75
      worker_1: 0.5
    distribution_hash: b45b84f7bd37845bb88eebd9764e4f5f4c822a467d95b4b7439febd988a1826d
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 7688c9c009ea4ef3e97b63ff8146f6b756fff8ffd79de1b64cdf3983c2e30567
  - id: 4
    dedication:
      worker_2: 1.0
      worker_4: 0.5
    distribution_hash: f45af4a62824239e049ad61f0f61a576c5a3a2e2af6915283d9e0a2257e812f9
  - id: 5
    dedication:
      worker_5: 0.5
      worker_2: 0.5
    distribution_hash: a0dd10d31f9ac50b8552aee1b699659012e9813a37943b70bc55a400658f09d7
  - id: 6
    dedication:
      worker_5: 1.0
      worker_2: 0.5
    distribution_hash: d4b10d4275f136bd0bf2e61c0e5419e3516824e297b498a59a47c5ed43ffc066
  - id: 7
    dedication:
      worker_5: 0.5
      worker_2: 0.75
    distribution_hash: 07bc99665477cc291ebce2cd94113d0d832184f7dc9168901dbbefc811d311b6
  - id: 8
    dedication:
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: beb83833fa15195be52899d77bb199496ae038b2f6c4b2ac296781d5067d4a97
  - id: 9
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: eff9e446981f97efc31fd487b0221cc2657d75dc3304b1979938cd2abbe537c5
  - id: 10
    dedication:
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 20b3ca7b41d72077d18235c075d7648119dea364b285f1d00c2ae15de8869fcc
  - id: 11
    dedication:
      worker_1: 1.0
      worker_2: 0.75
    distribution_hash: 14b328e344a2424f3e9535cad124e1382af7c682954a0cadc9a4af73f78a6807
  - id: 12
    dedication:
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: adb193a7a2b81588a3eaf3f346c474a02104e9050e95af8421c8c410621d790c
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_4: 1.0
      worker_2: 0.5
      worker_1: 0.5
      worker_7: 0.25
    distribution_hash: 5a4c2d255ca0a2c59ef6fe5547a7f43ee40fcc9eb6fea422709a4c584de50613
  - id: 2
    dedication:
      worker_5: 0.75
      worker_4: 0.75
      worker_2: 0.75
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: f84d44263443a9b34fd2cfe03cbaa90a515be367f8493ae221727d7c09b1b760
  - id: 3
    dedication:
      worker_5: 0.75
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: bfb9002edba07b5aae32537340a0c615aacf4b5372acf5aefad622fe4053e69d
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_5: 1.0
    distribution_hash: f7f2bd1b4db7c76bf71e879ea123f9616c01a055e847ecddffb3e4aaf52b2ffb
  - id: 2
    dedication:
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: 7ce661b97bf22c0be0215c0869e7233a28c1c8926d36c85a54dbabc5e95b515b
  - id: 3
    dedication:
      worker_2: 0.5
      worker_5: 1.0
      worker_1: 0.75
    distribution_hash: 4375f0ecdb7514e0ac87d33c834759901d2a6d274af570fd0073b21a0f038130
  - id: 4
    dedication:
      worker_2: 1.0
      worker_5: 0.5
      worker_1: 0.5
    distribution_hash: dc788362a069b14e65889ed39357defe4f9478e75459a67c928e06079b2c4a77
  - id: 5
    dedication:
      worker_2: 1.0
      worker_5: 0.75
      worker_1: 0.75
    distribution_hash: b505b3402342a2123dc0322488ecba1a831006bc9c9d1d2e69cf5e75b8d3f309
  - id: 6
    dedication:
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: bbc58db3fbd3c45c951c949136af5f0e7d36d6cf277ed5766143c15f859cb78f
  - id: 7
    dedication:
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: 9586189e2ff8f39c8b5633ba400adf7ea308545f2c6cf57f32dbe2bca2833a39
  - id: 8
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 6828b192ca7cf12a73f2ca723e8ab30e67aceda71e56141b9fe19b20b32acee6
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: 62b239df6812b141617d6f60bf0213c6b7f3dc59bb665e1eedac167980a43154
  - id: 10
    dedication:
      worker_1: 0.75
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: ba8dafb3d0ae96d026a108aedff4ee8d7bca067a2b6837ffd0728f9a951cbbf0
  - id: 11
    dedication:
      worker_5: 0.75
      worker_1: 0.5
    distribution_hash: 17b62974ca43a8cc5ec9759dc53c5c68d3e429787b96f9f863f73e60e34e78d5
  - id: 12
    dedication:
      worker_5: 1.0
      worker_1: 0.75
    distribution_hash: fbcf109a47a98743e5e2572a3505faa33bf7f999fc8330fe4bc2f89466c6ca0e
  - id: 13
    dedication:
      worker_5: 0.5
      worker_1: 1.0
    distribution_hash: dafdc0fd6f7b3f6f9e68e6eb20b83ddc76ac2c604edbc388f445b81558303a32
  - id: 14
    dedication:
      worker_5: 0.75
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 3f803206a163485b150638399958558e74e13ec39f5b994427e7dbcea46588c5
  - id: 15
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 6b05bded75fd9679156ffb6a32e5a2995270ce8081e5eaf8e94e6dfb4bc37f8b
  - id: 16
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_2: 0.75
    distribution_hash: 282e39567de3f12445f27bcf241f34ba9bf3f4e276ea48e27b771c7d966664d1
  - id: 17
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 87911578900cb3d8026b3da7c8b6aa27bdb0a3546e7f83cfe66d8d7aaf35f2b2
  - id: 18
    dedication:
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: 2373e3d70c8c81813648ecc84804d029f98eec3ba51838ae7921c4e8852827e9
  - id: 19
    dedication:
      worker_1: 1.0
      worker_2: 0.75
    distribution_hash: 34b5ec0c2a9d337b153022912b20fbb116999da705dea928d880e8ea017bcb3e
  - id: 20
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_4: 0.5
    distribution_hash: d31ebf5695803e61949936037be62205e6f77e6baf94ba3da90c88759ec9f785
  - id: 21
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 91c1b67041887e3260a6240bf45fa7fff756c936bb4bacb3b554b8f690d3760a
  - id: 22
    dedication:
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: f79f15781f4aee61d274740884d11c3a84213771b84f5b2400a8c0d3561c4625
  - id: 23
    dedication:
      worker_2: 0.75
      worker_4: 1.0
    distribution_hash: 33d636d28113c4352961b6590ce21ba6923581ae09e88cd1665914233008ab40
  - id: 24
    dedication:
      worker_2: 0.75
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 9056c4d9dc7c8226fdcf280eced68e5c4e5361a5f2d517faf81b75c2e18c6619
  - id: 25
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: d3c4fe951f13cb672e912d87fe3c93d18f0f466e82d45c0e1ce8fb43b6cb9baf
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: 8b67437f4dbe8974c447d0a5bba1a6df471d20013c33649d155bc856eb30fbd5
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: a78e978b94790bb65efbcd9a686961f1b7eed686ef25ccfe75994667507f9875
  - id: 3
    dedication:
      worker_1: 0.5
      worker_4: 0.75
    distribution_hash: 33cf684b10cb6de0d5a13399252913a29ad39b458ed87bab799a3df6616d4790
  - id: 4
    dedication:
      worker_5: 1.0
      worker_1: 0.75
    distribution_hash: 95ac8670ded34f6e3ce2807ee05ca15c2db17af781bdb7506a4227a8341f8e66
  - id: 5
    dedication:
      worker_5: 0.75
      worker_1: 1.0
    distribution_hash: 9f5b9ddada57a72fc2e72d9f98f754875164f47925d57752a5b6ec9127bd3e84
  - id: 6
    dedication:
      worker_5: 1.0
      worker_2: 0.75
    distribution_hash: 3a14965006cb7bb487fd04d4b52149ebbb1042dfe51d4f4fdade8266354d69f7
  - id: 7
    dedication:
      worker_5: 0.75
      worker_2: 0.75
    distribution_hash: 68737ddea44bd04c829ec8916c2fa80cb9b5b37af2e6d8f6b49eac78d2f127ba
  - id: 8
    dedication:
      worker_5: 1.0
      worker_2: 1.0
    distribution_hash: db962db6afd204ad819090ab8622d97411b76de566ea500cc0d9e16d611b595e
  - id: 9
    dedication:
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: ae71a09ed369459c020c52f994a7ad617b4306f857dc2073d0f88404540407b5
  - id: 10
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 742755e5ffdcb8c361ccd812b87e79c51663f93d4e20b461a7a8cd205dc61cfa
  - id: 11
    dedication:
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: d6e8c0776a8a2e1f33b27334a55659454d89bd90ebb8a6dcd93ac586f785e87a
  - id: 12
    dedication:
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 81fe20ce99d6d4011a18774df9d882953dec9d809befefea1692bc2f33b3ffbe
  - id: 13
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: f8aba8f0455cf345251667076911ada16ebaad23359642158638e4dff39c6e4b
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: c73f9c06f2886a913585d02ebd9ca4d93cacc3a52264efba4d728fa6e4057903
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 0.75
      worker_5: 1.0
    distribution_hash: 5eca47196f855a8d85affc9a55f3846e004c98bcf7482c7e234750f7860dfa7c
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 0.5
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: a37f63d6e299173ce6ef3ba72f5a3cf8d84a71568984652536c4e446ef43d427
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 6f79cfd4ce4de66910a01096f0806c03386a64849b3caf9d29bf5b590adf7a79
  - id: 2
    dedication:
      worker_4: 0.75
      worker_2: 0.5
      worker_1: 1.0
    distribution_hash: f1df208f70835c08bcc62655c37fd28206c128fc38578f2594111ceed7fd3aba
  - id: 3
    dedication:
      worker_4: 0.5
      worker_2: 0.5
      worker_1: 0.5
    distribution_hash: 0165cc4dfb93dcd17534da38d21784cfe70b8e1c7f893ccb0ca42c88d6bbd41b
  - id: 4
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: ee61542958da6ef81a009798f91e84da27db010c2c535ed76f588d4d2b814b67
  - id: 5
    dedication:
      worker_5: 0.5
      worker_1: 0.75
      worker_2: 0.75
    distribution_hash: 39c2dff767bb659910d3be04484ddbf40b7647813c28597839647fcb4d124ad8
  - id: 6
    dedication:
      worker_5: 0.75
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: d77179e4bc670d420c54c58d179aa1c6e9287c63900edd526a5482aa06fe540f
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: 116a1234d1586c0c0e96bdc5cfce3a80f1bb498846f00b3667193eaeab6e9bb2
  - id: 2
    dedication:
      worker_5: 0.75
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: cfeaefe45475c0d9572ba21b086a8a3a4fb4a317b8e12af7b80b0e7ff3a931ba
  - id: 3
    dedication:
      worker_5: 0.75
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 0.5
    distribution_hash: 23d35bce3b5b302c39650bf4dfabdfb20d14edefea1199044748b807bfc312e2
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 25effe9c280508a98bf205775ac464824402d361f4bc8e8a8d0c2cc362b51508
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_3: 1.0
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 1a3df1664567fc5304f249d7c9e63671e726cd3d9da8feba309f4218466a8bee
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 0.75
      worker_5: 0.75
      worker_6: 0.75
    distribution_hash: 0985bb6119e5161995052c816c7d5aee7ac1e5265350302124692f88cb22782d
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_5: 0.75
      worker_6: 0.75
    distribution_hash: 9d0c2afb12acefece5172e2fe880ad0bcc31af03bf685a56ba39aee6ee9f825d
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
    distribution_hash: ead14cbce5d2ecf9e767e33d49483e81c7a05110eb80d4cb3c67d84cdfec9e1f
  - id: 2
    dedication:
      worker_6: 0.5
    distribution_hash: c4ec1984a24e5ff34090e3a248c2618bf5d6d98f3c64ed984c279d05fc22b73d
  - id: 3
    dedication:
      worker_3: 1.0
    distribution_hash: ead31076bd347d92a000d86fcd75b2633ae71e71dd742f4267c030b9446b3535
  - id: 4
    dedication:
      worker_3: 0.75
    distribution_hash: 4c76b1d5195107ae0f9b1cbb6fc27eb40c59c3dbce969ad8436272293c865a4a
  - id: 5
    dedication:
      worker_5: 1.0
    distribution_hash: 39e815bb9051df631b6b24da3569d7ad0a0822415ae10c40f0786d0bdc532146
  - id: 6
    dedication:
      worker_1: 1.0
    distribution_hash: 5bb079268db7e441f5441b5315c2e1e689c86b93575a817144e55aba579c6bd6
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.25
    distribution_hash: 1889c3d19064fd9ad0ea4d52bd6973d72f4e2956a018b3d361404bd64f92f03b
  - id: 2
    dedication:
      worker_1: 0.5
    distribution_hash: ea483ef46ddd7d0a79096325523d9d49915dc9e3cf5f968ac5b8dc86600a0217
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
      worker_1: 0.5
    distribution_hash: 745ea7d99fa3a8ab5604d5f95befeb827b9d2e094ad9ae6737f57fd746ec4c4f
  - id: 2
    dedication:
      worker_5: 1.0
      worker_1: 0.75
    distribution_hash: 1776d50a5ac6d96e5874d33a2e27576fe4ff981e29b28ea1b9f02c7d1d82a391
  - id: 3
    dedication:
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: caa43c4d84fc0ef0609eaa54baa23b3e244a3bc6c185e726313fc1a4d915f6a2
  - id: 4
    dedication:
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: d3149c9ac90be8b74bbffec8d1ffb490ab438e51b69936a680ca79eb4f773181
  - id: 5
    dedication:
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: 45999ed1e5f989aee94aebfd82a4b949aa269923befb00953f6989d30336df43
  - id: 6
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 82e518f4e0e17aef2a50109bbca93d5ff5f20240c59a9f4500bb04a79a79b388
  - id: 7
    dedication:
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: 3c631272844174b75968de6c83ddb0c0e7ace2a60395a35dc6ad87a752f80528
  - id: 8
    dedication:
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: d31545cc31238db8fb7f90b5c48ab337929891b232eeb7858ca9ca37efe2d290
  - id: 9
    dedication:
      worker_5: 0.75
      worker_2: 1.0
    distribution_hash: 8dd75d84daf9b64b8b034be67801f97f0d47e27117e69c6fa999212280412a96
  - id: 10
    dedication:
      worker_5: 0.5
      worker_2: 0.75
    distribution_hash: 9182a3569be949e56a3733a6fc9f0fbf6d37fc33448a4967bed8af9b5dd1d6ff
  - id: 11
    dedication:
      worker_5: 1.0
      worker_2: 0.5
    distribution_hash: 3b8f9db9ea8a11350b659b5c760b74f8fe550018aa5f19f32017f875167de604
  - id: 12
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 2337becc2a277f682fd0478da4fa748626b6363c1d5a280f5fe13dcc2586e2b9
  - id: 13
    dedication:
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: 22d6b27d1e91f71f85aa41407d24bb45c3b7428f36fb29c141d0e983a0f94675
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_1: 0.5
      worker_2: 0.5
      worker_5: 0.5
    distribution_hash: 5a5838ea60234c92114591b5f04331e7c499510fbf18ef0b309cfb72974595eb
  - id: 2
    dedication:
      worker_4: 0.5
      worker_1: 0.75
      worker_2: 1.0
      worker_5: 1.0
    distribution_hash: d63a52b2d4daa845faaa1df696a765b8c16a29d77f0c4f5ceaad59ef83590cbf
  - id: 3
    dedication:
      worker_4: 0.75
      worker_1: 1.0
      worker_2: 0.5
      worker_5: 0.5
    distribution_hash: c79b84d915cb3983e646f6864179fa51c38ba16bcba33761e413a0918696efe1
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
      worker_7: 0.5
    distribution_hash: 416784e0320648be00a53881b954b34778e61e7950be1086bec4d65b34c89f5e
  - id: 2
    dedication:
      worker_1: 0.25
      worker_7: 0.25
    distribution_hash: e33d0c7659501c8c2886748dae792fd76d4bc30d4734c1763d88078efddfa5f9
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
  - task_14
- - task_1
  - task_15
- - task_1
  - task_16
- - task_1
  - task_17
- - task_1
  - task_18
- - task_1
  - task_19
- - task_1
  - task_20
- - task_1
  - task_21
- - task_1
  - task_22
- - task_1
  - task_23
- - task_1
  - task_24
- - task_1
  - task_25
- - task_1
  - task_28
- - task_1
  - task_29
- - task_1
  - task_30
- - task_1
  - task_31
- - task_3
  - task_11
- - task_4
  - task_12
- - task_5
  - task_13
- - task_6
  - task_10
- - task_7
  - task_9
- - task_8
  - task_9
- - task_6
  - task_27
- - task_18
  - task_9
- - task_2
  - task_26
- - task_9
  - task_32
- - task_10
  - task_32
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
  delta: 752
validation:
  project_key: 36e6a25b5a632570cc7089ab9275ad457ccb1ec0d5faf87f9c92898687f87898
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 50 days; worst-case serial bound: 1607 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
