# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_99
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
  relaxed_constraints: 4
  modes: 162
  tasks_at_cap: 0
  rewired_edges: 8
  departments: 1
  quality:
  - worker_3
  safety_skill: 2
  review_tasks: 3
  liaison_tasks: 3
  extra_tasks: 3
  barred_pairs: 6
  incompatible_pairs: 1
  edges: 60
n_workers: 7
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 517
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
  b9265255a8f9150d1ed24205ed11bb95aeb216aef7aa911ee03ba2938f7262a9:
    family: pert
    a: 28.745557972061935
    b: 47.90926328676989
    c: 142.0595557782116
  a693aecb52c0d782bb826b7994f1c260bdafd2ac417c48608c2a1f2130d274ff:
    family: pert
    a: 30.042795150062737
    b: 50.071325250104564
    c: 149.14301238860202
  73608b6bda91b451f95d72ca949c9710f57c4b5a6976d7a25fc1eda4aaf8da79:
    family: pert
    a: 24.569311144107242
    b: 40.948851906845405
    c: 158.79156039023562
  68133ee6dce39ae028ff26699e74c9c3c30b0ec44edbad0b68116f40620945ea:
    family: pert
    a: 17.250445112296116
    b: 24.643493017565884
    c: 43.63400163190003
  0efdc88488dd1da4d9771c784ce99f054b0707d94327f4922d4f6c119b8bf72a:
    family: pert
    a: 10.06082377586656
    b: 14.372605394095086
    c: 39.766045293913734
  b8ed1d868e499f691ca8eee7cefdfc9155c1859f7e3433d1407c2fe7c11ce460:
    family: pert
    a: 12.119055657595997
    b: 17.31293665370857
    c: 41.82093852099787
  c7b11aa7af09001ba9b2f35c7ceae4592333a9a077a462e22dfb85971b8fdc32:
    family: pert
    a: 28.056373902164882
    b: 35.0704673777061
    c: 175.35233688853052
  9c055579b6e32a6a84182413e05b26cf8e22f547ac0b3e441b0655faa963cc69:
    family: pert
    a: 31.96272304046879
    b: 39.95340380058599
    c: 199.76701900292994
  25e16801be06aad4ec79efcf25b341ee6fc9f3c44601718df60e05a0266f9dc5:
    family: pert
    a: 35.15056900742926
    b: 43.938211259286575
    c: 219.69105629643286
  9252901db7df134b5e169854c2f24c7c54d5b63f78d59a9d68f04f35e254401f:
    family: pert
    a: 34.561578342453146
    b: 43.20197292806643
    c: 216.00986464033215
  ba5c40b4eafdb7338f8c4b0b1ab3a24af8561061f2748241cb735fd737877a5a:
    family: pert
    a: 34.132164181726885
    b: 42.6652052271586
    c: 213.326026135793
  757d4cf8c0421686aa98302210afadbb1a897c6de2e8892d11dcc1edf4eece6a:
    family: pert
    a: 33.04226084182058
    b: 41.30282605227572
    c: 206.5141302613786
  d9aabd946ace9b3766857a13e169cfaa1179cc960d34ad2d1222d6c25bc5a5af:
    family: pert
    a: 23.047002564921613
    b: 28.808753206152012
    c: 144.04376603076005
  4a9e9162124471e66069fd494274e622b90e5b2f7d82dccdb95cee4f11a76f1d:
    family: pert
    a: 26.665971285953606
    b: 33.33246410744201
    c: 166.66232053721004
  a6ffde019c73749b5029d94a49acf7862cc16666a23bf12b73003b4f341ba1a7:
    family: pert
    a: 28.671714272678216
    b: 35.839642840847766
    c: 179.19821420423884
  688ded8f6f476b3e7da2d0eeba230d2ec1fe71601dabe952382d24b00ba654c7:
    family: pert
    a: 40.876509553416355
    b: 51.09563694177044
    c: 255.47818470885218
  04ad269ccefa60b49614a9a019e574b9d3e3fbbec0c05e180d95f8387fa77eb9:
    family: pert
    a: 39.12841052848021
    b: 48.91051316060026
    c: 244.5525658030013
  bc1ad4321f1948b03dfc77eae7449e1d814ddfa5c3364c554713ef1fd9e67447:
    family: pert
    a: 31.563946876334512
    b: 39.45493359541814
    c: 197.2746679770907
  67f0758f6036a1dde0156aaf077ae5cabb6dd9ab0aecad5b71d0b60612930e65:
    family: pert
    a: 7.871553077280244
    b: 9.839441346600305
    c: 22.638914167441378
  bf204599b5064dcbb178e11119a06a119bf16d1d55ae0282cf7db06b127299bd:
    family: pert
    a: 32.19131872666548
    b: 40.23914840833184
    c: 47.883598572663026
  66ec07537265f666ebdd3af46fcac13ceb1315c16ffb1e72e01dfa0ee3cb73be:
    family: pert
    a: 24.437294838619486
    b: 30.546618548274356
    c: 56.26894803801688
  c145a319161ab6123241611e7fa42e7098b230c4c1d5023a9f887740f36892cf:
    family: pert
    a: 27.679163648931343
    b: 34.59895456116418
    c: 50.27502516993861
  b1ef03738fc0d3320114a46f1684ac3bdd8505a6bfc6da49946e1aec390151dc:
    family: pert
    a: 34.54247710366012
    b: 43.178096379575145
    c: 77.55910480184197
  1e5427765bef23cd4711e22d763f706ccf65737beca6617380df05db41548d2f:
    family: pert
    a: 27.671883250475005
    b: 34.58985406309375
    c: 56.48850468160317
  fe9846d91342bc131a4b662ae8fd02b3bffa6c957ffe4aedcc1c8b110485d756:
    family: pert
    a: 38.05861909601499
    b: 47.57327387001874
    c: 70.67794530096504
  131db1f288a36c68f733054ba45524087dfd7ecd692ee22da7a65389cf973173:
    family: pert
    a: 28.95538324174612
    b: 36.19422905218265
    c: 49.22309037062946
  bf5365f7736feb3cf16a3339ab453618ae9c1c08a7bf69965fce0d2671d22d53:
    family: pert
    a: 19.424701973987823
    b: 24.28087746748478
    c: 64.77585529230198
  88df6d9794df485630a2c7a0b8b8be55cbaca161564e645676f46d450a8d8a44:
    family: pert
    a: 33.377280121949184
    b: 41.72160015243648
    c: 86.37424937217676
  bde8f17a9387eba3affc95f5a1ac36b95fba448deeaacdc3655b62122185827c:
    family: pert
    a: 21.977291603814386
    b: 27.47161450476798
    c: 60.96091758277365
  f8ad41d8b824571ba55ae0a24e25c461537e40069dac209e389e4e6cc2c3706a:
    family: pert
    a: 34.346418054900504
    b: 42.933022568625624
    c: 97.60453621697305
  bef9a50c0a6acb95800a01e071214230d5b3f8f12ae1040cb5cf8c7fe13e8c9e:
    family: pert
    a: 27.973364419553715
    b: 34.96670552444214
    c: 50.241096900437974
  e1a0f38fe4f363e275c78b592a0f45ca3b0c3f7364054f307d8e8d3d01a6b0fa:
    family: pert
    a: 27.776444864312186
    b: 34.72055608039023
    c: 53.82000274639346
  ac131ded2a5b6088e19e2d8ba32f560a06d46f2aeeecc7cd32ef1d7a75763317:
    family: pert
    a: 33.45347602011793
    b: 41.816845025147416
    c: 55.902390552279236
  4f84b5c233afb5d1047f8acb2d9248cb50bc54c38d96b4d269c3b4139790bce9:
    family: pert
    a: 25.38736611508486
    b: 31.734207643856074
    c: 47.65898933387751
  623fe4fffbfacfb55ed4e1ef4b224d8d18c33a13ba617b7c72f5dd0f97281199:
    family: pert
    a: 27.800062743894316
    b: 34.75007842986789
    c: 63.72729072246928
  ce610ba8d51a08be41e343a19f711aab78a6e510fc4da66313e4e67eacce6285:
    family: pert
    a: 28.889210751518842
    b: 36.11151343939855
    c: 67.96652844421162
  ba19fbb6d8786e7048b913bb7918a8f38f6a64e59bc138123ed211e49709dfc3:
    family: pert
    a: 22.599918568015827
    b: 28.249898210019783
    c: 45.33790925532569
  65847ac6861a316f2aa9511e574f15c99a2e39f2812219e5380aa6c724257f36:
    family: pert
    a: 42.00338255898593
    b: 52.50422819873241
    c: 67.10695453724485
  69718db6c8573346d7a9a083cee3a5736556791e800f0d4a7b1a441ddcd59453:
    family: pert
    a: 25.54293769874241
    b: 31.92867212342801
    c: 63.849988910696865
  6eed4d794ccbd614734293edd7d53dc9fdd54cc45d4439e87082bd3ad7f4b4f5:
    family: pert
    a: 29.43193959554118
    b: 36.78992449442647
    c: 54.42880993488275
  444e7469c8dbc80b9d5623ce1f91ca1a0f3cb4758f8a674ab4bc973526318e8a:
    family: pert
    a: 68.13079835162618
    b: 85.16349793953273
    c: 102.12477206122783
  5566be00cc754987887c43e2016f445b488d10160a8500bcbf9302bfcb9ca4d0:
    family: pert
    a: 22.40498794436691
    b: 28.006234930458636
    c: 52.001297846011
  60f9cdb1f3a50626a5dfee17fc5999ab319a44e5c8a817f72656d41bdd2572cb:
    family: pert
    a: 25.196368630937506
    b: 31.49546078867188
    c: 60.75596711201461
  0c81f55102d6bcf522a3b971de5a96ddd0d9e446a8ddaed95d0711b274421746:
    family: pert
    a: 28.95245542009107
    b: 36.19056927511384
    c: 51.03606878437526
  8edcfc72399d4bf2eb853d8672695df653d77ed63c02c89cab2b9adc527dbfc0:
    family: pert
    a: 35.54375037313434
    b: 44.42968796641792
    c: 66.48814363812507
  60124231404b30b036b4591ae67c8a8bac0c158bc201db63c62c127d509347b3:
    family: pert
    a: 36.52351335224449
    b: 45.654391690305616
    c: 62.0167571121986
  60a1894dd84e6a09f0f10bb52ab1c23ada62054e0c5e3c112cf14b9f94bdb54b:
    family: pert
    a: 33.107688296004305
    b: 41.384610370005376
    c: 57.913918011698506
  4bc27694464b3b53599ce65189527fc183cc8b207b6d31307d55accf506019da:
    family: pert
    a: 72.01677571043511
    b: 90.0209696380439
    c: 112.07170281069031
  8751593f321f4df37d4478ef12d10b135eb3f25cc37eb24e341c6cabad040a83:
    family: pert
    a: 41.39341783288452
    b: 51.74177229110565
    c: 68.43142353427355
  ff5d7e98b4a5f72323bf71986e24eff8c15282640c05e7e01a52eeca7178e782:
    family: pert
    a: 55.33234014637251
    b: 69.16542518296563
    c: 93.23064432608558
  410ae23164f1abb1fb3c4a1e7a265213771b95d2756bae8669cc039d7dd55ade:
    family: pert
    a: 40.59487557932306
    b: 50.74359447415382
    c: 65.24129049887244
  cdbff505b197fc3061605c5e0c82c6cd46fb2e0fddf24201ec15c4277c5aeee1:
    family: pert
    a: 37.341515618330504
    b: 46.67689452291313
    c: 85.69710809356074
  7eef548a46ea1cb5b6f5398749137b5c504779e843e39712c202f5dbb1db4799:
    family: pert
    a: 34.660751358099965
    b: 43.325939197624955
    c: 66.22901792037699
  163ca3c6cdacafe7b75ed40a62032849ac13dd7bb4a65305265e1be3dac1c0d0:
    family: pert
    a: 43.82857339599923
    b: 54.785716744999036
    c: 75.13623113888166
  9ea38d09ee58c79b3f1599013347a722075bfc162ecdd1b2cdb4ef8b5cb69e0c:
    family: pert
    a: 37.34828289008815
    b: 46.685353612610186
    c: 56.079077885076295
  c52900bb5896d14b9dea5d97f11b0e17c13b0ad3e72406d804151dbaf7ec2ed9:
    family: pert
    a: 35.608023309637225
    b: 44.51002913704653
    c: 74.79686993104227
  1f4f73b35dcbbeb0fff43e4a9abd594a9d8e2889c5d0da9e6ccd932095d32206:
    family: pert
    a: 33.044591131466134
    b: 41.305738914332665
    c: 61.24098745466239
  7d853c9b51285650f45aa4918372a22b2a5e8f212a04ad62cfda87f7cfc2ec7d:
    family: pert
    a: 29.37764831477025
    b: 36.72206039346281
    c: 67.9501209129303
  b3c9dca4e6001c6db1b95441db6ec46283133f6a31e9b547463394784e371b66:
    family: pert
    a: 39.511399875806994
    b: 49.38924984475874
    c: 82.23340829640055
  21a3d00b0b47e74b612a60c41a7e05c88abe10b74df7fce16f10277a2ca63ad1:
    family: pert
    a: 36.354850155166986
    b: 45.44356269395873
    c: 74.1123046176568
  311d2a933c63f205318d6bed43cb822ff12848dbcf6058ab82bc070a81562c20:
    family: pert
    a: 38.16483066856029
    b: 47.70603833570036
    c: 81.54130897298938
  9c6bb189e43e157a25b9894fc24ae138ee8230e111b722e0ee2c6e448ac5d3dc:
    family: pert
    a: 32.67373286805488
    b: 40.8421660850686
    c: 58.495952230444274
  13d30d0d1fd576e9c916bfbe11b5408c72d23b9e6a75597ec99751adabef784e:
    family: pert
    a: 64.13917575201498
    b: 80.17396969001872
    c: 102.77848110514851
  408d2d3b9f005172f5d71f5c7c1cd871a23a61b70f5a76e609ee06fa0dd69245:
    family: pert
    a: 51.125475857463044
    b: 63.906844821828805
    c: 83.00096244471429
  0383226b79f0ca80c9a05ecf7b253e94c37140db14babbffffed15823cf9d2c3:
    family: pert
    a: 33.95388482061761
    b: 42.442356025772014
    c: 61.9370176128525
  180170165bd3904847d0e15cbfbbcdd9edf873452179071c539a1f72af1434e5:
    family: pert
    a: 26.993317314237306
    b: 38.561881877481866
    c: 75.64121987725895
  f872708a522b282e3d30f338f3ae96a440c08064ce0d59703adc83f1a713ab14:
    family: pert
    a: 19.715638681391543
    b: 28.165198116273633
    c: 72.22886021363034
  8ed01efdbb4516e633aba6faa1fb4064115585a1cc85a7e6a79e5f83f322a5cf:
    family: pert
    a: 28.13138070145396
    b: 40.187686716362805
    c: 68.98243661145501
  e4ec4816e95795365341aee9dfa4bc2b441508d6c84ba00a7bb455962b1dade9:
    family: pert
    a: 28.605379173807258
    b: 40.86482739115323
    c: 94.93959691349602
  e945462fa04e2ebb59438ac4883f8b5de03d4cc1c3bd600c007fc5ade892461c:
    family: pert
    a: 24.680328248782267
    b: 35.25761178397467
    c: 91.25896534697162
  64354707dcb10df8a50c16a3f83b49391765e2735759a0026090d9c0e24e4bcf:
    family: pert
    a: 40.618746815812706
    b: 58.02678116544673
    c: 113.46396697997794
  2a869691dee7accd3cefe717526e700cb4e3914cecc323c50edbe202652ea134:
    family: pert
    a: 36.595155761610734
    b: 52.2787939451582
    c: 112.83068262994786
  b0c0ea0a6da44e1b019228fc3853bfd48f586857d539e38e088cf669d0fbede4:
    family: pert
    a: 18.434007129787602
    b: 26.334295899696574
    c: 81.39463776539624
  88893dd81fee076cc214fbdd5110ed0accafbd29eceecf754956b7645b1c1438:
    family: pert
    a: 27.331984316605226
    b: 39.04569188086461
    c: 126.05868988444925
  13ed7cfa74dbb8ca0e31fa51812e7c7375f36aa67d75e843290db83f984362e0:
    family: pert
    a: 25.18525220463018
    b: 35.97893172090026
    c: 91.98002992935218
  d0d3512bba5294ddcc323bcaaf40cecf8054198cfcfdb8540ec6af7d2846ab50:
    family: pert
    a: 23.471878832740497
    b: 29.33984854092562
    c: 41.087893281109984
  4951105863d9734947f7c52a4548e8bcff83e7f566d403ad927d09121f76e697:
    family: pert
    a: 17.20457511461812
    b: 21.505718893272647
    c: 47.69933641089045
  09e0ec82c0ffa96c3d47eb59eb3d9891eaa92bcba5351691d67ef271290d652f:
    family: pert
    a: 3.232339238879712
    b: 4.04042404859964
    c: 6.7392736028634745
  ff7012f04945dfb529aa26ae5174815f02de7d1c65d49abcbd999b33433688de:
    family: pert
    a: 4.401487106681385
    b: 5.501858883351731
    c: 7.7439534812079405
  c96e48bc5a41b0e0149d0489a9a6d8da190bb4f82c3006379d0155e4d1bc7c72:
    family: pert
    a: 4.053157534733985
    b: 5.066446918417481
    c: 6.363161003256607
  a2a529ea25bead01bdf2113b4a7ffc95c14b3933bbe4b710572fed3526e92931:
    family: pert
    a: 3.1396394699725114
    b: 3.9245493374656393
    c: 6.953986471042337
  2a16eecd16e7893e120ba543e50b4dcfb1747d479c6935c2dd6f182df863cdb7:
    family: pert
    a: 3.866402771049255
    b: 4.833003463811568
    c: 7.561223461302237
  59ec8b1572d242d82c918c059bff851fa7ccd9e94cdeb11ab54d40421a472245:
    family: pert
    a: 5.435213673714017
    b: 6.794017092142521
    c: 11.215338678504796
  b3063df2dd98ee1de03a9d388e9416d9ef56be646b611333eca35ec190f524cf:
    family: pert
    a: 3.3547189774780812
    b: 4.193398721847601
    c: 6.21390228155507
  97cf675534b7546f27f6b99a29138b1fbe2bbe2a9236d5c12d6961b0f543a952:
    family: pert
    a: 4.34177084385485
    b: 5.427213554818563
    c: 7.962503855300801
  b707ee73e18fa2d064475b8d25434fad975c368813a0f9cf19b541a93d23b539:
    family: pert
    a: 5.44147043936903
    b: 6.801838049211287
    c: 11.549267009821728
  27e1acd365707229503c9e2d4c100cab47f0b3ca41912cd64b46c8c929beecbb:
    family: pert
    a: 4.660727944933549
    b: 5.825909931166936
    c: 9.388272907946
  fef59d46bec48c9013463d69918854863a0aa3dd119b7914f731f51c714db9d6:
    family: pert
    a: 49.894854537665864
    b: 71.27836362523695
    c: 115.88326540696688
  e3e6e9b7d617e12bf6d253d5198e1f8484f84d5511dd3dec942c3321600b519a:
    family: pert
    a: 105.99079121875573
    b: 151.4154160267939
    c: 235.98944765915417
  0b1299665631343214b1b29e3fa0c011e91474150ba526aa198df3e05c8439ad:
    family: pert
    a: 36.496865017524
    b: 52.138378596462864
    c: 106.07184623539472
  17fd97fea88be7c66783c2c359ede5886d9400feb8504dc61cb75dce0884164d:
    family: pert
    a: 16.156784138691325
    b: 23.081120198130463
    c: 56.81349563553009
  84fdbe8141e9dfd3e6f81780a9bb40d2f8aa7a7651cd11a03b6311fbdfac47a7:
    family: pert
    a: 24.81718701082353
    b: 35.45312430117647
    c: 86.33676966680376
  dbaeae0eef09c6926eab27479aaf2b6617e8c4d902e69c7622e57f862549f80e:
    family: pert
    a: 20.629451408534354
    b: 29.470644869334794
    c: 70.65186105855797
  284fad4d3d6e474d0834152b15e1ba566c2e3a73583877ebd33de999373a5b66:
    family: pert
    a: 16.471971044914216
    b: 23.531387207020313
    c: 50.46355725536136
  f21044fa54465c8d1126afa62ca4b55f11f84786fc263b712571ab3d7de0717a:
    family: pert
    a: 22.370265424875072
    b: 31.957522035535817
    c: 64.72413665059275
  33ed5041e7978bae00deaf63e65fac04863f65f8c8548aa214e5fe786782c928:
    family: pert
    a: 42.357102102260754
    b: 60.51014586037251
    c: 124.59710600838453
  70f90b9268b0281ca1f0b8baad376f3f184cbfe979a6de3d97d15ed963d6ba59:
    family: pert
    a: 43.188052460623204
    b: 61.6972178008903
    c: 112.83221588879388
  5592b2860ca677fe81f7fab7856f8340769a42cb083503d1b1c4d58410aeab5c:
    family: pert
    a: 26.389588831050002
    b: 37.69941261578572
    c: 75.74709658189116
  4b20a93cbd2359026bc8145e87ad43c84c0263546a230da139f2d157df96ff6a:
    family: pert
    a: 18.831202542166988
    b: 26.901717917381415
    c: 56.102393659418475
  508d7acfec1cf31b004312ff53ce538e39e962efe2e7c99da9610368c1ab30f8:
    family: pert
    a: 29.33910251630985
    b: 36.67387814538731
    c: 64.23761059308852
  1b86dc80dfb8df65f59a50406bc50e3fdf5aad89732bd4d6a13ff3b61e84b58f:
    family: pert
    a: 22.725717907891063
    b: 28.407147384863826
    c: 75.89036100354338
  0475c0aca183efbfa2e5dc746e356089636b3558bb9547ecba8da456b506c666:
    family: pert
    a: 32.44772441743556
    b: 40.55965552179445
    c: 61.09409716299065
  f67d9e4f467959b01e559d56203aee6b96ea0b055d0b1a88d454c5f1540c67da:
    family: pert
    a: 20.559004395085296
    b: 25.69875549385662
    c: 33.47168603990493
  125e22e4081a34af64c80ef52e7c3e4d663f6d3a820f54248f52d5ca4b859c0d:
    family: pert
    a: 16.01726022537761
    b: 20.021575281722008
    c: 29.928483498971875
  480a971297dd87d6595c5c411300c93408ef4ef4039e6b978f33a780d55aae60:
    family: pert
    a: 15.631128163918781
    b: 19.538910204898475
    c: 35.09054719904473
  7ebbf37f6031b82b2c405173f1a97fc1a827a1ec4b4132ddef01c23bf77c5aab:
    family: pert
    a: 30.453280305773813
    b: 50.75546717628969
    c: 179.18199937855186
  d9f5d37a9c7cd3c69fe7ccb4f3e5a35fbf8ec074d3d53654b17e4ee4bb32c290:
    family: pert
    a: 40.11246852445482
    b: 66.8541142074247
    c: 267.98102679804106
  c34f539b42743c8c12429fca8ac58effa89681bc3bc9b73a6af2daf6b25dacdd:
    family: pert
    a: 20.17626379193044
    b: 33.62710631988407
    c: 152.01603755574573
  254a8b343bc73ea8090797427a499768e8658d5290bcae5cccd492ab9ff20d3e:
    family: pert
    a: 25.393509443247577
    b: 31.74188680405947
    c: 52.1299812167264
  dd9745d54678848a277a345238a04c88e42916464951ae0c45607c661bbd35a9:
    family: pert
    a: 20.80474846759791
    b: 26.005935584497387
    c: 44.2222265598852
  7822f7418952b7167fb2366dc013a865ba66fc3f1864e219a5403371e852ab1e:
    family: pert
    a: 25.671249227709293
    b: 32.08906153463661
    c: 44.967299427562814
  148259c1fbae55b55e46c4eb7406b1e0d4d09597237a0e0a00029f749d74b293:
    family: pert
    a: 47.276195223188495
    b: 59.09524402898562
    c: 93.34965991402784
  d4fd0cc09cb3405a681a36ea27b78f80e151a5560ec4d28c379264320779fa97:
    family: pert
    a: 34.118358276832105
    b: 42.647947846040125
    c: 81.7489414170632
  df512fb00d9844a44d57664d6f33e5285c483f0a3967135d433dc30b52e0c2f5:
    family: pert
    a: 29.81213348701128
    b: 37.2651668587641
    c: 52.110021969509376
  3ca03641a4ce6624592ea11ecddb439a5b75ab0bb578ec44832da0d0c2bf7bca:
    family: pert
    a: 17.997710653491527
    b: 22.497138316864408
    c: 40.50391810272655
  a6fdb75e1551c2b2df215cb2408178bdf285c0654cba3deef7ef94f77c5191b9:
    family: pert
    a: 27.39231972542196
    b: 34.24039965677745
    c: 44.207214387159524
  e93f316b3acf41367c229b78f98da0313129172ce45b48642a53b8b6d81944a3:
    family: pert
    a: 41.045312040057794
    b: 51.30664005007224
    c: 77.96921332677887
  1ff0ba15edc0f3c7672cc8ad8425ac79cb1e7dc515eec659fa71322266ac5b8b:
    family: pert
    a: 10.393461884887557
    b: 12.991827356109447
    c: 18.739364993451602
  36e572b6d26d8b14f55868927e6375f951348793292fcaaf7681f67d7d41eac9:
    family: pert
    a: 9.425485491566041
    b: 13.464979273665774
    c: 67.32489636832887
  19a3dd9bcce837e8e8885d99808e35a9c75bbd588613757c5613cc9c843f98c8:
    family: pert
    a: 7.488850978759021
    b: 10.698358541084316
    c: 53.49179270542158
  8bdb4a3cf5314bedc918f31c0b8ac4dbb0b38dfd56e8f4f3878f308cffeb80c0:
    family: pert
    a: 11.465333196175738
    b: 16.379047423108197
    c: 81.895237115541
  747cf89c597454b8c01a891c99d5547b91ce10a911becf02590328835ca06de1:
    family: pert
    a: 9.957378675284401
    b: 14.224826678977717
    c: 71.12413339488859
  47e6ac1d3988deab9e929e7a8b5811a52417b5c1bd316e41569ee849cf2ec259:
    family: pert
    a: 6.1241612952532245
    b: 8.74880185036175
    c: 43.74400925180875
  2c7b776c4dc49f0c5855e0e88db46c1d9689ecd35306a3549fd80b000622839a:
    family: pert
    a: 8.302158442109702
    b: 11.860226345871004
    c: 59.30113172935502
  71cdabb522adbb2da8c86d3bb8f2b4f9830790554bb30768e5463a6eb9de82e2:
    family: pert
    a: 7.738336486689283
    b: 11.05476640955612
    c: 55.2738320477806
  0cf7ae5caec328d27f7a045d1b45facd1c082e07f03d22cb64be6f9338966832:
    family: pert
    a: 13.717817160521061
    b: 19.59688165788723
    c: 97.98440828943615
  e2bb80a44b18ec5feec244189f1c972459b3396eb9f00aa220b32209b794e3d2:
    family: pert
    a: 12.797667019277924
    b: 18.28238145611132
    c: 91.4119072805566
  3b15d0710109fe152d22150bc001d9923fc9bebebc5cd036747d3e2399b21931:
    family: pert
    a: 6.679186803151504
    b: 9.541695433073578
    c: 47.70847716536789
  6e4f4b7eb34d9200b5f14318691713baec4e30848177bde3cb0b342f4d863bee:
    family: pert
    a: 10.889869928381833
    b: 15.556957040545477
    c: 77.78478520272739
  0603a3d54de8d386a99511eefa3b06b9d6e0f270a4029d77b6ca2d9e4c852dfe:
    family: pert
    a: 12.467546351198555
    b: 17.810780501712223
    c: 89.05390250856112
  ba3e5f378d61610d6a7a0047483747168133c2f72b4926d1c82ecf1ce36fa226:
    family: pert
    a: 10.055152709352607
    b: 14.364503870503725
    c: 71.82251935251863
  7abd831be586f21e6a7f4f57749fc7a316a4ffb6931d7cfde937da04278aeb77:
    family: pert
    a: 10.243085669343975
    b: 14.632979527634252
    c: 73.16489763817125
  5adc09944327dec1d25d25719ee964b5f76d1978566d01e36818cca944e7f44d:
    family: pert
    a: 10.441849793546277
    b: 14.916928276494684
    c: 74.58464138247342
  74ca3145cba15eebbd6c9e1d0d492eb9b93d1b68d5530d1ef99a6dc9dd6311fe:
    family: pert
    a: 10.85003515262521
    b: 15.500050218036016
    c: 77.50025109018009
  15e4788f764a420169b431b2171db2cf0196cdc4e80ba416cc70a99625e65229:
    family: pert
    a: 14.411526294510287
    b: 20.58789470644327
    c: 102.93947353221634
  2de75d130275915b0292ae7d239d78e3e581b3c613f11798acd0e95b0d512443:
    family: pert
    a: 7.539884659255584
    b: 9.42485582406948
    c: 20.581048102574957
  47e03fc1f0504b68efaa884e649fa982b03f34c1f290d7a1fcc12e4518c8798b:
    family: pert
    a: 9.603658456466185
    b: 12.004573070582731
    c: 21.09269621011533
  8e808281b8bcb02dc2d5cf9be18f21c818e0c96706ab56b8e518bf906092ea86:
    family: pert
    a: 17.573145216456435
    b: 25.10449316636634
    c: 68.61673896979575
  378393432a71cf11850b9f906342805831b4c17112d912b546d1c6efd34860c8:
    family: pert
    a: 51.731353690999576
    b: 73.90193384428511
    c: 149.9582327089461
  263a77672328c49bccb64ee0c691c176a4982c8fea588f31e6d24b1cd78bd78f:
    family: pert
    a: 39.873957153301575
    b: 56.962795933287964
    c: 94.61392144874834
  4deef86386e3e754f73e2f05b8b00ceb27ecae0172b31e3c614cbee21ba614a3:
    family: pert
    a: 27.071121387850845
    b: 38.67303055407264
    c: 86.23773526731011
  b4a5f9a85c22e39d64d9bef84fceef883e0f3a42e7ff6479da0697cf0b3d2fb8:
    family: pert
    a: 31.392952861272114
    b: 44.847075516103025
    c: 110.42454708436578
  3dad25c4aa9d679f0fc0446d116b1dba099e6783df4da577c8125847d94ce0ed:
    family: pert
    a: 52.27072958424838
    b: 74.67247083464055
    c: 142.61783269445024
  746167e6a064461379d99b9cbbe01d59ac6c9069ed33ac2ce6ad4878cf630617:
    family: pert
    a: 2.757702993402524
    b: 3.939575704860749
    c: 10.98563800344229
  00afd465da5cb6747d289410cbc876de26670a07397ed5f03490524c2ee99c7e:
    family: pert
    a: 2.6828745298305487
    b: 3.832677899757927
    c: 10.545355662411101
  c04c72a26549294ad3c37baee0ca8f37d05e3932890ecc90e4d562a589f11d59:
    family: pert
    a: 3.884007799823292
    b: 5.548582571176132
    c: 13.512378467892802
  a6e5f1df06bee33df3f5896cd6c6f284bf5424b6b0e4b948ac78405c7b663afd:
    family: pert
    a: 29.74681809729246
    b: 37.18352262161557
    c: 55.265249064922486
  f10ea1f7e8e9f9172fd6ae2249b794d002fca04e0887a4011438170247fa3373:
    family: pert
    a: 3.553010948296109
    b: 5.921684913826849
    c: 30.312961233477225
  98ec01b2f7af915d1a9ce7720f8af05d42c7dd2923321237b45c317acf6be5a6:
    family: pert
    a: 3.43185970982934
    b: 5.7197661830489
    c: 27.40952247130386
  0d4f8017544f73ab098aa3645072417e374b573ba542e4b086f9d6966ab1e2df:
    family: pert
    a: 46.71550570955955
    b: 66.73643672794222
    c: 185.4208739263847
  a2b7d69891a1949eec1c8c1414fec2c67adf7deec830bc967e2dae3c78fb2a76:
    family: pert
    a: 112.6069352135469
    b: 160.867050305067
    c: 281.78013349846987
  e599bffb80311058d234af818474465a6790071d2f19c4c429c7c53564e02a9c:
    family: pert
    a: 27.575658347725476
    b: 39.393797639607826
    c: 196.96898819803914
  5ba610aac943f5fa52838f4a13c8bf63a9ee2c78a0bce5cba5a6882560249dfd:
    family: pert
    a: 23.514169456964503
    b: 33.591670652806435
    c: 167.95835326403218
  8af2482cb2d3d11608170eda12085ef40eabcf79db336482ea7d38967ba1a19e:
    family: pert
    a: 17.174968918392256
    b: 24.53566988341751
    c: 122.67834941708755
  1461add401fd6e5589d158abe0c4428c4f6b0b2146933563796f1d024d1a1028:
    family: pert
    a: 35.77098180368133
    b: 59.618303006135555
    c: 153.4136278583658
  4450074abcd6c39cbb56b53acc863c42f7cd05d26cd06de272e46fe95670633c:
    family: pert
    a: 20.437995147577826
    b: 34.06332524596304
    c: 138.31887520860516
  651da58fadbd76cd6dd3034bc0b73007b511c3bb0bca4a249539eeafcc2e83c7:
    family: pert
    a: 23.917773295929006
    b: 39.86295549321501
    c: 164.79286176168597
  587a09b159c5ccbe52ea9b572faf21961a6127feba335d6c6881b56be97b064f:
    family: pert
    a: 25.037687162221843
    b: 31.297108952777304
    c: 42.74819342614922
  2766d8bdb8d10bdbae1aff2c7fe6d30ea8fbe27eef35d68649616b3d6523b2bf:
    family: pert
    a: 19.87746508244092
    b: 24.846831353051147
    c: 44.812443108211916
  88f5c35ecd5f868a47969da6d5805a08e853fc368e4ee0ff092235eb53541f70:
    family: pert
    a: 18.364995627885786
    b: 22.95624453485723
    c: 44.70557499967444
  84ae237616d400899c09188e1435e18f88e985a4157a38b68eaa73f151978ba5:
    family: pert
    a: 20.02518189758308
    b: 25.031477371978852
    c: 38.300127242490674
  1be8f85c04f25a6ad5d8cd427a6e004de2de884b5e98a15928b06c2d8ea9c12e:
    family: pert
    a: 17.55521342428497
    b: 21.944016780356208
    c: 39.503615409135904
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
      worker_5: 1.0
      worker_1: 0.75
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: b9265255a8f9150d1ed24205ed11bb95aeb216aef7aa911ee03ba2938f7262a9
  - id: 2
    dedication:
      worker_5: 1.0
      worker_1: 1.0
      worker_3: 0.75
      worker_2: 0.5
    distribution_hash: a693aecb52c0d782bb826b7994f1c260bdafd2ac417c48608c2a1f2130d274ff
  - id: 3
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_3: 0.75
      worker_2: 0.75
    distribution_hash: 73608b6bda91b451f95d72ca949c9710f57c4b5a6976d7a25fc1eda4aaf8da79
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 68133ee6dce39ae028ff26699e74c9c3c30b0ec44edbad0b68116f40620945ea
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 0efdc88488dd1da4d9771c784ce99f054b0707d94327f4922d4f6c119b8bf72a
  - id: 3
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: b8ed1d868e499f691ca8eee7cefdfc9155c1859f7e3433d1407c2fe7c11ce460
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_1: 1.0
      worker_4: 0.75
      worker_7: 0.25
    distribution_hash: c7b11aa7af09001ba9b2f35c7ceae4592333a9a077a462e22dfb85971b8fdc32
  - id: 2
    dedication:
      worker_6: 1.0
      worker_1: 0.75
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 9c055579b6e32a6a84182413e05b26cf8e22f547ac0b3e441b0655faa963cc69
  - id: 3
    dedication:
      worker_6: 1.0
      worker_1: 0.5
      worker_4: 0.75
      worker_7: 0.5
    distribution_hash: 25e16801be06aad4ec79efcf25b341ee6fc9f3c44601718df60e05a0266f9dc5
  - id: 4
    dedication:
      worker_4: 0.5
      worker_1: 1.0
      worker_2: 0.5
      worker_7: 0.25
    distribution_hash: 9252901db7df134b5e169854c2f24c7c54d5b63f78d59a9d68f04f35e254401f
  - id: 5
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_2: 0.75
      worker_7: 0.25
    distribution_hash: ba5c40b4eafdb7338f8c4b0b1ab3a24af8561061f2748241cb735fd737877a5a
  - id: 6
    dedication:
      worker_4: 1.0
      worker_1: 0.75
      worker_2: 1.0
      worker_7: 0.25
    distribution_hash: 757d4cf8c0421686aa98302210afadbb1a897c6de2e8892d11dcc1edf4eece6a
  - id: 7
    dedication:
      worker_6: 0.75
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: d9aabd946ace9b3766857a13e169cfaa1179cc960d34ad2d1222d6c25bc5a5af
  - id: 8
    dedication:
      worker_6: 1.0
      worker_2: 1.0
      worker_4: 0.5
      worker_7: 0.5
    distribution_hash: 4a9e9162124471e66069fd494274e622b90e5b2f7d82dccdb95cee4f11a76f1d
  - id: 9
    dedication:
      worker_6: 0.75
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: a6ffde019c73749b5029d94a49acf7862cc16666a23bf12b73003b4f341ba1a7
  - id: 10
    dedication:
      worker_6: 0.5
      worker_2: 1.0
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: 688ded8f6f476b3e7da2d0eeba230d2ec1fe71601dabe952382d24b00ba654c7
  - id: 11
    dedication:
      worker_6: 0.75
      worker_2: 1.0
      worker_1: 0.75
      worker_7: 0.25
    distribution_hash: 04ad269ccefa60b49614a9a019e574b9d3e3fbbec0c05e180d95f8387fa77eb9
  - id: 12
    dedication:
      worker_6: 0.5
      worker_2: 1.0
      worker_1: 1.0
      worker_7: 0.25
    distribution_hash: bc1ad4321f1948b03dfc77eae7449e1d814ddfa5c3364c554713ef1fd9e67447
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 67f0758f6036a1dde0156aaf077ae5cabb6dd9ab0aecad5b71d0b60612930e65
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: bf204599b5064dcbb178e11119a06a119bf16d1d55ae0282cf7db06b127299bd
  - id: 2
    dedication:
      worker_5: 0.75
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: 66ec07537265f666ebdd3af46fcac13ceb1315c16ffb1e72e01dfa0ee3cb73be
  - id: 3
    dedication:
      worker_5: 1.0
      worker_1: 0.5
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: c145a319161ab6123241611e7fa42e7098b230c4c1d5023a9f887740f36892cf
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: b1ef03738fc0d3320114a46f1684ac3bdd8505a6bfc6da49946e1aec390151dc
  - id: 2
    dedication:
      worker_5: 1.0
      worker_1: 0.5
      worker_4: 1.0
    distribution_hash: 1e5427765bef23cd4711e22d763f706ccf65737beca6617380df05db41548d2f
  - id: 3
    dedication:
      worker_5: 0.5
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: fe9846d91342bc131a4b662ae8fd02b3bffa6c957ffe4aedcc1c8b110485d756
  - id: 4
    dedication:
      worker_4: 1.0
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 131db1f288a36c68f733054ba45524087dfd7ecd692ee22da7a65389cf973173
  - id: 5
    dedication:
      worker_4: 0.75
      worker_5: 1.0
      worker_6: 0.75
    distribution_hash: bf5365f7736feb3cf16a3339ab453618ae9c1c08a7bf69965fce0d2671d22d53
  - id: 6
    dedication:
      worker_4: 0.5
      worker_5: 0.75
      worker_6: 0.5
    distribution_hash: 88df6d9794df485630a2c7a0b8b8be55cbaca161564e645676f46d450a8d8a44
  - id: 7
    dedication:
      worker_5: 1.0
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: bde8f17a9387eba3affc95f5a1ac36b95fba448deeaacdc3655b62122185827c
  - id: 8
    dedication:
      worker_5: 0.75
      worker_1: 0.5
      worker_6: 0.5
    distribution_hash: f8ad41d8b824571ba55ae0a24e25c461537e40069dac209e389e4e6cc2c3706a
  - id: 9
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_6: 0.5
    distribution_hash: bef9a50c0a6acb95800a01e071214230d5b3f8f12ae1040cb5cf8c7fe13e8c9e
  - id: 10
    dedication:
      worker_4: 1.0
      worker_1: 0.5
      worker_6: 0.75
    distribution_hash: e1a0f38fe4f363e275c78b592a0f45ca3b0c3f7364054f307d8e8d3d01a6b0fa
  - id: 11
    dedication:
      worker_4: 0.5
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: ac131ded2a5b6088e19e2d8ba32f560a06d46f2aeeecc7cd32ef1d7a75763317
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_4: 1.0
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: 4f84b5c233afb5d1047f8acb2d9248cb50bc54c38d96b4d269c3b4139790bce9
  - id: 2
    dedication:
      worker_5: 0.5
      worker_4: 1.0
      worker_6: 0.75
      worker_1: 0.75
    distribution_hash: 623fe4fffbfacfb55ed4e1ef4b224d8d18c33a13ba617b7c72f5dd0f97281199
  - id: 3
    dedication:
      worker_5: 0.5
      worker_4: 0.75
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: ce610ba8d51a08be41e343a19f711aab78a6e510fc4da66313e4e67eacce6285
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: ba19fbb6d8786e7048b913bb7918a8f38f6a64e59bc138123ed211e49709dfc3
  - id: 2
    dedication:
      worker_6: 0.5
      worker_4: 1.0
    distribution_hash: 65847ac6861a316f2aa9511e574f15c99a2e39f2812219e5380aa6c724257f36
  - id: 3
    dedication:
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: 69718db6c8573346d7a9a083cee3a5736556791e800f0d4a7b1a441ddcd59453
  - id: 4
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: 6eed4d794ccbd614734293edd7d53dc9fdd54cc45d4439e87082bd3ad7f4b4f5
  - id: 5
    dedication:
      worker_6: 0.5
      worker_1: 0.5
    distribution_hash: 444e7469c8dbc80b9d5623ce1f91ca1a0f3cb4758f8a674ab4bc973526318e8a
  - id: 6
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 5566be00cc754987887c43e2016f445b488d10160a8500bcbf9302bfcb9ca4d0
  - id: 7
    dedication:
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: 60f9cdb1f3a50626a5dfee17fc5999ab319a44e5c8a817f72656d41bdd2572cb
  - id: 8
    dedication:
      worker_5: 0.75
      worker_4: 1.0
    distribution_hash: 0c81f55102d6bcf522a3b971de5a96ddd0d9e446a8ddaed95d0711b274421746
  - id: 9
    dedication:
      worker_5: 0.5
      worker_4: 1.0
    distribution_hash: 8edcfc72399d4bf2eb853d8672695df653d77ed63c02c89cab2b9adc527dbfc0
  - id: 10
    dedication:
      worker_5: 1.0
      worker_6: 0.75
    distribution_hash: 60124231404b30b036b4591ae67c8a8bac0c158bc201db63c62c127d509347b3
  - id: 11
    dedication:
      worker_5: 0.75
      worker_6: 1.0
    distribution_hash: 60a1894dd84e6a09f0f10bb52ab1c23ada62054e0c5e3c112cf14b9f94bdb54b
  - id: 12
    dedication:
      worker_5: 0.5
      worker_6: 0.5
    distribution_hash: 4bc27694464b3b53599ce65189527fc183cc8b207b6d31307d55accf506019da
  - id: 13
    dedication:
      worker_5: 0.5
      worker_1: 1.0
    distribution_hash: 8751593f321f4df37d4478ef12d10b135eb3f25cc37eb24e341c6cabad040a83
  - id: 14
    dedication:
      worker_5: 0.5
      worker_1: 0.75
    distribution_hash: ff5d7e98b4a5f72323bf71986e24eff8c15282640c05e7e01a52eeca7178e782
  - id: 15
    dedication:
      worker_5: 1.0
      worker_1: 0.5
    distribution_hash: 410ae23164f1abb1fb3c4a1e7a265213771b95d2756bae8669cc039d7dd55ade
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_4: 0.5
    distribution_hash: cdbff505b197fc3061605c5e0c82c6cd46fb2e0fddf24201ec15c4277c5aeee1
  - id: 2
    dedication:
      worker_6: 0.75
      worker_4: 1.0
    distribution_hash: 7eef548a46ea1cb5b6f5398749137b5c504779e843e39712c202f5dbb1db4799
  - id: 3
    dedication:
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: 163ca3c6cdacafe7b75ed40a62032849ac13dd7bb4a65305265e1be3dac1c0d0
  - id: 4
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 9ea38d09ee58c79b3f1599013347a722075bfc162ecdd1b2cdb4ef8b5cb69e0c
  - id: 5
    dedication:
      worker_4: 1.0
      worker_2: 0.5
    distribution_hash: c52900bb5896d14b9dea5d97f11b0e17c13b0ad3e72406d804151dbaf7ec2ed9
  - id: 6
    dedication:
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 1f4f73b35dcbbeb0fff43e4a9abd594a9d8e2889c5d0da9e6ccd932095d32206
  - id: 7
    dedication:
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: 7d853c9b51285650f45aa4918372a22b2a5e8f212a04ad62cfda87f7cfc2ec7d
  - id: 8
    dedication:
      worker_2: 0.75
      worker_1: 0.75
    distribution_hash: b3c9dca4e6001c6db1b95441db6ec46283133f6a31e9b547463394784e371b66
  - id: 9
    dedication:
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 21a3d00b0b47e74b612a60c41a7e05c88abe10b74df7fce16f10277a2ca63ad1
  - id: 10
    dedication:
      worker_4: 0.75
      worker_1: 1.0
    distribution_hash: 311d2a933c63f205318d6bed43cb822ff12848dbcf6058ab82bc070a81562c20
  - id: 11
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 9c6bb189e43e157a25b9894fc24ae138ee8230e111b722e0ee2c6e448ac5d3dc
  - id: 12
    dedication:
      worker_6: 0.75
      worker_1: 0.5
    distribution_hash: 13d30d0d1fd576e9c916bfbe11b5408c72d23b9e6a75597ec99751adabef784e
  - id: 13
    dedication:
      worker_6: 0.75
      worker_1: 0.75
    distribution_hash: 408d2d3b9f005172f5d71f5c7c1cd871a23a61b70f5a76e609ee06fa0dd69245
  - id: 14
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: 0383226b79f0ca80c9a05ecf7b253e94c37140db14babbffffed15823cf9d2c3
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: 180170165bd3904847d0e15cbfbbcdd9edf873452179071c539a1f72af1434e5
  - id: 2
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_6: 1.0
    distribution_hash: f872708a522b282e3d30f338f3ae96a440c08064ce0d59703adc83f1a713ab14
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: 8ed01efdbb4516e633aba6faa1fb4064115585a1cc85a7e6a79e5f83f322a5cf
  - id: 4
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: e4ec4816e95795365341aee9dfa4bc2b441508d6c84ba00a7bb455962b1dade9
  - id: 5
    dedication:
      worker_1: 0.75
      worker_4: 0.75
      worker_6: 1.0
    distribution_hash: e945462fa04e2ebb59438ac4883f8b5de03d4cc1c3bd600c007fc5ade892461c
  - id: 6
    dedication:
      worker_1: 0.75
      worker_4: 0.5
      worker_6: 0.5
    distribution_hash: 64354707dcb10df8a50c16a3f83b49391765e2735759a0026090d9c0e24e4bcf
  - id: 7
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_6: 0.5
    distribution_hash: 2a869691dee7accd3cefe717526e700cb4e3914cecc323c50edbe202652ea134
  - id: 8
    dedication:
      worker_6: 1.0
      worker_2: 0.75
      worker_4: 1.0
    distribution_hash: b0c0ea0a6da44e1b019228fc3853bfd48f586857d539e38e088cf669d0fbede4
  - id: 9
    dedication:
      worker_6: 0.75
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: 88893dd81fee076cc214fbdd5110ed0accafbd29eceecf754956b7645b1c1438
  - id: 10
    dedication:
      worker_6: 0.5
      worker_2: 0.75
      worker_4: 1.0
    distribution_hash: 13ed7cfa74dbb8ca0e31fa51812e7c7375f36aa67d75e843290db83f984362e0
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: d0d3512bba5294ddcc323bcaaf40cecf8054198cfcfdb8540ec6af7d2846ab50
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 4951105863d9734947f7c52a4548e8bcff83e7f566d403ad927d09121f76e697
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 09e0ec82c0ffa96c3d47eb59eb3d9891eaa92bcba5351691d67ef271290d652f
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: ff7012f04945dfb529aa26ae5174815f02de7d1c65d49abcbd999b33433688de
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: c96e48bc5a41b0e0149d0489a9a6d8da190bb4f82c3006379d0155e4d1bc7c72
  - id: 4
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: a2a529ea25bead01bdf2113b4a7ffc95c14b3933bbe4b710572fed3526e92931
  - id: 5
    dedication:
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 2a16eecd16e7893e120ba543e50b4dcfb1747d479c6935c2dd6f182df863cdb7
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
      worker_1: 0.75
    distribution_hash: 59ec8b1572d242d82c918c059bff851fa7ccd9e94cdeb11ab54d40421a472245
  - id: 2
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: b3063df2dd98ee1de03a9d388e9416d9ef56be646b611333eca35ec190f524cf
  - id: 3
    dedication:
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 97cf675534b7546f27f6b99a29138b1fbe2bbe2a9236d5c12d6961b0f543a952
  - id: 4
    dedication:
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: b707ee73e18fa2d064475b8d25434fad975c368813a0f9cf19b541a93d23b539
  - id: 5
    dedication:
      worker_3: 1.0
      worker_1: 0.75
    distribution_hash: 27e1acd365707229503c9e2d4c100cab47f0b3ca41912cd64b46c8c929beecbb
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: fef59d46bec48c9013463d69918854863a0aa3dd119b7914f731f51c714db9d6
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: e3e6e9b7d617e12bf6d253d5198e1f8484f84d5511dd3dec942c3321600b519a
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.5
    distribution_hash: 0b1299665631343214b1b29e3fa0c011e91474150ba526aa198df3e05c8439ad
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: 17fd97fea88be7c66783c2c359ede5886d9400feb8504dc61cb75dce0884164d
  - id: 3
    dedication:
      worker_6: 0.75
    distribution_hash: 84fdbe8141e9dfd3e6f81780a9bb40d2f8aa7a7651cd11a03b6311fbdfac47a7
  - id: 4
    dedication:
      worker_2: 0.75
    distribution_hash: dbaeae0eef09c6926eab27479aaf2b6617e8c4d902e69c7622e57f862549f80e
  - id: 5
    dedication:
      worker_2: 1.0
    distribution_hash: 284fad4d3d6e474d0834152b15e1ba566c2e3a73583877ebd33de999373a5b66
  - id: 6
    dedication:
      worker_1: 1.0
    distribution_hash: f21044fa54465c8d1126afa62ca4b55f11f84786fc263b712571ab3d7de0717a
  - id: 7
    dedication:
      worker_1: 0.5
    distribution_hash: 33ed5041e7978bae00deaf63e65fac04863f65f8c8548aa214e5fe786782c928
  - id: 8
    dedication:
      worker_4: 0.5
    distribution_hash: 70f90b9268b0281ca1f0b8baad376f3f184cbfe979a6de3d97d15ed963d6ba59
  - id: 9
    dedication:
      worker_4: 0.75
    distribution_hash: 5592b2860ca677fe81f7fab7856f8340769a42cb083503d1b1c4d58410aeab5c
  - id: 10
    dedication:
      worker_4: 1.0
    distribution_hash: 4b20a93cbd2359026bc8145e87ad43c84c0263546a230da139f2d157df96ff6a
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_2: 0.75
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: 508d7acfec1cf31b004312ff53ce538e39e962efe2e7c99da9610368c1ab30f8
  - id: 2
    dedication:
      worker_4: 0.75
      worker_2: 1.0
      worker_1: 0.75
      worker_6: 0.75
    distribution_hash: 1b86dc80dfb8df65f59a50406bc50e3fdf5aad89732bd4d6a13ff3b61e84b58f
  - id: 3
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 0.5
      worker_6: 1.0
    distribution_hash: 0475c0aca183efbfa2e5dc746e356089636b3558bb9547ecba8da456b506c666
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.5
      worker_4: 0.5
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: f67d9e4f467959b01e559d56203aee6b96ea0b055d0b1a88d454c5f1540c67da
  - id: 2
    dedication:
      worker_6: 1.0
      worker_4: 0.75
      worker_5: 0.5
      worker_1: 1.0
    distribution_hash: 125e22e4081a34af64c80ef52e7c3e4d663f6d3a820f54248f52d5ca4b859c0d
  - id: 3
    dedication:
      worker_6: 0.5
      worker_4: 1.0
      worker_5: 0.75
      worker_1: 1.0
    distribution_hash: 480a971297dd87d6595c5c411300c93408ef4ef4039e6b978f33a780d55aae60
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: 7ebbf37f6031b82b2c405173f1a97fc1a827a1ec4b4132ddef01c23bf77c5aab
  - id: 2
    dedication:
      worker_6: 0.5
      worker_1: 0.75
    distribution_hash: d9f5d37a9c7cd3c69fe7ccb4f3e5a35fbf8ec074d3d53654b17e4ee4bb32c290
  - id: 3
    dedication:
      worker_6: 1.0
      worker_1: 1.0
    distribution_hash: c34f539b42743c8c12429fca8ac58effa89681bc3bc9b73a6af2daf6b25dacdd
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
    distribution_hash: 254a8b343bc73ea8090797427a499768e8658d5290bcae5cccd492ab9ff20d3e
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: dd9745d54678848a277a345238a04c88e42916464951ae0c45607c661bbd35a9
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: 7822f7418952b7167fb2366dc013a865ba66fc3f1864e219a5403371e852ab1e
  - id: 4
    dedication:
      worker_1: 0.5
    distribution_hash: 148259c1fbae55b55e46c4eb7406b1e0d4d09597237a0e0a00029f749d74b293
  - id: 5
    dedication:
      worker_2: 0.5
    distribution_hash: d4fd0cc09cb3405a681a36ea27b78f80e151a5560ec4d28c379264320779fa97
  - id: 6
    dedication:
      worker_2: 0.75
    distribution_hash: df512fb00d9844a44d57664d6f33e5285c483f0a3967135d433dc30b52e0c2f5
  - id: 7
    dedication:
      worker_2: 1.0
    distribution_hash: 3ca03641a4ce6624592ea11ecddb439a5b75ab0bb578ec44832da0d0c2bf7bca
  - id: 8
    dedication:
      worker_4: 1.0
    distribution_hash: a6fdb75e1551c2b2df215cb2408178bdf285c0654cba3deef7ef94f77c5191b9
  - id: 9
    dedication:
      worker_4: 0.5
    distribution_hash: e93f316b3acf41367c229b78f98da0313129172ce45b48642a53b8b6d81944a3
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 1ff0ba15edc0f3c7672cc8ad8425ac79cb1e7dc515eec659fa71322266ac5b8b
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: 36e572b6d26d8b14f55868927e6375f951348793292fcaaf7681f67d7d41eac9
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_7: 0.25
    distribution_hash: 19a3dd9bcce837e8e8885d99808e35a9c75bbd588613757c5613cc9c843f98c8
  - id: 3
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 8bdb4a3cf5314bedc918f31c0b8ac4dbb0b38dfd56e8f4f3878f308cffeb80c0
  - id: 4
    dedication:
      worker_2: 1.0
      worker_4: 0.5
      worker_7: 0.25
    distribution_hash: 747cf89c597454b8c01a891c99d5547b91ce10a911becf02590328835ca06de1
  - id: 5
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: 47e6ac1d3988deab9e929e7a8b5811a52417b5c1bd316e41569ee849cf2ec259
  - id: 6
    dedication:
      worker_2: 0.75
      worker_6: 0.75
      worker_7: 0.5
    distribution_hash: 2c7b776c4dc49f0c5855e0e88db46c1d9689ecd35306a3549fd80b000622839a
  - id: 7
    dedication:
      worker_2: 1.0
      worker_6: 0.75
      worker_7: 0.5
    distribution_hash: 71cdabb522adbb2da8c86d3bb8f2b4f9830790554bb30768e5463a6eb9de82e2
  - id: 8
    dedication:
      worker_2: 0.5
      worker_6: 0.75
      worker_7: 0.5
    distribution_hash: 0cf7ae5caec328d27f7a045d1b45facd1c082e07f03d22cb64be6f9338966832
  - id: 9
    dedication:
      worker_1: 1.0
      worker_6: 0.5
      worker_7: 0.25
    distribution_hash: e2bb80a44b18ec5feec244189f1c972459b3396eb9f00aa220b32209b794e3d2
  - id: 10
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_7: 0.25
    distribution_hash: 3b15d0710109fe152d22150bc001d9923fc9bebebc5cd036747d3e2399b21931
  - id: 11
    dedication:
      worker_1: 1.0
      worker_6: 0.75
      worker_7: 0.25
    distribution_hash: 6e4f4b7eb34d9200b5f14318691713baec4e30848177bde3cb0b342f4d863bee
  - id: 12
    dedication:
      worker_4: 1.0
      worker_6: 0.75
      worker_7: 0.25
    distribution_hash: 0603a3d54de8d386a99511eefa3b06b9d6e0f270a4029d77b6ca2d9e4c852dfe
  - id: 13
    dedication:
      worker_4: 0.75
      worker_6: 1.0
      worker_7: 0.5
    distribution_hash: ba3e5f378d61610d6a7a0047483747168133c2f72b4926d1c82ecf1ce36fa226
  - id: 14
    dedication:
      worker_4: 1.0
      worker_6: 1.0
      worker_7: 0.25
    distribution_hash: 7abd831be586f21e6a7f4f57749fc7a316a4ffb6931d7cfde937da04278aeb77
  - id: 15
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_7: 0.25
    distribution_hash: 5adc09944327dec1d25d25719ee964b5f76d1978566d01e36818cca944e7f44d
  - id: 16
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_7: 0.5
    distribution_hash: 74ca3145cba15eebbd6c9e1d0d492eb9b93d1b68d5530d1ef99a6dc9dd6311fe
  - id: 17
    dedication:
      worker_1: 1.0
      worker_2: 0.5
      worker_7: 0.25
    distribution_hash: 15e4788f764a420169b431b2171db2cf0196cdc4e80ba416cc70a99625e65229
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 2de75d130275915b0292ae7d239d78e3e581b3c613f11798acd0e95b0d512443
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 47e03fc1f0504b68efaa884e649fa982b03f34c1f290d7a1fcc12e4518c8798b
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
    distribution_hash: 8e808281b8bcb02dc2d5cf9be18f21c818e0c96706ab56b8e518bf906092ea86
  - id: 2
    dedication:
      worker_6: 0.5
    distribution_hash: 378393432a71cf11850b9f906342805831b4c17112d912b546d1c6efd34860c8
  - id: 3
    dedication:
      worker_6: 0.75
    distribution_hash: 263a77672328c49bccb64ee0c691c176a4982c8fea588f31e6d24b1cd78bd78f
  - id: 4
    dedication:
      worker_1: 1.0
    distribution_hash: 4deef86386e3e754f73e2f05b8b00ceb27ecae0172b31e3c614cbee21ba614a3
  - id: 5
    dedication:
      worker_1: 0.75
    distribution_hash: b4a5f9a85c22e39d64d9bef84fceef883e0f3a42e7ff6479da0697cf0b3d2fb8
  - id: 6
    dedication:
      worker_1: 0.5
    distribution_hash: 3dad25c4aa9d679f0fc0446d116b1dba099e6783df4da577c8125847d94ce0ed
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_5: 1.0
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: 746167e6a064461379d99b9cbbe01d59ac6c9069ed33ac2ce6ad4878cf630617
  - id: 2
    dedication:
      worker_6: 1.0
      worker_5: 0.5
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 00afd465da5cb6747d289410cbc876de26670a07397ed5f03490524c2ee99c7e
  - id: 3
    dedication:
      worker_6: 0.5
      worker_5: 0.75
      worker_4: 0.5
      worker_1: 1.0
    distribution_hash: c04c72a26549294ad3c37baee0ca8f37d05e3932890ecc90e4d562a589f11d59
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: a6e5f1df06bee33df3f5896cd6c6f284bf5424b6b0e4b948ac78405c7b663afd
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: f10ea1f7e8e9f9172fd6ae2249b794d002fca04e0887a4011438170247fa3373
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 98ec01b2f7af915d1a9ce7720f8af05d42c7dd2923321237b45c317acf6be5a6
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: 0d4f8017544f73ab098aa3645072417e374b573ba542e4b086f9d6966ab1e2df
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: a2b7d69891a1949eec1c8c1414fec2c67adf7deec830bc967e2dae3c78fb2a76
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 0.5
      worker_5: 0.75
      worker_6: 1.0
      worker_7: 0.25
    distribution_hash: e599bffb80311058d234af818474465a6790071d2f19c4c429c7c53564e02a9c
  - id: 2
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_5: 1.0
      worker_6: 0.5
      worker_7: 0.25
    distribution_hash: 5ba610aac943f5fa52838f4a13c8bf63a9ee2c78a0bce5cba5a6882560249dfd
  - id: 3
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_5: 1.0
      worker_6: 1.0
      worker_7: 0.5
    distribution_hash: 8af2482cb2d3d11608170eda12085ef40eabcf79db336482ea7d38967ba1a19e
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
      worker_6: 0.75
      worker_4: 0.75
      worker_5: 0.5
    distribution_hash: 1461add401fd6e5589d158abe0c4428c4f6b0b2146933563796f1d024d1a1028
  - id: 2
    dedication:
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 0.75
      worker_5: 1.0
    distribution_hash: 4450074abcd6c39cbb56b53acc863c42f7cd05d26cd06de272e46fe95670633c
  - id: 3
    dedication:
      worker_1: 0.75
      worker_6: 0.75
      worker_4: 0.5
      worker_5: 1.0
    distribution_hash: 651da58fadbd76cd6dd3034bc0b73007b511c3bb0bca4a249539eeafcc2e83c7
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 587a09b159c5ccbe52ea9b572faf21961a6127feba335d6c6881b56be97b064f
  - id: 2
    dedication:
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 2766d8bdb8d10bdbae1aff2c7fe6d30ea8fbe27eef35d68649616b3d6523b2bf
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 88f5c35ecd5f868a47969da6d5805a08e853fc368e4ee0ff092235eb53541f70
  - id: 4
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 84ae237616d400899c09188e1435e18f88e985a4157a38b68eaa73f151978ba5
  - id: 5
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 1be8f85c04f25a6ad5d8cd427a6e004de2de884b5e98a15928b06c2d8ea9c12e
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
  - task_11
