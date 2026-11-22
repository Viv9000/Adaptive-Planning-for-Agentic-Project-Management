# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_11
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
  modes: 157
  tasks_at_cap: 0
  relaxed_constraints: 3
  rewired_edges: 13
  departments: 1
  quality:
  - worker_3
  safety_skill: 0
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 5
  barred_pairs: 6
  incompatible_pairs: 0
  edges: 70
n_workers: 5
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 538
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
distributions:
  adebb98633477e150d5b30bc4d40109880125255f02e19b56fb44339244b0fa5:
    family: tabular
    probabilities:
      0: 1.0
  02390fa0b3cedb2b8fd94a893713afdd26d144a3b6c46f225066b2d0a84d1ccc:
    family: pert
    a: 20.245063913324103
    b: 25.30632989165513
    c: 41.16833999479783
  9210da44c10297fd5786c7e17b06c14c94d0494cb86299a72013e897cb159159:
    family: pert
    a: 13.176859111269977
    b: 16.47107388908747
    c: 27.682104460728187
  6910eeb9b1a2ddee07bf76ba95ccefb90593bd5d1be27e7c54db73a5342fe013:
    family: pert
    a: 15.582641277680436
    b: 19.478301597100543
    c: 31.565346913591405
  67fd467b27da241658eaca2df48f9bef57fd88fbfa24ffbb9b46e42f44cb1c4e:
    family: pert
    a: 30.719745931699574
    b: 38.399682414624465
    c: 57.7048629812945
  642d28799cd5c44d2b599d87e561d689c66c9d819b5ce05767c30df9f474552d:
    family: pert
    a: 40.17648650299281
    b: 50.220608128741006
    c: 68.58810705735506
  3f70891c7dd3258f22e29673fce1a477080544c16641ab5b0972e819917978b1:
    family: pert
    a: 31.876911159532682
    b: 39.84613894941585
    c: 56.85835604731312
  bd92b0749ac72bae6a50dec1dc41fdff89c97209bdddd5b6300ed7d2534cb5e1:
    family: pert
    a: 33.54690689685013
    b: 41.93363362106266
    c: 59.6957558238194
  deebd46975d8ec9b3cc176d14721a23bf911020b8095705cef4dbb3b0b85e88e:
    family: pert
    a: 37.42834212741544
    b: 46.7854276592693
    c: 61.83490820874883
  b8824867ea7a39bdf3eb8223444ace5e78f2f23688f7012a60458b6e129dd233:
    family: pert
    a: 35.96400273279659
    b: 44.95500341599573
    c: 71.22763351038857
  c3da3957ca7d93214bceb190241a82fde1725ee6fd52814a26dd95e2df6fe637:
    family: pert
    a: 35.80962692227666
    b: 44.76203365284582
    c: 56.881158931559135
  c6b54a7a6b035b084e595a187d598b5a081d9b4c9b9dddeade36c5964aebd9a6:
    family: pert
    a: 30.537060895500606
    b: 38.171326119375756
    c: 63.24299721445311
  bbb26c6741b246de035da22d0b3a69f1e42a823b62a4189c9a15f61b69f7b2c7:
    family: pert
    a: 41.83156268180108
    b: 52.28945335225135
    c: 73.60559807171278
  552f017fb245d4fdb7d7d0cd71449b9e6cffbd2c2579848b72d093cc93173da5:
    family: pert
    a: 40.00433960929402
    b: 50.00542451161753
    c: 65.97152860158285
  62a2187b1399ae71ecee081ba1d1cdee10d2919fc3deb9d06408018620caf314:
    family: pert
    a: 29.02801515175569
    b: 36.28501893969461
    c: 76.82757660996548
  7558aa547cf1d31e683f1c89c090c7eb0077651c0eec53fb3415b46a0f58fcf1:
    family: pert
    a: 25.263952343725833
    b: 31.57994042965729
    c: 55.635823690048234
  5113b3ff0dfee092b6c844d142231307816ffd8cec654d62fd493cba8c2b618d:
    family: pert
    a: 33.38412346273736
    b: 41.73015432842169
    c: 61.28617249168547
  fc390eb8ee97a955541f24397a899387af1631c274ccc671b4d34cfe4e5f0681:
    family: pert
    a: 26.344804226087458
    b: 32.93100528260932
    c: 53.959494843785514
  579ed774a7246b69fac70064797b0a739e072b36e8c2c8d6fa643444c541d0df:
    family: pert
    a: 27.859121040551976
    b: 34.82390130068997
    c: 75.25430264382001
  b43585b7f20574ad1d725ac1f47411d94b11f8fce6fb0c2d907a49e53a5171d5:
    family: pert
    a: 26.71195546347189
    b: 33.38994432933986
    c: 55.55594929441177
  12d722b85aebce40add92b0a3578c8fa539096df522dcd92052677775d77727e:
    family: pert
    a: 32.2765057392023
    b: 40.34563217400287
    c: 51.282041019151485
  cc02f2b9d14a86aeae50184cabbaeb26a98fb882d0d95a568612763696513cc1:
    family: pert
    a: 24.645057318956454
    b: 30.806321648695565
    c: 51.679332806401234
  62b7c36b72cf4f1c4305ace7620a09e8a08023080bacdb96a8f430bc96ae8e55:
    family: pert
    a: 34.55177877545264
    b: 43.189723469315794
    c: 60.459815467052884
  fcfa9d8f8bdbb7283aeb9496901ca46aa02a4c84e0eefd18670524c340e272f7:
    family: pert
    a: 23.980175393003925
    b: 29.975219241254905
    c: 47.9866805279864
  1a0483f2998f08df292103586b6631c625fd5ac7646d24dcb1ab9111595b457b:
    family: pert
    a: 24.912913819522753
    b: 31.14114227440344
    c: 53.82721613953801
  908404192ad2ac3b053b3c1016befc2d90a189cfbc9c7a68b9490704f4fbe722:
    family: pert
    a: 39.106682286801714
    b: 48.883352858502136
    c: 67.54806201843398
  fb26dfb0f6b46b7bbef221bcc47d1382097781010ee21e9e105c4b296b4d6669:
    family: pert
    a: 29.03167730935668
    b: 36.28959663669585
    c: 55.041688976526416
  f05babe866011bf7566a565a43f789f68a1b0096ac0336202ee1ee6f10c043f8:
    family: pert
    a: 15.539793376421606
    b: 19.424741720527006
    c: 35.3616435503386
  80698b77adf514eddedec81725726a76d839ce278194c6ba172ac2331a4d5855:
    family: pert
    a: 13.764651064641312
    b: 17.205813830801638
    c: 28.300888433569092
  f8f30768440f59b06e16d762cc37baee9a50d8921ef8b56c01521564d1b84903:
    family: pert
    a: 19.628767433581512
    b: 28.041096333687875
    c: 57.68526981608112
  5cf88c63ad29e106a40b086e77752799993b884b5c474a27ec9ede48dc499372:
    family: pert
    a: 29.148531189903398
    b: 41.640758842719144
    c: 66.51261670771069
  09cfb74160a79fccd48b66b1d386fc872495ded465e988d569ae3858dab5f27e:
    family: pert
    a: 13.013118824280507
    b: 18.590169748972155
    c: 41.49759691364175
  234e1f805cb9286072fe02998219d4ffb8bb5781ba74112951cad270a227bf4a:
    family: pert
    a: 18.358426032626536
    b: 26.226322903752198
    c: 42.268479171416814
  dc023720189d3c139f2d7a331e5ebb31d22c03d08f65d7b257ec3827fc7502ee:
    family: pert
    a: 19.398763688545955
    b: 27.712519555065654
    c: 54.30893366030787
  18e47bf689f8ef3d89932285dc83f01dc619af0bcea4a4730029f22444604e0d:
    family: pert
    a: 19.31856185526692
    b: 27.597945507524173
    c: 47.898608216626734
  c2a1907c32994213c15fd4ea7b9ca67f453eb6d073561fa4e67cf34049138a1f:
    family: pert
    a: 15.08902938602797
    b: 21.555756265754244
    c: 74.66876478013349
  f92a7e38f2e864625fe5a245701e1467068e8d2cec1c4051ab949405afd98d68:
    family: pert
    a: 17.68321877230356
    b: 25.261741103290802
    c: 49.63850041344725
  9d505aa35a20f38ba32b551db3bc963af25582979c42ffdf632d2fd5cc8e043c:
    family: pert
    a: 33.390162562150756
    b: 47.70023223164394
    c: 62.95867853257269
  4a33d7395683b758ca4d3210cd7706804716b52664d9806854be18b4e7a3ed87:
    family: pert
    a: 11.849559421408582
    b: 16.92794203058369
    c: 49.84362338487553
  a91dfd006bf3b7af046a4bd68673a3455e2e906ca5e8fc0752a775615f6ed357:
    family: pert
    a: 16.049286114400417
    b: 22.927551592000597
    c: 46.742494913334944
  754b2119448142a1a8c906627e984e1f8980ccc5c684552252e7aaf460ee0903:
    family: pert
    a: 16.894232141994124
    b: 24.134617345705895
    c: 54.01498458176664
  335e9aac1819fb781747eda51fd23e517b7283c6a08feaa9700c772580b77096:
    family: pert
    a: 15.207596332764375
    b: 21.72513761823482
    c: 47.06847688881902
  4dfb40bb9b45b80740b7588f9993c5544abdb8408f23c23cf10d21891f85bf2e:
    family: pert
    a: 17.2661373866364
    b: 24.665910552337717
    c: 72.3398737189359
  3f0bffa83b695109cfa925500e9b3eb18edc13897315cc26cdd6b6e7a1ae8497:
    family: pert
    a: 21.852778758194383
    b: 31.218255368849118
    c: 59.43209638927169
  ad13f0cc528d26f54072eb5c9fab779f4bfde84258484a045f439eb5b0e85cd6:
    family: pert
    a: 24.92313193286735
    b: 35.6044741898105
    c: 93.02166101996598
  ff141cb62a258146b7d9c5ba752eaf9a0c993f8fd26caf3bb6a7fe4e57905f32:
    family: pert
    a: 11.264684667894532
    b: 16.09240666842076
    c: 54.47808393411303
  8309712250d8c6394924854f6e7f4b3cf44b47bb08b358d86a6591abbaeddb47:
    family: pert
    a: 2.2793414211240277
    b: 3.798902368540046
    c: 11.910754235089831
  15b1d7b515bd8ee398ceb2cebb317272fc6dce1b47529937dc2e0660615b82c6:
    family: pert
    a: 2.2946729677156963
    b: 3.8244549461928274
    c: 13.945923765981645
  c6c5f4c53adf5746564efdfad255d16923fa9d118fad9f15d424e126c8514cb2:
    family: pert
    a: 2.17524609582613
    b: 3.625410159710217
    c: 9.867364528566926
  7be3c81dd36781f154475df74ef6c0b929c0b384579bbd25b7fe47850b4420ce:
    family: pert
    a: 24.378824785301198
    b: 34.82689255043029
    c: 74.16319773678126
  8e130f2e0ee1ceac5f71a1ff71f5302c541bcf5b7d9f1763c7946b3aa64fb396:
    family: pert
    a: 8.769990322747566
    b: 12.528557603925094
    c: 25.46028484931534
  ce744910e6001c26c85cdcfc4aaabd81f878df92e85cf25df2af0e5974844821:
    family: pert
    a: 18.22945465251192
    b: 26.04207807501703
    c: 48.35474990708358
  999de2a5bfbda4cbc987e1ad49b83a60cf397dca995cb2ecbd35688ffc0ede0b:
    family: pert
    a: 11.010876647180302
    b: 15.729823781686147
    c: 32.45105899219882
  6b888cee82cb22c3e01c676a9e6925acb165163c003befd44064951e2e41d152:
    family: pert
    a: 12.128082003722568
    b: 17.325831433889384
    c: 26.41961838061738
  7495426903a4a1a3f717fdb7e40cadbfd4db00a4f6b55f84f4d24e3dfc0c6781:
    family: pert
    a: 24.83901654968867
    b: 31.048770687110835
    c: 49.411446627750834
  8019a41a531e94d01c29d2215e1fb46b733d052be407c029bae438dbb0ed932a:
    family: pert
    a: 30.970465940718476
    b: 38.713082425898094
    c: 59.63734659043085
  6125f297390e3e10a6b56cf99c04f2b9395f71717564ef20540814d30ba0de34:
    family: pert
    a: 40.11469965805954
    b: 50.14337457257442
    c: 64.35917898707145
  31ababfd822788ad8621af208bf157d9de56418e57704b175493144d56c14c51:
    family: pert
    a: 28.66112552183766
    b: 40.944465031196664
    c: 87.90935654719848
  882b9e7bc94493f456232b021a8761342fb1fd9c47b35ab36ad6183873ab7d9b:
    family: pert
    a: 19.936368013444184
    b: 28.480525733491696
    c: 59.05800306825645
  486baf35bc4d494f96517ed67d762329e80de12da945721dc71f689462a6c479:
    family: pert
    a: 39.76687330395115
    b: 56.809819005644506
    c: 87.6775394842339
  ca6aa064a110c566de075fb7b708596d91a1ce5f6bac4f04b7e772767730f155:
    family: pert
    a: 21.78689171655768
    b: 31.12413102365383
    c: 65.68558006778865
  d3781c326037f19eb3e9f1e1c464721623d301f5f426f4cda8b1f864b9edbdf2:
    family: pert
    a: 30.41858679566727
    b: 43.45512399381039
    c: 74.23578980554622
  7d547cdc7380a618e0d11fe4d708b3b6f4583d3b73c1c7bac0d552d76315d1a7:
    family: pert
    a: 23.315051807752937
    b: 29.14381475969117
    c: 53.27938801845152
  ae404c8a40a987ca64cf163a9135945324c35ece3dc28036ae85b7bbbc364e6d:
    family: pert
    a: 28.716762693135166
    b: 35.89595336641896
    c: 48.820233293164826
  c92a2cc1933b11915818e5d82df06218f853c6f53a5fe7c2b681b5aeeb150a71:
    family: pert
    a: 17.87323689768455
    b: 22.341546122105687
    c: 61.38764866475823
  0ff7aede2d0fcc46929b28149ee93695eacecc4223279f086df30e0c8f5c3071:
    family: pert
    a: 41.29920732969206
    b: 51.62400916211507
    c: 93.91380777763437
  8f5210c39540923f613044b1e64b553c03aef5f1051395d7c1f1ae204a5a8cfb:
    family: pert
    a: 19.213514751518275
    b: 24.016893439397844
    c: 46.545996607570075
  4719e44bec084e4fef75ec7f0e205b6c18cb7a4235d4baacf02aa1651aacd6b7:
    family: pert
    a: 5.501871775522439
    b: 6.8773397194030474
    c: 34.38669859701524
  d8f9bdd6c9b228746a662fe9edee6063729454002a5c6220bd64b2203dc9083b:
    family: pert
    a: 3.791074902153627
    b: 4.738843627692034
    c: 23.69421813846017
  1e071676fbf6cab2a222d1db3d33057ef45f158a00f0b54282b7477aac02a979:
    family: pert
    a: 4.740186797589281
    b: 5.925233496986602
    c: 29.626167484933006
  f0f2ab683c20867129a4cc12ea0969f6572ce8990b5c3eca893ec2d6ba7bd49c:
    family: pert
    a: 32.18129452653112
    b: 40.226618158163895
    c: 53.829912061972976
  6a40a987e44ceac21e4e6b41b9867f294282d4b9d2a35668dc1ccb1b5179acb8:
    family: pert
    a: 19.437254325882886
    b: 24.296567907353605
    c: 45.41896951891436
  00cc07fb50d44b9a073a3970d20efd7ae4fc20888e58c0fc2ac296ab25b7441e:
    family: pert
    a: 25.49919898441675
    b: 31.873998730520935
    c: 55.07723472970402
  b93258554dad94be6c94d49dfc39cce93b9ea0edceece9a075707870730d834b:
    family: pert
    a: 16.019652624316596
    b: 20.024565780395744
    c: 35.13011945401682
  ac7f3ab6fc28fe3be1e20ce83175e7117c3fdba6a16f286b5df428f1ba3fb1d5:
    family: pert
    a: 20.016622208041976
    b: 25.020777760052468
    c: 38.04690544021236
  9a8c63fe7d0c3494f604d346d0b549fe89f13d9e1d9859a6d8c472188ea932fa:
    family: pert
    a: 16.704033412697022
    b: 20.880041765871276
    c: 35.882762334750815
  b944b2906b12d7966f1a6de50d08241958ada9f6f4bbe25bb9589d9fdc9136d8:
    family: pert
    a: 22.057001426322415
    b: 27.571251782903015
    c: 77.72192351692566
  2f4f0d70e74b97a410d7e75f0a87a5948d39df2a0842c5ab6e6c03076a6a0a6a:
    family: pert
    a: 25.713704955521383
    b: 32.14213119440173
    c: 46.75817246418997
  9a05461efce11916787cb67a70ab6a43b1c266e6181e78bb99d93e0a5a67ff0d:
    family: pert
    a: 18.9009197066356
    b: 23.6261496332945
    c: 43.27760686783609
  3f9e7fddd1ca0327c3574f9719466d1bc01f04978a29cad3c6f702656d5c637c:
    family: pert
    a: 20.09157855813174
    b: 25.114473197664672
    c: 44.975640587216766
  8ae4f860d1f60719551b62e8b5483cf7f111c7aee1a4a75562c5991d6abc2376:
    family: pert
    a: 17.06968602309002
    b: 21.337107528862525
    c: 40.315651047203644
  49890d2f52a77adc5eb3d44d4037ba8ad1ad237321050e4b37900b0308d952b7:
    family: pert
    a: 29.736639375852704
    b: 37.170799219815876
    c: 45.92652738663509
  cf5eb15e5b8b04fb7613dc84943ff951b995300346f8bbd7e8e54543cd52ce99:
    family: pert
    a: 28.78852123627333
    b: 35.98565154534166
    c: 68.28058648547933
  f54a278a3f555dabbbd4cb0905c765abadb4b91a006c5e10e359877d69b3b086:
    family: pert
    a: 15.578774440774048
    b: 19.473468050967558
    c: 39.29302972379193
  44593603fab757fbf0a9d24e1f796178af59bd1b37b4ec98f12c0220d0cb1b03:
    family: pert
    a: 14.827343227016328
    b: 18.53417903377041
    c: 39.63336614810172
  440c555014196480fb3054710fada43e44fe5da0bf3022d77729cb4c54b67ebd:
    family: pert
    a: 21.3182533079623
    b: 26.647816634952875
    c: 65.59070839600004
  e6b3fd63121682c707d44c4f2c5e5dbc7e34f89e381b53f6c01e80566d2b21dc:
    family: pert
    a: 5.699562741240441
    b: 8.142232487486345
    c: 11.466013657663606
  b51dd7c851e7f0366c1b68138c32fc94f762ac185d4073dfbb3c02aab8759f20:
    family: pert
    a: 2.440064904464284
    b: 3.4858070063775486
    c: 9.91606827859703
  611320ca59c80aa56d3bb716e8af8d70249cd6a6662177407769b8ec65c1b7e8:
    family: pert
    a: 2.3287174540492734
    b: 3.326739220070391
    c: 9.78268399915795
  06ae42d6bdffcac6179eaaa6d1d395fca13282653b00a9752a9a60c427241de1:
    family: pert
    a: 4.906647958227235
    b: 6.133309947784043
    c: 8.899658268753273
  be07a9803b8ca1658de84f7d7155c4a1912a2a2a2c8216b280e3d416f23b9f76:
    family: pert
    a: 3.5494501734133053
    b: 4.436812716766632
    c: 6.923540076787711
  c553531b589177f2cf500b24717872999337aa769a47aae862a5a314042c8ef9:
    family: pert
    a: 3.708999983784351
    b: 4.636249979730438
    c: 7.324180772281615
  1f663ab2dad23dfdf6e8f56b5e32feaee2c1e19b64e855a90143842ab340dc24:
    family: pert
    a: 34.84704345510519
    b: 49.781490650150275
    c: 121.45944088516467
  f3f4be4a60d3167ffa2efe4d649879d9fa53a2cb2e8582cc6ac6a357e40ae7cc:
    family: pert
    a: 24.918483866950538
    b: 35.59783409564363
    c: 189.655449234767
  5e933d39085613a9ee65d7012eb3bf5cd8ea79a94917e0feaefb2e9136055629:
    family: pert
    a: 25.499342659000156
    b: 36.427632370000225
    c: 164.6824879123791
  06e6822f22bf4fd436e7b611c1fa4bec97e4759475b314ca273750352f4ad983:
    family: pert
    a: 80.59904745521477
    b: 115.14149636459254
    c: 283.3887050431535
  617035df3042cd38b1caba22ee0433c1546e2b501b2e3a91fde374e9d3f1d32f:
    family: pert
    a: 26.78660827728772
    b: 33.48326034660965
    c: 48.37403361389659
  20a0a4fb9150df254bd0a1bb407a253cd03e91a2b5466510bebde1fd0d0b8d82:
    family: pert
    a: 19.08265168007176
    b: 23.8533146000897
    c: 40.2112437166249
  829c26d2d5a93b8d01a9b301a435843fd4d8ee042cc60d29b21d17835683aa05:
    family: pert
    a: 17.90629185539846
    b: 22.382864819248077
    c: 34.80055583828127
  f416ff7b27de07f0a99ea2e702a7322460aafd8a4e8d02ac95f32ffb53477afa:
    family: pert
    a: 18.729844971026605
    b: 23.412306213783257
    c: 32.165175213721405
  44621a0280fa91b22015c1b40f2e093486b5fbfcd063225e6035526bdb8fd4fc:
    family: pert
    a: 14.110752206095496
    b: 17.63844025761937
    c: 34.09640609983982
  5871483492f0c1b16db829ba741975667dd4e725ad778f9e9aafbb4838b78284:
    family: pert
    a: 14.032501346096943
    b: 17.540626682621177
    c: 29.845018375421873
  c7027c8b8d18c177d1ad9498c1164bbb6aa6391b1bfcb3c84dc8024b8c3eaa32:
    family: pert
    a: 11.223031952607716
    b: 18.705053254346193
    c: 43.398099153917705
  0e71eafbf1b8cef71cd4a00862864c7689e0524aa436511ac2a510f4cff6c3ed:
    family: pert
    a: 6.805345630142733
    b: 11.342242716904554
    c: 49.69687288512965
  102086e79666f6d0b47dab48e2c4e42138cb8ffe50c6e834b363c3cbd4fa09d9:
    family: pert
    a: 8.971751338214908
    b: 14.952918897024848
    c: 65.15032813625106
  3b2d7cbb7d9ece71dbc1a328cf677b96a22301e412f9c64aa9c12fd84e7d9d22:
    family: pert
    a: 12.042338179351638
    b: 20.070563632252732
    c: 67.55241827448876
  c7d4b255994019e0749e330edbfd200fbb3a66a97222b92257b0d345dc90f62f:
    family: pert
    a: 10.498977340841103
    b: 17.498295568068507
    c: 45.226035136094524
  7d9029ef403576906ccf8fa0c235bca59ee436ff96f18dbaafacf930c2be201b:
    family: pert
    a: 10.740861574073984
    b: 17.901435956789975
    c: 39.966688449472485
  bd4e4070c9444a3bfd8d015dd15657182fa5294bfe6da737b455499af1f36dea:
    family: pert
    a: 9.576428921420106
    b: 15.960714869033511
    c: 58.581554758600134
  d3b7887af0a426142d392bcf0b924d6d7cb2a426d033a53c82bbec931e9ab252:
    family: pert
    a: 8.124985625956025
    b: 13.54164270992671
    c: 33.49746287885533
  403719ed05933a8c806d85ee72590998a7d16d897bd8f4678dbde7119d386d53:
    family: pert
    a: 6.219078369213072
    b: 10.36513061535512
    c: 32.09196573161622
  c32950c16827e393ba3e7e8b0072c1590aa7b0f408781aeaee5054cb6482b9aa:
    family: pert
    a: 10.97274954234473
    b: 18.287915903907884
    c: 37.17373545925396
  0f3f960783bb6442a4e312fb9f0550a8beb39953fd33b788d749c58cee9a3475:
    family: pert
    a: 7.795607155491104
    b: 12.992678592485174
    c: 50.85718449848
  8b16429e760719d78acd536013a1d20b871af84dfa6b95110f710aaa78890466:
    family: pert
    a: 4.647188565719437
    b: 7.745314276199063
    c: 81.60835657157064
  787d50cabbc484f444789122fdda2309382b99c2ec586adbfd06cbe41c652735:
    family: pert
    a: 7.791208182672295
    b: 12.985346971120492
    c: 64.92673485560246
  32504c06558b2f2333bef7d389807361005330b16cd646eced2b57ab6033ebc2:
    family: pert
    a: 7.873076261304215
    b: 13.121793768840359
    c: 65.6089688442018
  9cf9a42f44be6dec361b780bcd9cfda9ebd063f8f51480378b4ae52c75c57edd:
    family: pert
    a: 22.781544197884056
    b: 37.96924032980676
    c: 110.54721436275739
  8ee00910d9432431faf864b92858a38c0a2319f6d1d01640c5a46e6bb0eb140e:
    family: pert
    a: 15.338113797387718
    b: 25.5635229956462
    c: 106.94194944839715
  ed9a77653b54a680bb1a29b845c8085989b7f47e600789d65f4537cf89185a46:
    family: pert
    a: 18.451266073679097
    b: 30.7521101227985
    c: 189.9106280976579
  a2d2b5f886c931725b4f6551b6fc5f3e3b90133e6f21d106ac898aa5eeb7af51:
    family: pert
    a: 9.528325029194962
    b: 15.880541715324938
    c: 113.85311121664152
  719ce46807cf620d065a4c37b7a37af711f9020927ce56a4bde98595097558fa:
    family: pert
    a: 13.884348957957743
    b: 23.14058159659624
    c: 58.94659488575895
  9767ef28391005ea8cb35f7bfd6c9130b2f1c61d22751539b8ec708ed1ce1a11:
    family: pert
    a: 13.235421679550996
    b: 22.059036132584993
    c: 69.66155535343523
  cca327b242480e1dd2b86b39a1411c959c6013141d8e52f7cb5c931c02a5f7f1:
    family: pert
    a: 11.216236056700065
    b: 18.693726761166776
    c: 70.49194765251312
  07a2bc29947eff2ca27007a4401f1d36e5a138689f69e99122bb6156b9592a9e:
    family: pert
    a: 16.0059602093642
    b: 26.676600348940333
    c: 121.01786116394628
  9406641a8b245777f537d14fc382c96469f79d6e8c54e1c2ef26c6e45538bcf3:
    family: pert
    a: 12.166422356921888
    b: 20.277370594869815
    c: 78.17179951098268
  99e3df59b35ae22475f87d6e8340603d258fac0d7fd25d1291f0ac61c4e7c796:
    family: pert
    a: 13.695293860502495
    b: 22.82548976750416
    c: 107.22944105275285
  63e844140f037a3c9ab521cb379c65f59ccb0849599a1d64a3301391ed27f8c9:
    family: pert
    a: 14.839025225797446
    b: 24.73170870966241
    c: 129.67007580435896
  e7da37a35e0d2e7de8aa745612612a7e099b1a2b557aee7b29afc3c075d6cc3e:
    family: pert
    a: 8.707537704565715
    b: 12.43933957795102
    c: 34.6138199485286
  7ad1fa2b2696dd4f5ba8132c2350c6dafa15be62a427419e956b75ebfa8e0ab6:
    family: pert
    a: 8.575344886369512
    b: 12.250492694813591
    c: 45.23893615337038
  5005876550f25317f41480ca420bec273671953ac8e6d45581577d397449799d:
    family: pert
    a: 14.643886699332688
    b: 20.919838141903842
    c: 38.52346736256364
  00d85c633db7dd85dcd8ae3b2252a4631fa2acc8eefd333ccf7ce46085f074ba:
    family: pert
    a: 9.215647327260012
    b: 11.519559159075014
    c: 20.579841967320878
  c650c21e8592d7ceb63d3fdcce5889f592c57a0d1a1318f25627723c16b87a02:
    family: pert
    a: 10.124937495369522
    b: 12.656171869211903
    c: 18.174999198294003
  3eea811886b58a6235130e071f37b89726efe9c65f697f5fa4d3d8290c58073a:
    family: pert
    a: 14.464683531843349
    b: 18.080854414804186
    c: 26.670181617175444
  e5f317f83e3287f4bd9573b56b92f483a8c30a67271b0df0d4e8ca506eb01b2b:
    family: pert
    a: 13.856347145806524
    b: 17.320433932258155
    c: 22.603742293966754
  f0dee8b91a0ef377a81973445f872f08a3223978cf7a0643f27c3c3447ad6c7d:
    family: pert
    a: 11.285901198312544
    b: 14.10737649789068
    c: 25.796924538210014
  f3c40a6e5cc1816b9b967ac008ad249961eb3c909232933fbdb60bbb69b2cd89:
    family: pert
    a: 11.691306719020368
    b: 14.61413339877546
    c: 39.79520650748459
  3ec877e793ff3e467654e2d51da0143917222ee8ada150f7bcddf2aaefef7085:
    family: pert
    a: 12.548740323700601
    b: 15.68592540462575
    c: 18.943326522610526
  3fb036bf75e8c8e0d224c1ab9c0e335eb1eb8cfb24c1f8b3e4e0636193819aa3:
    family: pert
    a: 12.314734805258157
    b: 15.393418506572695
    c: 23.597597051630864
  d6dca124151a5d9dea0e5063b08dc31ea92d6271648fc826a7f19020faf4b15a:
    family: pert
    a: 11.63210915427824
    b: 14.540136442847798
    c: 20.86921184390999
  8e29f8a6257c350b082fcab971e058e99a9e0965a8330690dfacac50e7592f01:
    family: pert
    a: 13.889836580091227
    b: 17.362295725114034
    c: 27.477103649088
  1c85b8c7d59c50bb5e3888b1745cfac4a847c1a6e0922a2c6ecdb9487845e9f8:
    family: pert
    a: 18.033299535809054
    b: 22.541624419761316
    c: 41.77354715930791
  74c3fedf37225e566bfc1b554f294cef60a6dd7b5a9d084236b6caabdb9b2871:
    family: pert
    a: 12.97513904014039
    b: 16.218923800175485
    c: 21.3752235263972
  e2a6d71e3b7e09d7ac98ba7d0249af9c9df995193f6af88f9fb73f6518f236c4:
    family: pert
    a: 9.581390234469374
    b: 11.976737793086718
    c: 20.567815987571436
  5cca5614389a56bfc53d60d5accd5b02895285f1a4b011cec00f1ca67b45a5f9:
    family: pert
    a: 8.768427816515619
    b: 10.960534770644523
    c: 21.854566505972556
  e7eb88bb85282937160d94a5b23dfb909ddc7dc13a12ef043abc007a4344ff5b:
    family: pert
    a: 15.979573798194245
    b: 19.974467247742805
    c: 30.771847800581654
  86ba84239c0d7777ce19bfdec61543d764177e74f05e3cc363886b60149ca3bd:
    family: pert
    a: 10.880814912054346
    b: 13.601018640067931
    c: 24.517648986913578
  a2e7f9975a19af7953d1dd1f01fcc23dcae5503f0d54add11e0d1064a7f52a5b:
    family: pert
    a: 26.332004447679083
    b: 32.91500555959885
    c: 48.47450113974221
  27fafe63f5e6113fb49df096fba17ab9f7fe01beaceffd3bdb5cb6e42841b049:
    family: pert
    a: 27.279212095656625
    b: 38.97030299379518
    c: 123.05759793982544
  9ad32eadc076b716ba1c157243075a5ce6645e74ca5072b52f24d90b0244f755:
    family: pert
    a: 51.80527966564719
    b: 74.00754237949599
    c: 195.6857334798006
  d7caa8adc50532131a30d30933e8f2de5ad0e8aacccd8a5889f56217e7b29e5d:
    family: pert
    a: 23.223515557556556
    b: 29.029394446945695
    c: 54.8770659978781
  2cdc804de6c1656d3ce2b954d9628ca9315f23a55e5bb6b6b208d912ae8d72ed:
    family: pert
    a: 36.380367284108665
    b: 45.475459105135826
    c: 227.37729552567913
  2d4e292d70320c565b9c657d94acd5e644229fc11ac32a47a905814ec5b90a9d:
    family: pert
    a: 34.771867024428886
    b: 43.464833780536104
    c: 217.32416890268053
  11bd2b871baa84a1219a75f7184fe0a965cf495858ddbeac61b0769cf552347f:
    family: pert
    a: 3.0775309170922682
    b: 3.846913646365335
    c: 6.905495481388759
  cb57d22d6b8237f04ecfde1a5ef6407b7f3018ecba78910d1f69393ea9ec5cb9:
    family: pert
    a: 2.530162168720996
    b: 3.162702710901245
    c: 5.682433937209933
  e2aa3e87fe604d8cc5aa543c440eab615b511a67555eabb630c45b14952e94b0:
    family: pert
    a: 4.312624336486231
    b: 5.390780420607789
    c: 7.100134033814498
  964d9c96f643569e79d517a43412b4f0d5df03d8518dc28830d59ad0248755e0:
    family: pert
    a: 25.20942725333356
    b: 42.015712088889266
    c: 132.99868721306726
  25c15bc47354e72fcacb06d6892d5013d259ef5a2d90633d96a9ef9bf1bed95b:
    family: pert
    a: 19.86035579871977
    b: 33.100592997866286
    c: 160.62988672794071
  c10050ff646ef27b16d1ed445a5139b93eb63f494e68cd7f940cd96356856c11:
    family: pert
    a: 24.402592113095345
    b: 40.67098685515891
    c: 192.02347362701573
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
      worker_2: 0.75
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: 02390fa0b3cedb2b8fd94a893713afdd26d144a3b6c46f225066b2d0a84d1ccc
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_4: 0.75
      worker_1: 1.0
    distribution_hash: 9210da44c10297fd5786c7e17b06c14c94d0494cb86299a72013e897cb159159
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 0.5
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 6910eeb9b1a2ddee07bf76ba95ccefb90593bd5d1be27e7c54db73a5342fe013
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 67fd467b27da241658eaca2df48f9bef57fd88fbfa24ffbb9b46e42f44cb1c4e
  - id: 2
    dedication:
      worker_2: 0.75
      worker_4: 0.75
      worker_3: 0.75
    distribution_hash: 642d28799cd5c44d2b599d87e561d689c66c9d819b5ce05767c30df9f474552d
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: 3f70891c7dd3258f22e29673fce1a477080544c16641ab5b0972e819917978b1
  - id: 4
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: bd92b0749ac72bae6a50dec1dc41fdff89c97209bdddd5b6300ed7d2534cb5e1
  - id: 5
    dedication:
      worker_3: 0.75
      worker_4: 0.75
      worker_1: 0.75
    distribution_hash: deebd46975d8ec9b3cc176d14721a23bf911020b8095705cef4dbb3b0b85e88e
  - id: 6
    dedication:
      worker_3: 0.5
      worker_4: 0.75
      worker_1: 1.0
    distribution_hash: b8824867ea7a39bdf3eb8223444ace5e78f2f23688f7012a60458b6e129dd233
  - id: 7
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: c3da3957ca7d93214bceb190241a82fde1725ee6fd52814a26dd95e2df6fe637
  - id: 8
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: c6b54a7a6b035b084e595a187d598b5a081d9b4c9b9dddeade36c5964aebd9a6
  - id: 9
    dedication:
      worker_1: 0.75
      worker_4: 0.5
      worker_2: 1.0
    distribution_hash: bbb26c6741b246de035da22d0b3a69f1e42a823b62a4189c9a15f61b69f7b2c7
  - id: 10
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 552f017fb245d4fdb7d7d0cd71449b9e6cffbd2c2579848b72d093cc93173da5
  - id: 11
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: 62a2187b1399ae71ecee081ba1d1cdee10d2919fc3deb9d06408018620caf314
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_3: 0.5
    distribution_hash: 7558aa547cf1d31e683f1c89c090c7eb0077651c0eec53fb3415b46a0f58fcf1
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 0.5
    distribution_hash: 5113b3ff0dfee092b6c844d142231307816ffd8cec654d62fd493cba8c2b618d
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: fc390eb8ee97a955541f24397a899387af1631c274ccc671b4d34cfe4e5f0681
  - id: 4
    dedication:
      worker_3: 0.75
      worker_4: 0.75
      worker_1: 0.5
    distribution_hash: 579ed774a7246b69fac70064797b0a739e072b36e8c2c8d6fa643444c541d0df
  - id: 5
    dedication:
      worker_3: 0.75
      worker_4: 0.75
      worker_1: 1.0
    distribution_hash: b43585b7f20574ad1d725ac1f47411d94b11f8fce6fb0c2d907a49e53a5171d5
  - id: 6
    dedication:
      worker_3: 1.0
      worker_4: 0.5
      worker_1: 1.0
    distribution_hash: 12d722b85aebce40add92b0a3578c8fa539096df522dcd92052677775d77727e
  - id: 7
    dedication:
      worker_2: 0.75
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: cc02f2b9d14a86aeae50184cabbaeb26a98fb882d0d95a568612763696513cc1
  - id: 8
    dedication:
      worker_2: 0.75
      worker_1: 0.5
      worker_4: 1.0
    distribution_hash: 62b7c36b72cf4f1c4305ace7620a09e8a08023080bacdb96a8f430bc96ae8e55
  - id: 9
    dedication:
      worker_2: 1.0
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: fcfa9d8f8bdbb7283aeb9496901ca46aa02a4c84e0eefd18670524c340e272f7
  - id: 10
    dedication:
      worker_3: 1.0
      worker_1: 0.75
      worker_2: 0.75
    distribution_hash: 1a0483f2998f08df292103586b6631c625fd5ac7646d24dcb1ab9111595b457b
  - id: 11
    dedication:
      worker_3: 0.75
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: 908404192ad2ac3b053b3c1016befc2d90a189cfbc9c7a68b9490704f4fbe722
  - id: 12
    dedication:
      worker_3: 1.0
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: fb26dfb0f6b46b7bbef221bcc47d1382097781010ee21e9e105c4b296b4d6669
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: f05babe866011bf7566a565a43f789f68a1b0096ac0336202ee1ee6f10c043f8
  - id: 2
    dedication:
      worker_1: 1.0
    distribution_hash: 80698b77adf514eddedec81725726a76d839ce278194c6ba172ac2331a4d5855
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: f8f30768440f59b06e16d762cc37baee9a50d8921ef8b56c01521564d1b84903
  - id: 2
    dedication:
      worker_4: 0.5
      worker_2: 0.75
    distribution_hash: 5cf88c63ad29e106a40b086e77752799993b884b5c474a27ec9ede48dc499372
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 09cfb74160a79fccd48b66b1d386fc872495ded465e988d569ae3858dab5f27e
  - id: 4
    dedication:
      worker_1: 0.75
      worker_3: 0.75
    distribution_hash: 234e1f805cb9286072fe02998219d4ffb8bb5781ba74112951cad270a227bf4a
  - id: 5
    dedication:
      worker_1: 0.5
      worker_3: 1.0
    distribution_hash: dc023720189d3c139f2d7a331e5ebb31d22c03d08f65d7b257ec3827fc7502ee
  - id: 6
    dedication:
      worker_3: 1.0
      worker_4: 0.5
    distribution_hash: 18e47bf689f8ef3d89932285dc83f01dc619af0bcea4a4730029f22444604e0d
  - id: 7
    dedication:
      worker_3: 0.5
      worker_4: 1.0
    distribution_hash: c2a1907c32994213c15fd4ea7b9ca67f453eb6d073561fa4e67cf34049138a1f
  - id: 8
    dedication:
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: f92a7e38f2e864625fe5a245701e1467068e8d2cec1c4051ab949405afd98d68
  - id: 9
    dedication:
      worker_1: 0.5
      worker_2: 0.75
    distribution_hash: 9d505aa35a20f38ba32b551db3bc963af25582979c42ffdf632d2fd5cc8e043c
  - id: 10
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 4a33d7395683b758ca4d3210cd7706804716b52664d9806854be18b4e7a3ed87
  - id: 11
    dedication:
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: a91dfd006bf3b7af046a4bd68673a3455e2e906ca5e8fc0752a775615f6ed357
  - id: 12
    dedication:
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: 754b2119448142a1a8c906627e984e1f8980ccc5c684552252e7aaf460ee0903
  - id: 13
    dedication:
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: 335e9aac1819fb781747eda51fd23e517b7283c6a08feaa9700c772580b77096
  - id: 14
    dedication:
      worker_1: 0.75
      worker_4: 0.5
    distribution_hash: 4dfb40bb9b45b80740b7588f9993c5544abdb8408f23c23cf10d21891f85bf2e
  - id: 15
    dedication:
      worker_2: 0.75
      worker_3: 0.75
    distribution_hash: 3f0bffa83b695109cfa925500e9b3eb18edc13897315cc26cdd6b6e7a1ae8497
  - id: 16
    dedication:
      worker_2: 0.5
      worker_3: 0.5
    distribution_hash: ad13f0cc528d26f54072eb5c9fab779f4bfde84258484a045f439eb5b0e85cd6
  - id: 17
    dedication:
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: ff141cb62a258146b7d9c5ba752eaf9a0c993f8fd26caf3bb6a7fe4e57905f32
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
    distribution_hash: 8309712250d8c6394924854f6e7f4b3cf44b47bb08b358d86a6591abbaeddb47
  - id: 2
    dedication:
      worker_2: 1.0
    distribution_hash: 15b1d7b515bd8ee398ceb2cebb317272fc6dce1b47529937dc2e0660615b82c6
  - id: 3
    dedication:
      worker_4: 1.0
    distribution_hash: c6c5f4c53adf5746564efdfad255d16923fa9d118fad9f15d424e126c8514cb2
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
    distribution_hash: 7be3c81dd36781f154475df74ef6c0b929c0b384579bbd25b7fe47850b4420ce
  - id: 2
    dedication:
      worker_2: 1.0
    distribution_hash: 8e130f2e0ee1ceac5f71a1ff71f5302c541bcf5b7d9f1763c7946b3aa64fb396
  - id: 3
    dedication:
      worker_2: 0.5
    distribution_hash: ce744910e6001c26c85cdcfc4aaabd81f878df92e85cf25df2af0e5974844821
  - id: 4
    dedication:
      worker_2: 0.75
    distribution_hash: 999de2a5bfbda4cbc987e1ad49b83a60cf397dca995cb2ecbd35688ffc0ede0b
  - id: 5
    dedication:
      worker_1: 1.0
    distribution_hash: 6b888cee82cb22c3e01c676a9e6925acb165163c003befd44064951e2e41d152
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 0.5
      worker_1: 0.75
    distribution_hash: 7495426903a4a1a3f717fdb7e40cadbfd4db00a4f6b55f84f4d24e3dfc0c6781
  - id: 2
    dedication:
      worker_3: 0.75
      worker_4: 0.5
      worker_1: 0.5
    distribution_hash: 8019a41a531e94d01c29d2215e1fb46b733d052be407c029bae438dbb0ed932a
  - id: 3
    dedication:
      worker_3: 0.5
      worker_4: 0.5
      worker_1: 1.0
    distribution_hash: 6125f297390e3e10a6b56cf99c04f2b9395f71717564ef20540814d30ba0de34
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: 31ababfd822788ad8621af208bf157d9de56418e57704b175493144d56c14c51
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 882b9e7bc94493f456232b021a8761342fb1fd9c47b35ab36ad6183873ab7d9b
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: 486baf35bc4d494f96517ed67d762329e80de12da945721dc71f689462a6c479
  - id: 4
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: ca6aa064a110c566de075fb7b708596d91a1ce5f6bac4f04b7e772767730f155
  - id: 5
    dedication:
      worker_4: 1.0
    distribution_hash: d3781c326037f19eb3e9f1e1c464721623d301f5f426f4cda8b1f864b9edbdf2
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 0.75
      worker_3: 0.75
    distribution_hash: 7d547cdc7380a618e0d11fe4d708b3b6f4583d3b73c1c7bac0d552d76315d1a7
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: ae404c8a40a987ca64cf163a9135945324c35ece3dc28036ae85b7bbbc364e6d
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: c92a2cc1933b11915818e5d82df06218f853c6f53a5fe7c2b681b5aeeb150a71
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 0ff7aede2d0fcc46929b28149ee93695eacecc4223279f086df30e0c8f5c3071
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 8f5210c39540923f613044b1e64b553c03aef5f1051395d7c1f1ae204a5a8cfb
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_1: 0.5
      worker_4: 0.5
      worker_5: 0.5
    distribution_hash: 4719e44bec084e4fef75ec7f0e205b6c18cb7a4235d4baacf02aa1651aacd6b7
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_1: 0.75
      worker_4: 0.75
      worker_5: 0.25
    distribution_hash: d8f9bdd6c9b228746a662fe9edee6063729454002a5c6220bd64b2203dc9083b
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 0.75
      worker_4: 0.5
      worker_5: 0.25
    distribution_hash: 1e071676fbf6cab2a222d1db3d33057ef45f158a00f0b54282b7477aac02a979
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: f0f2ab683c20867129a4cc12ea0969f6572ce8990b5c3eca893ec2d6ba7bd49c
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 6a40a987e44ceac21e4e6b41b9867f294282d4b9d2a35668dc1ccb1b5179acb8
  - id: 3
    dedication:
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: 00cc07fb50d44b9a073a3970d20efd7ae4fc20888e58c0fc2ac296ab25b7441e
  - id: 4
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: b93258554dad94be6c94d49dfc39cce93b9ea0edceece9a075707870730d834b
  - id: 5
    dedication:
      worker_4: 1.0
      worker_2: 0.75
      worker_1: 0.75
    distribution_hash: ac7f3ab6fc28fe3be1e20ce83175e7117c3fdba6a16f286b5df428f1ba3fb1d5
  - id: 6
    dedication:
      worker_4: 1.0
      worker_2: 0.5
      worker_1: 1.0
    distribution_hash: 9a8c63fe7d0c3494f604d346d0b549fe89f13d9e1d9859a6d8c472188ea932fa
  - id: 7
    dedication:
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: b944b2906b12d7966f1a6de50d08241958ada9f6f4bbe25bb9589d9fdc9136d8
  - id: 8
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 2f4f0d70e74b97a410d7e75f0a87a5948d39df2a0842c5ab6e6c03076a6a0a6a
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 0.5
      worker_2: 0.75
    distribution_hash: 9a05461efce11916787cb67a70ab6a43b1c266e6181e78bb99d93e0a5a67ff0d
  - id: 10
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: 3f9e7fddd1ca0327c3574f9719466d1bc01f04978a29cad3c6f702656d5c637c
  - id: 11
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 8ae4f860d1f60719551b62e8b5483cf7f111c7aee1a4a75562c5991d6abc2376
  - id: 12
    dedication:
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: 49890d2f52a77adc5eb3d44d4037ba8ad1ad237321050e4b37900b0308d952b7
  - id: 13
    dedication:
      worker_2: 0.75
      worker_1: 0.5
    distribution_hash: cf5eb15e5b8b04fb7613dc84943ff951b995300346f8bbd7e8e54543cd52ce99
  - id: 14
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 0.75
    distribution_hash: f54a278a3f555dabbbd4cb0905c765abadb4b91a006c5e10e359877d69b3b086
  - id: 15
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: 44593603fab757fbf0a9d24e1f796178af59bd1b37b4ec98f12c0220d0cb1b03
  - id: 16
    dedication:
      worker_2: 0.5
      worker_1: 0.5
      worker_4: 0.75
    distribution_hash: 440c555014196480fb3054710fada43e44fe5da0bf3022d77729cb4c54b67ebd
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_2: 1.0
      worker_1: 0.5
      worker_4: 0.5
    distribution_hash: e6b3fd63121682c707d44c4f2c5e5dbc7e34f89e381b53f6c01e80566d2b21dc
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 0.5
    distribution_hash: b51dd7c851e7f0366c1b68138c32fc94f762ac185d4073dfbb3c02aab8759f20
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 611320ca59c80aa56d3bb716e8af8d70249cd6a6662177407769b8ec65c1b7e8
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_2: 0.5
    distribution_hash: 06ae42d6bdffcac6179eaaa6d1d395fca13282653b00a9752a9a60c427241de1
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: be07a9803b8ca1658de84f7d7155c4a1912a2a2a2c8216b280e3d416f23b9f76
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: c553531b589177f2cf500b24717872999337aa769a47aae862a5a314042c8ef9
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 0.75
      worker_2: 0.5
    distribution_hash: 1f663ab2dad23dfdf6e8f56b5e32feaee2c1e19b64e855a90143842ab340dc24
  - id: 2
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: f3f4be4a60d3167ffa2efe4d649879d9fa53a2cb2e8582cc6ac6a357e40ae7cc
  - id: 3
    dedication:
      worker_3: 0.5
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: 5e933d39085613a9ee65d7012eb3bf5cd8ea79a94917e0feaefb2e9136055629
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 06e6822f22bf4fd436e7b611c1fa4bec97e4759475b314ca273750352f4ad983
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_2: 0.5
      worker_4: 1.0
    distribution_hash: 617035df3042cd38b1caba22ee0433c1546e2b501b2e3a91fde374e9d3f1d32f
  - id: 2
    dedication:
      worker_1: 0.75
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 20a0a4fb9150df254bd0a1bb407a253cd03e91a2b5466510bebde1fd0d0b8d82
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 829c26d2d5a93b8d01a9b301a435843fd4d8ee042cc60d29b21d17835683aa05
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: f416ff7b27de07f0a99ea2e702a7322460aafd8a4e8d02ac95f32ffb53477afa
  - id: 2
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 44621a0280fa91b22015c1b40f2e093486b5fbfcd063225e6035526bdb8fd4fc
  - id: 3
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 5871483492f0c1b16db829ba741975667dd4e725ad778f9e9aafbb4838b78284
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: c7027c8b8d18c177d1ad9498c1164bbb6aa6391b1bfcb3c84dc8024b8c3eaa32
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_3: 0.75
    distribution_hash: 0e71eafbf1b8cef71cd4a00862864c7689e0524aa436511ac2a510f4cff6c3ed
  - id: 3
    dedication:
      worker_2: 0.75
      worker_4: 0.75
      worker_3: 0.75
    distribution_hash: 102086e79666f6d0b47dab48e2c4e42138cb8ffe50c6e834b363c3cbd4fa09d9
  - id: 4
    dedication:
      worker_4: 0.5
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: 3b2d7cbb7d9ece71dbc1a328cf677b96a22301e412f9c64aa9c12fd84e7d9d22
  - id: 5
    dedication:
      worker_4: 1.0
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: c7d4b255994019e0749e330edbfd200fbb3a66a97222b92257b0d345dc90f62f
  - id: 6
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_2: 0.75
    distribution_hash: 7d9029ef403576906ccf8fa0c235bca59ee436ff96f18dbaafacf930c2be201b
  - id: 7
    dedication:
      worker_1: 0.5
      worker_4: 0.75
      worker_3: 0.75
    distribution_hash: bd4e4070c9444a3bfd8d015dd15657182fa5294bfe6da737b455499af1f36dea
  - id: 8
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: d3b7887af0a426142d392bcf0b924d6d7cb2a426d033a53c82bbec931e9ab252
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 403719ed05933a8c806d85ee72590998a7d16d897bd8f4678dbde7119d386d53
  - id: 10
    dedication:
      worker_2: 1.0
      worker_3: 0.5
      worker_1: 1.0
    distribution_hash: c32950c16827e393ba3e7e8b0072c1590aa7b0f408781aeaee5054cb6482b9aa
  - id: 11
    dedication:
      worker_2: 0.75
      worker_3: 0.75
      worker_1: 1.0
    distribution_hash: 0f3f960783bb6442a4e312fb9f0550a8beb39953fd33b788d749c58cee9a3475
  - id: 12
    dedication:
      worker_2: 1.0
      worker_3: 0.75
      worker_1: 1.0
    distribution_hash: 8b16429e760719d78acd536013a1d20b871af84dfa6b95110f710aaa78890466
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: 787d50cabbc484f444789122fdda2309382b99c2ec586adbfd06cbe41c652735
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
      worker_5: 0.25
    distribution_hash: 32504c06558b2f2333bef7d389807361005330b16cd646eced2b57ab6033ebc2
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_2: 1.0
      worker_4: 0.5
    distribution_hash: 9cf9a42f44be6dec361b780bcd9cfda9ebd063f8f51480378b4ae52c75c57edd
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: 8ee00910d9432431faf864b92858a38c0a2319f6d1d01640c5a46e6bb0eb140e
  - id: 3
    dedication:
      worker_3: 0.5
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: ed9a77653b54a680bb1a29b845c8085989b7f47e600789d65f4537cf89185a46
  - id: 4
    dedication:
      worker_3: 1.0
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: a2d2b5f886c931725b4f6551b6fc5f3e3b90133e6f21d106ac898aa5eeb7af51
  - id: 5
    dedication:
      worker_3: 1.0
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 719ce46807cf620d065a4c37b7a37af711f9020927ce56a4bde98595097558fa
  - id: 6
    dedication:
      worker_3: 0.75
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 9767ef28391005ea8cb35f7bfd6c9130b2f1c61d22751539b8ec708ed1ce1a11
  - id: 7
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: cca327b242480e1dd2b86b39a1411c959c6013141d8e52f7cb5c931c02a5f7f1
  - id: 8
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 07a2bc29947eff2ca27007a4401f1d36e5a138689f69e99122bb6156b9592a9e
  - id: 9
    dedication:
      worker_4: 1.0
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 9406641a8b245777f537d14fc382c96469f79d6e8c54e1c2ef26c6e45538bcf3
  - id: 10
    dedication:
      worker_4: 0.75
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 99e3df59b35ae22475f87d6e8340603d258fac0d7fd25d1291f0ac61c4e7c796
  - id: 11
    dedication:
      worker_4: 0.75
      worker_2: 0.5
      worker_1: 1.0
    distribution_hash: 63e844140f037a3c9ab521cb379c65f59ccb0849599a1d64a3301391ed27f8c9
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: e7da37a35e0d2e7de8aa745612612a7e099b1a2b557aee7b29afc3c075d6cc3e
  - id: 2
    dedication:
      worker_4: 0.5
      worker_1: 0.5
      worker_3: 1.0
    distribution_hash: 7ad1fa2b2696dd4f5ba8132c2350c6dafa15be62a427419e956b75ebfa8e0ab6
  - id: 3
    dedication:
      worker_4: 0.5
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: 5005876550f25317f41480ca420bec273671953ac8e6d45581577d397449799d
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: 00d85c633db7dd85dcd8ae3b2252a4631fa2acc8eefd333ccf7ce46085f074ba
  - id: 2
    dedication:
      worker_1: 1.0
      worker_2: 0.75
    distribution_hash: c650c21e8592d7ceb63d3fdcce5889f592c57a0d1a1318f25627723c16b87a02
  - id: 3
    dedication:
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: 3eea811886b58a6235130e071f37b89726efe9c65f697f5fa4d3d8290c58073a
  - id: 4
    dedication:
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: e5f317f83e3287f4bd9573b56b92f483a8c30a67271b0df0d4e8ca506eb01b2b
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 0.5
    distribution_hash: f0dee8b91a0ef377a81973445f872f08a3223978cf7a0643f27c3c3447ad6c7d
  - id: 6
    dedication:
      worker_3: 0.5
      worker_1: 0.5
    distribution_hash: f3c40a6e5cc1816b9b967ac008ad249961eb3c909232933fbdb60bbb69b2cd89
  - id: 7
    dedication:
      worker_3: 1.0
      worker_1: 0.75
    distribution_hash: 3ec877e793ff3e467654e2d51da0143917222ee8ada150f7bcddf2aaefef7085
  - id: 8
    dedication:
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: 3fb036bf75e8c8e0d224c1ab9c0e335eb1eb8cfb24c1f8b3e4e0636193819aa3
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 0.75
    distribution_hash: d6dca124151a5d9dea0e5063b08dc31ea92d6271648fc826a7f19020faf4b15a
  - id: 10
    dedication:
      worker_1: 0.5
      worker_4: 1.0
    distribution_hash: 8e29f8a6257c350b082fcab971e058e99a9e0965a8330690dfacac50e7592f01
  - id: 11
    dedication:
      worker_2: 0.5
      worker_3: 0.5
    distribution_hash: 1c85b8c7d59c50bb5e3888b1745cfac4a847c1a6e0922a2c6ecdb9487845e9f8
  - id: 12
    dedication:
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 74c3fedf37225e566bfc1b554f294cef60a6dd7b5a9d084236b6caabdb9b2871
  - id: 13
    dedication:
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: e2a6d71e3b7e09d7ac98ba7d0249af9c9df995193f6af88f9fb73f6518f236c4
  - id: 14
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 5cca5614389a56bfc53d60d5accd5b02895285f1a4b011cec00f1ca67b45a5f9
  - id: 15
    dedication:
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: e7eb88bb85282937160d94a5b23dfb909ddc7dc13a12ef043abc007a4344ff5b
  - id: 16
    dedication:
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: 86ba84239c0d7777ce19bfdec61543d764177e74f05e3cc363886b60149ca3bd
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: a2e7f9975a19af7953d1dd1f01fcc23dcae5503f0d54add11e0d1064a7f52a5b
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: 27fafe63f5e6113fb49df096fba17ab9f7fe01beaceffd3bdb5cb6e42841b049
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: 9ad32eadc076b716ba1c157243075a5ce6645e74ca5072b52f24d90b0244f755
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: d7caa8adc50532131a30d30933e8f2de5ad0e8aacccd8a5889f56217e7b29e5d
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_5: 0.5
    distribution_hash: 2cdc804de6c1656d3ce2b954d9628ca9315f23a55e5bb6b6b208d912ae8d72ed
  - id: 2
    dedication:
      worker_3: 0.5
      worker_5: 0.25
    distribution_hash: 2d4e292d70320c565b9c657d94acd5e644229fc11ac32a47a905814ec5b90a9d
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
    distribution_hash: 11bd2b871baa84a1219a75f7184fe0a965cf495858ddbeac61b0769cf552347f
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: cb57d22d6b8237f04ecfde1a5ef6407b7f3018ecba78910d1f69393ea9ec5cb9
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: e2aa3e87fe604d8cc5aa543c440eab615b511a67555eabb630c45b14952e94b0
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 0.5
      worker_4: 1.0
    distribution_hash: 964d9c96f643569e79d517a43412b4f0d5df03d8518dc28830d59ad0248755e0
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 25c15bc47354e72fcacb06d6892d5013d259ef5a2d90633d96a9ef9bf1bed95b
  - id: 3
    dedication:
      worker_1: 0.5
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: c10050ff646ef27b16d1ed445a5139b93eb63f494e68cd7f940cd96356856c11
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
  - task_15
