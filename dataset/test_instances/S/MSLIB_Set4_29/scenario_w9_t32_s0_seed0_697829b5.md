# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_29
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
  modes: 127
  tasks_at_cap: 0
  relaxed_constraints: 5
  rewired_edges: 8
  departments: 2
  quality:
  - worker_3
  safety_skill: 2
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 2
  barred_pairs: 8
  incompatible_pairs: 1
  edges: 64
n_workers: 9
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 514
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
distributions:
  adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5:
    family: tabular
    probabilities:
      0: 1.0
  510935c893b773b485115765dacc4a81388e48e0a3eafaaa6a845e72f0c3a424:
    family: pert
    a: 13.651640243486364
    b: 22.75273373914394
    c: 66.5566310653254
  c926c9283650f607909418baee0f6b323a49651d6ebe8d9f0a63485894f9fdbf:
    family: pert
    a: 6.800211119915234
    b: 11.333685199858724
    c: 30.041061999700077
  8effacee2b23577c90d10b052dafd5a84a3f77a9d17e8966aa9a68d03f697d01:
    family: pert
    a: 32.9513709402481
    b: 41.18921367531012
    c: 57.57232275378986
  62232ef14466c6a062744827ae53315b72dce9dd14f7b0e27ac92d25789d1904:
    family: pert
    a: 24.007756374503387
    b: 30.009695468129234
    c: 67.82119644853543
  09db97598fe332bf5bfbccbecbff1c683f2c77969979a9231eb3a98bed46429d:
    family: pert
    a: 28.57114674412804
    b: 35.71393343016005
    c: 55.92039574028021
  6e92b536f878d791bf893b10cf870c70422faf9ed586169360986df29bd6b4dd:
    family: pert
    a: 33.91259126367556
    b: 42.39073907959445
    c: 63.6854743587354
  16d8825e12f18fd99f7a4f7ee49fe39243fcd7047f582d9e2e48caf753fc74c0:
    family: pert
    a: 17.51111939969061
    b: 29.18519899948435
    c: 141.84224451178252
  b2d57a04b30032cfb44d691b82a4aaf008ffe0c491049f2b9bbab8b74b607624:
    family: pert
    a: 20.45712037893194
    b: 34.09520063155323
    c: 126.01674963392632
  490acfb966b968e0f6dd165ea594a19d833c4f1d8efe0228516b246826b95c27:
    family: pert
    a: 24.544998188615924
    b: 40.90833031435987
    c: 127.59947221344125
  68b223215981678c7eecb67a61b1d4f6de1ee3459024ac38efccf2e04e40c556:
    family: pert
    a: 11.046805118773952
    b: 18.411341864623253
    c: 86.95568612894759
  2090bd16147c87646718217bea5f421b170872100a7949caf9e38e2baa2dced5:
    family: pert
    a: 13.89637310146822
    b: 23.160621835780365
    c: 115.59788332364701
  337cc487db9f1fe70287f1fd696ad99495fe4872aaff304580232787a4362b0e:
    family: pert
    a: 13.058715748410517
    b: 21.76452624735086
    c: 51.37581355284523
  cf919aff81141e19567089e3948392cd86782c819c95381897769a3f3fad6f8f:
    family: pert
    a: 18.322060421099767
    b: 30.536767368499614
    c: 90.10430360360424
  c22183350d9eab9314bd4a6d1329c6989efdd58acf3c533aecc419067281496d:
    family: pert
    a: 10.506342754721368
    b: 17.510571257868946
    c: 99.69563103795566
  1c02b1eb9d4a598890c8086a40134de4dfbc328fdde09426a94047a040848830:
    family: pert
    a: 9.26489432418117
    b: 15.441490540301952
    c: 53.83293674504737
  beba8ab0a18ddbde4701e421c81067f9f348b6e3e23cda55140a5b92c47933e6:
    family: pert
    a: 28.845472383454414
    b: 41.207817690649165
    c: 66.9694828827199
  b9957eac8aa19c2a27873f3b0f36b774096826dc86b3407885f6da48ca3ff3b4:
    family: pert
    a: 34.03932242878255
    b: 48.62760346968936
    c: 109.51384311833867
  8f74f014e2e5206498d32bd9469a42aba2c26beebca002c32e897f096df98a62:
    family: pert
    a: 15.80544514785326
    b: 22.579207354076086
    c: 37.76069244224592
  df2cd1105716b633343b4f667bb9b8668ceef44eba2c01e090869949c7f2c835:
    family: pert
    a: 12.608144808506648
    b: 18.011635440723783
    c: 41.16227788715996
  39a8158dca8e5e6ac21a7b493a4fb645772450022789aed0dd1801eda4ced94d:
    family: pert
    a: 15.701809315665196
    b: 22.431156165235997
    c: 57.880955519500226
  f5ae64ba33401ff920d8e6ce17829952ec89d9030140559bafc74b19a9046288:
    family: pert
    a: 135.77824559625626
    b: 169.7228069953203
    c: 277.61031757364054
  a4dd1ba2ac73775b3b13e06a5960e009d2290cb54657c504ffd531d891852c44:
    family: pert
    a: 31.426535131280158
    b: 39.283168914100195
    c: 196.41584457050098
  d19307a4f2a01cd2d58b438c87f484a037624b0e0afdedf8377dab279fc04ad6:
    family: pert
    a: 29.855307177730516
    b: 37.319133972163144
    c: 186.59566986081572
  ac30b2f4e7bf00953c470e07cd02c76087f7266c0fc9b7befcf9bff84259191d:
    family: pert
    a: 33.712249086136644
    b: 42.140311357670804
    c: 210.70155678835403
  f9fda46365a845ed63f1d0a5df8982d4e01ff9bbe57d40554caaf6f982b07707:
    family: pert
    a: 13.436582429946576
    b: 16.795728037433218
    c: 27.899039902589678
  0eb945bb9c9ecf653d98ce56d5d1fef1a88fdb2aee5464502474c990aba754fc:
    family: pert
    a: 12.969270461884676
    b: 16.211588077355845
    c: 25.719318726744852
  0faa92a6115e8ff16c7e69fec58aff378432221c4e9e8011b4ebe9acc846fdce:
    family: pert
    a: 2.2506594018408284
    b: 3.7510990030680476
    c: 17.088911290857734
  fd920aa31d6b9c458fb8668d28921fb302e6ca1096ab71abe9f56bd51c91cf35:
    family: pert
    a: 2.4856029552792713
    b: 4.142671592132119
    c: 13.410395060069325
  6b57735e4ab31095d233f3223808f3b082ab3aa18b7f4a54e2e81a7cdae2f89d:
    family: pert
    a: 3.5772776560176696
    b: 5.962129426696116
    c: 11.45432957626763
  2dbee242425803ca7ddde8e45250e265c3ccc02bb91b6227376c492c8cbb2bd1:
    family: pert
    a: 11.668791655319488
    b: 19.447986092199148
    c: 100.59758053099897
  3f91734cd8a8d773960b681f4d311b5fcfec6a2c035f99693731f88561a70ae1:
    family: pert
    a: 13.051456041144691
    b: 21.75242673524115
    c: 108.76213367620576
  852ab2b10100df444fee012c69095cbf7bce5afc276dffdaeccc8c66006efb8c:
    family: pert
    a: 20.760900300164256
    b: 34.60150050027376
    c: 173.00750250136878
  5c4cedfbe71e1a45a020909d91ab818b5405d1e2a9672f7b6b0106eddf2aff87:
    family: pert
    a: 12.376236173715373
    b: 20.627060289525623
    c: 147.00862783671886
  6910662c8aa93724a54b3e07fcecebe5c8ec5ac121fb4446b2cc287706e1e759:
    family: pert
    a: 14.41792743497611
    b: 24.02987905829352
    c: 120.1493952914676
  9ef0148f4327f1cca2e95964fd263cc3cfd34b0608952ff21f51b75b5102223a:
    family: pert
    a: 18.00680893388591
    b: 30.011348223143184
    c: 150.0567411157159
  72ed12126de6d5834ba96ac4ff314b7693b47ba0fbc813ba9fa33104f2cd6612:
    family: pert
    a: 15.93114439365803
    b: 26.551907322763384
    c: 132.75953661381692
  df514a8e56be60943a8a49d0b6f103f29bd72cf7283ede5464c79c4d1ef036a9:
    family: pert
    a: 16.893702470176418
    b: 28.156170783627367
    c: 140.78085391813684
  3ddadc86bbd6aa4ed87ab8b7327d6dfd81c3749254de25d584bdc928a205a013:
    family: pert
    a: 13.9845177052751
    b: 23.307529508791834
    c: 116.53764754395917
  ccc0f9036ca5b8860d00f119d9a556f66c159ef5b1f965c1e74525b80922c829:
    family: pert
    a: 6.926932048641913
    b: 8.65866506080239
    c: 12.627152869605267
  eddd899f3c95ab5dee1a4d3824b2ea52a08a37c49079ae47d53e97a6d9b9b942:
    family: pert
    a: 4.520659868542583
    b: 5.650824835678229
    c: 9.910305223582949
  293261af3ebdabe37a80119065442cb912cfec266cb09027ee48c1d481a91928:
    family: pert
    a: 5.330063908530105
    b: 6.662579885662631
    c: 15.64396175627475
  2705811139cf9587cc386bf73dea1104d8c33a66eb1bad02afbc1cf35d070e85:
    family: pert
    a: 5.872493621584969
    b: 7.340617026981211
    c: 10.547344621153059
  e2ae5b0df64244dd349a8203eac44c88627e743a63b3a942948845335135f6af:
    family: pert
    a: 150.90209404215835
    b: 215.57442006022623
    c: 465.97688887445156
  7d0962609616ec981a770b73abc39f61310a941ae454fa87a6154c87399a794f:
    family: pert
    a: 88.02197733195628
    b: 125.74568190279469
    c: 209.67199986312067
  b07fabd927af86fa911e9f47aef339b9b2732820eeed8c32c9af978b8fa5fb88:
    family: pert
    a: 9.096157366886175
    b: 11.370196708607718
    c: 19.764304242304636
  37c7fbdc4937ab8ee9e1763999274e9f6eac27d25d8112940e20c6a19f2906b3:
    family: pert
    a: 7.183026843427294
    b: 8.978783554284117
    c: 19.029629989845677
  44b120bc7abb05c8f1cbda94d7e7dc7a887f1e1a9989e5be16db2acfd6f3e538:
    family: pert
    a: 10.190203277937087
    b: 12.737754097421357
    c: 19.393516562080112
  2f7250737cac826ae6100335bc38b0a1e42d525f32b6130e75d05328806895cb:
    family: pert
    a: 13.09716891516618
    b: 16.371461143957724
    c: 20.808883649746548
  1fa5d4eddd336158a5c7abbc03b1bc5b5d0ef81ee85b9cdb116a804c1eb4cf76:
    family: pert
    a: 13.289709316627645
    b: 16.612136645784556
    c: 25.546905942161956
  58516e8e06f9fe8e081e2e958293c6696e2d997c681b7d677390ee3e97017648:
    family: pert
    a: 14.891487282642494
    b: 18.614359103303116
    c: 24.607984387277696
  9da41651cda33a0e8c8b10a45f7798fc52473c27cc31d0766708041e43bcaeb9:
    family: pert
    a: 11.342011246776718
    b: 14.177514058470896
    c: 21.3353616646342
  9b362b514bb4cb29fccd69c543c20a3f25646cfb676b371c8d1bbe9d32d9c698:
    family: pert
    a: 17.479117717878207
    b: 24.97016816839744
    c: 44.42869478965281
  f7f8adfd43d040773fa599d684d32b591586c456c1fbea80a3e8ca97ef9d63e6:
    family: pert
    a: 9.98521415433384
    b: 12.4815176929173
    c: 62.4075884645865
  5eee5fefb92b81d4d2e077ad8359c7984acda3a94a5113a44e36d9d6c491a1f0:
    family: pert
    a: 11.580764847486124
    b: 14.475956059357655
    c: 72.37978029678827
  9a2bcf5ecb747e9eacd1be5f8cfe577a007f7d3e2fc176bb4bbdd72a36fe8a4b:
    family: pert
    a: 11.22653838613057
    b: 14.033172982663213
    c: 70.16586491331607
  05e8d420596bf769235178a6bda8e2cf21f414b942c704155b80065c0bd97390:
    family: pert
    a: 17.484645771543384
    b: 24.978065387919123
    c: 37.224198215264956
  30b86e436b0fbf016188dbc132969c2e1b7af4d9ce811dd4f68a3724c600c6f3:
    family: pert
    a: 9.084949404424991
    b: 12.978499149178559
    c: 42.46060631822109
  590ac17c23ce9ac6773d16a7873c8f580b5212cedca19314956a1924a4a99069:
    family: pert
    a: 11.259034772773669
    b: 16.08433538967667
    c: 53.36178730845467
  83b55626c54ada8afe8b8b6be824ae9c1824948b383f6c8bc2fc79e2ffa7fefe:
    family: pert
    a: 12.024839197369069
    b: 17.178341710527242
    c: 45.12262574487778
  94a18e44093b1c80cea594bd3bfe6f6b60320a4d468a9ac00ccf7799ac8f9415:
    family: pert
    a: 10.191912490966924
    b: 14.559874987095608
    c: 48.85585172802598
  e6dbec5ffc679c2139f7bd2a036870dda6f4eebf84d4a1431c6a462b7f20bb94:
    family: pert
    a: 17.809383670694213
    b: 25.441976672420306
    c: 49.04234073775248
  cde7a5c4d3ed60cfbb5030a626850b58de23a424ee55bd04e8d5aade17adb8f8:
    family: pert
    a: 11.703234876396767
    b: 16.718906966281097
    c: 35.67642529635085
  a5a06e793814d1cf40b0e0990cddcf2298afda46a45eca04a910faae05ab79f8:
    family: pert
    a: 12.353053838633604
    b: 17.647219769476578
    c: 45.182982231472074
  3e02d5c19b352faa2009811cc33111100208860310dacf58047eb4960ce9921c:
    family: pert
    a: 8.195800694845765
    b: 11.708286706922523
    c: 54.95672244310681
  d80292c336bfe30b4a49ffcc84e2f44d0762f8a6fdac55eff8e324da90efbddf:
    family: pert
    a: 11.500987079928217
    b: 16.429981542754597
    c: 71.68822338624106
  bccc95d6d4177e6d9af27a61011791c145856887940a74fb8df830a22f864abb:
    family: pert
    a: 14.3867978115405
    b: 20.552568302200715
    c: 55.48886395167358
  31da2c51655cc2067ea15281e3c15406cd47e4ef53393c0fdc88bdccd53af270:
    family: pert
    a: 14.727143344106418
    b: 21.038776205866313
    c: 36.81970060561745
  49f5a99c8e07de8f2a2be5ee1b5e3f57b3b12dde05d5dca983a9a4432dc982f9:
    family: pert
    a: 11.095824198427461
    b: 15.851177426324947
    c: 36.437896780087065
  7c139ecc3fba5d0fc49156cea10dbed060be0949b22ea58b5fe9c8b15021bc63:
    family: pert
    a: 19.498918656399354
    b: 27.85559808057051
    c: 41.967979400502095
  80542cf211331aed23b8365ebfad979191185fdf6b71ee9d14c6795667966460:
    family: pert
    a: 8.484279152834556
    b: 10.605348941043195
    c: 25.08171934999357
  523ab33526a7f2257b6052c4179fe9989f264b6e85da5a7ec5ee73b1cfc5de81:
    family: pert
    a: 23.277134731278853
    b: 29.096418414098565
    c: 41.65810236752072
  91bc091297a447b1a43e744ddd6334c541802cd79331ef3d03b242324226f78a:
    family: pert
    a: 20.18778139426574
    b: 25.234726742832176
    c: 34.05147776706151
  4833b2413bc7133e0ccbbb4a141a5b78f1a6cad5707921aed6767996eaa81c87:
    family: pert
    a: 14.909909093974244
    b: 18.637386367467805
    c: 28.199267937678712
  99396b8f11bf338090099c795cb6e415c2a82effed9ac0a5783d07288e123f19:
    family: pert
    a: 8.882143870638679
    b: 12.688776958055255
    c: 56.60717532885333
  eb6f194894018f411186ab4567778158a9c9cbf600d3d2a2c6d865e32fa5a9ab:
    family: pert
    a: 14.404111838825337
    b: 20.57730262689334
    c: 58.288887338282954
  964fcff859e7122b56288afd1364610098e261f3fd8eb526a0526ace59af1f7f:
    family: pert
    a: 10.93376025223372
    b: 15.619657503191029
    c: 37.93868074738714
  8eb5f18e659bbe077d48f9697ddce3842c8d5b8242070903ea62e7639fe46a11:
    family: pert
    a: 20.328139432623487
    b: 29.04019918946213
    c: 67.79504775605355
  a2dde9e55d020232f3bcd63ec68cf719a327a379060b9b22646d1edaf46e5456:
    family: pert
    a: 14.17244925176649
    b: 20.246356073952132
    c: 60.48943007201599
  d60f5fe7964d0e0ab957d4943164fbfc1fd63463a53f1d33fdfce5e775bc719f:
    family: pert
    a: 12.178080479923041
    b: 17.397257828461488
    c: 54.87011441000568
  1b7a7e33eee696f8686df503d8cc068a53679fac1f4176c8053e62af7f26e497:
    family: pert
    a: 11.190681258590475
    b: 15.986687512272109
    c: 35.69639518947137
  60789aca9ca81f9bdd6cb1a3998d8c26073b6c56734d4dd7f1157821000fd40b:
    family: pert
    a: 27.31557028149247
    b: 34.14446285186558
    c: 68.72511000929012
  155aad5a957e57dfb1f287a4c043b18ff87650ecff754fdd17672c671ca6dd46:
    family: pert
    a: 36.52729383343379
    b: 45.659117291792235
    c: 75.5048305830701
  367e1499386bb10c3ef0238f8052fef880beb9c742e10ef3f5b860e27e0c20a4:
    family: pert
    a: 35.5425626069566
    b: 44.42820325869575
    c: 60.07387600751145
  779cc43a2acb42f18bbf76b45a272d0636ba4e92c81ce37026279611d8d63628:
    family: pert
    a: 30.34508225556705
    b: 37.93135281945881
    c: 64.75901235721916
  38bd9e06a04a3a23c2d771573bbd3d3d89d3470ace4e2ff470613040d73b0861:
    family: pert
    a: 5.655105795719849
    b: 8.07872256531407
    c: 22.039870210983217
  9cf72761b96749ae00b75ea99ccce39cd23d08ef636af09fd657da8934068b5c:
    family: pert
    a: 5.644491596671662
    b: 8.06355942381666
    c: 23.237635261715564
  2b4993ace777c3292086129d67f34651e5d91f175328dce7151ac807cb25cdbd:
    family: pert
    a: 9.45920578197885
    b: 13.513151117112645
    c: 21.974113257799694
  dee2d656cb183ac314308ac6e61a9892abaa562917790f2ac066e21de9fcc1fa:
    family: pert
    a: 19.06726596339408
    b: 23.8340824542426
    c: 36.35585055193104
  5f2ffa5c713ecab06735c56dffe3b43adc87b95b784810da4e173c0e488352f2:
    family: pert
    a: 14.701690700916949
    b: 18.377113376146184
    c: 31.56426032998214
  e0ad1e79a70d9bbdc00059481936e26158ff30d3dd2faf6cb29fe6f01a367ed5:
    family: pert
    a: 16.1708208073926
    b: 20.213526009240752
    c: 29.458671468547426
  39897182ce4b834eaeb5ecf9cd714509e809a98d580a8fd8ab4825e136fbd6d4:
    family: pert
    a: 16.54080537363104
    b: 20.676006717038803
    c: 33.82046567354245
  86b4c135b02e7ed1da894d835a43d8a23d5fcf0f5af2d65fb8d6da75c5fdf50b:
    family: pert
    a: 12.701598598229431
    b: 15.876998247786789
    c: 33.883537959585155
  f2776627d5d7f6033fd33b175d39ffded9694fa557c2e5a65461c348847a0bbd:
    family: pert
    a: 14.548917991183883
    b: 18.186147488979852
    c: 36.42017409899107
  d1b1d0520276a58ab45d383adc63aefacc040ee8708ac213d2f37dc0768ca4d5:
    family: pert
    a: 18.51470631193496
    b: 23.1433828899187
    c: 28.487908502489624
  c746db580aeb0f5a7003a3323ca4bf10b8d1bbe3fc3f72f2f0027a6d5dc43f74:
    family: pert
    a: 14.456596524810175
    b: 18.07074565601272
    c: 30.159339879693913
  3ce8744cf70690a11973cca82b29e984a029f14480eb2d8ae4432d050adf2f36:
    family: pert
    a: 14.240809542842317
    b: 17.801011928552896
    c: 29.365152515324322
  1442333da936fb0bc56de66c5cfbbe107836e859d28df70f49139f1b188b67b6:
    family: pert
    a: 16.40866039450383
    b: 23.44094342071976
    c: 80.73759433371703
  8a0376f29df129f0fc950fd62c4cd4ad6df7c8f39fc961767a29738f1a67fb7c:
    family: pert
    a: 41.367414930922195
    b: 59.096307044174566
    c: 105.03339383629685
  1b2f3ac291720ff242881437a943f431c2de9f1852721c5df674156d337d076b:
    family: pert
    a: 22.63877854657061
    b: 32.34111220938659
    c: 69.21657347879918
  498584759e794cb374f473fc0a6e8e4b7fe14a54c32222d603e491caf4436110:
    family: pert
    a: 19.965774784030714
    b: 28.522535405758166
    c: 43.71063593596212
  ee98d0672f5cccb15f04b56e8b46a8b427747a48e1761c8e4adddac5da9671f3:
    family: pert
    a: 15.654319303836031
    b: 22.36331329119433
    c: 47.14948769022095
  3e0f9a4687523945db1124219f3caedddca4af8ed04a3959a16187dd28a528ec:
    family: pert
    a: 15.617104091108706
    b: 22.310148701583866
    c: 62.57803141280818
  128dba80f3d4385b9e32e1586e12abef5347edcc9450895974280c022835c37d:
    family: pert
    a: 16.45248856592179
    b: 23.503555094173986
    c: 42.45968249021677
  970b9f6faf227d3a54ad12fd417c53419c93559a77d73a93f66856e9ae3834be:
    family: pert
    a: 36.80210749737795
    b: 46.00263437172244
    c: 73.90917065238347
  69b4b7df909a91eaa07a78124d7e0d3bac3efade38e31b329d2a1da55795b33d:
    family: pert
    a: 27.690500076348528
    b: 34.613125095435656
    c: 69.21746175053967
  1f369fc37304ac24c200ce29cc65f3312499165aee88c76ea3fa285938bf31c3:
    family: pert
    a: 37.470455409921215
    b: 46.83806926240152
    c: 73.60921313430977
  d018b9fdd008a2c18cef248f3c0338dc0072a14625c7a19539f2f6283e74ea25:
    family: pert
    a: 50.52872750384117
    b: 63.16090937980145
    c: 84.58042078306296
  a38173fe4fd5e709e7102eb7dc3db4f13b3fdf69e6222446130e95af5f8fe203:
    family: pert
    a: 29.63139687607392
    b: 37.0392460950924
    c: 71.84208293511135
  fcf79c4b7a540596e1e254c6794b91a97eac82ed8d1a7f31dff66a687cc4f525:
    family: pert
    a: 59.41824240626997
    b: 74.27280300783745
    c: 94.39876808709815
  5f626cf221523cd3bd40021313c8b2f3b2363599e9f5ec5177ef69c3347b8352:
    family: pert
    a: 17.442522249408025
    b: 21.803152811760032
    c: 36.233167112115815
  e14e279aa7c58c77652206cca49809c31550e941d5badc166bf44dfa15c2436b:
    family: pert
    a: 23.136895114154267
    b: 28.92111889269283
    c: 42.102474318081896
  af771586b82fcc8fa37c726e634e3570bc27399caff129cbde7b89c88eb22444:
    family: pert
    a: 25.275935615841345
    b: 36.10847945120192
    c: 69.45168726459045
  6d3b48bf1be47b4588e10d798e17277a57321b94177129204efc1e8e23405701:
    family: pert
    a: 29.852804355389505
    b: 42.646863364842154
    c: 104.84406696065803
  1ba36dc2fb045c37e9e4264c975f86643c054b23098deacb4caf145790c94b2e:
    family: pert
    a: 30.45614644180475
    b: 43.50878063114965
    c: 68.34138860565304
  34031a70e06566aeb093d6185265b7ac9c0319f054b9fafa06feecb9156995c1:
    family: pert
    a: 22.339256038999206
    b: 31.91322291285601
    c: 106.52304864105034
  727da2b541e4db0923170fc3ffad49d95be19e3988974d2d5b8dafdf494e5810:
    family: pert
    a: 20.7222154229911
    b: 29.603164889987283
    c: 78.40031877109674
  dc2fb37e8dfb6489bfc7802897900feeb256b2c5d1bd8ba9a6fb9178e02c944c:
    family: pert
    a: 19.776252551531165
    b: 28.25178935933024
    c: 115.05456835584505
  b8a1a349107ee0a088450ee5a24fbee36103674a8d3826a7dd0af68b583b81d1:
    family: pert
    a: 54.053668553682456
    b: 77.21952650526066
    c: 96.7052265623726
  1317f0084c02ef004803371d0ff08df49e8902b34fb33cc044c829c55c724674:
    family: pert
    a: 24.610600989405402
    b: 35.15800141343629
    c: 101.02460554871465
  f506016f4ee2eaae9b3e942d7209a94a0af9a3d5241ac6adf66fbcde4fa8aefa:
    family: pert
    a: 22.526428861003474
    b: 32.18061265857639
    c: 59.39330871572032
  0eb0679635c24fe7ad958a2b77a023ecdf70f0caad5aeae4ce663d0fb352e9a2:
    family: pert
    a: 43.3704148723595
    b: 61.95773553194214
    c: 95.65623811318949
  34232122d2df10ec69f4fb894fc1b859ea09c2c63b017d64e18af746f41c9296:
    family: pert
    a: 23.086865293649854
    b: 32.98123613378551
    c: 94.39578076885209
  6fded97abe84ab32b8f04e8e96b99a27a1a54cd93cd11cb28951f4641d7ea59d:
    family: pert
    a: 20.440925416979617
    b: 29.201322024256598
    c: 80.20784436558314
  8e8704af1395b89976aeda26fa80a9ad33f1fd1eaabd118ae30af56814b87be9:
    family: pert
    a: 21.957969584357137
    b: 31.368527977653056
    c: 81.90240078071746
  15bac258c5d21844bedec5f3894a61bb8b66dcac21bc6ae51799a97bea7d8127:
    family: pert
    a: 24.565888418646534
    b: 35.094126312352195
    c: 73.31507730357
  1055acea4d2919edae39b506de094fec19da731d4bd9beb93a39c96009592571:
    family: pert
    a: 28.791042543158422
    b: 41.130060775940606
    c: 95.08084529693163
  c2082a3b023f6cb646769655bac4deaa8fdc95d870adb8cdb42d5a2d3d3c5f19:
    family: pert
    a: 31.623315467948164
    b: 45.176164954211664
    c: 84.81028202986442
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
      worker_3: 0.5
    distribution_hash: 510935c893b773b485115765dacc4a81388e48e0a3eafaaa6a845e72f0c3a424
  - id: 2
    dedication:
      worker_3: 1.0
    distribution_hash: c926c9283650f607909418baee0f6b323a49651d6ebe8d9f0a63485894f9fdbf
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_7: 1.0
      worker_2: 1.0
    distribution_hash: 8effacee2b23577c90d10b052dafd5a84a3f77a9d17e8966aa9a68d03f697d01
  - id: 2
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_8: 1.0
    distribution_hash: 62232ef14466c6a062744827ae53315b72dce9dd14f7b0e27ac92d25789d1904
  - id: 3
    dedication:
      worker_2: 1.0
      worker_8: 1.0
      worker_7: 1.0
    distribution_hash: 09db97598fe332bf5bfbccbecbff1c683f2c77969979a9231eb3a98bed46429d
  - id: 4
    dedication:
      worker_3: 1.0
      worker_8: 1.0
      worker_7: 1.0
    distribution_hash: 6e92b536f878d791bf893b10cf870c70422faf9ed586169360986df29bd6b4dd
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_8: 0.5
      worker_7: 0.75
      worker_1: 1.0
    distribution_hash: 16d8825e12f18fd99f7a4f7ee49fe39243fcd7047f582d9e2e48caf753fc74c0
  - id: 2
    dedication:
      worker_5: 0.5
      worker_8: 1.0
      worker_7: 0.75
      worker_1: 0.75
    distribution_hash: b2d57a04b30032cfb44d691b82a4aaf008ffe0c491049f2b9bbab8b74b607624
  - id: 3
    dedication:
      worker_5: 0.5
      worker_8: 1.0
      worker_7: 0.5
      worker_1: 1.0
    distribution_hash: 490acfb966b968e0f6dd165ea594a19d833c4f1d8efe0228516b246826b95c27
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
    distribution_hash: 68b223215981678c7eecb67a61b1d4f6de1ee3459024ac38efccf2e04e40c556
  - id: 2
    dedication:
      worker_7: 0.75
    distribution_hash: 2090bd16147c87646718217bea5f421b170872100a7949caf9e38e2baa2dced5
  - id: 3
    dedication:
      worker_8: 1.0
    distribution_hash: 337cc487db9f1fe70287f1fd696ad99495fe4872aaff304580232787a4362b0e
  - id: 4
    dedication:
      worker_8: 0.75
    distribution_hash: cf919aff81141e19567089e3948392cd86782c819c95381897769a3f3fad6f8f
  - id: 5
    dedication:
      worker_5: 0.75
    distribution_hash: c22183350d9eab9314bd4a6d1329c6989efdd58acf3c533aecc419067281496d
  - id: 6
    dedication:
      worker_1: 1.0
    distribution_hash: 1c02b1eb9d4a598890c8086a40134de4dfbc328fdde09426a94047a040848830
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
    distribution_hash: beba8ab0a18ddbde4701e421c81067f9f348b6e3e23cda55140a5b92c47933e6
  - id: 2
    dedication:
      worker_2: 0.5
    distribution_hash: b9957eac8aa19c2a27873f3b0f36b774096826dc86b3407885f6da48ca3ff3b4
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: 8f74f014e2e5206498d32bd9469a42aba2c26beebca002c32e897f096df98a62
  - id: 4
    dedication:
      worker_5: 1.0
    distribution_hash: df2cd1105716b633343b4f667bb9b8668ceef44eba2c01e090869949c7f2c835
  - id: 5
    dedication:
      worker_5: 0.75
    distribution_hash: 39a8158dca8e5e6ac21a7b493a4fb645772450022789aed0dd1801eda4ced94d
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: f5ae64ba33401ff920d8e6ce17829952ec89d9030140559bafc74b19a9046288
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_7: 0.75
      worker_5: 1.0
      worker_8: 0.75
      worker_9: 0.5
    distribution_hash: a4dd1ba2ac73775b3b13e06a5960e009d2290cb54657c504ffd531d891852c44
  - id: 2
    dedication:
      worker_1: 1.0
      worker_7: 1.0
      worker_5: 0.5
      worker_8: 0.75
      worker_9: 0.5
    distribution_hash: d19307a4f2a01cd2d58b438c87f484a037624b0e0afdedf8377dab279fc04ad6
  - id: 3
    dedication:
      worker_1: 1.0
      worker_7: 1.0
      worker_5: 0.5
      worker_8: 1.0
      worker_9: 0.25
    distribution_hash: ac30b2f4e7bf00953c470e07cd02c76087f7266c0fc9b7befcf9bff84259191d
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: f9fda46365a845ed63f1d0a5df8982d4e01ff9bbe57d40554caaf6f982b07707
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_7: 1.0
      worker_8: 1.0
    distribution_hash: 0eb945bb9c9ecf653d98ce56d5d1fef1a88fdb2aee5464502474c990aba754fc
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: 0faa92a6115e8ff16c7e69fec58aff378432221c4e9e8011b4ebe9acc846fdce
  - id: 2
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: fd920aa31d6b9c458fb8668d28921fb302e6ca1096ab71abe9f56bd51c91cf35
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 0.75
      worker_3: 0.5
      worker_5: 1.0
    distribution_hash: 6b57735e4ab31095d233f3223808f3b082ab3aa18b7f4a54e2e81a7cdae2f89d
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_9: 0.5
    distribution_hash: 2dbee242425803ca7ddde8e45250e265c3ccc02bb91b6227376c492c8cbb2bd1
  - id: 2
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_9: 0.25
    distribution_hash: 3f91734cd8a8d773960b681f4d311b5fcfec6a2c035f99693731f88561a70ae1
  - id: 3
    dedication:
      worker_4: 0.75
      worker_3: 0.75
      worker_9: 0.25
    distribution_hash: 852ab2b10100df444fee012c69095cbf7bce5afc276dffdaeccc8c66006efb8c
  - id: 4
    dedication:
      worker_4: 0.75
      worker_6: 0.75
      worker_9: 0.5
    distribution_hash: 5c4cedfbe71e1a45a020909d91ab818b5405d1e2a9672f7b6b0106eddf2aff87
  - id: 5
    dedication:
      worker_4: 1.0
      worker_6: 0.75
      worker_9: 0.5
    distribution_hash: 6910662c8aa93724a54b3e07fcecebe5c8ec5ac121fb4446b2cc287706e1e759
  - id: 6
    dedication:
      worker_4: 1.0
      worker_6: 1.0
      worker_9: 0.5
    distribution_hash: 9ef0148f4327f1cca2e95964fd263cc3cfd34b0608952ff21f51b75b5102223a
  - id: 7
    dedication:
      worker_3: 0.75
      worker_6: 1.0
      worker_9: 0.25
    distribution_hash: 72ed12126de6d5834ba96ac4ff314b7693b47ba0fbc813ba9fa33104f2cd6612
  - id: 8
    dedication:
      worker_3: 0.5
      worker_6: 1.0
      worker_9: 0.5
    distribution_hash: df514a8e56be60943a8a49d0b6f103f29bd72cf7283ede5464c79c4d1ef036a9
  - id: 9
    dedication:
      worker_3: 1.0
      worker_6: 1.0
      worker_9: 0.25
    distribution_hash: 3ddadc86bbd6aa4ed87ab8b7327d6dfd81c3749254de25d584bdc928a205a013
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 1.0
    distribution_hash: ccc0f9036ca5b8860d00f119d9a556f66c159ef5b1f965c1e74525b80922c829
  - id: 2
    dedication:
      worker_2: 1.0
    distribution_hash: eddd899f3c95ab5dee1a4d3824b2ea52a08a37c49079ae47d53e97a6d9b9b942
  - id: 3
    dedication:
      worker_3: 1.0
    distribution_hash: 293261af3ebdabe37a80119065442cb912cfec266cb09027ee48c1d481a91928
  - id: 4
    dedication:
      worker_7: 1.0
    distribution_hash: 2705811139cf9587cc386bf73dea1104d8c33a66eb1bad02afbc1cf35d070e85
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: e2ae5b0df64244dd349a8203eac44c88627e743a63b3a942948845335135f6af
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 7d0962609616ec981a770b73abc39f61310a941ae454fa87a6154c87399a794f
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_8: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: b07fabd927af86fa911e9f47aef339b9b2732820eeed8c32c9af978b8fa5fb88
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 1.0
      worker_1: 1.0
      worker_5: 1.0
    distribution_hash: 37c7fbdc4937ab8ee9e1763999274e9f6eac27d25d8112940e20c6a19f2906b3
  - id: 2
    dedication:
      worker_8: 1.0
      worker_1: 0.75
      worker_5: 1.0
    distribution_hash: 44b120bc7abb05c8f1cbda94d7e7dc7a887f1e1a9989e5be16db2acfd6f3e538
  - id: 3
    dedication:
      worker_8: 0.75
      worker_1: 1.0
      worker_5: 1.0
    distribution_hash: 2f7250737cac826ae6100335bc38b0a1e42d525f32b6130e75d05328806895cb
  - id: 4
    dedication:
      worker_8: 0.5
      worker_5: 0.75
      worker_7: 1.0
    distribution_hash: 1fa5d4eddd336158a5c7abbc03b1bc5b5d0ef81ee85b9cdb116a804c1eb4cf76
  - id: 5
    dedication:
      worker_8: 0.75
      worker_5: 1.0
      worker_7: 0.75
    distribution_hash: 58516e8e06f9fe8e081e2e958293c6696e2d997c681b7d677390ee3e97017648
  - id: 6
    dedication:
      worker_8: 0.75
      worker_5: 1.0
      worker_7: 1.0
    distribution_hash: 9da41651cda33a0e8c8b10a45f7798fc52473c27cc31d0766708041e43bcaeb9
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_8: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 9b362b514bb4cb29fccd69c543c20a3f25646cfb676b371c8d1bbe9d32d9c698
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 1.0
      worker_5: 0.75
      worker_7: 1.0
      worker_1: 1.0
      worker_9: 0.5
    distribution_hash: f7f8adfd43d040773fa599d684d32b591586c456c1fbea80a3e8ca97ef9d63e6
  - id: 2
    dedication:
      worker_8: 0.5
      worker_5: 1.0
      worker_7: 0.5
      worker_1: 0.75
      worker_9: 0.5
    distribution_hash: 5eee5fefb92b81d4d2e077ad8359c7984acda3a94a5113a44e36d9d6c491a1f0
  - id: 3
    dedication:
      worker_8: 1.0
      worker_5: 1.0
      worker_7: 0.5
      worker_1: 0.5
      worker_9: 0.5
    distribution_hash: 9a2bcf5ecb747e9eacd1be5f8cfe577a007f7d3e2fc176bb4bbdd72a36fe8a4b
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
      worker_1: 1.0
    distribution_hash: 05e8d420596bf769235178a6bda8e2cf21f414b942c704155b80065c0bd97390
  - id: 2
    dedication:
      worker_5: 0.75
      worker_1: 1.0
    distribution_hash: 30b86e436b0fbf016188dbc132969c2e1b7af4d9ce811dd4f68a3724c600c6f3
  - id: 3
    dedication:
      worker_5: 1.0
      worker_1: 0.5
    distribution_hash: 590ac17c23ce9ac6773d16a7873c8f580b5212cedca19314956a1924a4a99069
  - id: 4
    dedication:
      worker_8: 1.0
      worker_5: 0.5
    distribution_hash: 83b55626c54ada8afe8b8b6be824ae9c1824948b383f6c8bc2fc79e2ffa7fefe
  - id: 5
    dedication:
      worker_8: 0.75
      worker_5: 1.0
    distribution_hash: 94a18e44093b1c80cea594bd3bfe6f6b60320a4d468a9ac00ccf7799ac8f9415
  - id: 6
    dedication:
      worker_8: 0.75
      worker_5: 0.5
    distribution_hash: e6dbec5ffc679c2139f7bd2a036870dda6f4eebf84d4a1431c6a462b7f20bb94
  - id: 7
    dedication:
      worker_8: 1.0
      worker_1: 0.75
    distribution_hash: cde7a5c4d3ed60cfbb5030a626850b58de23a424ee55bd04e8d5aade17adb8f8
  - id: 8
    dedication:
      worker_8: 0.75
      worker_1: 1.0
    distribution_hash: a5a06e793814d1cf40b0e0990cddcf2298afda46a45eca04a910faae05ab79f8
  - id: 9
    dedication:
      worker_8: 1.0
      worker_1: 1.0
    distribution_hash: 3e02d5c19b352faa2009811cc33111100208860310dacf58047eb4960ce9921c
  - id: 10
    dedication:
      worker_8: 0.75
      worker_7: 0.75
    distribution_hash: d80292c336bfe30b4a49ffcc84e2f44d0762f8a6fdac55eff8e324da90efbddf
  - id: 11
    dedication:
      worker_8: 1.0
      worker_7: 0.5
    distribution_hash: bccc95d6d4177e6d9af27a61011791c145856887940a74fb8df830a22f864abb
  - id: 12
    dedication:
      worker_7: 1.0
      worker_5: 0.75
    distribution_hash: 31da2c51655cc2067ea15281e3c15406cd47e4ef53393c0fdc88bdccd53af270
  - id: 13
    dedication:
      worker_7: 0.75
      worker_5: 1.0
    distribution_hash: 49f5a99c8e07de8f2a2be5ee1b5e3f57b3b12dde05d5dca983a9a4432dc982f9
  - id: 14
    dedication:
      worker_7: 0.5
      worker_5: 1.0
    distribution_hash: 7c139ecc3fba5d0fc49156cea10dbed060be0949b22ea58b5fe9c8b15021bc63
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 80542cf211331aed23b8365ebfad979191185fdf6b71ee9d14c6795667966460
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_3: 1.0
    distribution_hash: 523ab33526a7f2257b6052c4179fe9989f264b6e85da5a7ec5ee73b1cfc5de81
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 0.75
    distribution_hash: 91bc091297a447b1a43e744ddd6334c541802cd79331ef3d03b242324226f78a
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 4833b2413bc7133e0ccbbb4a141a5b78f1a6cad5707921aed6767996eaa81c87
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: 99396b8f11bf338090099c795cb6e415c2a82effed9ac0a5783d07288e123f19
  - id: 2
    dedication:
      worker_6: 0.75
      worker_3: 0.75
    distribution_hash: eb6f194894018f411186ab4567778158a9c9cbf600d3d2a2c6d865e32fa5a9ab
  - id: 3
    dedication:
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 964fcff859e7122b56288afd1364610098e261f3fd8eb526a0526ace59af1f7f
  - id: 4
    dedication:
      worker_6: 0.5
      worker_4: 0.75
    distribution_hash: 8eb5f18e659bbe077d48f9697ddce3842c8d5b8242070903ea62e7639fe46a11
  - id: 5
    dedication:
      worker_6: 1.0
      worker_4: 0.5
    distribution_hash: a2dde9e55d020232f3bcd63ec68cf719a327a379060b9b22646d1edaf46e5456
  - id: 6
    dedication:
      worker_3: 1.0
      worker_4: 0.5
    distribution_hash: d60f5fe7964d0e0ab957d4943164fbfc1fd63463a53f1d33fdfce5e775bc719f
  - id: 7
    dedication:
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: 1b7a7e33eee696f8686df503d8cc068a53679fac1f4176c8053e62af7f26e497
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_7: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 60789aca9ca81f9bdd6cb1a3998d8c26073b6c56734d4dd7f1157821000fd40b
  - id: 2
    dedication:
      worker_3: 1.0
      worker_8: 1.0
      worker_7: 1.0
    distribution_hash: 155aad5a957e57dfb1f287a4c043b18ff87650ecff754fdd17672c671ca6dd46
  - id: 3
    dedication:
      worker_7: 1.0
      worker_8: 1.0
      worker_2: 1.0
    distribution_hash: 367e1499386bb10c3ef0238f8052fef880beb9c742e10ef3f5b860e27e0c20a4
  - id: 4
    dedication:
      worker_2: 1.0
      worker_8: 1.0
      worker_3: 1.0
    distribution_hash: 779cc43a2acb42f18bbf76b45a272d0636ba4e92c81ce37026279611d8d63628
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_5: 1.0
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: 38bd9e06a04a3a23c2d771573bbd3d3d89d3470ace4e2ff470613040d73b0861
  - id: 2
    dedication:
      worker_1: 0.5
      worker_5: 1.0
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: 9cf72761b96749ae00b75ea99ccce39cd23d08ef636af09fd657da8934068b5c
  - id: 3
    dedication:
      worker_1: 0.5
      worker_5: 0.75
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: 2b4993ace777c3292086129d67f34651e5d91f175328dce7151ac807cb25cdbd
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
      worker_8: 0.75
      worker_7: 0.5
      worker_5: 0.75
    distribution_hash: dee2d656cb183ac314308ac6e61a9892abaa562917790f2ac066e21de9fcc1fa
  - id: 2
    dedication:
      worker_1: 1.0
      worker_8: 1.0
      worker_7: 1.0
      worker_5: 0.5
    distribution_hash: 5f2ffa5c713ecab06735c56dffe3b43adc87b95b784810da4e173c0e488352f2
  - id: 3
    dedication:
      worker_1: 1.0
      worker_8: 0.5
      worker_7: 0.5
      worker_5: 1.0
    distribution_hash: e0ad1e79a70d9bbdc00059481936e26158ff30d3dd2faf6cb29fe6f01a367ed5
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_8: 1.0
      worker_3: 1.0
    distribution_hash: 39897182ce4b834eaeb5ecf9cd714509e809a98d580a8fd8ab4825e136fbd6d4
  - id: 2
    dedication:
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 86b4c135b02e7ed1da894d835a43d8a23d5fcf0f5af2d65fb8d6da75c5fdf50b
  - id: 3
    dedication:
      worker_3: 1.0
      worker_7: 1.0
    distribution_hash: f2776627d5d7f6033fd33b175d39ffded9694fa557c2e5a65461c348847a0bbd
  - id: 4
    dedication:
      worker_2: 1.0
      worker_8: 1.0
    distribution_hash: d1b1d0520276a58ab45d383adc63aefacc040ee8708ac213d2f37dc0768ca4d5
  - id: 5
    dedication:
      worker_7: 1.0
      worker_2: 1.0
    distribution_hash: c746db580aeb0f5a7003a3323ca4bf10b8d1bbe3fc3f72f2f0027a6d5dc43f74
  - id: 6
    dedication:
      worker_7: 1.0
      worker_8: 1.0
    distribution_hash: 3ce8744cf70690a11973cca82b29e984a029f14480eb2d8ae4432d050adf2f36
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 0.75
      worker_6: 1.0
    distribution_hash: 1442333da936fb0bc56de66c5cfbbe107836e859d28df70f49139f1b188b67b6
  - id: 2
    dedication:
      worker_3: 0.5
      worker_4: 0.5
      worker_6: 0.75
    distribution_hash: 8a0376f29df129f0fc950fd62c4cd4ad6df7c8f39fc961767a29738f1a67fb7c
  - id: 3
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 1b2f3ac291720ff242881437a943f431c2de9f1852721c5df674156d337d076b
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_7: 1.0
      worker_3: 1.0
    distribution_hash: 498584759e794cb374f473fc0a6e8e4b7fe14a54c32222d603e491caf4436110
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_8: 1.0
    distribution_hash: ee98d0672f5cccb15f04b56e8b46a8b427747a48e1761c8e4adddac5da9671f3
  - id: 3
    dedication:
      worker_7: 1.0
      worker_3: 1.0
      worker_8: 1.0
    distribution_hash: 3e0f9a4687523945db1124219f3caedddca4af8ed04a3959a16187dd28a528ec
  - id: 4
    dedication:
      worker_8: 1.0
      worker_7: 1.0
      worker_2: 1.0
    distribution_hash: 128dba80f3d4385b9e32e1586e12abef5347edcc9450895974280c022835c37d
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_4: 1.0
    distribution_hash: 970b9f6faf227d3a54ad12fd417c53419c93559a77d73a93f66856e9ae3834be
  - id: 2
    dedication:
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 69b4b7df909a91eaa07a78124d7e0d3bac3efade38e31b329d2a1da55795b33d
  - id: 3
    dedication:
      worker_6: 0.75
      worker_3: 1.0
    distribution_hash: 1f369fc37304ac24c200ce29cc65f3312499165aee88c76ea3fa285938bf31c3
  - id: 4
    dedication:
      worker_6: 1.0
      worker_3: 0.5
    distribution_hash: d018b9fdd008a2c18cef248f3c0338dc0072a14625c7a19539f2f6283e74ea25
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 0.75
    distribution_hash: a38173fe4fd5e709e7102eb7dc3db4f13b3fdf69e6222446130e95af5f8fe203
  - id: 6
    dedication:
      worker_4: 0.5
      worker_3: 0.75
    distribution_hash: fcf79c4b7a540596e1e254c6794b91a97eac82ed8d1a7f31dff66a687cc4f525
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_5: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 5f626cf221523cd3bd40021313c8b2f3b2363599e9f5ec5177ef69c3347b8352
  - id: 2
    dedication:
      worker_2: 0.75
      worker_5: 1.0
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: e14e279aa7c58c77652206cca49809c31550e941d5badc166bf44dfa15c2436b
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_1: 1.0
    distribution_hash: af771586b82fcc8fa37c726e634e3570bc27399caff129cbde7b89c88eb22444
  - id: 2
    dedication:
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: 6d3b48bf1be47b4588e10d798e17277a57321b94177129204efc1e8e23405701
  - id: 3
    dedication:
      worker_3: 1.0
      worker_1: 0.75
    distribution_hash: 1ba36dc2fb045c37e9e4264c975f86643c054b23098deacb4caf145790c94b2e
  - id: 4
    dedication:
      worker_5: 0.75
      worker_1: 0.75
    distribution_hash: 34031a70e06566aeb093d6185265b7ac9c0319f054b9fafa06feecb9156995c1
  - id: 5
    dedication:
      worker_5: 0.75
      worker_1: 1.0
    distribution_hash: 727da2b541e4db0923170fc3ffad49d95be19e3988974d2d5b8dafdf494e5810
  - id: 6
    dedication:
      worker_2: 0.75
      worker_3: 1.0
    distribution_hash: dc2fb37e8dfb6489bfc7802897900feeb256b2c5d1bd8ba9a6fb9178e02c944c
  - id: 7
    dedication:
      worker_2: 0.5
      worker_3: 1.0
    distribution_hash: b8a1a349107ee0a088450ee5a24fbee36103674a8d3826a7dd0af68b583b81d1
  - id: 8
    dedication:
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 1317f0084c02ef004803371d0ff08df49e8902b34fb33cc044c829c55c724674
  - id: 9
    dedication:
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: f506016f4ee2eaae9b3e942d7209a94a0af9a3d5241ac6adf66fbcde4fa8aefa
  - id: 10
    dedication:
      worker_5: 0.5
      worker_3: 0.75
    distribution_hash: 0eb0679635c24fe7ad958a2b77a023ecdf70f0caad5aeae4ce663d0fb352e9a2
  - id: 11
    dedication:
      worker_5: 0.75
      worker_3: 0.75
    distribution_hash: 34232122d2df10ec69f4fb894fc1b859ea09c2c63b017d64e18af746f41c9296
  - id: 12
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 6fded97abe84ab32b8f04e8e96b99a27a1a54cd93cd11cb28951f4641d7ea59d
  - id: 13
    dedication:
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: 8e8704af1395b89976aeda26fa80a9ad33f1fd1eaabd118ae30af56814b87be9
  - id: 14
    dedication:
      worker_2: 0.75
      worker_5: 1.0
    distribution_hash: 15bac258c5d21844bedec5f3894a61bb8b66dcac21bc6ae51799a97bea7d8127
  - id: 15
    dedication:
      worker_2: 0.75
      worker_5: 0.75
    distribution_hash: 1055acea4d2919edae39b506de094fec19da731d4bd9beb93a39c96009592571
  - id: 16
    dedication:
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: c2082a3b023f6cb646769655bac4deaa8fdc95d870adb8cdb42d5a2d3d3c5f19
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
  - task_28
- - task_1
  - task_29
- - task_1
  - task_30
- - task_1
  - task_31
- - task_2
  - task_15
- - task_2
  - task_17
- - task_2
  - task_18
- - task_2
  - task_19
- - task_3
  - task_13
- - task_3
  - task_17
- - task_3
  - task_18
- - task_4
  - task_15
- - task_4
  - task_18
- - task_4
  - task_21
- - task_5
  - task_13
- - task_5
  - task_19
- - task_6
  - task_16
- - task_7
  - task_16
- - task_7
  - task_17
- - task_8
  - task_14
- - task_10
  - task_14
- - task_12
  - task_13
- - task_10
  - task_21
- - task_6
  - task_20
- - task_3
  - task_16
- - task_2
  - task_20
- - task_25
  - task_15
- - task_3
  - task_27
- - task_24
  - task_20
- - task_9
  - task_32
- - task_11
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
- - task_23
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
  delta: 642
validation:
  project_key: a832e572b1e0455502582259f44e9a54d5aa559d813a84898009e95b909ce9ff
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 154 days; worst-case serial bound: 1853 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
