# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_93
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
  modes: 134
  tasks_at_cap: 0
  relaxed_constraints: 7
  rewired_edges: 18
  departments: 1
  quality:
  - worker_2
  safety_skill: 2
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 1
  barred_pairs: 6
  incompatible_pairs: 1
  edges: 88
n_workers: 7
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 473
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
  26f464b00f9e232ad0032116efd163cb670149f4594671c4af95de5131df467a:
    family: pert
    a: 54.06315627062163
    b: 67.57894533827704
    c: 84.30232298734707
  6f08986e50a8447be29cb54e63426e74e80df280491b78f2221fce304acc95f9:
    family: pert
    a: 63.18662917368184
    b: 78.98328646710229
    c: 96.67277756175432
  f9364cf4c5efbe6d32b94aa0e43e95403ef916231de5112d6591b1a61bf6edf3:
    family: pert
    a: 27.9809184209183
    b: 34.976148026147875
    c: 69.3085097122009
  7f88b78de868dde5132a29b6e7c37891867d70cb671b79100fe8fb941c5d897d:
    family: pert
    a: 43.73434932453605
    b: 54.667936655670054
    c: 79.7575394150637
  a19c43470224ddb382b89ad61e5a6cbbdb22a83852c2192c82a1ceaa211fd20c:
    family: pert
    a: 34.82199576250203
    b: 43.52749470312753
    c: 58.84397448033982
  73c3a8712b97af8b151fcce8600f5bc2e8805acc5da74e9fdfc05c7f5a36dad0:
    family: pert
    a: 52.22283832810729
    b: 65.27854791013411
    c: 109.38843584482561
  688b001dd55ccaccae09ea27adfd33547fbc06a4404cdd51e088ae5961a23250:
    family: pert
    a: 43.916540047964176
    b: 54.89567505995522
    c: 80.60013940331265
  fba15aab6553c62d8999fd9ef01cd89df6c960cb19a13ed43ee0154efeaa3a20:
    family: pert
    a: 34.10187645036649
    b: 48.71696635766642
    c: 243.5848317883321
  7b6787002c433e26493f20d53f41308b30ac17d0a45062f4e8c824b6c62febdc:
    family: pert
    a: 36.23164764665151
    b: 51.75949663807359
    c: 258.797483190368
  12f2e3bca26e5b671a76ce0830918c4002fef9ee199615d3e74cd564ef82e858:
    family: pert
    a: 28.500677244011232
    b: 40.715253205730335
    c: 203.57626602865167
  a94e7b83cd483e25928fb9243ab10a246f2359b7fef1e9f9bf22cc22ea5dfed0:
    family: pert
    a: 7.664440692005987
    b: 10.949200988579982
    c: 26.426805423344153
  207bd4adfebc0e6f555aa1528ce35194ce507834fafbb1c9b7bd88c5656b5fb6:
    family: pert
    a: 8.99042400784246
    b: 12.843462868346371
    c: 24.4223036997082
  4cf2b61790c4599e0823d389f99a7c48ec1f631986d3d68eef702cbf4a2ccf2e:
    family: pert
    a: 6.426974798515932
    b: 9.181392569308475
    c: 29.15615734626904
  6463c3501bd93cb33fee2287a2258ade1fe15d393231764686dcc39e59159b8f:
    family: pert
    a: 2.6847051859635482
    b: 3.835293122805069
    c: 10.393171679338533
  c1e9f5ea64b3cbe5a86c034a32b0b7ed3f335e046800981d739afbd06e3f8511:
    family: pert
    a: 16.921840508797647
    b: 24.174057869710925
    c: 43.56766345853471
  4fd99911bb78e2f65c0b142f4fdcfbe6441edfc81ae366a77e469a096f3a85cb:
    family: pert
    a: 14.475893901671208
    b: 20.67984843095887
    c: 38.93411394723754
  113e2e074772bf673de8532d59c9523d6e6dc1bd14c9db59cb48edfd20aa4513:
    family: pert
    a: 10.049554877527248
    b: 14.356506967896069
    c: 50.50314209761498
  c2c5ff9c4b3a4ea3d6040ee8f7166c03038e4080402201c5e8a5b0de0762114a:
    family: pert
    a: 29.29177926314551
    b: 41.84539894735073
    c: 71.96680821195476
  5e38406eb6a45344937622c72fe900dc997f82957345d726f8f1cc960b585fd0:
    family: pert
    a: 24.89400553195157
    b: 35.562865045645104
    c: 72.82974767241235
  335116f9dac02bdcce5b0ecaaf189725b8254e371f2273d832b6e638c8be11c1:
    family: pert
    a: 22.83787475212577
    b: 32.625535360179676
    c: 71.46776098265553
  f68588a26fe06b0e3f476866b760cb632356cf051c4a781c47392c57c8a5c0e2:
    family: pert
    a: 13.563094252084051
    b: 16.953867815105063
    c: 23.16736576303575
  bd7d2bf5dd9eed5fe5e588b179705ded49dafb839566758e7444d69b832e9767:
    family: pert
    a: 11.838344898881804
    b: 14.797931123602254
    c: 21.2205996621551
  13d9f35bc4643a0905d5b8f54dd9d4ba1f472a740a323ff075d8871ef15a3f54:
    family: pert
    a: 11.100268362801382
    b: 13.875335453501727
    c: 19.394696429705583
  d0f9e543d65720508f6bd23593b70ed19d15154ecb574b8d54422c85ba86ca3b:
    family: pert
    a: 15.85798345013654
    b: 22.65426207162363
    c: 37.69536842494304
  285928893482380bf50397962e49cd069b371df4bc4a4b1d38d79a3933e94a05:
    family: pert
    a: 14.63776848938774
    b: 20.91109784198249
    c: 39.84253017890492
  eced57241147ecc8bc4386b67df286edf28baecc00ce8a8312c66da57de56cc8:
    family: pert
    a: 13.761359980458458
    b: 19.659085686369227
    c: 44.55384522226895
  47ecf80b1c68342e321ed17cffc17fd01526a7acceba98e52145698c014da728:
    family: pert
    a: 14.619861560177569
    b: 20.885516514539386
    c: 45.468373764061276
  1ae23a09b6abbe52c9dc52bc35128f366816564cfbb121e79dff99e7097c0ae6:
    family: pert
    a: 15.30771658136142
    b: 21.86816654480203
    c: 39.40147265437716
  3d7196094d451a1c1e3d184636c03d53a502888a0beb1d2086cfea8af9fbe640:
    family: pert
    a: 35.54677319937735
    b: 44.43346649922169
    c: 67.18573147069021
  ca73bf55ccf771054cbb14a2d633cf5bf17d747d239279535adda14df0b96419:
    family: pert
    a: 41.02022808878977
    b: 51.27528511098721
    c: 66.10599958301833
  b9a3ab79cc717d71cb19f3408be63be006d22611797c5bd1d9873c3864c783f7:
    family: pert
    a: 41.419391365283886
    b: 51.774239206604854
    c: 71.41138625980251
  a815f8d462ee71f093ce4c1ca994225c6d2902f43f3b4dfbea9d8544c577d0b8:
    family: pert
    a: 51.063335470481704
    b: 63.829169338102126
    c: 71.45620175652982
  de005359b49ea27a0c170788641ede1a17245408cd8aca2bf129d5b6657630e5:
    family: pert
    a: 39.58781188194973
    b: 49.484764852437166
    c: 68.07386359602856
  b6c6d9e8e6995eedff55f9facf35b5da03ac6e60732edd85169c5dad139ac4d5:
    family: pert
    a: 31.834056992879933
    b: 39.792571241099914
    c: 61.69344859539771
  92d2887f8ed6a87b63d90cc2a4674cadd08f4803ca9ef9dfa95709d247f0e214:
    family: pert
    a: 34.148627273573865
    b: 56.91437878928978
    c: 206.5735740205167
  b78305289002ac20a949279eddefd522b6f6c86eda349b8fc9f2ccee26129a29:
    family: pert
    a: 19.195237154682243
    b: 23.9940464433528
    c: 38.32273774633727
  4ce75c99069866109e569a2027aa367fa9c8f92260ccaae6fea2d9beb31dc83f:
    family: pert
    a: 15.86224387292923
    b: 19.827804841161537
    c: 45.274991441744845
  79f5f1c0fae7932cb014c7554c0c1885259f6fad7bb3f2ebbe0581efd7c8239e:
    family: pert
    a: 22.22082008717591
    b: 27.776025108969883
    c: 37.894219017890535
  ad8a89f318b4ef35177054dc8988756006422db881e38a999f6bb754644752a0:
    family: pert
    a: 19.442297569340795
    b: 24.30287196167599
    c: 38.519615350079754
  1aad81c6c8fae1d56ff672f0666fe53fa2ac6ac378b928d5e5b05bcd82083e58:
    family: pert
    a: 25.169757391920864
    b: 31.462196739901078
    c: 58.6350561299698
  31e87fa9d4d9a25e1e10c100d3451fcf124eb086d4898f0e24b260100fc42089:
    family: pert
    a: 23.28671827260471
    b: 29.108397840755885
    c: 39.08068285026286
  bd3151638bd4e8c72511add0cb7c0db0fb7d4318d5c8cd4ae4ea2eac4bf9e492:
    family: pert
    a: 22.584391915521653
    b: 28.230489894402066
    c: 42.4717826321026
  69af75e62a2073041b2ebf4224682c7b449169ad3a45002b54adede3c5d70925:
    family: pert
    a: 26.498295563422882
    b: 33.1228694542786
    c: 46.772700121720334
  1ae2f4b2b92345cb882483cee1ac92b729ac3a4bbfb690ebe60d87261c25fb1c:
    family: pert
    a: 23.02412399384701
    b: 28.78015499230876
    c: 43.79720340745232
  ba8a565bf1e9f70e12a56c2ecb376a2fa9bd1dc98ce7a47f1dabb7516179eff8:
    family: pert
    a: 17.708469856146788
    b: 22.135587320183486
    c: 39.46080722353945
  126e6e2c08b2c3ae135da616e88e4003303d223588bc03b8b5476053346bc982:
    family: pert
    a: 19.866551112298296
    b: 24.83318889037287
    c: 37.08371002165834
  ce3cacd41500f78f4985b3a8d7d0446255a37b85d38889dca158385faca75907:
    family: pert
    a: 15.579197009887658
    b: 19.47399626235957
    c: 26.82784848096605
  1b7f6618766fcfcc75c78e141c2a05b181614b7246f8eefc974b911dd1b79b8a:
    family: pert
    a: 5.7572117608183335
    b: 7.196514701022917
    c: 13.251876192911736
  bd3a38dcc5dea7797d65c5d120ba3c41796f2879a26a3536c4fc5d809f5ac69b:
    family: pert
    a: 24.63424129790151
    b: 35.19177328271645
    c: 69.18419008608097
  d4f5ca80e5b16d9f7db0d0be2a44bd22e5fb6f7a4906eadc9e84ba49ebd25fc2:
    family: pert
    a: 19.64030574261765
    b: 28.05757963231093
    c: 66.20684361214707
  1a9cfacc170c762e16d21f55c56d94936346569dbf9cf0c83339d7ae035aef20:
    family: pert
    a: 29.091094163280385
    b: 41.55870594754341
    c: 85.28176602376237
  491df6e4bfa0134c3db1d07ad46d0bfc085d9ee8e081f647eb97d2e37c6ea76b:
    family: pert
    a: 22.566751373243374
    b: 32.238216247490534
    c: 80.74725941754197
  42e79510da0529bbf8168c9035a9ab4d0bd597ea6e2d434870aaf923456b2d52:
    family: pert
    a: 26.707104085365316
    b: 38.15300583623617
    c: 96.00164793166269
  3bca752dc6f6fd73fd9e11072d45a8786a33ef6e9d6c28979569afb213febc38:
    family: pert
    a: 37.171115840415965
    b: 53.101594057737096
    c: 78.71650717681476
  99fbb203071bca86a73feb242e32d646ca39b17a3b2c9d6c2a48758c1252b406:
    family: pert
    a: 24.48533890274931
    b: 34.979055575356156
    c: 65.25199909805168
  0e5bfcb2489054bcc1b7eee81ddf047c5bddd93ec39f51718ff5f253b4b78b7d:
    family: pert
    a: 23.681046971463584
    b: 33.83006710209084
    c: 68.24068425990288
  4a956de7a46e8ead4915a47904e0e2576a3c3b739cf8b6d123a798f2f96220c7:
    family: pert
    a: 30.718086946377394
    b: 43.88298135196771
    c: 90.72925014160892
  64973a459636675ae44c31245379ae7f9feac6e9b9c3ca1035180d917728b0b5:
    family: pert
    a: 27.380910389111904
    b: 39.115586270159866
    c: 93.47395345789157
  b8ff4b76f9c2cd1ccbab7fb2178bd0a69ae0d90436edaf6a8a1ab0d3e6fbc628:
    family: pert
    a: 21.906697610178455
    b: 31.29528230025494
    c: 51.00567007087459
  c22538ba1b014b1a153b2de80f783a04fae1d0f02794304aa5098e406899a201:
    family: pert
    a: 21.75208395651156
    b: 31.07440565215937
    c: 63.190294012529634
  d6894a56f1918eef630f354d60455e15213d355299f6427a6e8cb422bcd5964b:
    family: pert
    a: 23.612294489321638
    b: 33.731849270459485
    c: 92.61699359636944
  75a667cb07c7cecb4879592137fec38e8e75c663c52447c44f48d6e10136aee3:
    family: pert
    a: 19.943208221100825
    b: 28.490297458715467
    c: 81.37727828375473
  75882659c5bb80bbb4421b2424bd7016120f8efc9a59b03d4d902c917453ebf5:
    family: pert
    a: 36.072396484933904
    b: 51.53199497847701
    c: 67.51364952707469
  25c215aa425e2425d8ea5b7ed0c29064886fc0b98c4796635712cdcf30bd4c16:
    family: pert
    a: 4.043017004811926
    b: 5.053771256014907
    c: 6.302993199009032
  6324158381a63dccbb7906e8df10666c8f5bfb5b75418fbdfaf9a3aa735007b5:
    family: pert
    a: 4.8047689523466355
    b: 6.005961190433294
    c: 7.779503648599819
  da120989d4501e8fdb777c32c920e02f9f86758968614ca5edef103889f097bd:
    family: pert
    a: 4.202159114711864
    b: 5.25269889338983
    c: 7.26462171033767
  8b3cc13b108071c4d517b3faa28d7d37ce7df592e70c03d086c8170302c42b30:
    family: pert
    a: 14.363321012770667
    b: 20.51903001824381
    c: 45.3024483648273
  205b91c4a73c7de4df5b2062cee1dabaa21c739d9422aece6131a87d408931b3:
    family: pert
    a: 14.882398143820515
    b: 21.26056877688645
    c: 40.365796404290066
  c6b4a5ff72cfb418dbd62c2d24921af6d2c8a5d172804846b50b7578d7053d81:
    family: pert
    a: 7.002704097115537
    b: 8.753380121394422
    c: 43.76690060697211
  0dde9bd6d083c3ced682ee0ff27334042a2b3bd04b2881f9de2cff85a7340d5e:
    family: pert
    a: 8.585868552846192
    b: 10.73233569105774
    c: 53.6616784552887
  7214c3f960f6df223474f02b603907de70aa24250ffc0d16e6a819fb0937b25f:
    family: pert
    a: 6.471635401258165
    b: 8.089544251572706
    c: 40.44772125786353
  f9a451886112399f04331462495fc61bc906026563d50cff00fa21d8c9f9339d:
    family: pert
    a: 5.207101928190491
    b: 6.508877410238114
    c: 32.54438705119057
  c905f619db8f8991983be96deccb53657f4ab8a754b0f2f5fa59359964d8071c:
    family: pert
    a: 8.46619643501459
    b: 10.582745543768237
    c: 52.91372771884119
  82f9e0283836b5c7017b7391553e7eebbb55c96a8656867c2291b8ea00f73e56:
    family: pert
    a: 6.656379981436306
    b: 8.320474976795381
    c: 41.60237488397691
  86953f0cdf488c8a96ef7a1493703e400c20fa9e544102d95470b2f4e7509396:
    family: pert
    a: 31.317354000883356
    b: 39.14669250110419
    c: 67.16916200943217
  89811259c8a9da6e6bcde9b076c8556ed27821d847022b6dd1b1d939fe9e93ea:
    family: pert
    a: 17.098670649919537
    b: 21.373338312399422
    c: 33.948082181008765
  20dce66a73fa0e02b551e0e65c9c6b96970d84142a67979476410b67705163c9:
    family: pert
    a: 18.48967201868482
    b: 30.81612003114137
    c: 95.77039654316039
  cc230d4d48893db22b38b92c147bcbc55962efdc30e19d2aa3534b4367561648:
    family: pert
    a: 28.401499610331076
    b: 47.33583268388513
    c: 122.28999255315408
  f3b85cb075875914a26c1fc3351a2b2b9c22b8aa30dd0bd10be4e59aaeb0bb89:
    family: pert
    a: 12.084490835183843
    b: 20.140818058639738
    c: 90.44318622929421
  4c948269e7d08e1a0f85842c1ace285054de89a07089b773d7ce583c250c5534:
    family: pert
    a: 15.138787909765998
    b: 25.23131318294333
    c: 61.103696969233155
  b4caffd0a01fee0362893620e6ceef0dbe7a1cd05bb8fbbb2e01eb6b54e44491:
    family: pert
    a: 16.880462918653635
    b: 28.134104864422728
    c: 90.68663119172379
  74384f91c399414773c2b14ffa8774eed630964c84d0c3ce452b04364e1d7d79:
    family: pert
    a: 15.43780427385786
    b: 25.7296737897631
    c: 153.36856475483017
  45923d4416180ab003901c00b438895eba6d5b1d73acb06150d4c36be0328a18:
    family: pert
    a: 17.327410912269187
    b: 28.879018187115314
    c: 56.64298042218394
  3eb9840316ea442802777616186086ef46f3c5191dc899c24e132a9dd8684ce9:
    family: pert
    a: 17.64078785712022
    b: 29.40131309520037
    c: 94.71500699706073
  88d11d3ede6b965f3a3c29907df7b0195d5d21048e65746d9029c8ec4d640358:
    family: pert
    a: 18.18621970701107
    b: 30.31036617835178
    c: 90.63287911874133
  42a83b2927fb6deaa88b7e8c75996c85a5f4caceb0032d404ec827537921af6b:
    family: pert
    a: 22.595398487284303
    b: 37.65899747880717
    c: 104.37441976924964
  4a87356d93f18b6b8a53d3ec700f8e551f59545c4621834ab7e4ea8032b70073:
    family: pert
    a: 12.21801616301308
    b: 20.363360271688467
    c: 78.6836157960562
  4613c156f97770d7bfdab9c978fabe5763c3522b334b6da10d126311ed8444d7:
    family: pert
    a: 13.277223588692275
    b: 22.128705981153793
    c: 127.61917582052517
  71c0ad5e868cfcac2ebe97f4fcc546d485b56bf77131e19815e1730ec55a69c3:
    family: pert
    a: 15.838323566646402
    b: 26.397205944410672
    c: 111.58591988361385
  a559ccde5b1f811df70ee30000afb99bb741a1740faf4c294c47917fa5996132:
    family: pert
    a: 70.13560211133024
    b: 87.6695026391628
    c: 127.89218456704252
  5f05c156af332e96a33bd40c496a8d88f78612ee132d61cabf468beab976cbeb:
    family: pert
    a: 44.602732975195934
    b: 55.753416218994914
    c: 86.25236000325826
  6e5a352cbe771ad1eca584f4be906504c4a10cb191722f0cacdea7db5089db31:
    family: pert
    a: 28.444446882563625
    b: 35.55555860320453
    c: 65.18035417695243
  a52413a2ee31ee9d4f7bd6e1b5e85ef93b4397bf64d23b4eb1ce5a5de454b72f:
    family: pert
    a: 49.34147011541421
    b: 61.67683764426776
    c: 82.45309937469682
  cf7f5a1c27f20c890e843d92f634bceccf9297171dc7ed4ddf4d2aa4dac0af8e:
    family: pert
    a: 31.34135624790056
    b: 39.1766953098757
    c: 71.12581958125737
  d0e56049e512b6f658afacc6c5496785b08c7027ba5e8b7bb084f44e7019de22:
    family: pert
    a: 68.9161022928204
    b: 86.14512786602549
    c: 119.54483238556439
  d8332ae193bce945f16bd99a0b990f4a3d133b4d32c0723ab9155246841bb604:
    family: pert
    a: 13.563869832331571
    b: 19.376956903330818
    c: 50.57122641243232
  b51d88e88198d2f75a7989cdac7dbe0793942e49ef2399dda0371e4455d3c21f:
    family: pert
    a: 38.89959944025796
    b: 55.57085634322566
    c: 127.91052566381653
  00fa433c54470abd18bb589c12657ce1430288396c65ac435a25a70a43e78b40:
    family: pert
    a: 47.53198849923207
    b: 67.90284071318868
    c: 501.7334616070502
  d1d211d292816f7589f2d098f555ba7245045ede2102f078e218c1230998d80a:
    family: pert
    a: 29.099855309296387
    b: 41.571221870423415
    c: 151.03456640376984
  00a06734eb3358ec972e7a7eb68fd52f08acf850d146cd158e6ed5369d0a5d7c:
    family: pert
    a: 52.39675884673561
    b: 74.85251263819373
    c: 135.64581372869026
  a83ea21a6e647ae803d9e6abf50c4cdb70e3fa08dfde002d37834c580221b977:
    family: pert
    a: 53.452903172231004
    b: 76.36129024604429
    c: 153.12517237468901
  586bdf893e9809a0bbe33d7a36b281bad47faa7ca19f4e4279e2366937455342:
    family: pert
    a: 25.8014199390661
    b: 36.859171341523
    c: 83.61917524919144
  ae5bac5b03d3c3c4bac5371381b57ea0f8d9917b2e27394c88490d582e92b64c:
    family: pert
    a: 47.15218719084225
    b: 67.36026741548893
    c: 209.87273861268324
  602701c29c2755f9ee577cd9b4986c91a8962aad048a8b74003a02f0fe9adc6e:
    family: pert
    a: 30.258355945935268
    b: 43.22622277990753
    c: 83.4069907354062
  3be4cc18cd5ba512369d32e9414b813393535111e37ecaf16e8c2528d03c43c7:
    family: pert
    a: 16.952127839889286
    b: 21.190159799861608
    c: 26.956775085479702
  a413fd5084d93935c8abfa4b7fc17ddf76df621d457539845a74297be22c5315:
    family: pert
    a: 35.520099528366885
    b: 44.4001244104586
    c: 71.14659412650084
  2d3f56b500202eb92b5afdb05c7a46a878a2caa92cbe5768cb831ab762a7d606:
    family: pert
    a: 28.71935347923724
    b: 35.899191849046545
    c: 52.02779914659865
  0c0e2380b848fc9c1fa05b89c2b2ecc0d27a0fcd5d92ade3c54cb632c2848a6f:
    family: pert
    a: 16.451765974847667
    b: 20.564707468559583
    c: 38.39405958804011
  7227ad1cf938a7fc29a4101d1fbb9510b98d829c355a113859e90a5f531bdc0e:
    family: pert
    a: 24.04559931499962
    b: 30.056999143749522
    c: 60.02261446968176
  2b0e821e15fcf49d3f4e9a13d1529a5cb8af822dd71832d50709c09b4c5f0696:
    family: pert
    a: 15.295285683977207
    b: 19.11910710497151
    c: 25.8234391184713
  c50b6ca4e7f8d8105097b2f1bccb33dc2cc28bd3019880e3203bf724f85e4b0d:
    family: pert
    a: 24.134555401071108
    b: 30.168194251338882
    c: 51.638226909398114
  80187b6b4d1fe72d3c35ab4bb6b66fbfdda54f1b9defe20b160c20082b7df4a0:
    family: pert
    a: 4.8575016262388875
    b: 6.9392880374841255
    c: 15.412971159851251
  c040bb0279b26cdf4f263ea90d8c625fe4038624b3fe001999880b5fa30d8289:
    family: pert
    a: 4.181557845164489
    b: 5.9736540645207
    c: 22.978206206674084
  ccd9ee84ccd634e19a01677036e5868aea16b5a3c3e706896599a4d3195af98c:
    family: pert
    a: 5.800073702546182
    b: 8.285819575065975
    c: 19.428440695563047
  dc94a08eb637a990111b5fd937d3a109bf626100ae9af23b210c4497156ee6d5:
    family: pert
    a: 6.250057050210184
    b: 8.928652928871692
    c: 13.651277456168541
  ee9d68d51c78ba15724160ad5b7d8f5326ab3f0283426b23e5b43bea4ada6148:
    family: pert
    a: 6.370845554290584
    b: 9.101207934700835
    c: 17.884437311769442
  0014040397f0823530b409b86aa3ca66d8e605e3aac6ff03a191f18711785f7e:
    family: pert
    a: 16.849967326131967
    b: 24.071381894474243
    c: 53.94305806375723
  317aa3873cc169d4c9f6273fc62f00b655589a42baede5d5d484f1dc1bf4cee7:
    family: pert
    a: 28.003345409056458
    b: 40.00477915579494
    c: 101.81042453035303
  1c05c89e93ae19c9a3dc81d385e9ef1c683b65d2317c1a689b528a6a908e77b9:
    family: pert
    a: 18.517823263750063
    b: 23.14727907968758
    c: 40.00103257585418
  91e6307a183b6524a54189fe02407ac164f1198bfc10e0ee86430d0e416d9d42:
    family: pert
    a: 23.016438556123692
    b: 28.770548195154614
    c: 40.91895964982178
  03ca2d0afb4cbab9269018f41774f18c1b0801afbd7e7545fc91f65e97789aa1:
    family: pert
    a: 24.565976491837404
    b: 30.707470614796755
    c: 50.40303833608186
  fb68188b0c5e81f0f1eed8da6981ce6e413063148d984af76f169e9abdc29b2f:
    family: pert
    a: 22.450708234925298
    b: 28.06338529365662
    c: 140.3169264682831
  76ee489616cca086c68be087ce0a7efafae32fd31fac42fc9fede8400d8618ee:
    family: pert
    a: 25.726725025215842
    b: 32.1584062815198
    c: 160.792031407599
  1e6385eff6d2557489b08a576204536c0676186aabd194dcede882cec3cc43c9:
    family: pert
    a: 26.789188837567977
    b: 33.48648604695997
    c: 167.43243023479982
  dc0f79fccd0b8f8b21b719f9f174bdff971020c6bb84685ee3a2e022108abe6e:
    family: pert
    a: 25.849405114985917
    b: 32.311756393732395
    c: 161.55878196866198
  51bbef5f4179ee12c08e057365995eae9ba097a6891c8eb745a742e2dfee46ed:
    family: pert
    a: 20.176333862668372
    b: 25.22041732833546
    c: 126.1020866416773
  c34efc303a108b5df8abd067fc418e2370036676afbd9cc6ebee32b9f9061ead:
    family: pert
    a: 23.471079811898345
    b: 29.33884976487293
    c: 146.69424882436465
  872cf178e158dae4671db643633e937cb80f18e5fed02ded87a0d1b93c4a3fa6:
    family: pert
    a: 20.377037929884388
    b: 25.471297412355483
    c: 43.95065399942713
  9354de39be7e7f9143086318c998d3b0f6b5e9e187d53a983847f5b5c88fa692:
    family: pert
    a: 36.88211200592539
    b: 46.10264000740674
    c: 73.65550807740095
  059442ffe036189f6027b9942fe630adc24d920c164c2e24eb2ef342842b7baa:
    family: pert
    a: 24.18244467118959
    b: 30.228055838986986
    c: 48.94103391983294
  b6a3435647d3be213e8580c9deab9abb4c6c872f71c9b19bcef633f8053270da:
    family: pert
    a: 23.67636174189788
    b: 29.595452177372348
    c: 47.17792908254331
  dd909f702c6ddbfb73e9a73360d68304d4bb2df3abcacc0759fe1b2e47a838f6:
    family: pert
    a: 28.225151226959667
    b: 35.281439033699584
    c: 45.294574138732266
  576bd823eb77c893f15ec276aff18f89dcc714d8386b978e60aa53c7087520e1:
    family: pert
    a: 36.511983702175314
    b: 45.63997962771914
    c: 56.106186842449915
  097710a5d59cde0c9f5b16872252a1b43f5bccb7cb4f339cfe71af95f9af1b88:
    family: pert
    a: 22.341150969182202
    b: 27.92643871147775
    c: 52.06879789785431
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
      worker_6: 0.75
    distribution_hash: 26f464b00f9e232ad0032116efd163cb670149f4594671c4af95de5131df467a
  - id: 2
    dedication:
      worker_5: 0.5
      worker_6: 1.0
    distribution_hash: 6f08986e50a8447be29cb54e63426e74e80df280491b78f2221fce304acc95f9
  - id: 3
    dedication:
      worker_6: 1.0
      worker_3: 1.0
    distribution_hash: f9364cf4c5efbe6d32b94aa0e43e95403ef916231de5112d6591b1a61bf6edf3
  - id: 4
    dedication:
      worker_6: 0.75
      worker_3: 0.75
    distribution_hash: 7f88b78de868dde5132a29b6e7c37891867d70cb671b79100fe8fb941c5d897d
  - id: 5
    dedication:
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: a19c43470224ddb382b89ad61e5a6cbbdb22a83852c2192c82a1ceaa211fd20c
  - id: 6
    dedication:
      worker_5: 0.75
      worker_3: 0.5
    distribution_hash: 73c3a8712b97af8b151fcce8600f5bc2e8805acc5da74e9fdfc05c7f5a36dad0
  - id: 7
    dedication:
      worker_5: 0.75
      worker_3: 0.75
    distribution_hash: 688b001dd55ccaccae09ea27adfd33547fbc06a4404cdd51e088ae5961a23250
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.5
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: fba15aab6553c62d8999fd9ef01cd89df6c960cb19a13ed43ee0154efeaa3a20
  - id: 2
    dedication:
      worker_6: 1.0
      worker_2: 1.0
      worker_4: 0.75
      worker_7: 0.5
    distribution_hash: 7b6787002c433e26493f20d53f41308b30ac17d0a45062f4e8c824b6c62febdc
  - id: 3
    dedication:
      worker_6: 0.75
      worker_2: 0.75
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: 12f2e3bca26e5b671a76ce0830918c4002fef9ee199615d3e74cd564ef82e858
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: a94e7b83cd483e25928fb9243ab10a246f2359b7fef1e9f9bf22cc22ea5dfed0
  - id: 2
    dedication:
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 207bd4adfebc0e6f555aa1528ce35194ce507834fafbb1c9b7bd88c5656b5fb6
  - id: 3
    dedication:
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 4cf2b61790c4599e0823d389f99a7c48ec1f631986d3d68eef702cbf4a2ccf2e
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_6: 1.0
      worker_5: 1.0
    distribution_hash: 6463c3501bd93cb33fee2287a2258ade1fe15d393231764686dcc39e59159b8f
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_3: 1.0
      worker_5: 1.0
      worker_1: 0.5
    distribution_hash: c1e9f5ea64b3cbe5a86c034a32b0b7ed3f335e046800981d739afbd06e3f8511
  - id: 2
    dedication:
      worker_6: 1.0
      worker_3: 1.0
      worker_5: 0.75
      worker_1: 0.75
    distribution_hash: 4fd99911bb78e2f65c0b142f4fdcfbe6441edfc81ae366a77e469a096f3a85cb
  - id: 3
    dedication:
      worker_6: 0.75
      worker_3: 0.75
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: 113e2e074772bf673de8532d59c9523d6e6dc1bd14c9db59cb48edfd20aa4513
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_5: 0.75
      worker_4: 0.75
      worker_2: 0.75
    distribution_hash: c2c5ff9c4b3a4ea3d6040ee8f7166c03038e4080402201c5e8a5b0de0762114a
  - id: 2
    dedication:
      worker_3: 1.0
      worker_5: 1.0
      worker_4: 0.5
      worker_2: 0.75
    distribution_hash: 5e38406eb6a45344937622c72fe900dc997f82957345d726f8f1cc960b585fd0
  - id: 3
    dedication:
      worker_3: 1.0
      worker_5: 1.0
      worker_4: 0.5
      worker_2: 1.0
    distribution_hash: 335116f9dac02bdcce5b0ecaaf189725b8254e371f2273d832b6e638c8be11c1
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_5: 1.0
      worker_3: 1.0
      worker_1: 0.75
    distribution_hash: f68588a26fe06b0e3f476866b760cb632356cf051c4a781c47392c57c8a5c0e2
  - id: 2
    dedication:
      worker_6: 1.0
      worker_5: 1.0
      worker_3: 0.5
      worker_1: 1.0
    distribution_hash: bd7d2bf5dd9eed5fe5e588b179705ded49dafb839566758e7444d69b832e9767
  - id: 3
    dedication:
      worker_6: 1.0
      worker_5: 1.0
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: 13d9f35bc4643a0905d5b8f54dd9d4ba1f472a740a323ff075d8871ef15a3f54
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: d0f9e543d65720508f6bd23593b70ed19d15154ecb574b8d54422c85ba86ca3b
  - id: 2
    dedication:
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 285928893482380bf50397962e49cd069b371df4bc4a4b1d38d79a3933e94a05
  - id: 3
    dedication:
      worker_6: 1.0
      worker_5: 1.0
    distribution_hash: eced57241147ecc8bc4386b67df286edf28baecc00ce8a8312c66da57de56cc8
  - id: 4
    dedication:
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: 47ecf80b1c68342e321ed17cffc17fd01526a7acceba98e52145698c014da728
  - id: 5
    dedication:
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: 1ae23a09b6abbe52c9dc52bc35128f366816564cfbb121e79dff99e7097c0ae6
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 0.5
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 3d7196094d451a1c1e3d184636c03d53a502888a0beb1d2086cfea8af9fbe640
  - id: 2
    dedication:
      worker_2: 1.0
      worker_1: 0.75
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: ca73bf55ccf771054cbb14a2d633cf5bf17d747d239279535adda14df0b96419
  - id: 3
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 0.5
      worker_6: 1.0
    distribution_hash: b9a3ab79cc717d71cb19f3408be63be006d22611797c5bd1d9873c3864c783f7
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_2: 0.75
      worker_5: 1.0
      worker_3: 0.75
    distribution_hash: a815f8d462ee71f093ce4c1ca994225c6d2902f43f3b4dfbea9d8544c577d0b8
  - id: 2
    dedication:
      worker_4: 0.5
      worker_2: 0.5
      worker_5: 0.75
      worker_3: 0.75
    distribution_hash: de005359b49ea27a0c170788641ede1a17245408cd8aca2bf129d5b6657630e5
  - id: 3
    dedication:
      worker_4: 0.5
      worker_2: 0.5
      worker_5: 1.0
      worker_3: 0.75
    distribution_hash: b6c6d9e8e6995eedff55f9facf35b5da03ac6e60732edd85169c5dad139ac4d5
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.25
    distribution_hash: 92d2887f8ed6a87b63d90cc2a4674cadd08f4803ca9ef9dfa95709d247f0e214
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 0.75
      worker_3: 0.75
    distribution_hash: b78305289002ac20a949279eddefd522b6f6c86eda349b8fc9f2ccee26129a29
  - id: 2
    dedication:
      worker_4: 0.75
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 4ce75c99069866109e569a2027aa367fa9c8f92260ccaae6fea2d9beb31dc83f
  - id: 3
    dedication:
      worker_3: 0.75
      worker_2: 0.75
      worker_5: 1.0
    distribution_hash: 79f5f1c0fae7932cb014c7554c0c1885259f6fad7bb3f2ebbe0581efd7c8239e
  - id: 4
    dedication:
      worker_3: 1.0
      worker_2: 0.5
      worker_5: 0.75
    distribution_hash: ad8a89f318b4ef35177054dc8988756006422db881e38a999f6bb754644752a0
  - id: 5
    dedication:
      worker_3: 0.5
      worker_2: 0.5
      worker_5: 0.5
    distribution_hash: 1aad81c6c8fae1d56ff672f0666fe53fa2ac6ac378b928d5e5b05bcd82083e58
  - id: 6
    dedication:
      worker_2: 0.75
      worker_4: 0.75
      worker_5: 1.0
    distribution_hash: 31e87fa9d4d9a25e1e10c100d3451fcf124eb086d4898f0e24b260100fc42089
  - id: 7
    dedication:
      worker_2: 0.75
      worker_4: 1.0
      worker_5: 1.0
    distribution_hash: bd3151638bd4e8c72511add0cb7c0db0fb7d4318d5c8cd4ae4ea2eac4bf9e492
  - id: 8
    dedication:
      worker_2: 1.0
      worker_4: 0.5
      worker_5: 0.5
    distribution_hash: 69af75e62a2073041b2ebf4224682c7b449169ad3a45002b54adede3c5d70925
  - id: 9
    dedication:
      worker_3: 0.5
      worker_5: 1.0
      worker_4: 1.0
    distribution_hash: 1ae2f4b2b92345cb882483cee1ac92b729ac3a4bbfb690ebe60d87261c25fb1c
  - id: 10
    dedication:
      worker_3: 1.0
      worker_5: 0.75
      worker_4: 1.0
    distribution_hash: ba8a565bf1e9f70e12a56c2ecb376a2fa9bd1dc98ce7a47f1dabb7516179eff8
  - id: 11
    dedication:
      worker_3: 1.0
      worker_5: 1.0
      worker_4: 1.0
    distribution_hash: 126e6e2c08b2c3ae135da616e88e4003303d223588bc03b8b5476053346bc982
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.25
    distribution_hash: ce3cacd41500f78f4985b3a8d7d0446255a37b85d38889dca158385faca75907
  - id: 2
    dedication:
      worker_2: 0.5
    distribution_hash: 1b7f6618766fcfcc75c78e141c2a05b181614b7246f8eefc974b911dd1b79b8a
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_5: 1.0
      worker_4: 0.75
    distribution_hash: bd3a38dcc5dea7797d65c5d120ba3c41796f2879a26a3536c4fc5d809f5ac69b
  - id: 2
    dedication:
      worker_2: 1.0
      worker_5: 1.0
      worker_4: 1.0
    distribution_hash: d4f5ca80e5b16d9f7db0d0be2a44bd22e5fb6f7a4906eadc9e84ba49ebd25fc2
  - id: 3
    dedication:
      worker_2: 1.0
      worker_5: 0.75
      worker_4: 0.5
    distribution_hash: 1a9cfacc170c762e16d21f55c56d94936346569dbf9cf0c83339d7ae035aef20
  - id: 4
    dedication:
      worker_5: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 491df6e4bfa0134c3db1d07ad46d0bfc085d9ee8e081f647eb97d2e37c6ea76b
  - id: 5
    dedication:
      worker_5: 0.75
      worker_4: 1.0
      worker_3: 0.75
    distribution_hash: 42e79510da0529bbf8168c9035a9ab4d0bd597ea6e2d434870aaf923456b2d52
  - id: 6
    dedication:
      worker_5: 1.0
      worker_4: 0.5
      worker_3: 1.0
    distribution_hash: 3bca752dc6f6fd73fd9e11072d45a8786a33ef6e9d6c28979569afb213febc38
  - id: 7
    dedication:
      worker_3: 1.0
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: 99fbb203071bca86a73feb242e32d646ca39b17a3b2c9d6c2a48758c1252b406
  - id: 8
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_2: 0.75
    distribution_hash: 0e5bfcb2489054bcc1b7eee81ddf047c5bddd93ec39f51718ff5f253b4b78b7d
  - id: 9
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_2: 0.5
    distribution_hash: 4a956de7a46e8ead4915a47904e0e2576a3c3b739cf8b6d123a798f2f96220c7
  - id: 10
    dedication:
      worker_3: 0.75
      worker_5: 0.75
      worker_2: 0.75
    distribution_hash: 64973a459636675ae44c31245379ae7f9feac6e9b9c3ca1035180d917728b0b5
  - id: 11
    dedication:
      worker_3: 1.0
      worker_5: 1.0
      worker_2: 1.0
    distribution_hash: b8ff4b76f9c2cd1ccbab7fb2178bd0a69ae0d90436edaf6a8a1ab0d3e6fbc628
  - id: 12
    dedication:
      worker_3: 0.75
      worker_5: 1.0
      worker_2: 1.0
    distribution_hash: c22538ba1b014b1a153b2de80f783a04fae1d0f02794304aa5098e406899a201
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 0.75
      worker_5: 1.0
    distribution_hash: d6894a56f1918eef630f354d60455e15213d355299f6427a6e8cb422bcd5964b
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: 75a667cb07c7cecb4879592137fec38e8e75c663c52447c44f48d6e10136aee3
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 0.5
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: 75882659c5bb80bbb4421b2424bd7016120f8efc9a59b03d4d902c917453ebf5
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: 25c215aa425e2425d8ea5b7ed0c29064886fc0b98c4796635712cdcf30bd4c16
  - id: 2
    dedication:
      worker_1: 0.5
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: 6324158381a63dccbb7906e8df10666c8f5bfb5b75418fbdfaf9a3aa735007b5
  - id: 3
    dedication:
      worker_1: 0.75
      worker_3: 1.0
      worker_5: 0.75
    distribution_hash: da120989d4501e8fdb777c32c920e02f9f86758968614ca5edef103889f097bd
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 8b3cc13b108071c4d517b3faa28d7d37ce7df592e70c03d086c8170302c42b30
  - id: 2
    dedication:
      worker_5: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 205b91c4a73c7de4df5b2062cee1dabaa21c739d9422aece6131a87d408931b3
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: c6b4a5ff72cfb418dbd62c2d24921af6d2c8a5d172804846b50b7578d7053d81
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 0.5
      worker_1: 1.0
      worker_7: 0.25
    distribution_hash: 0dde9bd6d083c3ced682ee0ff27334042a2b3bd04b2881f9de2cff85a7340d5e
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_1: 1.0
      worker_7: 0.25
    distribution_hash: 7214c3f960f6df223474f02b603907de70aa24250ffc0d16e6a819fb0937b25f
  - id: 4
    dedication:
      worker_6: 1.0
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: f9a451886112399f04331462495fc61bc906026563d50cff00fa21d8c9f9339d
  - id: 5
    dedication:
      worker_6: 0.5
      worker_2: 1.0
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: c905f619db8f8991983be96deccb53657f4ab8a754b0f2f5fa59359964d8071c
  - id: 6
    dedication:
      worker_6: 0.75
      worker_2: 1.0
      worker_4: 0.75
      worker_7: 0.25
    distribution_hash: 82f9e0283836b5c7017b7391553e7eebbb55c96a8656867c2291b8ea00f73e56
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.25
    distribution_hash: 86953f0cdf488c8a96ef7a1493703e400c20fa9e544102d95470b2f4e7509396
  - id: 2
    dedication:
      worker_2: 0.5
    distribution_hash: 89811259c8a9da6e6bcde9b076c8556ed27821d847022b6dd1b1d939fe9e93ea
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_6: 0.75
    distribution_hash: 20dce66a73fa0e02b551e0e65c9c6b96970d84142a67979476410b67705163c9
  - id: 2
    dedication:
      worker_2: 0.75
      worker_6: 0.5
    distribution_hash: cc230d4d48893db22b38b92c147bcbc55962efdc30e19d2aa3534b4367561648
  - id: 3
    dedication:
      worker_2: 1.0
      worker_6: 1.0
    distribution_hash: f3b85cb075875914a26c1fc3351a2b2b9c22b8aa30dd0bd10be4e59aaeb0bb89
  - id: 4
    dedication:
      worker_4: 1.0
      worker_6: 0.75
    distribution_hash: 4c948269e7d08e1a0f85842c1ace285054de89a07089b773d7ce583c250c5534
  - id: 5
    dedication:
      worker_4: 1.0
      worker_6: 0.5
    distribution_hash: b4caffd0a01fee0362893620e6ceef0dbe7a1cd05bb8fbbb2e01eb6b54e44491
  - id: 6
    dedication:
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: 74384f91c399414773c2b14ffa8774eed630964c84d0c3ce452b04364e1d7d79
  - id: 7
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 45923d4416180ab003901c00b438895eba6d5b1d73acb06150d4c36be0328a18
  - id: 8
    dedication:
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 3eb9840316ea442802777616186086ef46f3c5191dc899c24e132a9dd8684ce9
  - id: 9
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 88d11d3ede6b965f3a3c29907df7b0195d5d21048e65746d9029c8ec4d640358
  - id: 10
    dedication:
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: 42a83b2927fb6deaa88b7e8c75996c85a5f4caceb0032d404ec827537921af6b
  - id: 11
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 4a87356d93f18b6b8a53d3ec700f8e551f59545c4621834ab7e4ea8032b70073
  - id: 12
    dedication:
      worker_2: 0.75
      worker_4: 1.0
    distribution_hash: 4613c156f97770d7bfdab9c978fabe5763c3522b334b6da10d126311ed8444d7
  - id: 13
    dedication:
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 71c0ad5e868cfcac2ebe97f4fcc546d485b56bf77131e19815e1730ec55a69c3
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.75
    distribution_hash: a559ccde5b1f811df70ee30000afb99bb741a1740faf4c294c47917fa5996132
  - id: 2
    dedication:
      worker_5: 1.0
    distribution_hash: 5f05c156af332e96a33bd40c496a8d88f78612ee132d61cabf468beab976cbeb
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: 6e5a352cbe771ad1eca584f4be906504c4a10cb191722f0cacdea7db5089db31
  - id: 4
    dedication:
      worker_2: 0.75
    distribution_hash: a52413a2ee31ee9d4f7bd6e1b5e85ef93b4397bf64d23b4eb1ce5a5de454b72f
  - id: 5
    dedication:
      worker_3: 1.0
    distribution_hash: cf7f5a1c27f20c890e843d92f634bceccf9297171dc7ed4ddf4d2aa4dac0af8e
  - id: 6
    dedication:
      worker_3: 0.5
    distribution_hash: d0e56049e512b6f658afacc6c5496785b08c7027ba5e8b7bb084f44e7019de22
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_6: 1.0
      worker_1: 1.0
      worker_5: 1.0
    distribution_hash: d8332ae193bce945f16bd99a0b990f4a3d133b4d32c0723ab9155246841bb604
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: b51d88e88198d2f75a7989cdac7dbe0793942e49ef2399dda0371e4455d3c21f
  - id: 2
    dedication:
      worker_2: 0.5
    distribution_hash: 00fa433c54470abd18bb589c12657ce1430288396c65ac435a25a70a43e78b40
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: d1d211d292816f7589f2d098f555ba7245045ede2102f078e218c1230998d80a
  - id: 4
    dedication:
      worker_1: 0.75
    distribution_hash: 00a06734eb3358ec972e7a7eb68fd52f08acf850d146cd158e6ed5369d0a5d7c
  - id: 5
    dedication:
      worker_6: 0.5
    distribution_hash: a83ea21a6e647ae803d9e6abf50c4cdb70e3fa08dfde002d37834c580221b977
  - id: 6
    dedication:
      worker_6: 1.0
    distribution_hash: 586bdf893e9809a0bbe33d7a36b281bad47faa7ca19f4e4279e2366937455342
  - id: 7
    dedication:
      worker_4: 0.5
    distribution_hash: ae5bac5b03d3c3c4bac5371381b57ea0f8d9917b2e27394c88490d582e92b64c
  - id: 8
    dedication:
      worker_4: 1.0
    distribution_hash: 602701c29c2755f9ee577cd9b4986c91a8962aad048a8b74003a02f0fe9adc6e
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
    distribution_hash: 3be4cc18cd5ba512369d32e9414b813393535111e37ecaf16e8c2528d03c43c7
  - id: 2
    dedication:
      worker_4: 0.5
    distribution_hash: a413fd5084d93935c8abfa4b7fc17ddf76df621d457539845a74297be22c5315
  - id: 3
    dedication:
      worker_4: 0.75
    distribution_hash: 2d3f56b500202eb92b5afdb05c7a46a878a2caa92cbe5768cb831ab762a7d606
  - id: 4
    dedication:
      worker_4: 1.0
    distribution_hash: 0c0e2380b848fc9c1fa05b89c2b2ecc0d27a0fcd5d92ade3c54cb632c2848a6f
  - id: 5
    dedication:
      worker_2: 0.5
    distribution_hash: 7227ad1cf938a7fc29a4101d1fbb9510b98d829c355a113859e90a5f531bdc0e
  - id: 6
    dedication:
      worker_2: 1.0
    distribution_hash: 2b0e821e15fcf49d3f4e9a13d1529a5cb8af822dd71832d50709c09b4c5f0696
  - id: 7
    dedication:
      worker_5: 0.75
    distribution_hash: c50b6ca4e7f8d8105097b2f1bccb33dc2cc28bd3019880e3203bf724f85e4b0d
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 80187b6b4d1fe72d3c35ab4bb6b66fbfdda54f1b9defe20b160c20082b7df4a0
  - id: 2
    dedication:
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: c040bb0279b26cdf4f263ea90d8c625fe4038624b3fe001999880b5fa30d8289
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: ccd9ee84ccd634e19a01677036e5868aea16b5a3c3e706896599a4d3195af98c
  - id: 4
    dedication:
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: dc94a08eb637a990111b5fd937d3a109bf626100ae9af23b210c4497156ee6d5
  - id: 5
    dedication:
      worker_5: 1.0
      worker_1: 1.0
    distribution_hash: ee9d68d51c78ba15724160ad5b7d8f5326ab3f0283426b23e5b43bea4ada6148
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
    distribution_hash: 0014040397f0823530b409b86aa3ca66d8e605e3aac6ff03a191f18711785f7e
  - id: 2
    dedication:
      worker_2: 0.25
    distribution_hash: 317aa3873cc169d4c9f6273fc62f00b655589a42baede5d5d484f1dc1bf4cee7
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_6: 0.75
      worker_1: 1.0
    distribution_hash: 1c05c89e93ae19c9a3dc81d385e9ef1c683b65d2317c1a689b528a6a908e77b9
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_6: 0.75
      worker_1: 0.75
    distribution_hash: 91e6307a183b6524a54189fe02407ac164f1198bfc10e0ee86430d0e416d9d42
  - id: 3
    dedication:
      worker_2: 0.75
      worker_4: 1.0
      worker_6: 0.5
      worker_1: 0.75
    distribution_hash: 03ca2d0afb4cbab9269018f41774f18c1b0801afbd7e7545fc91f65e97789aa1
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_6: 0.75
      worker_7: 0.25
    distribution_hash: fb68188b0c5e81f0f1eed8da6981ce6e413063148d984af76f169e9abdc29b2f
  - id: 2
    dedication:
      worker_2: 0.75
      worker_4: 1.0
      worker_6: 0.5
      worker_7: 0.25
    distribution_hash: 76ee489616cca086c68be087ce0a7efafae32fd31fac42fc9fede8400d8618ee
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_6: 0.5
      worker_7: 0.5
    distribution_hash: 1e6385eff6d2557489b08a576204536c0676186aabd194dcede882cec3cc43c9
  - id: 4
    dedication:
      worker_1: 0.5
      worker_4: 0.75
      worker_2: 1.0
      worker_7: 0.5
    distribution_hash: dc0f79fccd0b8f8b21b719f9f174bdff971020c6bb84685ee3a2e022108abe6e
  - id: 5
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 1.0
      worker_7: 0.25
    distribution_hash: 51bbef5f4179ee12c08e057365995eae9ba097a6891c8eb745a742e2dfee46ed
  - id: 6
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_2: 1.0
      worker_7: 0.5
    distribution_hash: c34efc303a108b5df8abd067fc418e2370036676afbd9cc6ebee32b9f9061ead
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
      worker_3: 1.0
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: 872cf178e158dae4671db643633e937cb80f18e5fed02ded87a0d1b93c4a3fa6
  - id: 2
    dedication:
      worker_5: 0.5
      worker_3: 0.5
      worker_1: 1.0
      worker_6: 0.5
    distribution_hash: 9354de39be7e7f9143086318c998d3b0f6b5e9e187d53a983847f5b5c88fa692
  - id: 3
    dedication:
      worker_5: 1.0
      worker_3: 0.75
      worker_1: 1.0
      worker_6: 1.0
    distribution_hash: 059442ffe036189f6027b9942fe630adc24d920c164c2e24eb2ef342842b7baa
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
    distribution_hash: b6a3435647d3be213e8580c9deab9abb4c6c872f71c9b19bcef633f8053270da
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: dd909f702c6ddbfb73e9a73360d68304d4bb2df3abcacc0759fe1b2e47a838f6
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: 576bd823eb77c893f15ec276aff18f89dcc714d8386b978e60aa53c7087520e1
  - id: 4
    dedication:
      worker_3: 1.0
    distribution_hash: 097710a5d59cde0c9f5b16872252a1b43f5bccb7cb4f339cfe71af95f9af1b88
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
  - task_14