- - task_1
  - task_16
- - task_1
  - task_17
- - task_1
  - task_29
- - task_1
  - task_30
- - task_2
  - task_6
- - task_2
  - task_7
- - task_2
  - task_13
- - task_2
  - task_27
- - task_2
  - task_28
- - task_3
  - task_7
- - task_3
  - task_22
- - task_4
  - task_6
- - task_4
  - task_14
- - task_4
  - task_20
- - task_4
  - task_23
- - task_5
  - task_13
- - task_5
  - task_14
- - task_5
  - task_22
- - task_6
  - task_18
- - task_6
  - task_24
- - task_7
  - task_18
- - task_7
  - task_19
- - task_7
  - task_23
- - task_8
  - task_18
- - task_8
  - task_25
- - task_9
  - task_18
- - task_9
  - task_23
- - task_9
  - task_24
- - task_10
  - task_22
- - task_11
  - task_22
- - task_13
  - task_19
- - task_14
  - task_18
- - task_15
  - task_26
- - task_16
  - task_21
- - task_17
  - task_19
- - task_29
  - task_25
- - task_5
  - task_27
- - task_11
  - task_21
- - task_4
  - task_26
- - task_29
  - task_19
- - task_9
  - task_22
- - task_15
  - task_24
- - task_28
  - task_19
- - task_15
  - task_22
- - task_29
  - task_20
- - task_12
  - task_21
- - task_5
  - task_31
- - task_9
  - task_7
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
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 672
validation:
  project_key: e0a8fb49c8f9c48ccf4848e2bbf0b74b1620cc44faf0812a9dcfd3000a66b2eb
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 120 days; worst-case serial bound: 1790 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
