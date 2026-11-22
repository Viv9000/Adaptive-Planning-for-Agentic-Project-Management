# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_8
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
  relaxed_constraints: 5
  rewired_edges: 11
  departments: 1
  quality:
  - worker_3
  safety_skill: 1
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 3
  barred_pairs: 6
  incompatible_pairs: 0
  edges: 66
n_workers: 5
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 545
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
  c6e6ae83b24ec19bfb77ad3e4518473166bcb810fe3fa3c9578f82e4c254479a:
    family: pert
    a: 20.572400450144645
    b: 29.389143500206636
    c: 54.83209893979783
  1607dc5d09d669cc9637573e3c7b5d7af060d9584fd412f999b7c55b3469bd09:
    family: pert
    a: 22.182554336649112
    b: 31.689363338070162
    c: 68.06316287325446
  bfaa90d221269779b03e3fddab55e631572a615360b241cf986b05adba207782:
    family: pert
    a: 23.727122621247688
    b: 33.89588945892527
    c: 64.23488562928144
  604c52251dedebd33561f5dbd7fb610539f0eb280104090c9ef2cc931fc6e70e:
    family: pert
    a: 35.05547633935458
    b: 50.079251913363684
    c: 89.93862004330138
  25e4d22540b94d0b03032cbcbc29af66124f428f8ba1966258a2ba6b6999d60d:
    family: pert
    a: 38.87019566763986
    b: 55.52885095377123
    c: 112.7618684490415
  94f056e56242dda06acc56365e175129e2f2fa0be39109d0e7d9d4f89b6cb112:
    family: pert
    a: 21.627124366139512
    b: 30.895891951627878
    c: 51.9406469950173
  473baf4dd4cbc0b4208841bf8488710e0ffcc6851e85e45aa435d601070550d7:
    family: pert
    a: 22.589832042877866
    b: 32.271188632682666
    c: 53.67359306162789
  8c10e9584d29101e1dfeb17922fc328f09963ee70ab1950457fc6f695e2fe02f:
    family: pert
    a: 12.214962498399496
    b: 17.449946426284995
    c: 61.61613954637499
  d25ef1e63bfae4f03cf2c9832512f01b1bbd22397bbe86ae70bd9026782c6f3a:
    family: pert
    a: 22.437017860141808
    b: 32.05288265734544
    c: 47.89893122377902
  0de34ce55bfc4eec5e4845789fd92999d934b837d229723a8b80afb4a47ce8aa:
    family: pert
    a: 25.043273719457652
    b: 35.77610531351093
    c: 68.2160175022581
  3114ff8326c5c6fadf8f916757716fbe5d43f2cc04963ebd42bc2f0482f2e99a:
    family: pert
    a: 27.331638319275942
    b: 39.045197598965636
    c: 83.14989417629506
  94084d0bdfcf3df3bb1eea9a284869cd5d2d1a4294035d399233c38111b330e0:
    family: pert
    a: 14.015844385700742
    b: 20.022634836715348
    c: 82.38604159009846
  5ad5496660a7b6a073b69968a79204cdb11869676d1b891b6f75b3c3bf5b3961:
    family: pert
    a: 17.75154596723453
    b: 25.359351381763616
    c: 65.09041777053385
  cad23e890e072fb9708c3eb689b6024f3675777b76ee65fc1b1ddc7f20d934c9:
    family: pert
    a: 17.585275449668984
    b: 25.12182207095569
    c: 62.7405245052263
  33a03083a2d7825a5a7ce1a3953d14dbac8d7f7112bd79744c4ee4de91707239:
    family: pert
    a: 31.448515026435935
    b: 44.926450037765626
    c: 74.74227672927204
  74db2303537dc27b047dd367720e9823af724e04cc3394e263dc98f119e3f3da:
    family: pert
    a: 21.047533971716053
    b: 30.067905673880077
    c: 62.65743221178894
  c340373ffff7dc620c2736f8fffd992787cb3d2a683f0caea0077b500e80f7be:
    family: pert
    a: 13.683873207003327
    b: 19.548390295719038
    c: 83.63542245102633
  ee40e117e3125cf02f92ad5805632c2a802f71d3d729fe855e3c08efc10fa46e:
    family: pert
    a: 20.61793930978331
    b: 29.454199013976158
    c: 60.58575026160075
  87569193420890595b99badd24a69ba902c0851bae1a44b989ce33ae624d3be0:
    family: pert
    a: 18.4644815217213
    b: 26.377830745316142
    c: 63.684281390008344
  8d3b7c09f61cdb69ce30974bd8ebf5a45d43567e098d5776e1b931872f817d6c:
    family: pert
    a: 16.312246868216082
    b: 23.30320981173726
    c: 45.241662797933536
  0aadc7a5fd91d2c3f7a03375faddf63282ba849b64feaee0ba3383ec7c62f1e3:
    family: pert
    a: 20.093661781253605
    b: 33.489436302089345
    c: 86.02877078678995
  03263a5e73a77c535813f79aa8ff9042fce27744a2e6ea160a6e5660ab705071:
    family: pert
    a: 3.101724393422246
    b: 3.877155491777807
    c: 6.310818220022386
  5c855cc5666cd6ba41c52957cfc4f3ba2ff416e58ecb69d1f1acf28b22cbecad:
    family: pert
    a: 7.053073176298948
    b: 8.816341470373684
    c: 12.36171873944731
  59ac74b8173c27ec8b276d7f562add0798bbe8df8372423786320548a60615d7:
    family: pert
    a: 4.416942324731036
    b: 5.521177905913795
    c: 9.027265866377103
  d1159506c7b49625816a2d6c12890686d9931422b20752fe6ae813d6d0946c49:
    family: pert
    a: 7.610457010022078
    b: 9.513071262527596
    c: 11.68231868391988
  35cbaa28be131fc3a54ef95d04a8e4a10eab64a3b7102172025f7c0d3f371003:
    family: pert
    a: 4.106812568647531
    b: 5.133515710809414
    c: 8.422012138821605
  6f69c23e03764f4f2d317093d220206776f8168a4d1c8de95ccd68b126c4f884:
    family: pert
    a: 4.999392785318008
    b: 6.24924098164751
    c: 13.686765820005805
  db2add4e62d6ea4de754fc16988f8a8d5aa6a8ab8edf12e3997d96a82c446994:
    family: pert
    a: 6.79117179639514
    b: 8.488964745493925
    c: 13.479103168773719
  5d08662f7d160919502339ca76d7264a9a2f3c897f11b772f9a7752bb3af24f7:
    family: pert
    a: 5.018899654041495
    b: 6.2736245675518685
    c: 7.435591376037797
  916771230f1efd1402feec432af2212a8794729f9481b31c40c9e5fde5e2237c:
    family: pert
    a: 3.870428708465078
    b: 4.8380358855813475
    c: 8.987985066144837
  d588db445cb2d65b201f64496380c7accd5c5cf0fe0d2ff2c16b4a9a59882ac7:
    family: pert
    a: 35.09858825983437
    b: 43.873235324792965
    c: 72.13214812080314
  05c8ad48b854d0f4cac66faccbc5200c2fa8d465b008ec9c310024ad925825c3:
    family: pert
    a: 41.517288509081574
    b: 51.896610636351966
    c: 75.26702439759566
  7aeb73314ceb1fe2f0ae352a46b42fddb18392c9e24ce7eb94cee8c1658c37ad:
    family: pert
    a: 60.61785927132412
    b: 75.77232408915515
    c: 95.92854550368519
  f703281721a0c6a55951882bbe1d0c0cd3eed39c7745a5f9dba4f2fc6809a2f6:
    family: pert
    a: 30.854522106333942
    b: 38.568152632917425
    c: 116.01562113546689
  1dad2845d1eab7e71e6edeac8c4b8b0bcd5e539d10cf521763fa91d36344db1b:
    family: pert
    a: 25.86960361661813
    b: 32.33700452077266
    c: 58.46339303885585
  e5244b72ad3f577078ae2b9cb1a67c5c2ca4b0551eb04be5cacb1c0f1ea94ce6:
    family: pert
    a: 29.455907063935275
    b: 36.81988382991909
    c: 69.09223197687353
  4722c0039c24386c85cd9176c7d0efa379990975ed70fa3a067c6bc9232397fd:
    family: pert
    a: 57.03288807752449
    b: 71.29111009690561
    c: 100.60925626549874
  219fb2dfdb33db131ef907754dd811030fbc58c2f3de78259f24c7045dd88924:
    family: pert
    a: 38.61347094614934
    b: 48.266838682686675
    c: 69.11135713592871
  953f3cb44b068f8f2e45acee3467cc7a95e8c88528f0ec96c7e6577013e3d98a:
    family: pert
    a: 36.51570981913039
    b: 45.64463727391299
    c: 72.02397848216265
  3405af538d369e49d0b39cb78e120b269ca5caecc55932f7a7813f6981ac4d37:
    family: pert
    a: 56.787905481672766
    b: 70.98488185209095
    c: 95.69971792957999
  22a4e89a719fda42e16dc3c4b0487c83a442546330b8d3633bc41518372fb49c:
    family: pert
    a: 46.573047489687546
    b: 58.21630936210943
    c: 103.94658961274152
  868d56445dadf19093a1b7cbd255bb978c2c0641dbadd2a659edb37dc1cb89e7:
    family: pert
    a: 52.62695016191975
    b: 65.78368770239969
    c: 83.05562193153757
  7232711640b8be2ad39dba6550612c6867c70478280cf39e6021dde8ff64369c:
    family: pert
    a: 60.29063374686686
    b: 86.12947678123838
    c: 205.07520308789142
  94b1e4f820730954cbf2ab72cc523bf8de6d28732528d93e205b3083fa48d37a:
    family: pert
    a: 30.224415596815376
    b: 43.17773656687911
    c: 102.02091179067293
  d332bb3a4c41a092449002f4cd5959d1c4bce40bcae3730f714ee96a97a58951:
    family: pert
    a: 16.301191308525205
    b: 27.168652180875345
    c: 128.4622519851892
  e2299b0e263bdc0705754d71906a362345495c5e12043a7921754ac91cb913df:
    family: pert
    a: 23.964358977720085
    b: 39.94059829620014
    c: 87.3982285837769
  6cfb5c146b771af2f89a900d2e4c339894913d09e398616505ba0dc91fa24576:
    family: pert
    a: 16.12973244782737
    b: 26.882887413045616
    c: 121.11587460123603
  2cfe38a6da8fb2eb687f8c49f8e272b2d19a68f869b528a0d4a7ae01819c4d13:
    family: pert
    a: 25.51969123236907
    b: 42.53281872061512
    c: 159.63214045082802
  e38060ed7622bbdf11aa47a8f1f009730a162ed24ed9cc7e11c7fba635bd6b0a:
    family: pert
    a: 29.991245060595283
    b: 49.98540843432547
    c: 206.4459166589684
  aa90a6bffa2d481dfbecc02046a1d4c2799dfb0a8b473cdf62e373453bda7b59:
    family: pert
    a: 26.544093719761417
    b: 44.24015619960236
    c: 144.94013188710764
  b3ac00efa47c18aa6e22702f43c6a1b7ad351625da0d0412c225acbc409a348c:
    family: pert
    a: 17.37584418680789
    b: 28.959740311346483
    c: 133.2435809114349
  d66559295baebf7015ed2d2801ed423caf54823301a951fff262201acb49e428:
    family: pert
    a: 27.32987371192544
    b: 45.54978951987574
    c: 177.2988597995887
  ddb3108def1348f4ccc165553d97f5de029652112bec3f7ba377c0c9abc30f57:
    family: pert
    a: 9.469998070778505
    b: 13.528568672540723
    c: 19.207714804316975
  171c80c983420530d14128a175826847f9cf400913fb06f682c4c0ea637557f5:
    family: pert
    a: 7.354305185238026
    b: 10.506150264625752
    c: 23.7616995731568
  9bee15a528b0c3be0b80988d84cc5ec131bb6777d2ebc9def344053eaf8254e4:
    family: pert
    a: 5.697777893423862
    b: 8.139682704891232
    c: 18.997387777490875
  421a1ca63c3d603249285116f1f960737dcad515f762603ae34d4cd3cc7ceb48:
    family: pert
    a: 6.388173450050757
    b: 9.125962071501082
    c: 26.961767903254398
  ee74a3f21a3c95f7c4fd0520174cf7097eeb307c945dfa433cab32a281a0ff71:
    family: pert
    a: 5.112369231007156
    b: 7.303384615724508
    c: 18.230278413431247
  53791f96b55bcef9dedd8ca81894c95d392dcedb0407b2f36bfc646df7aec7f5:
    family: pert
    a: 9.083273289154167
    b: 12.97610469879167
    c: 18.490044063177656
  3717a4060b69122a0f5a0851649d316fe66426f6b407070b9e1ddccdb2f8d8c9:
    family: pert
    a: 7.097294958673981
    b: 10.138992798105688
    c: 24.091186930764877
  d0f4da0ce4dbf208fd1df6795d96d933f6d2c55be7d99a9142d60989fd4624e9:
    family: pert
    a: 7.530441913652261
    b: 10.757774162360374
    c: 23.586240503902314
  23e2526c94689e1c1886c5123898ffed187c22ca4a4000b4d59f2ddf32977b75:
    family: pert
    a: 6.103925739381357
    b: 8.71989391340194
    c: 46.511556504721966
  ab695ad1a671f88d3d18fed9b0beac6b776a8064bde4748b1447c0f7b0be3ae2:
    family: pert
    a: 5.241663730230632
    b: 7.488091043186619
    c: 26.06026867010062
  5ff0545526e8f625d5b3cf436cf9d78118a9f7f56c6bd2c59a1b18f8e5273f3c:
    family: pert
    a: 6.541749412983991
    b: 9.345356304262845
    c: 23.70143450550952
  fd822f3ac2ea7e6e3f86e19a69598b31f2da755e02e46e0ac5144304a48ebe92:
    family: pert
    a: 3.423688661100032
    b: 4.890983801571474
    c: 7.515782937660545
  6608d77e21da2d8182ebee82b63814842921fae1350f8d8d123974b57bb16ee1:
    family: pert
    a: 19.712090847544438
    b: 24.640113559430546
    c: 31.193459168347665
  c011a8b3313d71644a09f34c560d1a32c02e4f097ddb712de967620d22b7e1bc:
    family: pert
    a: 10.928805164289168
    b: 13.66100645536146
    c: 34.130476339271674
  7d58b436807bea728a44ffb2676952daa5469d9d26cce49750dac4d76094bfa9:
    family: pert
    a: 10.175432812282587
    b: 16.959054687137645
    c: 77.14977601225405
  771b105133a9d26c6abdfd38fa31e8830366f37d21e83b0228370007c9b9c37e:
    family: pert
    a: 9.359507947086122
    b: 15.599179911810204
    c: 37.8185075966868
  cb3bab56da2b80db7d88e5ef5ec4e1c528cfb9974c1da2115a9e290b99e68374:
    family: pert
    a: 8.048421725364383
    b: 13.41403620894064
    c: 51.63296740870782
  313427b463e6b9b4a79e44f6b7851ad7520f8c749a4daa801066364f2be1a27b:
    family: pert
    a: 10.295511558386869
    b: 17.15918593064478
    c: 59.656500694152314
  a66d494a0f7cb44a88d827ea3d88e920ad635de482411e1d72a9f0a668524dca:
    family: pert
    a: 17.692092597476975
    b: 29.486820995794957
    c: 96.43887329078821
  6d515ab53af963dbced2b885dc6f7800ae0031da6db08dfdb10fa2df6e3031d4:
    family: pert
    a: 9.33285282352175
    b: 15.554754705869584
    c: 85.76462087145467
  9c33d23863a847e4031eadce2557e669e6cda4cc9bc9cea38701b00908f2b36a:
    family: pert
    a: 16.52375729734529
    b: 27.539595495575487
    c: 93.9583605809729
  841cdf79141cbdbc09cd275c3c749dbfa1d192283f536cf7a1aac74ad0a3d4ee:
    family: pert
    a: 13.473252196216547
    b: 22.45542032702758
    c: 61.65517181736229
  33a0af9be61a7e9936eafc0a26809782d14b89fce49d44a07183b17bc5ad75fb:
    family: pert
    a: 24.878932681842485
    b: 41.46488780307081
    c: 119.97974034258371
  21d82d37dc91e22fa9a4b1111c283c11efd062bc9d56abe3bb3db9acd32ee7e5:
    family: pert
    a: 3.461347008383131
    b: 4.326683760478914
    c: 6.197570480319907
  72abda2ea0d97f9bb88ac4fabef5df67bb8fdfa6a1b199a3e7f016ae5125b152:
    family: pert
    a: 30.521759523671392
    b: 38.15219940458924
    c: 73.37962234980338
  2b4e7cf1ff951b91b895a98398092190fd7456a0fc7af1049b742705fcf3f1b5:
    family: pert
    a: 25.801749190014807
    b: 32.25218648751851
    c: 53.80802821618955
  bc61d8cc194363ecdf47089ee28ee839bf35dc26c71ae7a01e651eb3bd7b002f:
    family: pert
    a: 48.88918173202036
    b: 61.11147716502545
    c: 82.03725609729362
  25f21d6ead5325987e7c1c986f5d04e2e92c1b1b2f6f2b71be8f3ffde2f65528:
    family: pert
    a: 27.84751090964757
    b: 34.80938863705946
    c: 72.5444204684286
  84e2df9c2b297eebbb2340631aa99eb4d10085e7d84699f41a9bf053413561a0:
    family: pert
    a: 19.112482829140053
    b: 23.890603536425065
    c: 36.56302309293927
  2fb347a4b1f4c45f895a592c5e04ea88a2207ab2fa93d53a0303570905156298:
    family: pert
    a: 18.307968086803516
    b: 22.884960108504394
    c: 33.58964857220075
  234f812b1654bad699d2e780f5d4451975fdf7cce2807c1f819c4f01194f6c5a:
    family: pert
    a: 16.245714396747456
    b: 20.30714299593432
    c: 39.55069320320858
  81c751eb638b0dc35bd2d69b0bcb0c057c1a71899325ef2077705386c7c58b92:
    family: pert
    a: 21.533835005698137
    b: 26.91729375712267
    c: 36.37858239233266
  ad50fa8c5858a27e1ab151919410c290f950b68151b2db2dc41eb6a4aa0bedb4:
    family: pert
    a: 19.138290115965766
    b: 23.922862644957206
    c: 43.921411897262885
  0a493648564b32720e7881380df735641a9b2001668905259dfc51e40685ed6c:
    family: pert
    a: 22.353678475916457
    b: 27.94209809489557
    c: 48.24742306096141
  d42305b649738f2dd073d2af13208c11327be15c3c2fe13b43cf6f95135ff3f3:
    family: pert
    a: 9.358265475340966
    b: 13.368950679058523
    c: 31.84769055428545
  2f22afa6f6ec8e36fba1741723879cccdfe026ffb17a1e430655eac9035fd179:
    family: pert
    a: 11.04763233743934
    b: 15.782331910627631
    c: 35.81707092651441
  3dadaf1af8a55946adbdd0c7255a7392db4769cfaf80ea2befbba224a0dee2f1:
    family: pert
    a: 18.175775764064525
    b: 25.96539394866361
    c: 43.931304563887764
  ce01f92d4416b5561c4787212a34fde3cdfcefacbbbd36d879a8036c13188245:
    family: pert
    a: 7.711591690571341
    b: 11.01655955795906
    c: 23.430775538538875
  702e70a6b2b5a97728416a827cded2f91b87b4919a23e4d3b8a3506f69dfd387:
    family: pert
    a: 27.493803089892182
    b: 34.367253862365224
    c: 107.22393452803267
  85db9f9b9be0b26537e9a56d8daa4f430f362b138bf7fd7ddf09c1e4b34680bf:
    family: pert
    a: 17.31824180956958
    b: 21.647802261961974
    c: 35.148091142401015
  37f3beb47f86ab123c0c22daf1c5b70a5e3c5dcbe8b19120879ddf6c41ed495c:
    family: pert
    a: 30.468682413061853
    b: 38.08585301632731
    c: 56.555617721349925
  c63ee06ad7b72fe57d1b7bd3abf872da02150bbebdcdd2f1e6d0c8f629c4ea33:
    family: pert
    a: 33.81166142690991
    b: 42.26457678363738
    c: 62.55215838730794
  a8fefb7aeffa45352b3b47f5ab79fb0077088c274b25135d7647d7d8cdd80137:
    family: pert
    a: 46.310290545539374
    b: 57.88786318192422
    c: 78.92505757357587
  16d604cbece20aae344ab0c7bf68fba3fca95960782f121a34da8f7e2cf6cabc:
    family: pert
    a: 3.21070466443295
    b: 4.0133808305411875
    c: 7.234025825200689
  84b6a0233eced040dae3a752d3ce4e11198b2bcc8901a8c368b972247c6af16b:
    family: pert
    a: 6.016922212064189
    b: 7.521152765080236
    c: 9.469931597692401
  b625da8a9fa421a51e322e9b04c05b89aab18495622851da26bb8e95706a9215:
    family: pert
    a: 3.04013742183583
    b: 3.8001717772947874
    c: 6.158700400569085
  ebdf869e6894e5724b8dee99649284cef02c642fed16c8f80c99b5e62f868465:
    family: pert
    a: 2.476689996212538
    b: 3.0958624952656724
    c: 8.500959651414416
  687a974343f8e05d5865b06429c70f387048e5b3a67abd72fca383ffcc571d04:
    family: pert
    a: 5.019605177172808
    b: 6.27450647146601
    c: 12.940221379240496
  c49ec8d5e1ca72c9c55373600edfeef2130b44118da7e9551d9f687ae8c328ee:
    family: pert
    a: 4.693277541583977
    b: 5.8665969269799705
    c: 9.225050511802143
  e56a9533a4edbeb28f9563c50decc28d35d4483ed5b979d40c6a8cb75358f6ae:
    family: pert
    a: 4.631738385251206
    b: 5.789672981564008
    c: 10.13467711871227
  bf3e174804e408e110de49c568203eeef3262df4dc527af73b90b1cd1a24cf6f:
    family: pert
    a: 54.32856217933179
    b: 67.91070272416474
    c: 93.75006841849309
  8b6525921cf2ddf5c2b921371dd3a8c73af11960d3c2c039858eaf679652b7f8:
    family: pert
    a: 20.793205595036525
    b: 25.991506993795653
    c: 49.45697409666637
  b864550cf59375e5c73e074303fdddb32b5189bbb3c9be62879072562e506643:
    family: pert
    a: 18.011857096657987
    b: 22.514821370822485
    c: 38.70498122776791
  54a76f93c5f6f6da97f1ee15c0edf9a02a2a061847872ebb36a718e37d55a95f:
    family: pert
    a: 27.797738578641766
    b: 34.747173223302205
    c: 59.24766525648513
  6c1e3e37f0b3f8757424166db377bf5700abd4c58c8bf02b2594890acb983192:
    family: pert
    a: 13.110910561669659
    b: 16.388638202087073
    c: 36.17412095379216
  380bc465af0e4c123c1dbf581483d8afea0bda9d4b73e63519153a220a90f130:
    family: pert
    a: 16.996824521830252
    b: 21.246030652287814
    c: 51.1894570728599
  f16fe7bda15d42a60a4cea3a5ca30152b32e45a68cbb8caac92de5a4bcbe42f2:
    family: pert
    a: 36.113370749194544
    b: 45.14171343649318
    c: 69.09997122448364
  d67001762209d8019b64e0b7f9659bc14a75097aa1585b791e1e997e2fbae599:
    family: pert
    a: 15.730751977572092
    b: 19.663439971965115
    c: 33.75068275733868
  288932f032708f1418d6652f37940c38c6784ae9de07dd1c2c4973cf733932cf:
    family: pert
    a: 19.990169321148784
    b: 24.98771165143598
    c: 37.852268227684625
  2b50e7e97fea94926ae4504503116625344608ac343b112884464bc03ccd1dd9:
    family: pert
    a: 22.833982048868762
    b: 28.542477561085953
    c: 142.71238780542976
  52a65eb1c12ee5f69a9faf32e019dd3ae299d70f18ed5b6db7684c74ad8323d3:
    family: pert
    a: 38.42828081949719
    b: 48.03535102437148
    c: 240.1767551218574
  f76f1b77097877393c9ea16db869e574e20a8bd1b57056670dbe104a3986b317:
    family: pert
    a: 15.932683406418441
    b: 19.91585425802305
    c: 38.61621039900461
  17409bc38420a0ab8e0d84c31156f42d5518e03ff3c6e3466e5727b26cecf7c3:
    family: pert
    a: 21.02268572490052
    b: 26.278357156125647
    c: 40.972415195738826
  b3064b1e32360e591ad20b70d7fc2a8be4a3e0ffffd86da43870c85c91421a3b:
    family: pert
    a: 26.957865931770403
    b: 33.697332414713
    c: 60.73587653478686
  4b2b6be481414aed5dd4f184c464302ae26c566ee4d1be1ad0523d947ed8bd23:
    family: pert
    a: 15.610171370076126
    b: 19.512714212595156
    c: 51.01567224265585
  04b68e052787426f38fb2a2266e4b45dd863c0e61f1d4ca27f1aec42a78974d9:
    family: pert
    a: 10.23698368386081
    b: 12.796229604826012
    c: 25.51098362480909
  92e704d27ecee4d31494db0b0e817b1c31326470a40fdbf03f4eae2cc4183edc:
    family: pert
    a: 8.636256039371196
    b: 10.795320049213995
    c: 24.151449963825108
  c77b8a88eb1390a9bfb891991d6e3127eb1ec94ff61fdfdaf48ce9201bcf39ec:
    family: pert
    a: 11.541412533024097
    b: 14.42676566628012
    c: 34.0662154978046
  dd59cfebc9e16359ec3810b55121d63305563b50baedf3634a123c0b69316514:
    family: pert
    a: 23.061631248233184
    b: 28.827039060291476
    c: 34.030709948894845
  b3825ded3ad70470d8cdecc9a68e40bf1844a4dc94896cb00c0b44c0210b5212:
    family: pert
    a: 20.67027879588243
    b: 25.837848494853038
    c: 31.843291835318205
  b30708a3072fa7fd921ae5758c8d559d55d0af8298504157bf2c47133513ac7a:
    family: pert
    a: 13.398549595511609
    b: 16.74818699438951
    c: 25.384474714959534
  078ac4c4cda98df99fe43ee37629a37b4985ff8efde09383a66875c9877deefc:
    family: pert
    a: 13.080468950709728
    b: 16.350586188387158
    c: 22.929359429774244
  d3accc36450643b8c14f9da48412e94d180afefb6ceb340132b758445af4a859:
    family: pert
    a: 14.656497104396008
    b: 18.32062138049501
    c: 26.08606436360575
  432e9a3771ccc9c6959079444037975eded222a2c5fe4df187cb26d255d611a5:
    family: pert
    a: 10.446912031648877
    b: 13.058640039561094
    c: 20.581735538082896
  9de02fe004f464196b9554e2f72ec5caa72670c16a915a9284c52f8ec6ab11d1:
    family: pert
    a: 12.008032674312325
    b: 15.010040842890406
    c: 23.665682660518716
  4bb3f88301efcb5df7771ca79cdae3d7588a7e1377cbb7f05cfa5bb60237ccd8:
    family: pert
    a: 11.56412206561099
    b: 14.455152582013737
    c: 21.804080141071204
  3924cff2ff839f2a4c56ef1a0962709c5d394955f3836e8aa97b4309b4909b0c:
    family: pert
    a: 17.223716057759514
    b: 21.52964507219939
    c: 31.34384267159972
  8bd6e2fd82401b0865e309cfeacd285448f58b51a2889e3beffcfa887ad01d38:
    family: pert
    a: 25.749775721383685
    b: 32.187219651729606
    c: 41.318782830953374
  7fe7371f4e53d48b9ddb8276fc25b28a3763ae0a3db292faa73cdc18726c7127:
    family: pert
    a: 24.78366106643955
    b: 30.979576333049437
    c: 42.75736740159866
  947da0543011dcc595f7defc4be61c455731cbdeccd137a08bfd3887ee3c7f3e:
    family: pert
    a: 23.7277485812664
    b: 29.659685726583
    c: 33.68622928606979
  b851aba5905fffbc3a85869fbd8455e2757ba75a817bdb9a4fa85eca054b0c82:
    family: pert
    a: 18.189570259834337
    b: 22.736962824792922
    c: 34.405211866833795
  1d4caf96b8c01d38e2300ce0b7a045e98068575ba8b42a78e48aa5fb3b63b0a6:
    family: pert
    a: 14.510527967109722
    b: 18.13815995888715
    c: 30.908612544100208
  0793e403be69d150e9fbf81eceea27ed4926d78296d25dbc823ff44fa503b1df:
    family: pert
    a: 15.287765699783165
    b: 19.109707124728956
    c: 35.29179986175241
  d8d5bfa70f96db43ad654ca4096a81fce5e2d3765d53fe99365368039a007407:
    family: pert
    a: 49.952297187168114
    b: 62.440371483960135
    c: 100.97363737834475
  b07cfb83fcc8c3d8eba16920272c0049d6f9353c7802375c0b0d4a08e39eb81a:
    family: pert
    a: 22.555310709739945
    b: 32.22187244248564
    c: 161.1093622124282
  0c0d0919435ca985c060ce459b086257b7b3c2dd524aca9bfc7347470c88fe6b:
    family: pert
    a: 40.98634362504859
    b: 58.55191946435514
    c: 292.7595973217757
  b0476660146ea90f34a08de651e9d1024900cae32e8a42865128c5fe341b676a:
    family: pert
    a: 36.470281286058096
    b: 52.10040183722586
    c: 260.50200918612927
  472f821493db6ab7f5c26dc0d475292cfdba9fe5b1b824ef9c2d7de6b923f5ea:
    family: pert
    a: 12.66288995609331
    b: 15.828612445116635
    c: 38.928910772997874
  b99695307ed82f5127a00eea4857ccfeda0eae1969e194fcd4ac5c45276f4bf5:
    family: pert
    a: 16.130725467408435
    b: 20.16340683426054
    c: 29.391874243048935
  54a01c4a5aed40400e30ed42044a1a42b6f088a0233c718e785f1eea51a757ed:
    family: pert
    a: 11.367383729161414
    b: 14.209229661451767
    c: 24.63755281901638
  836c250965bdee3f8afdab786cca7f5a885db15ac18586106f293e0a93f72f6d:
    family: pert
    a: 11.322607194076099
    b: 14.153258992595122
    c: 27.459245023622945
  8a6ac381581869887d68c2d4518e665b14b0fad595e640698d89f94d776c1255:
    family: pert
    a: 9.286056034429734
    b: 13.26579433489962
    c: 66.3289716744981
  db7f753712a6b2ab119eb88bcf922615e929916ffa44d05243a570ccd69d6dbc:
    family: pert
    a: 10.775052611093985
    b: 15.392932301562837
    c: 76.96466150781418
  88a2f11c11e3b914b3df418fef96167ecbe0b156c22d06a71b95b2d0fc1274f6:
    family: pert
    a: 9.811064443092167
    b: 14.015806347274527
    c: 70.07903173637263
  e76bbed70c6ba22b7e87772d096bd9425a1c00df0af18a80cfc3c10be0de5844:
    family: pert
    a: 6.801947532529276
    b: 9.717067903613252
    c: 48.58533951806626
  2ae8db97e1f734926efcf9c2eead4f61b4df045c8d47823997abe423d527bf20:
    family: pert
    a: 7.932258628723236
    b: 11.331798041033196
    c: 56.65899020516598
  72da33778319585348b1c6579e9c19ebdf8904cecacb8d493b324615a593eb96:
    family: pert
    a: 10.274332285750353
    b: 14.677617551071933
    c: 73.38808775535966
  d91ebcabffc5b580461992ac07d53cb0dca1cfd36bf7baf3e0ef26c3224fa0cf:
    family: pert
    a: 8.48115258456251
    b: 12.11593226366073
    c: 60.57966131830365
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
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: c6e6ae83b24ec19bfb77ad3e4518473166bcb810fe3fa3c9578f82e4c254479a
  - id: 2
    dedication:
      worker_1: 0.5
      worker_2: 0.5
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 1607dc5d09d669cc9637573e3c7b5d7af060d9584fd412f999b7c55b3469bd09
  - id: 3
    dedication:
      worker_1: 0.5
      worker_2: 1.0
      worker_4: 0.5
      worker_3: 0.75
    distribution_hash: bfaa90d221269779b03e3fddab55e631572a615360b241cf986b05adba207782
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_3: 0.5
    distribution_hash: 604c52251dedebd33561f5dbd7fb610539f0eb280104090c9ef2cc931fc6e70e
  - id: 2
    dedication:
      worker_4: 0.5
      worker_3: 0.5
    distribution_hash: 25e4d22540b94d0b03032cbcbc29af66124f428f8ba1966258a2ba6b6999d60d
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 94f056e56242dda06acc56365e175129e2f2fa0be39109d0e7d9d4f89b6cb112
  - id: 4
    dedication:
      worker_4: 0.75
      worker_3: 0.75
      worker_2: 0.75
    distribution_hash: 473baf4dd4cbc0b4208841bf8488710e0ffcc6851e85e45aa435d601070550d7
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: 8c10e9584d29101e1dfeb17922fc328f09963ee70ab1950457fc6f695e2fe02f
  - id: 6
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: d25ef1e63bfae4f03cf2c9832512f01b1bbd22397bbe86ae70bd9026782c6f3a
  - id: 7
    dedication:
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 0de34ce55bfc4eec5e4845789fd92999d934b837d229723a8b80afb4a47ce8aa
  - id: 8
    dedication:
      worker_2: 0.75
      worker_4: 0.75
    distribution_hash: 3114ff8326c5c6fadf8f916757716fbe5d43f2cc04963ebd42bc2f0482f2e99a
  - id: 9
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 0.5
    distribution_hash: 94084d0bdfcf3df3bb1eea9a284869cd5d2d1a4294035d399233c38111b330e0
  - id: 10
    dedication:
      worker_2: 1.0
      worker_4: 0.5
      worker_3: 0.5
    distribution_hash: 5ad5496660a7b6a073b69968a79204cdb11869676d1b891b6f75b3c3bf5b3961
  - id: 11
    dedication:
      worker_2: 0.75
      worker_4: 0.5
      worker_3: 1.0
    distribution_hash: cad23e890e072fb9708c3eb689b6024f3675777b76ee65fc1b1ddc7f20d934c9
  - id: 12
    dedication:
      worker_3: 0.75
      worker_2: 0.5
    distribution_hash: 33a03083a2d7825a5a7ce1a3953d14dbac8d7f7112bd79744c4ee4de91707239
  - id: 13
    dedication:
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: 74db2303537dc27b047dd367720e9823af724e04cc3394e263dc98f119e3f3da
  - id: 14
    dedication:
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: c340373ffff7dc620c2736f8fffd992787cb3d2a683f0caea0077b500e80f7be
  - id: 15
    dedication:
      worker_3: 0.75
      worker_2: 0.75
      worker_4: 0.5
    distribution_hash: ee40e117e3125cf02f92ad5805632c2a802f71d3d729fe855e3c08efc10fa46e
  - id: 16
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: 87569193420890595b99badd24a69ba902c0851bae1a44b989ce33ae624d3be0
  - id: 17
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_4: 1.0
    distribution_hash: 8d3b7c09f61cdb69ce30974bd8ebf5a45d43567e098d5776e1b931872f817d6c
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 0aadc7a5fd91d2c3f7a03375faddf63282ba849b64feaee0ba3383ec7c62f1e3
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: 03263a5e73a77c535813f79aa8ff9042fce27744a2e6ea160a6e5660ab705071
  - id: 2
    dedication:
      worker_2: 0.5
    distribution_hash: 5c855cc5666cd6ba41c52957cfc4f3ba2ff416e58ecb69d1f1acf28b22cbecad
  - id: 3
    dedication:
      worker_4: 1.0
    distribution_hash: 59ac74b8173c27ec8b276d7f562add0798bbe8df8372423786320548a60615d7
  - id: 4
    dedication:
      worker_4: 0.75
    distribution_hash: d1159506c7b49625816a2d6c12890686d9931422b20752fe6ae813d6d0946c49
  - id: 5
    dedication:
      worker_1: 0.75
    distribution_hash: 35cbaa28be131fc3a54ef95d04a8e4a10eab64a3b7102172025f7c0d3f371003
  - id: 6
    dedication:
      worker_1: 0.5
    distribution_hash: 6f69c23e03764f4f2d317093d220206776f8168a4d1c8de95ccd68b126c4f884
  - id: 7
    dedication:
      worker_3: 0.5
    distribution_hash: db2add4e62d6ea4de754fc16988f8a8d5aa6a8ab8edf12e3997d96a82c446994
  - id: 8
    dedication:
      worker_3: 1.0
    distribution_hash: 5d08662f7d160919502339ca76d7264a9a2f3c897f11b772f9a7752bb3af24f7
  - id: 9
    dedication:
      worker_3: 0.75
    distribution_hash: 916771230f1efd1402feec432af2212a8794729f9481b31c40c9e5fde5e2237c
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: d588db445cb2d65b201f64496380c7accd5c5cf0fe0d2ff2c16b4a9a59882ac7
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: 05c8ad48b854d0f4cac66faccbc5200c2fa8d465b008ec9c310024ad925825c3
  - id: 3
    dedication:
      worker_1: 0.75
      worker_3: 0.75
      worker_4: 0.75
    distribution_hash: 7aeb73314ceb1fe2f0ae352a46b42fddb18392c9e24ce7eb94cee8c1658c37ad
  - id: 4
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_1: 0.5
    distribution_hash: f703281721a0c6a55951882bbe1d0c0cd3eed39c7745a5f9dba4f2fc6809a2f6
  - id: 5
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 1dad2845d1eab7e71e6edeac8c4b8b0bcd5e539d10cf521763fa91d36344db1b
  - id: 6
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: e5244b72ad3f577078ae2b9cb1a67c5c2ca4b0551eb04be5cacb1c0f1ea94ce6
  - id: 7
    dedication:
      worker_4: 0.5
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: 4722c0039c24386c85cd9176c7d0efa379990975ed70fa3a067c6bc9232397fd
  - id: 8
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 219fb2dfdb33db131ef907754dd811030fbc58c2f3de78259f24c7045dd88924
  - id: 9
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 953f3cb44b068f8f2e45acee3467cc7a95e8c88528f0ec96c7e6577013e3d98a
  - id: 10
    dedication:
      worker_4: 0.75
      worker_1: 0.5
      worker_2: 1.0
    distribution_hash: 3405af538d369e49d0b39cb78e120b269ca5caecc55932f7a7813f6981ac4d37
  - id: 11
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: 22a4e89a719fda42e16dc3c4b0487c83a442546330b8d3633bc41518372fb49c
  - id: 12
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: 868d56445dadf19093a1b7cbd255bb978c2c0641dbadd2a659edb37dc1cb89e7
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 7232711640b8be2ad39dba6550612c6867c70478280cf39e6021dde8ff64369c
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 94b1e4f820730954cbf2ab72cc523bf8de6d28732528d93e205b3083fa48d37a
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: d332bb3a4c41a092449002f4cd5959d1c4bce40bcae3730f714ee96a97a58951
  - id: 2
    dedication:
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: e2299b0e263bdc0705754d71906a362345495c5e12043a7921754ac91cb913df
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 6cfb5c146b771af2f89a900d2e4c339894913d09e398616505ba0dc91fa24576
  - id: 4
    dedication:
      worker_4: 0.5
      worker_2: 1.0
    distribution_hash: 2cfe38a6da8fb2eb687f8c49f8e272b2d19a68f869b528a0d4a7ae01819c4d13
  - id: 5
    dedication:
      worker_4: 0.5
      worker_2: 0.75
    distribution_hash: e38060ed7622bbdf11aa47a8f1f009730a162ed24ed9cc7e11c7fba635bd6b0a
  - id: 6
    dedication:
      worker_4: 1.0
      worker_2: 0.5
    distribution_hash: aa90a6bffa2d481dfbecc02046a1d4c2799dfb0a8b473cdf62e373453bda7b59
  - id: 7
    dedication:
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: b3ac00efa47c18aa6e22702f43c6a1b7ad351625da0d0412c225acbc409a348c
  - id: 8
    dedication:
      worker_3: 0.75
      worker_4: 0.5
    distribution_hash: d66559295baebf7015ed2d2801ed423caf54823301a951fff262201acb49e428
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: ddb3108def1348f4ccc165553d97f5de029652112bec3f7ba377c0c9abc30f57
  - id: 2
    dedication:
      worker_4: 0.5
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 171c80c983420530d14128a175826847f9cf400913fb06f682c4c0ea637557f5
  - id: 3
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 9bee15a528b0c3be0b80988d84cc5ec131bb6777d2ebc9def344053eaf8254e4
  - id: 4
    dedication:
      worker_1: 0.75
      worker_2: 0.5
      worker_4: 1.0
    distribution_hash: 421a1ca63c3d603249285116f1f960737dcad515f762603ae34d4cd3cc7ceb48
  - id: 5
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: ee74a3f21a3c95f7c4fd0520174cf7097eeb307c945dfa433cab32a281a0ff71
  - id: 6
    dedication:
      worker_1: 1.0
      worker_2: 0.5
      worker_4: 0.75
    distribution_hash: 53791f96b55bcef9dedd8ca81894c95d392dcedb0407b2f36bfc646df7aec7f5
  - id: 7
    dedication:
      worker_2: 0.5
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: 3717a4060b69122a0f5a0851649d316fe66426f6b407070b9e1ddccdb2f8d8c9
  - id: 8
    dedication:
      worker_2: 0.5
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: d0f4da0ce4dbf208fd1df6795d96d933f6d2c55be7d99a9142d60989fd4624e9
  - id: 9
    dedication:
      worker_2: 0.5
      worker_3: 0.75
      worker_1: 0.5
    distribution_hash: 23e2526c94689e1c1886c5123898ffed187c22ca4a4000b4d59f2ddf32977b75
  - id: 10
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: ab695ad1a671f88d3d18fed9b0beac6b776a8064bde4748b1447c0f7b0be3ae2
  - id: 11
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: 5ff0545526e8f625d5b3cf436cf9d78118a9f7f56c6bd2c59a1b18f8e5273f3c
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: fd822f3ac2ea7e6e3f86e19a69598b31f2da755e02e46e0ac5144304a48ebe92
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 0.5
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 6608d77e21da2d8182ebee82b63814842921fae1350f8d8d123974b57bb16ee1
  - id: 2
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: c011a8b3313d71644a09f34c560d1a32c02e4f097ddb712de967620d22b7e1bc
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
    distribution_hash: 7d58b436807bea728a44ffb2676952daa5469d9d26cce49750dac4d76094bfa9
  - id: 2
    dedication:
      worker_3: 1.0
    distribution_hash: 771b105133a9d26c6abdfd38fa31e8830366f37d21e83b0228370007c9b9c37e
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: cb3bab56da2b80db7d88e5ef5ec4e1c528cfb9974c1da2115a9e290b99e68374
  - id: 4
    dedication:
      worker_2: 0.75
    distribution_hash: 313427b463e6b9b4a79e44f6b7851ad7520f8c749a4daa801066364f2be1a27b
  - id: 5
    dedication:
      worker_1: 0.5
    distribution_hash: a66d494a0f7cb44a88d827ea3d88e920ad635de482411e1d72a9f0a668524dca
  - id: 6
    dedication:
      worker_1: 0.75
    distribution_hash: 6d515ab53af963dbced2b885dc6f7800ae0031da6db08dfdb10fa2df6e3031d4
  - id: 7
    dedication:
      worker_4: 0.75
    distribution_hash: 9c33d23863a847e4031eadce2557e669e6cda4cc9bc9cea38701b00908f2b36a
  - id: 8
    dedication:
      worker_4: 1.0
    distribution_hash: 841cdf79141cbdbc09cd275c3c749dbfa1d192283f536cf7a1aac74ad0a3d4ee
  - id: 9
    dedication:
      worker_4: 0.5
    distribution_hash: 33a0af9be61a7e9936eafc0a26809782d14b89fce49d44a07183b17bc5ad75fb
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 21d82d37dc91e22fa9a4b1111c283c11efd062bc9d56abe3bb3db9acd32ee7e5
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: 72abda2ea0d97f9bb88ac4fabef5df67bb8fdfa6a1b199a3e7f016ae5125b152
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 2b4e7cf1ff951b91b895a98398092190fd7456a0fc7af1049b742705fcf3f1b5
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 0.5
    distribution_hash: bc61d8cc194363ecdf47089ee28ee839bf35dc26c71ae7a01e651eb3bd7b002f
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 25f21d6ead5325987e7c1c986f5d04e2e92c1b1b2f6f2b71be8f3ffde2f65528
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 84e2df9c2b297eebbb2340631aa99eb4d10085e7d84699f41a9bf053413561a0
  - id: 2
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 2fb347a4b1f4c45f895a592c5e04ea88a2207ab2fa93d53a0303570905156298
  - id: 3
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 234f812b1654bad699d2e780f5d4451975fdf7cce2807c1f819c4f01194f6c5a
  - id: 4
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: 81c751eb638b0dc35bd2d69b0bcb0c057c1a71899325ef2077705386c7c58b92
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: ad50fa8c5858a27e1ab151919410c290f950b68151b2db2dc41eb6a4aa0bedb4
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: 0a493648564b32720e7881380df735641a9b2001668905259dfc51e40685ed6c
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
    distribution_hash: d42305b649738f2dd073d2af13208c11327be15c3c2fe13b43cf6f95135ff3f3
  - id: 2
    dedication:
      worker_3: 0.75
    distribution_hash: 2f22afa6f6ec8e36fba1741723879cccdfe026ffb17a1e430655eac9035fd179
  - id: 3
    dedication:
      worker_3: 0.5
    distribution_hash: 3dadaf1af8a55946adbdd0c7255a7392db4769cfaf80ea2befbba224a0dee2f1
  - id: 4
    dedication:
      worker_3: 1.0
    distribution_hash: ce01f92d4416b5561c4787212a34fde3cdfcefacbbbd36d879a8036c13188245
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: 702e70a6b2b5a97728416a827cded2f91b87b4919a23e4d3b8a3506f69dfd387
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 85db9f9b9be0b26537e9a56d8daa4f430f362b138bf7fd7ddf09c1e4b34680bf
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 37f3beb47f86ab123c0c22daf1c5b70a5e3c5dcbe8b19120879ddf6c41ed495c
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_4: 0.75
    distribution_hash: c63ee06ad7b72fe57d1b7bd3abf872da02150bbebdcdd2f1e6d0c8f629c4ea33
  - id: 3
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_4: 0.5
    distribution_hash: a8fefb7aeffa45352b3b47f5ab79fb0077088c274b25135d7647d7d8cdd80137
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: 16d604cbece20aae344ab0c7bf68fba3fca95960782f121a34da8f7e2cf6cabc
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 0.5
    distribution_hash: 84b6a0233eced040dae3a752d3ce4e11198b2bcc8901a8c368b972247c6af16b
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: b625da8a9fa421a51e322e9b04c05b89aab18495622851da26bb8e95706a9215
  - id: 4
    dedication:
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: ebdf869e6894e5724b8dee99649284cef02c642fed16c8f80c99b5e62f868465
  - id: 5
    dedication:
      worker_3: 0.5
      worker_2: 0.5
    distribution_hash: 687a974343f8e05d5865b06429c70f387048e5b3a67abd72fca383ffcc571d04
  - id: 6
    dedication:
      worker_4: 0.5
      worker_2: 1.0
    distribution_hash: c49ec8d5e1ca72c9c55373600edfeef2130b44118da7e9551d9f687ae8c328ee
  - id: 7
    dedication:
      worker_4: 0.75
      worker_2: 0.5
    distribution_hash: e56a9533a4edbeb28f9563c50decc28d35d4483ed5b979d40c6a8cb75358f6ae
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.5
    distribution_hash: bf3e174804e408e110de49c568203eeef3262df4dc527af73b90b1cd1a24cf6f
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: 8b6525921cf2ddf5c2b921371dd3a8c73af11960d3c2c039858eaf679652b7f8
  - id: 3
    dedication:
      worker_3: 0.75
    distribution_hash: b864550cf59375e5c73e074303fdddb32b5189bbb3c9be62879072562e506643
  - id: 4
    dedication:
      worker_3: 0.5
    distribution_hash: 54a76f93c5f6f6da97f1ee15c0edf9a02a2a061847872ebb36a718e37d55a95f
  - id: 5
    dedication:
      worker_2: 1.0
    distribution_hash: 6c1e3e37f0b3f8757424166db377bf5700abd4c58c8bf02b2594890acb983192
  - id: 6
    dedication:
      worker_2: 0.75
    distribution_hash: 380bc465af0e4c123c1dbf581483d8afea0bda9d4b73e63519153a220a90f130
  - id: 7
    dedication:
      worker_1: 0.5
    distribution_hash: f16fe7bda15d42a60a4cea3a5ca30152b32e45a68cbb8caac92de5a4bcbe42f2
  - id: 8
    dedication:
      worker_1: 1.0
    distribution_hash: d67001762209d8019b64e0b7f9659bc14a75097aa1585b791e1e997e2fbae599
  - id: 9
    dedication:
      worker_1: 0.75
    distribution_hash: 288932f032708f1418d6652f37940c38c6784ae9de07dd1c2c4973cf733932cf
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_5: 0.25
    distribution_hash: 2b50e7e97fea94926ae4504503116625344608ac343b112884464bc03ccd1dd9
  - id: 2
    dedication:
      worker_3: 0.25
      worker_5: 0.25
    distribution_hash: 52a65eb1c12ee5f69a9faf32e019dd3ae299d70f18ed5b6db7684c74ad8323d3
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
    distribution_hash: f76f1b77097877393c9ea16db869e574e20a8bd1b57056670dbe104a3986b317
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: 17409bc38420a0ab8e0d84c31156f42d5518e03ff3c6e3466e5727b26cecf7c3
  - id: 3
    dedication:
      worker_4: 0.75
    distribution_hash: b3064b1e32360e591ad20b70d7fc2a8be4a3e0ffffd86da43870c85c91421a3b
  - id: 4
    dedication:
      worker_3: 0.75
    distribution_hash: 4b2b6be481414aed5dd4f184c464302ae26c566ee4d1be1ad0523d947ed8bd23
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 04b68e052787426f38fb2a2266e4b45dd863c0e61f1d4ca27f1aec42a78974d9
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 92e704d27ecee4d31494db0b0e817b1c31326470a40fdbf03f4eae2cc4183edc
  - id: 3
    dedication:
      worker_4: 1.0
      worker_1: 0.75
      worker_2: 0.5
    distribution_hash: c77b8a88eb1390a9bfb891991d6e3127eb1ec94ff61fdfdaf48ce9201bcf39ec
  - id: 4
    dedication:
      worker_4: 0.5
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: dd59cfebc9e16359ec3810b55121d63305563b50baedf3634a123c0b69316514
  - id: 5
    dedication:
      worker_4: 0.75
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: b3825ded3ad70470d8cdecc9a68e40bf1844a4dc94896cb00c0b44c0210b5212
  - id: 6
    dedication:
      worker_4: 1.0
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: b30708a3072fa7fd921ae5758c8d559d55d0af8298504157bf2c47133513ac7a
  - id: 7
    dedication:
      worker_1: 0.5
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: 078ac4c4cda98df99fe43ee37629a37b4985ff8efde09383a66875c9877deefc
  - id: 8
    dedication:
      worker_1: 0.75
      worker_3: 0.75
      worker_2: 0.75
    distribution_hash: d3accc36450643b8c14f9da48412e94d180afefb6ceb340132b758445af4a859
  - id: 9
    dedication:
      worker_1: 0.75
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: 432e9a3771ccc9c6959079444037975eded222a2c5fe4df187cb26d255d611a5
  - id: 10
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 9de02fe004f464196b9554e2f72ec5caa72670c16a915a9284c52f8ec6ab11d1
  - id: 11
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 4bb3f88301efcb5df7771ca79cdae3d7588a7e1377cbb7f05cfa5bb60237ccd8
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 3924cff2ff839f2a4c56ef1a0962709c5d394955f3836e8aa97b4309b4909b0c
  - id: 2
    dedication:
      worker_1: 0.5
      worker_4: 1.0
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: 8bd6e2fd82401b0865e309cfeacd285448f58b51a2889e3beffcfa887ad01d38
  - id: 3
    dedication:
      worker_1: 0.75
      worker_4: 1.0
      worker_3: 0.75
      worker_2: 0.75
    distribution_hash: 7fe7371f4e53d48b9ddb8276fc25b28a3763ae0a3db292faa73cdc18726c7127
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 947da0543011dcc595f7defc4be61c455731cbdeccd137a08bfd3887ee3c7f3e
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: b851aba5905fffbc3a85869fbd8455e2757ba75a817bdb9a4fa85eca054b0c82
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 1d4caf96b8c01d38e2300ce0b7a045e98068575ba8b42a78e48aa5fb3b63b0a6
  - id: 4
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 0793e403be69d150e9fbf81eceea27ed4926d78296d25dbc823ff44fa503b1df
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: d8d5bfa70f96db43ad654ca4096a81fce5e2d3765d53fe99365368039a007407
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_3: 1.0
      worker_5: 0.25
    distribution_hash: b07cfb83fcc8c3d8eba16920272c0049d6f9353c7802375c0b0d4a08e39eb81a
  - id: 2
    dedication:
      worker_4: 0.75
      worker_2: 0.5
      worker_3: 0.75
      worker_5: 0.5
    distribution_hash: 0c0d0919435ca985c060ce459b086257b7b3c2dd524aca9bfc7347470c88fe6b
  - id: 3
    dedication:
      worker_4: 0.75
      worker_2: 1.0
      worker_3: 0.5
      worker_5: 0.25
    distribution_hash: b0476660146ea90f34a08de651e9d1024900cae32e8a42865128c5fe341b676a
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
    distribution_hash: 472f821493db6ab7f5c26dc0d475292cfdba9fe5b1b824ef9c2d7de6b923f5ea
  - id: 2
    dedication:
      worker_4: 1.0
    distribution_hash: b99695307ed82f5127a00eea4857ccfeda0eae1969e194fcd4ac5c45276f4bf5
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: 54a01c4a5aed40400e30ed42044a1a42b6f088a0233c718e785f1eea51a757ed
  - id: 4
    dedication:
      worker_1: 1.0
    distribution_hash: 836c250965bdee3f8afdab786cca7f5a885db15ac18586106f293e0a93f72f6d
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: 8a6ac381581869887d68c2d4518e665b14b0fad595e640698d89f94d776c1255
  - id: 2
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_2: 1.0
      worker_5: 0.25
    distribution_hash: db7f753712a6b2ab119eb88bcf922615e929916ffa44d05243a570ccd69d6dbc
  - id: 3
    dedication:
      worker_3: 1.0
      worker_1: 1.0
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: 88a2f11c11e3b914b3df418fef96167ecbe0b156c22d06a71b95b2d0fc1274f6
  - id: 4
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 1.0
      worker_5: 0.25
    distribution_hash: e76bbed70c6ba22b7e87772d096bd9425a1c00df0af18a80cfc3c10be0de5844
  - id: 5
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 1.0
      worker_5: 0.5
    distribution_hash: 2ae8db97e1f734926efcf9c2eead4f61b4df045c8d47823997abe423d527bf20
  - id: 6
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_5: 0.5
    distribution_hash: 72da33778319585348b1c6579e9c19ebdf8904cecacb8d493b324615a593eb96
  - id: 7
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: d91ebcabffc5b580461992ac07d53cb0dca1cfd36bf7baf3e0ef26c3224fa0cf
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
  - task_11