- - task_1
  - task_15
- - task_1
  - task_16
- - task_1
  - task_25
- - task_1
  - task_30
- - task_1
  - task_31
- - task_2
  - task_7
- - task_2
  - task_17
- - task_2
  - task_20
- - task_2
  - task_23
- - task_2
  - task_27
- - task_2
  - task_29
- - task_3
  - task_10
- - task_3
  - task_17
- - task_3
  - task_18
- - task_3
  - task_20
- - task_3
  - task_21
- - task_3
  - task_22
- - task_3
  - task_24
- - task_3
  - task_26
- - task_3
  - task_27
- - task_3
  - task_29
- - task_4
  - task_10
- - task_4
  - task_12
- - task_4
  - task_13
- - task_4
  - task_20
- - task_4
  - task_21
- - task_5
  - task_10
- - task_5
  - task_18
- - task_5
  - task_19
- - task_5
  - task_20
- - task_5
  - task_22
- - task_5
  - task_24
- - task_5
  - task_26
- - task_5
  - task_28
- - task_6
  - task_11
- - task_6
  - task_17
- - task_6
  - task_19
- - task_6
  - task_20
- - task_6
  - task_21
- - task_7
  - task_21
- - task_7
  - task_22
- - task_8
  - task_20
- - task_8
  - task_21
- - task_8
  - task_22
- - task_9
  - task_17
- - task_9
  - task_23
- - task_12
  - task_17
- - task_13
  - task_19
- - task_14
  - task_17
- - task_15
  - task_18
- - task_16
  - task_18
- - task_29
  - task_19
- - task_26
  - task_18
- - task_9
  - task_22
- - task_5
  - task_17
- - task_31
  - task_19
- - task_29
  - task_22
- - task_2
  - task_11
- - task_3
  - task_12
- - task_15
  - task_23
- - task_13
  - task_24
- - task_8
  - task_28
- - task_15
  - task_17
- - task_29
  - task_24
- - task_3
  - task_13
- - task_15
  - task_24
- - task_10
  - task_32
- - task_11
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
- - task_27
  - task_32
- - task_28
  - task_32
- - task_30
  - task_32
deadline:
  delta: 591
validation:
  project_key: e99080e26d6af75900853f2bb0f16a1b053b0b4d195decef69dc176f3af66f38
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 80 days; worst-case serial bound: 1701 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
