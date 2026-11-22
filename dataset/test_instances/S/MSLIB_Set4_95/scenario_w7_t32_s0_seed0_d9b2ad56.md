# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_95
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
  modes: 150
  tasks_at_cap: 0
  relaxed_constraints: 2
  rewired_edges: 14
  departments: 1
  quality:
  - worker_5
  safety_skill: 3
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 1
  barred_pairs: 2
  incompatible_pairs: 1
  edges: 75
n_workers: 7
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 429
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
  6f5cd932d960655f40f037a132bd6a1ad90ff0dcc48ae0fe84639ba401a6c1d6:
    family: pert
    a: 3.5670523739096462
    b: 4.4588154673870575
    c: 6.9461613161533995
  a315eac7f508b8dc9383095e37ed5099c4d9fc61787941186ee879f648b6ea7f:
    family: pert
    a: 2.701772175158224
    b: 3.3772152189477795
    c: 6.678489483362605
  f8b9dcebfaa0139a5d30e3766f847ceea10fe78184ddd57cc114139fdbb0498b:
    family: pert
    a: 2.991569975673638
    b: 3.739462469592047
    c: 6.693219664178702
  82cdddb9d7dddb8f075b91af1cff4128d344e94476a7f5fefc942b86d99cc7f5:
    family: pert
    a: 6.451289410436356
    b: 8.064111763045444
    c: 10.651112440529127
  d39edeb0eca80b623923d2bd60457bc7db9cf3a11fc7ca8d77e7d0071ed405f7:
    family: pert
    a: 3.9789512363443573
    b: 4.973689045430446
    c: 8.195920903428451
  2069657f8eb9f4dd6c9efe1af14cabe4fe31d89dd1da46f1ad37c4f87e494cbb:
    family: pert
    a: 5.6982088963961495
    b: 7.122761120495187
    c: 12.671875891933762
  529c3afca5304cf525d7baf5cf3b2ab07328e60041df6e5336ad8b07eba43bd6:
    family: pert
    a: 5.362190457401493
    b: 6.702738071751866
    c: 10.371950474435627
  29dbd9c2bbc65a5f3726df42ddcc2da00828c2919fa08e070ea79a5dac79350e:
    family: pert
    a: 5.520968964259136
    b: 6.90121120532392
    c: 13.039890128839254
  54ea7a1ced70733e67629f54d094c50443437003cdeab57212aba5e52e78a6da:
    family: pert
    a: 23.227780469797224
    b: 29.03472558724653
    c: 53.45285753611962
  42687f591a6ceab5c632861f4d6b182dff729dbd1d246da747a0dc9190650046:
    family: pert
    a: 20.607478265054105
    b: 25.75934783131763
    c: 36.78067499789241
  4f5e48cf2f7f856307a738b4add02829f7aacb9292c534061efeaab3ed8f6c88:
    family: pert
    a: 13.897515282900953
    b: 17.37189410362619
    c: 47.000194346838065
  f4fe4a5a66fcc67968e96d4570e0dcc6e88bdef7ce49a84c32a8113b4da1ba92:
    family: pert
    a: 26.923762902615813
    b: 33.654703628269765
    c: 46.81418137205802
  1ba93e8d3b7e459745939843c6e10aec822347b6fb72020093b91219817cda5d:
    family: pert
    a: 47.86386377915494
    b: 59.829829723943675
    c: 82.27722935446846
  cf5072b9b1361ebeafbec17b40c485d12fd66736964167c4bb357aced37e98ad:
    family: pert
    a: 24.164144587840884
    b: 30.205180734801104
    c: 39.35491037723866
  ed33284dc711b8f387b2e5fe3ec0feb62dbfc33efff12a1f276142bc599f69c6:
    family: pert
    a: 28.240026234051225
    b: 40.34289462007318
    c: 102.81934166802223
  b133065dd02bb6c23cc1ca95b4a73dd46e0c767389c62bfc43d14f4726090ea1:
    family: pert
    a: 21.788723967566217
    b: 31.126748525094595
    c: 82.44447643261117
  1432338eb1077d6fb77ca79afb764833940e07b951c8a6e868dfcae91ee2faf6:
    family: pert
    a: 21.07112433879468
    b: 30.101606198278112
    c: 86.8617344906929
  59495c1cc2d45d351a19e0f53c060e42df758fca2adb45c62852f7527ead6692:
    family: pert
    a: 28.534863236168906
    b: 40.764090337384154
    c: 57.916776776447264
  f1c7b3e8ab54176895328d0a42b31d58fb48fb2527ec0fd1b984fa3de6e7a4df:
    family: pert
    a: 15.668475294836457
    b: 22.383536135480654
    c: 71.57450305924367
  0fad8e378f874d58adaece17b44820f02dab63edd6059dcf309426e2fdad9a03:
    family: pert
    a: 24.218967401754742
    b: 34.598524859649636
    c: 62.74302502688207
  df2fd99fe41af2ef385a14fdb613711df7aa4848658fc9c70cd69baf7ecb6eb7:
    family: pert
    a: 32.27075486268397
    b: 46.101078375262816
    c: 65.26547020111352
  c49ca91cf96e6fc6697174b13c5f6d9a6f2aaf3c07879926feef9147b5d55cb5:
    family: pert
    a: 17.183830787363135
    b: 24.54832969623305
    c: 69.70345569396893
  4cef1dda78c22c42cc320ecd980153672314da68217fda8cafad21fd6d5c1a22:
    family: pert
    a: 23.915897176736927
    b: 34.16556739533847
    c: 97.24344839644976
  4699631eb31d685f45189affa828cf8e80df3e1ab8076c3bca8e0a2b322979f8:
    family: pert
    a: 24.959809413216448
    b: 35.65687059030921
    c: 67.57562094111807
  853f20de0b878a1457140657d0e5bbe23df696f304597cde816ab5d75806a89f:
    family: pert
    a: 22.918641524292045
    b: 32.74091646327435
    c: 62.95386832330259
  e1cc7dbc8eb44d315fda25a036b56a39f9a69c4dd247d91b3203bf9eacfc634e:
    family: pert
    a: 19.67629870252895
    b: 28.10899814646993
    c: 96.9566660150571
  4d2de07b530847a4acf5158653cd1308b299baadb4a3a0c18bb84e607b6ba721:
    family: pert
    a: 55.19245899523751
    b: 68.99057374404688
    c: 85.35189914531406
  a73225a64b6efdf866315f63b7646d41db8bfb45121479fe2df9396addf9446b:
    family: pert
    a: 32.1865969091127
    b: 40.233246136390875
    c: 81.72221168248184
  aaecd419eee1fc6f46b07d1ced8cf329692ef981864300b507d35dd385ea5a1b:
    family: pert
    a: 29.661207239242255
    b: 37.07650904905282
    c: 66.22306026565872
  e48a24530d2fdb1d077fdc33a1c34a0c115243edf1cd87f330123332216f0946:
    family: pert
    a: 18.947486806381196
    b: 23.684358507976494
    c: 42.22788738672447
  3c14b3a05e9e97762a42cf9b9f182417205ce9b98b7e70201e37e8bab94a2591:
    family: pert
    a: 17.12281230187368
    b: 21.4035153773421
    c: 33.8678070739227
  2900b238c20a99506f7066005d7b9e6c697bcb90e559857041532b030e59b97a:
    family: pert
    a: 19.616978292560148
    b: 24.521222865700185
    c: 39.27382331210603
  d957327d04d7291e735e8f6093f17c719807adb3b525241215d57461c9109c47:
    family: pert
    a: 39.43966859545069
    b: 49.29958574431336
    c: 72.64993221766288
  c72e7b611b3cdbbb19751dd02e205e5c5c7402e5cb9ce88d656eef715cdce175:
    family: pert
    a: 27.543654848206337
    b: 34.42956856025792
    c: 59.04777806512179
  f669308edaf9fd205dfcd73ea7c51cbdac8decf75bf2062f749fb6b41335a2ba:
    family: pert
    a: 39.582304516555624
    b: 49.477880645694526
    c: 72.34654213760584
  ef42f7d4837cd4c1ab1731e461a6ffe9373d3818fde33de45a7513dc7b5eafe4:
    family: pert
    a: 40.33704947068074
    b: 50.421311838350924
    c: 71.37759780953334
  014963a8a400eb6ddeed14410ced5c4c83e2cf05679542934198cfacbd2cf286:
    family: pert
    a: 26.320414621215903
    b: 32.900518276519875
    c: 77.28664338265757
  7ccb161fd5f82d35c965cfa69d873aff4fefc886f579d21e067276d70897b9ba:
    family: pert
    a: 40.54926743843563
    b: 50.68658429804453
    c: 62.88636086500502
  96321587a7d20924ee135d03772ad11896cb5bbc9865fd172610d3804bd4669c:
    family: pert
    a: 15.455037862519521
    b: 22.078625517885033
    c: 71.66284661130265
  f67b132834a13d8e67f24ce68237ab6562166fc0500d1e6c5db36368754f8616:
    family: pert
    a: 8.739118435016945
    b: 12.484454907167065
    c: 78.76586172602813
  a82499af26b2d7357a2acfa6c6c2848514687aff8efcf2732359d4f0554058e2:
    family: pert
    a: 41.673375680380644
    b: 59.533393829115205
    c: 108.36380871989316
  c4c57f4e789729b7291d1a5ec5a04902019063893c53301eea82ea420c3ac32d:
    family: pert
    a: 46.88523683905301
    b: 66.97890977007573
    c: 123.98543533869052
  da119311391f2031e483b1e640dfecfc61439a341a89986b23d51b36c736949d:
    family: pert
    a: 41.93923322667561
    b: 59.913190323822306
    c: 94.04105502360457
  25fc8f7fa074e4a01b0a9daf6e699ee193969ca8924a81b4c7ed76934a59c768:
    family: pert
    a: 23.432254152970483
    b: 33.47464878995783
    c: 150.01480300941265
  6e039f85dea4d52519482f42ee842905f99f6d9db1b2b9b1e87bc4e0a959dd54:
    family: pert
    a: 32.73034896476208
    b: 46.75764137823155
    c: 109.29257089379003
  7e124a066ad5e7f393c90e57c2227b05e9d549a5a4d9013457b7e4c3fa37fce2:
    family: pert
    a: 22.711544450366496
    b: 32.44506350052357
    c: 54.052337206924804
  fe5b157346a51fb1969f532e08d281f5e85d55f6d887a133693d8206646b373b:
    family: pert
    a: 17.35527042944642
    b: 24.793243470637744
    c: 71.38560216323697
  4f790b897b4a81c93eb8c267d1485676b8f9ddcab362babb7841d7926eac44a8:
    family: pert
    a: 15.360737739307071
    b: 21.94391105615296
    c: 41.537439476978776
  68b3debf7129e7c7fa7ec0b31d933077e4abfd61b88a7a750a04346a8e11d5c1:
    family: pert
    a: 19.845251496194354
    b: 28.35035928027765
    c: 51.42238578798627
  4d2a1b35ef191f0de0e201490b90f80942398053ca6ad077ee419e04c1560006:
    family: pert
    a: 22.582030183262546
    b: 32.2600431189465
    c: 74.97730112491865
  fcc1401ebf06dad3ac74f2adceacc09af451c67728be08fa68b03910aac2c636:
    family: pert
    a: 21.7613327363076
    b: 31.087618194725145
    c: 75.15304616780423
  d39bab6bdc8e2c30c71593e998f6ed13f1eef58e49f71ac0e404d18ea52e9b89:
    family: pert
    a: 16.669980734789856
    b: 23.814258192556938
    c: 62.54273006733844
  194c646ca146ce2a38daf4e780466177e6f87f8d297b3613adfd5319ed78c836:
    family: pert
    a: 13.780180275821296
    b: 19.685971822601854
    c: 64.37848242101892
  10b6cc5cc49d2de6457040d768e23528a0bea99b24f8a83a8c6cbf0cbd7daa7c:
    family: pert
    a: 25.23805041421462
    b: 36.054357734592315
    c: 107.04007230731337
  bafe7e2e978283279c6fc7a82b3df46b7e977cab4c4f2f8df1a035933f346de4:
    family: pert
    a: 18.505655040228582
    b: 26.436650057469404
    c: 77.12527244366777
  433e507fa64f8326c6b41d340aea7bd560282fce42536ddf43d228e4a12896ae:
    family: pert
    a: 17.03435511580692
    b: 24.33479302258132
    c: 57.780901984982215
  1756fe49b53f83f8a83b8c364dec966b354b22f33f4242caa181e55767ec4327:
    family: pert
    a: 17.741877631305815
    b: 25.345539473294025
    c: 57.248301459409745
  95abd106bab0c81e7d8c623b09cc62295e7363e97d5b6cc44ef32f99e0b7bd47:
    family: pert
    a: 14.189753075049289
    b: 20.271075821498986
    c: 49.77925155713659
  710f5194c638c546b6490ff19445f68cab3f9f3860d955891f325e3cc02c7721:
    family: pert
    a: 11.180003206162695
    b: 15.971433151660994
    c: 60.32455475975779
  6f6f4f70c12a572d640d5c4e3f8d8cd78be4cbb3806150becc9e49d60655c208:
    family: pert
    a: 18.287945453965033
    b: 26.125636362807192
    c: 79.14623982080093
  dfe7593309a37c27fe7710208fc527ff0dc6b97755f95efab0f5b5d6648031b8:
    family: pert
    a: 26.7530781583825
    b: 38.218683083403576
    c: 114.56077942249473
  c4ff61e6f7d3604d1ade2927af30a9fa74e768ae76bfbe8251a36274e9d00325:
    family: pert
    a: 50.46907839729718
    b: 63.08634799662148
    c: 94.10764045350521
  2f27c1a23293a0b9c5651ee5aa9e659b17f96008c2b9c4f9a25a007483673c42:
    family: pert
    a: 2.9057573314455207
    b: 4.842928885742535
    c: 18.9593918848613
  4e968189a05ceed6617cd4e28516a51d9f977de4753b3b04438ac1151cc781f3:
    family: pert
    a: 3.401257217033515
    b: 5.6687620283891915
    c: 50.11923909385834
  2ae3417fa09d048269d6c221d3a2a7e88ca72f20f90f558c2873fbbe0355f4f7:
    family: pert
    a: 1.6830229531916912
    b: 2.8050382553194853
    c: 13.469758420451885
  ad16798f772a3345a02da4b126b3901d08e54cfc5d755be7f61913bc0ba1d2f7:
    family: pert
    a: 3.1638176749148967
    b: 5.273029458191495
    c: 14.863589790117341
  7115fcdc38d3ae8eb7d1d72c6de538e743e5443feee532f6d77ab9c1e6aee8ed:
    family: pert
    a: 1.9596298532567495
    b: 3.266049755427916
    c: 15.253328971476426
  38a8e8a82dbe724257f39943a96e2fd43b221cfc7ec872bc15f6d9b2ef379e82:
    family: pert
    a: 5.2895180737650564
    b: 8.815863456275094
    c: 28.85322734035002
  82a10d752df6e59b58e98cbf58f1938edaedbc2799e0ec9785461ed8c8127f91:
    family: pert
    a: 23.898604350488775
    b: 29.873255438110967
    c: 46.95684655246948
  acfac055e7cb011771a3a21b997f126c6c8eb80cc8f5770cd2ef7f2d6696294f:
    family: pert
    a: 19.746219197166425
    b: 24.68277399645803
    c: 43.65051852306951
  12e4375370acad9eb6eec475d42a791c5cca8314d1265a4029a69438b530edec:
    family: pert
    a: 31.26661998330567
    b: 39.083274979132085
    c: 48.46125026819714
  2bfb74d710d9655780cc170ebda242285cea6d4b890f071d6d7f5b6ee295b741:
    family: pert
    a: 21.28786321609463
    b: 30.411233165849477
    c: 70.56068344098783
  6cb6740ac4f6f5f41485dd3883ef4f50acec0f8dd0cf085d6651c871150c2cf6:
    family: pert
    a: 26.642096356856317
    b: 38.06013765265188
    c: 87.49228684729462
  c819ea4c288084615c308afa742358e50e86ffcd9da774c802cff655f82ed1c5:
    family: pert
    a: 39.544693965054044
    b: 56.492419950077206
    c: 133.82987227600117
  3ef9d950d0c678ab54e98d6414fb63693237f10c2b51fa9c06d81a44886908f7:
    family: pert
    a: 65.70789834766131
    b: 93.86842621094475
    c: 142.94630212967255
  9af7358234b5611680f0f07a1d509fb89fbf0a5828522ef30361eeaa1e440683:
    family: pert
    a: 28.18467617196676
    b: 40.26382310280966
    c: 74.48701693689176
  15808ee857dc95d6de9092db84a5a3894c8efb0a8c8c3dba78177fdccf45ab8c:
    family: pert
    a: 19.63224283505261
    b: 28.046061192932303
    c: 91.9779109572681
  140fbe78f4da09ef5f5378d72a726efa5571e5ee8ee6ae2d6ec939420f5883c9:
    family: pert
    a: 59.66100103165776
    b: 85.2300014737968
    c: 129.33543830302213
  e91a990e82c9e772c46ba2632f66a131cdaa5d1a4a72caef92cdaa66a9453334:
    family: pert
    a: 30.199231285411333
    b: 43.14175897915905
    c: 93.27495671072755
  5dc150d6d8adc2e3715297e6d3ddc0bdf0e0628dc98891d88da48052a9ce88c6:
    family: pert
    a: 22.835214200036525
    b: 32.62173457148075
    c: 65.28441358887375
  0411633e4a631e75a18d51fc606cd42030acee31dace453384962f7aa81f36da:
    family: pert
    a: 32.84396978254119
    b: 41.05496222817648
    c: 58.12638180948278
  32de936d84ce07bbdb9de3866da9101603e5ffc200000bb95880315ad96455d1:
    family: pert
    a: 31.04970632778823
    b: 38.81213290973528
    c: 66.39441838048144
  ac24b46ce0bbaa8f149d577e275b35cf2c4d30a8346774fc68129f8a6513e9ba:
    family: pert
    a: 38.21343763405697
    b: 47.76679704257121
    c: 73.46995277454859
  c9f2af2e2dd3dbc0bb99ed94e056b1fa42bebaff6341c4ea93a60076278d16b3:
    family: pert
    a: 10.853243608402794
    b: 15.504633726289708
    c: 77.52316863144854
  af32257c0cd46c22611292ed68cc20304b278fc2925ab73af9bbe86bec10bf31:
    family: pert
    a: 13.608213078463194
    b: 19.440304397804564
    c: 97.20152198902282
  cd86ff081909a7262fd49598135894e373865caedbc15a92f11f90e6f8292fe5:
    family: pert
    a: 12.127835123209998
    b: 17.325478747442855
    c: 86.62739373721428
  698b7b19f038fbb2e0a9913ff9f6577c83babad7ed3d97c9cd953cc47171f780:
    family: pert
    a: 10.726090721673115
    b: 15.322986745247308
    c: 76.61493372623654
  6532a4237399eb7fae81a4151081a9bfabd77955aad786080fc97e6402c83ed5:
    family: pert
    a: 11.708623721493703
    b: 16.726605316419576
    c: 83.63302658209788
  b387684d44c0075e884be902a7f430112b4a9c11716d4e75e54e79d4ab4affd2:
    family: pert
    a: 7.2182824300538035
    b: 10.311832042934006
    c: 51.55916021467003
  7d582d8bd8807d244971887847136f3c8895600ddea7627c730a3ea839af2635:
    family: pert
    a: 10.987182538262504
    b: 15.69597505466072
    c: 78.47987527330359
  d031a713ad8c87fd414716c45d067feb53171104bbda319ad13f2b40d6f05b68:
    family: pert
    a: 8.31420453345019
    b: 11.877435047785987
    c: 59.387175238929935
  89eb5a3723653589e705a17788fa86ad78b01a2987037fbf6882d6f5dcba735e:
    family: pert
    a: 31.50136038932166
    b: 39.37670048665208
    c: 196.8835024332604
  6eb2f8b0465fd31489f56a420f27a0c09da1b5796a4204893fe2c6737bea8871:
    family: pert
    a: 40.59118448028215
    b: 50.73898060035268
    c: 253.6949030017634
  f6e1003473524fba43d5d9904d4dd145f7d4fa6e89f130d6f7fa84299f8f2a4f:
    family: pert
    a: 24.65766922534769
    b: 30.82208653168461
    c: 154.11043265842306
  a29d6c5969df06429c98738f20c0586b5079699371da3576bada2f5403b78574:
    family: pert
    a: 24.425484084614425
    b: 30.531855105768027
    c: 152.65927552884014
  93723a41b695e8ff8820e9542c41d685713b18424d218cb664469d0f5e5d6944:
    family: pert
    a: 23.44175818724685
    b: 29.302197734058563
    c: 146.51098867029282
  b8566cf78099a97a49e69c3ce0c14c85c6e55c0c480ed4764295680ba723b376:
    family: pert
    a: 28.408301549729245
    b: 35.51037693716155
    c: 177.55188468580775
  6b9c01c1e4606f90435bf656c8e796d9168905ced8873ea31e5fae2042f22617:
    family: pert
    a: 5.575626147026479
    b: 6.969532683783098
    c: 11.935956654161666
  b191da6ce1e14a14c568f232be0d90dcfadf69c5041ffdc6139b7e8ebc35a76d:
    family: pert
    a: 5.264839420828446
    b: 6.581049276035557
    c: 13.349392692079014
  ecc1cc686ecf3b92556fb5f5d6cb06690c7fb526f87ac446937b85c7ad91fa1c:
    family: pert
    a: 8.322133298048286
    b: 10.402666622560357
    c: 13.87572247132166
  8febcd7edaa055b6d0b594e4e431f94eada8d3e254b4ab962fa9fd121112bc9b:
    family: pert
    a: 3.131739678315342
    b: 5.21956613052557
    c: 16.19421044433507
  6e704b46e4806a93f5621ef1b18d42af293a2ad2f22b45ab7055b8272d0e6f99:
    family: pert
    a: 2.6477033332971183
    b: 4.412838888828531
    c: 13.613232270404191
  4d893dd7cad3179f9c56c4bf1ffe8fe9b8a819c91049af0bf157d665396935aa:
    family: pert
    a: 2.769444458314891
    b: 4.615740763858152
    c: 15.06003943832256
  8c0e11c377460133ab0c114f45843f1f0e432fea703c7dde8b70330794cb161a:
    family: pert
    a: 103.270928192452
    b: 129.088660240565
    c: 200.64568560895867
  5558fc3422ff5362f58b5933dddfed378f24d79c68f7d28c536a9579880ab82b:
    family: pert
    a: 48.41231126739871
    b: 60.515389084248376
    c: 103.55352572262085
  1faf476f55a87787b1a2f6793b5a8ef792bf03bed0812f406d9ab5b05345d4c4:
    family: pert
    a: 20.856109264263544
    b: 29.79444180609078
    c: 74.59686203454139
  1447e25054a6d936b7d746c2151d0bae521206b82283ed5c6f701942ec1b3da5:
    family: pert
    a: 21.76399087706464
    b: 31.091415538663774
    c: 80.4036617589918
  8aa7ec320de026845e28824e8421329aa4e8e654568aa9a9a509f643d429abf8:
    family: pert
    a: 22.54296817122438
    b: 32.20424024460626
    c: 67.67691272700195
  188020d316873fe0e3f1daa3b9a921efa260a14847ce5c5760cf58a02ea05f0a:
    family: pert
    a: 31.840602787621677
    b: 39.80075348452709
    c: 76.96193541159367
  cae7cb50bfe7b7818f21a5167352c849b5e25f29520fbc95ea016eca9e574a4a:
    family: pert
    a: 36.777256168577686
    b: 45.971570210722106
    c: 73.85698937246067
  da8ac84c0960cc0b7a4d53f0e63adca4a5da89b92b1b00df74b09e7f25bd1845:
    family: pert
    a: 20.683435279812084
    b: 25.854294099765102
    c: 72.73455939806473
  c9e11e0f8213aeb3631692ba645e4cfa208ae33571b038426d247455219da9d4:
    family: pert
    a: 28.215523002884186
    b: 35.26940375360523
    c: 57.80845040556853
  0c6a75175264f7e6ef014c9991367d90728efd2baab12c9cdfee8e364bc09494:
    family: pert
    a: 43.51433330430059
    b: 54.39291663037574
    c: 87.50828274933497
  0a573c4ea1c4d91caedb66494ed8cc8abf3d2e188b468cc9d4db816e689e87b0:
    family: pert
    a: 24.43323460667672
    b: 30.5415432583459
    c: 45.60215441944522
  8e9aa556b72483bd712e5d07caa754d2e94adf5bed35bc08ddbd54d5c35b58da:
    family: pert
    a: 49.04671098163979
    b: 61.30838872704973
    c: 96.91101415080895
  85286291c575c1908e653c65b5482da4ca571d4a995c37efb7a50d7458e37cee:
    family: pert
    a: 50.539345823929516
    b: 63.17418227991189
    c: 82.2753609583276
  3cdf926c54d9889eb2dd28f6707d8fc5329058153569246009cb3b21232c57dd:
    family: pert
    a: 42.59398552165841
    b: 53.24248190207301
    c: 67.44463097715447
  0af8cf63a0a2abcf974041c4fa8cbe7182b440cbeb5f06d6b30009ca4550c585:
    family: pert
    a: 39.531122532265876
    b: 49.41390316533234
    c: 247.0695158266617
  fef4a8f8a316900391e9ffd4d0628ead70cd2fa871111f93ed62194c3d964251:
    family: pert
    a: 103.66030105950426
    b: 129.57537632438033
    c: 647.8768816219017
  79ac5b476774d841186fc792ac964bc658b90e2a6b3a659e5de87d1760ed5cf9:
    family: pert
    a: 36.12662248708479
    b: 45.15827810885598
    c: 225.79139054427992
  6603c9ab8e0671a1d5bde218444e311c5707162098bb0d741cea781c4b420d84:
    family: pert
    a: 28.396871369010217
    b: 35.49608921126277
    c: 177.48044605631384
  75d8fa0b5f315464a8ef13f5d925d7228e258417023ec5a24cef64ebfa83f181:
    family: pert
    a: 49.09400958517538
    b: 61.36751198146922
    c: 306.8375599073461
  908436975e16334dfedfdd5654f6b023d89bbe3d097ea7a738659e75cac36b32:
    family: pert
    a: 25.70609444714897
    b: 32.13261805893621
    c: 160.66309029468104
  2d6ca5419c3fe118c385c0a03a69b1c3a13cc5647334e4bba85711565f940bc9:
    family: pert
    a: 71.99720879830268
    b: 89.99651099787835
    c: 449.9825549893917
  6233124b99ba7889b73da9c1e14df7de7854040c82c25fb2297aead01b9df9d4:
    family: pert
    a: 39.254258329336615
    b: 49.06782291167077
    c: 245.33911455835383
  a5b9c878e7c3e95282fa4f420198a9935ce33dffb9e8362abf0d2ea17270c7d9:
    family: pert
    a: 44.095577698672514
    b: 55.11947212334064
    c: 275.5973606167032
  dd1333a8dbff6e0035c2928cd23e9031f06c4d18633a1f7b801e000670e2429e:
    family: pert
    a: 59.653422126331606
    b: 99.42237021055269
    c: 287.3134881495079
  a1cf236c8176fa2e95dbe6bd36a341acdfdb3991c183d48e197250a441af521f:
    family: pert
    a: 29.02247750873528
    b: 48.37079584789214
    c: 157.11454556134285
  8ca42fb61773df3b04ac7384fe920f02521249a3a917d59f56949bfe45a337a4:
    family: pert
    a: 11.152613341616808
    b: 13.94076667702101
    c: 19.364917148592305
  48dbf526169de7f1fbe6b56605f66f11e34702ba9cbb1a188a597b82057aa447:
    family: pert
    a: 13.481394614103259
    b: 16.85174326762907
    c: 31.98827982702093
  896641997668ca9b629229a5bc817af5bce6c246392dc89aed14bf340e4371b2:
    family: pert
    a: 11.135103494453098
    b: 13.91887936806637
    c: 23.04363177600729
  15e4784e8caf8351dbe3bd5ea556a318d59775f03841d992b21d295bb5d88596:
    family: pert
    a: 13.479726183243361
    b: 16.8496577290542
    c: 24.12943900624719
  fdb37ea154692d608f08aa046714699f45861903b7f8a8a47e15ca6548bf59f0:
    family: pert
    a: 16.707893993752343
    b: 20.884867492190427
    c: 28.047315654082883
  1bc1e16e09ae43856509d48bf6b2f33e5bb5562e98f9fb67188fceff2e87b5ba:
    family: pert
    a: 11.945062478355304
    b: 14.931328097944128
    c: 22.001817128226577
  dd96a22232ddb6bbd59aa632df03297d37da89f1a55c9b1fb48246bda024dd66:
    family: pert
    a: 8.738037579219826
    b: 10.922546974024783
    c: 23.15468054892389
  693cc6f1c6b46023a39d6d75e01177a15988dcaad2a6d523504e48a4bef51594:
    family: pert
    a: 12.789650586115755
    b: 15.987063232644692
    c: 24.509855829878152
  73bc8af3a3f374f78a829def303090eea52915ac35b1ba54e171fd8f27ed9131:
    family: pert
    a: 13.104989915944458
    b: 16.381237394930572
    c: 25.942476701983857
  b91009aaf64b6bc5afc5e26bfeb6bcad12fd113ff1fc18faf345d83c7ce1dfa8:
    family: pert
    a: 21.932163923659353
    b: 27.41520490457419
    c: 33.973363439257426
  7bf8c85a337650611e042608bdadd480c8b150bd945271ee1242cc991c802a3e:
    family: pert
    a: 14.57017724652588
    b: 18.212721558157348
    c: 23.65327542442991
  3c0e540e2110723a6d5a4d5aadb6ec907c0424eedf1f49113575e33b6485a73c:
    family: pert
    a: 10.237289723573042
    b: 12.796612154466303
    c: 21.88888948822156
  34dba72027efb76b134a8f54cc842afb48be279c61db3997cf296f7146e069a1:
    family: pert
    a: 11.314782716277119
    b: 14.143478395346397
    c: 30.399402769571516
  78bd043a06902beda040104c653a145534f517f99924ecc257595f56740e8ada:
    family: pert
    a: 6.0976812222610395
    b: 7.622101527826299
    c: 17.035995050800484
  4de1e2b2b6589f00501d314d0aef69aede15d02871049c81daa1d680207c88a1:
    family: pert
    a: 10.758541890043531
    b: 13.448177362554414
    c: 23.022706193752033
  2b4af4a83e802b1689e5f61101ea759279f385f9fc5e83e84f8eff254e5d392e:
    family: pert
    a: 7.311261221037197
    b: 9.139076526296495
    c: 14.60121853087168
  580afe2d520dc8cbc2e468b08cf6f373983fb6364b52f2c0545a22d7db51f1ac:
    family: pert
    a: 20.71185811006625
    b: 25.88982263758281
    c: 44.43848385964056
  14c1b1c130f4ba9471e9dfad60e5ced3bcb9ab683424cd29dc0a5954e28c115d:
    family: pert
    a: 23.364294762570434
    b: 38.94049127095072
    c: 162.55500729054913
  d93ebf0902a094e8e5130ad2d870ccb03e413f9062f545bf4427a61f61517156:
    family: pert
    a: 24.69174631777984
    b: 41.15291052963307
    c: 186.72576823054666
  119a83190a81a90d8f4e4364c50cad62889c92df26f135b944f4d2f6d229ad82:
    family: pert
    a: 28.190956608366164
    b: 46.98492768061028
    c: 208.49609791483374
  46088f13d6de550ad043596643322f3abf82fc17dbc707a452d05fd545e4de89:
    family: pert
    a: 100.94115695445953
    b: 126.17644619307441
    c: 214.04066587308878
  1a12a419d8af4628dc7c733062135c651501f9d8a85d9fb9c3c0d794c1651957:
    family: pert
    a: 71.52945076143565
    b: 89.41181345179456
    c: 119.96770135388844
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
    distribution_hash: 6f5cd932d960655f40f037a132bd6a1ad90ff0dcc48ae0fe84639ba401a6c1d6
  - id: 2
    dedication:
      worker_2: 1.0
    distribution_hash: a315eac7f508b8dc9383095e37ed5099c4d9fc61787941186ee879f648b6ea7f
  - id: 3
    dedication:
      worker_3: 1.0
    distribution_hash: f8b9dcebfaa0139a5d30e3766f847ceea10fe78184ddd57cc114139fdbb0498b
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 1.0
    distribution_hash: 82cdddb9d7dddb8f075b91af1cff4128d344e94476a7f5fefc942b86d99cc7f5
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: d39edeb0eca80b623923d2bd60457bc7db9cf3a11fc7ca8d77e7d0071ed405f7
  - id: 3
    dedication:
      worker_6: 0.75
    distribution_hash: 2069657f8eb9f4dd6c9efe1af14cabe4fe31d89dd1da46f1ad37c4f87e494cbb
  - id: 4
    dedication:
      worker_4: 1.0
    distribution_hash: 529c3afca5304cf525d7baf5cf3b2ab07328e60041df6e5336ad8b07eba43bd6
  - id: 5
    dedication:
      worker_4: 0.75
    distribution_hash: 29dbd9c2bbc65a5f3726df42ddcc2da00828c2919fa08e070ea79a5dac79350e
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
    distribution_hash: 54ea7a1ced70733e67629f54d094c50443437003cdeab57212aba5e52e78a6da
  - id: 2
    dedication:
      worker_6: 1.0
    distribution_hash: 42687f591a6ceab5c632861f4d6b182dff729dbd1d246da747a0dc9190650046
  - id: 3
    dedication:
      worker_4: 1.0
    distribution_hash: 4f5e48cf2f7f856307a738b4add02829f7aacb9292c534061efeaab3ed8f6c88
  - id: 4
    dedication:
      worker_4: 0.75
    distribution_hash: f4fe4a5a66fcc67968e96d4570e0dcc6e88bdef7ce49a84c32a8113b4da1ba92
  - id: 5
    dedication:
      worker_5: 0.5
    distribution_hash: 1ba93e8d3b7e459745939843c6e10aec822347b6fb72020093b91219817cda5d
  - id: 6
    dedication:
      worker_5: 1.0
    distribution_hash: cf5072b9b1361ebeafbec17b40c485d12fd66736964167c4bb357aced37e98ad
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_4: 0.75
      worker_6: 0.75
    distribution_hash: ed33284dc711b8f387b2e5fe3ec0feb62dbfc33efff12a1f276142bc599f69c6
  - id: 2
    dedication:
      worker_3: 1.0
      worker_4: 0.5
      worker_6: 0.75
    distribution_hash: b133065dd02bb6c23cc1ca95b4a73dd46e0c767389c62bfc43d14f4726090ea1
  - id: 3
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 1432338eb1077d6fb77ca79afb764833940e07b951c8a6e868dfcae91ee2faf6
  - id: 4
    dedication:
      worker_5: 1.0
      worker_6: 1.0
      worker_4: 0.5
    distribution_hash: 59495c1cc2d45d351a19e0f53c060e42df758fca2adb45c62852f7527ead6692
  - id: 5
    dedication:
      worker_5: 1.0
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: f1c7b3e8ab54176895328d0a42b31d58fb48fb2527ec0fd1b984fa3de6e7a4df
  - id: 6
    dedication:
      worker_5: 0.75
      worker_6: 0.5
      worker_4: 1.0
    distribution_hash: 0fad8e378f874d58adaece17b44820f02dab63edd6059dcf309426e2fdad9a03
  - id: 7
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_5: 0.5
    distribution_hash: df2fd99fe41af2ef385a14fdb613711df7aa4848658fc9c70cd69baf7ecb6eb7
  - id: 8
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: c49ca91cf96e6fc6697174b13c5f6d9a6f2aaf3c07879926feef9147b5d55cb5
  - id: 9
    dedication:
      worker_4: 0.5
      worker_3: 0.75
      worker_5: 1.0
    distribution_hash: 4cef1dda78c22c42cc320ecd980153672314da68217fda8cafad21fd6d5c1a22
  - id: 10
    dedication:
      worker_5: 0.75
      worker_3: 0.75
      worker_6: 1.0
    distribution_hash: 4699631eb31d685f45189affa828cf8e80df3e1ab8076c3bca8e0a2b322979f8
  - id: 11
    dedication:
      worker_5: 0.75
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 853f20de0b878a1457140657d0e5bbe23df696f304597cde816ab5d75806a89f
  - id: 12
    dedication:
      worker_5: 1.0
      worker_3: 1.0
      worker_6: 0.5
    distribution_hash: e1cc7dbc8eb44d315fda25a036b56a39f9a69c4dd247d91b3203bf9eacfc634e
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_1: 1.0
    distribution_hash: 4d2de07b530847a4acf5158653cd1308b299baadb4a3a0c18bb84e607b6ba721
  - id: 2
    dedication:
      worker_3: 0.75
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: a73225a64b6efdf866315f63b7646d41db8bfb45121479fe2df9396addf9446b
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: aaecd419eee1fc6f46b07d1ced8cf329692ef981864300b507d35dd385ea5a1b
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_3: 1.0
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: e48a24530d2fdb1d077fdc33a1c34a0c115243edf1cd87f330123332216f0946
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 3c14b3a05e9e97762a42cf9b9f182417205ce9b98b7e70201e37e8bab94a2591
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_5: 0.5
      worker_6: 0.75
    distribution_hash: 2900b238c20a99506f7066005d7b9e6c697bcb90e559857041532b030e59b97a
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_6: 1.0
      worker_5: 0.5
    distribution_hash: d957327d04d7291e735e8f6093f17c719807adb3b525241215d57461c9109c47
  - id: 2
    dedication:
      worker_4: 1.0
      worker_6: 0.5
      worker_5: 1.0
    distribution_hash: c72e7b611b3cdbbb19751dd02e205e5c5c7402e5cb9ce88d656eef715cdce175
  - id: 3
    dedication:
      worker_4: 1.0
      worker_6: 0.5
      worker_5: 0.75
    distribution_hash: f669308edaf9fd205dfcd73ea7c51cbdac8decf75bf2062f749fb6b41335a2ba
  - id: 4
    dedication:
      worker_6: 1.0
      worker_1: 0.75
      worker_4: 0.75
    distribution_hash: ef42f7d4837cd4c1ab1731e461a6ffe9373d3818fde33de45a7513dc7b5eafe4
  - id: 5
    dedication:
      worker_6: 1.0
      worker_1: 0.5
      worker_4: 1.0
    distribution_hash: 014963a8a400eb6ddeed14410ced5c4c83e2cf05679542934198cfacbd2cf286
  - id: 6
    dedication:
      worker_6: 0.75
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: 7ccb161fd5f82d35c965cfa69d873aff4fefc886f579d21e067276d70897b9ba
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: 96321587a7d20924ee135d03772ad11896cb5bbc9865fd172610d3804bd4669c
  - id: 2
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: f67b132834a13d8e67f24ce68237ab6562166fc0500d1e6c5db36368754f8616
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: a82499af26b2d7357a2acfa6c6c2848514687aff8efcf2732359d4f0554058e2
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 0.5
      worker_6: 0.5
    distribution_hash: c4c57f4e789729b7291d1a5ec5a04902019063893c53301eea82ea420c3ac32d
  - id: 3
    dedication:
      worker_4: 1.0
      worker_1: 0.75
      worker_6: 0.75
    distribution_hash: da119311391f2031e483b1e640dfecfc61439a341a89986b23d51b36c736949d
  - id: 4
    dedication:
      worker_6: 0.5
      worker_5: 1.0
      worker_4: 1.0
    distribution_hash: 25fc8f7fa074e4a01b0a9daf6e699ee193969ca8924a81b4c7ed76934a59c768
  - id: 5
    dedication:
      worker_6: 1.0
      worker_5: 0.75
      worker_4: 0.75
    distribution_hash: 6e039f85dea4d52519482f42ee842905f99f6d9db1b2b9b1e87bc4e0a959dd54
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_6: 1.0
    distribution_hash: 7e124a066ad5e7f393c90e57c2227b05e9d549a5a4d9013457b7e4c3fa37fce2
  - id: 2
    dedication:
      worker_4: 1.0
      worker_6: 0.5
    distribution_hash: fe5b157346a51fb1969f532e08d281f5e85d55f6d887a133693d8206646b373b
  - id: 3
    dedication:
      worker_4: 1.0
      worker_6: 1.0
    distribution_hash: 4f790b897b4a81c93eb8c267d1485676b8f9ddcab362babb7841d7926eac44a8
  - id: 4
    dedication:
      worker_3: 1.0
      worker_6: 1.0
    distribution_hash: 68b3debf7129e7c7fa7ec0b31d933077e4abfd61b88a7a750a04346a8e11d5c1
  - id: 5
    dedication:
      worker_3: 0.75
      worker_6: 0.75
    distribution_hash: 4d2a1b35ef191f0de0e201490b90f80942398053ca6ad077ee419e04c1560006
  - id: 6
    dedication:
      worker_3: 0.5
      worker_5: 1.0
    distribution_hash: fcc1401ebf06dad3ac74f2adceacc09af451c67728be08fa68b03910aac2c636
  - id: 7
    dedication:
      worker_3: 1.0
      worker_5: 1.0
    distribution_hash: d39bab6bdc8e2c30c71593e998f6ed13f1eef58e49f71ac0e404d18ea52e9b89
  - id: 8
    dedication:
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 194c646ca146ce2a38daf4e780466177e6f87f8d297b3613adfd5319ed78c836
  - id: 9
    dedication:
      worker_3: 0.75
      worker_4: 0.5
    distribution_hash: 10b6cc5cc49d2de6457040d768e23528a0bea99b24f8a83a8c6cbf0cbd7daa7c
  - id: 10
    dedication:
      worker_3: 0.75
      worker_4: 1.0
    distribution_hash: bafe7e2e978283279c6fc7a82b3df46b7e977cab4c4f2f8df1a035933f346de4
  - id: 11
    dedication:
      worker_5: 1.0
      worker_6: 0.75
    distribution_hash: 433e507fa64f8326c6b41d340aea7bd560282fce42536ddf43d228e4a12896ae
  - id: 12
    dedication:
      worker_5: 0.75
      worker_6: 0.75
    distribution_hash: 1756fe49b53f83f8a83b8c364dec966b354b22f33f4242caa181e55767ec4327
  - id: 13
    dedication:
      worker_5: 1.0
      worker_6: 1.0
    distribution_hash: 95abd106bab0c81e7d8c623b09cc62295e7363e97d5b6cc44ef32f99e0b7bd47
  - id: 14
    dedication:
      worker_4: 1.0
      worker_5: 1.0
    distribution_hash: 710f5194c638c546b6490ff19445f68cab3f9f3860d955891f325e3cc02c7721
  - id: 15
    dedication:
      worker_4: 0.75
      worker_5: 0.75
    distribution_hash: 6f6f4f70c12a572d640d5c4e3f8d8cd78be4cbb3806150becc9e49d60655c208
  - id: 16
    dedication:
      worker_4: 0.5
      worker_5: 0.5
    distribution_hash: dfe7593309a37c27fe7710208fc527ff0dc6b97755f95efab0f5b5d6648031b8
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.25
    distribution_hash: c4ff61e6f7d3604d1ade2927af30a9fa74e768ae76bfbe8251a36274e9d00325
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
    distribution_hash: 2f27c1a23293a0b9c5651ee5aa9e659b17f96008c2b9c4f9a25a007483673c42
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 4e968189a05ceed6617cd4e28516a51d9f977de4753b3b04438ac1151cc781f3
  - id: 3
    dedication:
      worker_1: 1.0
    distribution_hash: 2ae3417fa09d048269d6c221d3a2a7e88ca72f20f90f558c2873fbbe0355f4f7
  - id: 4
    dedication:
      worker_1: 0.75
    distribution_hash: ad16798f772a3345a02da4b126b3901d08e54cfc5d755be7f61913bc0ba1d2f7
  - id: 5
    dedication:
      worker_2: 1.0
    distribution_hash: 7115fcdc38d3ae8eb7d1d72c6de538e743e5443feee532f6d77ab9c1e6aee8ed
  - id: 6
    dedication:
      worker_2: 0.5
    distribution_hash: 38a8e8a82dbe724257f39943a96e2fd43b221cfc7ec872bc15f6d9b2ef379e82
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
    distribution_hash: 82a10d752df6e59b58e98cbf58f1938edaedbc2799e0ec9785461ed8c8127f91
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: acfac055e7cb011771a3a21b997f126c6c8eb80cc8f5770cd2ef7f2d6696294f
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: 12e4375370acad9eb6eec475d42a791c5cca8314d1265a4029a69438b530edec
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
    distribution_hash: 2bfb74d710d9655780cc170ebda242285cea6d4b890f071d6d7f5b6ee295b741
  - id: 2
    dedication:
      worker_4: 0.75
    distribution_hash: 6cb6740ac4f6f5f41485dd3883ef4f50acec0f8dd0cf085d6651c871150c2cf6
  - id: 3
    dedication:
      worker_4: 0.5
    distribution_hash: c819ea4c288084615c308afa742358e50e86ffcd9da774c802cff655f82ed1c5
  - id: 4
    dedication:
      worker_1: 0.5
    distribution_hash: 3ef9d950d0c678ab54e98d6414fb63693237f10c2b51fa9c06d81a44886908f7
  - id: 5
    dedication:
      worker_1: 1.0
    distribution_hash: 9af7358234b5611680f0f07a1d509fb89fbf0a5828522ef30361eeaa1e440683
  - id: 6
    dedication:
      worker_6: 1.0
    distribution_hash: 15808ee857dc95d6de9092db84a5a3894c8efb0a8c8c3dba78177fdccf45ab8c
  - id: 7
    dedication:
      worker_6: 0.5
    distribution_hash: 140fbe78f4da09ef5f5378d72a726efa5571e5ee8ee6ae2d6ec939420f5883c9
  - id: 8
    dedication:
      worker_6: 0.75
    distribution_hash: e91a990e82c9e772c46ba2632f66a131cdaa5d1a4a72caef92cdaa66a9453334
  - id: 9
    dedication:
      worker_5: 1.0
    distribution_hash: 5dc150d6d8adc2e3715297e6d3ddc0bdf0e0628dc98891d88da48052a9ce88c6
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 0411633e4a631e75a18d51fc606cd42030acee31dace453384962f7aa81f36da
  - id: 2
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: 32de936d84ce07bbdb9de3866da9101603e5ffc200000bb95880315ad96455d1
  - id: 3
    dedication:
      worker_2: 0.75
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: ac24b46ce0bbaa8f149d577e275b35cf2c4d30a8346774fc68129f8a6513e9ba
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_1: 0.75
      worker_7: 0.25
    distribution_hash: c9f2af2e2dd3dbc0bb99ed94e056b1fa42bebaff6341c4ea93a60076278d16b3
  - id: 2
    dedication:
      worker_3: 1.0
      worker_1: 0.5
      worker_7: 0.5
    distribution_hash: af32257c0cd46c22611292ed68cc20304b278fc2925ab73af9bbe86bec10bf31
  - id: 3
    dedication:
      worker_3: 0.5
      worker_1: 0.75
      worker_7: 0.25
    distribution_hash: cd86ff081909a7262fd49598135894e373865caedbc15a92f11f90e6f8292fe5
  - id: 4
    dedication:
      worker_3: 1.0
      worker_2: 0.5
      worker_7: 0.25
    distribution_hash: 698b7b19f038fbb2e0a9913ff9f6577c83babad7ed3d97c9cd953cc47171f780
  - id: 5
    dedication:
      worker_3: 0.75
      worker_2: 0.75
      worker_7: 0.25
    distribution_hash: 6532a4237399eb7fae81a4151081a9bfabd77955aad786080fc97e6402c83ed5
  - id: 6
    dedication:
      worker_2: 0.75
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: b387684d44c0075e884be902a7f430112b4a9c11716d4e75e54e79d4ab4affd2
  - id: 7
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_7: 0.5
    distribution_hash: 7d582d8bd8807d244971887847136f3c8895600ddea7627c730a3ea839af2635
  - id: 8
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_7: 0.25
    distribution_hash: d031a713ad8c87fd414716c45d067feb53171104bbda319ad13f2b40d6f05b68
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_6: 0.75
      worker_1: 0.75
      worker_4: 0.75
      worker_7: 0.5
    distribution_hash: 89eb5a3723653589e705a17788fa86ad78b01a2987037fbf6882d6f5dcba735e
  - id: 2
    dedication:
      worker_6: 1.0
      worker_1: 1.0
      worker_4: 0.5
      worker_7: 0.25
    distribution_hash: 6eb2f8b0465fd31489f56a420f27a0c09da1b5796a4204893fe2c6737bea8871
  - id: 3
    dedication:
      worker_6: 0.75
      worker_1: 1.0
      worker_4: 1.0
      worker_7: 0.5
    distribution_hash: f6e1003473524fba43d5d9904d4dd145f7d4fa6e89f130d6f7fa84299f8f2a4f
  - id: 4
    dedication:
      worker_6: 1.0
      worker_4: 1.0
      worker_5: 0.75
      worker_7: 0.25
    distribution_hash: a29d6c5969df06429c98738f20c0586b5079699371da3576bada2f5403b78574
  - id: 5
    dedication:
      worker_6: 1.0
      worker_4: 1.0
      worker_5: 1.0
      worker_7: 0.25
    distribution_hash: 93723a41b695e8ff8820e9542c41d685713b18424d218cb664469d0f5e5d6944
  - id: 6
    dedication:
      worker_6: 1.0
      worker_4: 1.0
      worker_5: 0.5
      worker_7: 0.25
    distribution_hash: b8566cf78099a97a49e69c3ce0c14c85c6e55c0c480ed4764295680ba723b376
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: 6b9c01c1e4606f90435bf656c8e796d9168905ced8873ea31e5fae2042f22617
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: b191da6ce1e14a14c568f232be0d90dcfadf69c5041ffdc6139b7e8ebc35a76d
  - id: 3
    dedication:
      worker_3: 1.0
    distribution_hash: ecc1cc686ecf3b92556fb5f5d6cb06690c7fb526f87ac446937b85c7ad91fa1c
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
      worker_6: 0.75
      worker_5: 1.0
      worker_3: 0.75
    distribution_hash: 8febcd7edaa055b6d0b594e4e431f94eada8d3e254b4ab962fa9fd121112bc9b
  - id: 2
    dedication:
      worker_4: 1.0
      worker_6: 0.5
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: 6e704b46e4806a93f5621ef1b18d42af293a2ad2f22b45ab7055b8272d0e6f99
  - id: 3
    dedication:
      worker_4: 0.75
      worker_6: 0.5
      worker_5: 1.0
      worker_3: 1.0
    distribution_hash: 4d893dd7cad3179f9c56c4bf1ffe8fe9b8a819c91049af0bf157d665396935aa
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.25
    distribution_hash: 8c0e11c377460133ab0c114f45843f1f0e432fea703c7dde8b70330794cb161a
  - id: 2
    dedication:
      worker_5: 0.5
    distribution_hash: 5558fc3422ff5362f58b5933dddfed378f24d79c68f7d28c536a9579880ab82b
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 1faf476f55a87787b1a2f6793b5a8ef792bf03bed0812f406d9ab5b05345d4c4
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 1447e25054a6d936b7d746c2151d0bae521206b82283ed5c6f701942ec1b3da5
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 8aa7ec320de026845e28824e8421329aa4e8e654568aa9a9a509f643d429abf8
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_3: 0.75
    distribution_hash: 188020d316873fe0e3f1daa3b9a921efa260a14847ce5c5760cf58a02ea05f0a
  - id: 2
    dedication:
      worker_2: 1.0
      worker_3: 0.5
    distribution_hash: cae7cb50bfe7b7818f21a5167352c849b5e25f29520fbc95ea016eca9e574a4a
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: da8ac84c0960cc0b7a4d53f0e63adca4a5da89b92b1b00df74b09e7f25bd1845
  - id: 4
    dedication:
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: c9e11e0f8213aeb3631692ba645e4cfa208ae33571b038426d247455219da9d4
  - id: 5
    dedication:
      worker_3: 0.5
      worker_1: 0.5
    distribution_hash: 0c6a75175264f7e6ef014c9991367d90728efd2baab12c9cdfee8e364bc09494
  - id: 6
    dedication:
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 0a573c4ea1c4d91caedb66494ed8cc8abf3d2e188b468cc9d4db816e689e87b0
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.5
      worker_1: 0.5
      worker_6: 1.0
      worker_4: 0.75
    distribution_hash: 8e9aa556b72483bd712e5d07caa754d2e94adf5bed35bc08ddbd54d5c35b58da
  - id: 2
    dedication:
      worker_5: 0.5
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 85286291c575c1908e653c65b5482da4ca571d4a995c37efb7a50d7458e37cee
  - id: 3
    dedication:
      worker_5: 0.75
      worker_1: 1.0
      worker_6: 1.0
      worker_4: 1.0
    distribution_hash: 3cdf926c54d9889eb2dd28f6707d8fc5329058153569246009cb3b21232c57dd
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_7: 0.5
    distribution_hash: 0af8cf63a0a2abcf974041c4fa8cbe7182b440cbeb5f06d6b30009ca4550c585
  - id: 2
    dedication:
      worker_3: 0.5
      worker_7: 0.25
    distribution_hash: fef4a8f8a316900391e9ffd4d0628ead70cd2fa871111f93ed62194c3d964251
  - id: 3
    dedication:
      worker_6: 1.0
      worker_7: 0.25
    distribution_hash: 79ac5b476774d841186fc792ac964bc658b90e2a6b3a659e5de87d1760ed5cf9
  - id: 4
    dedication:
      worker_6: 0.75
      worker_7: 0.5
    distribution_hash: 6603c9ab8e0671a1d5bde218444e311c5707162098bb0d741cea781c4b420d84
  - id: 5
    dedication:
      worker_6: 0.5
      worker_7: 0.5
    distribution_hash: 75d8fa0b5f315464a8ef13f5d925d7228e258417023ec5a24cef64ebfa83f181
  - id: 6
    dedication:
      worker_4: 1.0
      worker_7: 0.25
    distribution_hash: 908436975e16334dfedfdd5654f6b023d89bbe3d097ea7a738659e75cac36b32
  - id: 7
    dedication:
      worker_5: 0.5
      worker_7: 0.25
    distribution_hash: 2d6ca5419c3fe118c385c0a03a69b1c3a13cc5647334e4bba85711565f940bc9
  - id: 8
    dedication:
      worker_5: 0.75
      worker_7: 0.5
    distribution_hash: 6233124b99ba7889b73da9c1e14df7de7854040c82c25fb2297aead01b9df9d4
  - id: 9
    dedication:
      worker_5: 0.75
      worker_7: 0.25
    distribution_hash: a5b9c878e7c3e95282fa4f420198a9935ce33dffb9e8362abf0d2ea17270c7d9
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.25
    distribution_hash: dd1333a8dbff6e0035c2928cd23e9031f06c4d18633a1f7b801e000670e2429e
  - id: 2
    dedication:
      worker_5: 0.5
    distribution_hash: a1cf236c8176fa2e95dbe6bd36a341acdfdb3991c183d48e197250a441af521f
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 8ca42fb61773df3b04ac7384fe920f02521249a3a917d59f56949bfe45a337a4
  - id: 2
    dedication:
      worker_4: 0.5
      worker_1: 1.0
    distribution_hash: 48dbf526169de7f1fbe6b56605f66f11e34702ba9cbb1a188a597b82057aa447
  - id: 3
    dedication:
      worker_6: 1.0
      worker_5: 0.75
    distribution_hash: 896641997668ca9b629229a5bc817af5bce6c246392dc89aed14bf340e4371b2
  - id: 4
    dedication:
      worker_6: 0.75
      worker_5: 1.0
    distribution_hash: 15e4784e8caf8351dbe3bd5ea556a318d59775f03841d992b21d295bb5d88596
  - id: 5
    dedication:
      worker_4: 0.75
      worker_5: 0.5
    distribution_hash: fdb37ea154692d608f08aa046714699f45861903b7f8a8a47e15ca6548bf59f0
  - id: 6
    dedication:
      worker_4: 0.75
      worker_5: 1.0
    distribution_hash: 1bc1e16e09ae43856509d48bf6b2f33e5bb5562e98f9fb67188fceff2e87b5ba
  - id: 7
    dedication:
      worker_4: 1.0
      worker_5: 0.75
    distribution_hash: dd96a22232ddb6bbd59aa632df03297d37da89f1a55c9b1fb48246bda024dd66
  - id: 8
    dedication:
      worker_1: 1.0
      worker_6: 0.75
    distribution_hash: 693cc6f1c6b46023a39d6d75e01177a15988dcaad2a6d523504e48a4bef51594
  - id: 9
    dedication:
      worker_1: 0.75
      worker_6: 1.0
    distribution_hash: 73bc8af3a3f374f78a829def303090eea52915ac35b1ba54e171fd8f27ed9131
  - id: 10
    dedication:
      worker_1: 0.75
      worker_6: 0.5
    distribution_hash: b91009aaf64b6bc5afc5e26bfeb6bcad12fd113ff1fc18faf345d83c7ce1dfa8
  - id: 11
    dedication:
      worker_6: 0.5
      worker_4: 1.0
    distribution_hash: 7bf8c85a337650611e042608bdadd480c8b150bd945271ee1242cc991c802a3e
  - id: 12
    dedication:
      worker_6: 0.75
      worker_4: 1.0
    distribution_hash: 3c0e540e2110723a6d5a4d5aadb6ec907c0424eedf1f49113575e33b6485a73c
  - id: 13
    dedication:
      worker_6: 0.5
      worker_4: 0.75
    distribution_hash: 34dba72027efb76b134a8f54cc842afb48be279c61db3997cf296f7146e069a1
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_6: 1.0
      worker_1: 0.75
      worker_5: 0.75
    distribution_hash: 78bd043a06902beda040104c653a145534f517f99924ecc257595f56740e8ada
  - id: 2
    dedication:
      worker_4: 0.5
      worker_6: 0.5
      worker_1: 0.75
      worker_5: 0.75
    distribution_hash: 4de1e2b2b6589f00501d314d0aef69aede15d02871049c81daa1d680207c88a1
  - id: 3
    dedication:
      worker_4: 1.0
      worker_6: 1.0
      worker_1: 0.75
      worker_5: 1.0
    distribution_hash: 2b4af4a83e802b1689e5f61101ea759279f385f9fc5e83e84f8eff254e5d392e
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 580afe2d520dc8cbc2e468b08cf6f373983fb6364b52f2c0545a22d7db51f1ac
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: 14c1b1c130f4ba9471e9dfad60e5ced3bcb9ab683424cd29dc0a5954e28c115d
  - id: 2
    dedication:
      worker_2: 0.75
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: d93ebf0902a094e8e5130ad2d870ccb03e413f9062f545bf4427a61f61517156
  - id: 3
    dedication:
      worker_2: 0.75
      worker_1: 0.5
      worker_3: 1.0
    distribution_hash: 119a83190a81a90d8f4e4364c50cad62889c92df26f135b944f4d2f6d229ad82
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_5: 0.25
    distribution_hash: 46088f13d6de550ad043596643322f3abf82fc17dbc707a452d05fd545e4de89
  - id: 2
    dedication:
      worker_5: 0.5
    distribution_hash: 1a12a419d8af4628dc7c733062135c651501f9d8a85d9fb9c3c0d794c1651957
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
  - task_11