- - task_1
  - task_12
- - task_1
  - task_17
- - task_1
  - task_18
- - task_1
  - task_19
- - task_1
  - task_20
- - task_1
  - task_31
- - task_2
  - task_10
- - task_2
  - task_21
- - task_2
  - task_24
- - task_2
  - task_28
- - task_4
  - task_10
- - task_4
  - task_13
- - task_4
  - task_25
- - task_5
  - task_14
- - task_5
  - task_23
- - task_5
  - task_30
- - task_6
  - task_21
- - task_6
  - task_23
- - task_6
  - task_29
- - task_8
  - task_24
- - task_9
  - task_14
- - task_9
  - task_28
- - task_10
  - task_22
- - task_10
  - task_26
- - task_11
  - task_21
- - task_11
  - task_25
- - task_12
  - task_22
- - task_12
  - task_24
- - task_14
  - task_21
- - task_17
  - task_23
- - task_18
  - task_23
- - task_19
  - task_21
- - task_7
  - task_29
- - task_7
  - task_24
- - task_29
  - task_27
- - task_11
  - task_13
- - task_8
  - task_29
- - task_2
  - task_16
- - task_6
  - task_25
- - task_16
  - task_15
- - task_6
  - task_24
- - task_4
  - task_28
- - task_12
  - task_21
- - task_3
  - task_32
- - task_13
  - task_32
- - task_15
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
- - task_30
  - task_32
- - task_31
  - task_32
deadline:
  delta: 681
validation:
  project_key: 0d3abfa0c89991b5bfa930b673ec4a0d7a34f560deec0045d3aaa7404623d829
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 71 days; worst-case serial bound: 1515 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