- - task_1
  - task_12
- - task_1
  - task_13
- - task_1
  - task_14
- - task_1
  - task_15
- - task_1
  - task_23
- - task_1
  - task_27
- - task_1
  - task_28
- - task_1
  - task_29
- - task_1
  - task_30
- - task_2
  - task_7
- - task_2
  - task_16
- - task_2
  - task_17
- - task_2
  - task_24
- - task_3
  - task_16
- - task_3
  - task_18
- - task_3
  - task_21
- - task_4
  - task_17
- - task_4
  - task_22
- - task_5
  - task_16
- - task_5
  - task_26
- - task_6
  - task_18
- - task_7
  - task_20
- - task_10
  - task_19
- - task_11
  - task_21
- - task_12
  - task_18
- - task_13
  - task_25
- - task_14
  - task_17
- - task_15
  - task_16
- - task_10
  - task_22
- - task_9
  - task_31
- - task_14
  - task_25
- - task_5
  - task_31
- - task_13
  - task_26
- - task_8
  - task_21
- - task_11
  - task_17
- - task_28
  - task_21
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
- - task_29
  - task_32
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 646
validation:
  project_key: 7af1aa444f58ba450f1bcd7dfceb2df2f5c79523fab49eeea701e69b08ebcafa
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 67 days; worst-case serial bound: 1913 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