- - task_1
  - task_12
- - task_1
  - task_28
- - task_1
  - task_29
- - task_1
  - task_30
- - task_1
  - task_31
- - task_2
  - task_9
- - task_2
  - task_13
- - task_2
  - task_15
- - task_2
  - task_16
- - task_2
  - task_17
- - task_2
  - task_18
- - task_2
  - task_20
- - task_2
  - task_27
- - task_3
  - task_7
- - task_3
  - task_15
- - task_3
  - task_16
- - task_3
  - task_24
- - task_4
  - task_15
- - task_4
  - task_16
- - task_4
  - task_18
- - task_4
  - task_20
- - task_4
  - task_21
- - task_4
  - task_23
- - task_4
  - task_24
- - task_5
  - task_14
- - task_5
  - task_17
- - task_5
  - task_21
- - task_5
  - task_22
- - task_5
  - task_25
- - task_5
  - task_26
- - task_6
  - task_10
- - task_6
  - task_14
- - task_6
  - task_16
- - task_6
  - task_19
- - task_7
  - task_17
- - task_8
  - task_16
- - task_8
  - task_17
- - task_8
  - task_18
- - task_9
  - task_14
- - task_10
  - task_13
- - task_11
  - task_15
- - task_28
  - task_22
- - task_2
  - task_23
- - task_6
  - task_18
- - task_20
  - task_18
- - task_27
  - task_17
- - task_28
  - task_13
- - task_20
  - task_13
- - task_4
  - task_26
- - task_27
  - task_13
- - task_11
  - task_13
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
- - task_29
  - task_32
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 536
validation:
  project_key: 3dddc7ce705303c2e780947bb3eaa890aa45dca864ebab95ddf0d41a833fa8f2
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 72 days; worst-case serial bound: 1952 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
