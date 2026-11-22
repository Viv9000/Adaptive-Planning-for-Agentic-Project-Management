# Configuration

```yaml
generator: dataset.generator.generator
source_id: MSLIB_Set4_6
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
  modes: 159
  tasks_at_cap: 0
  relaxed_constraints: 2
  rewired_edges: 4
  departments: 1
  quality:
  - worker_3
  safety_skill: 1
  review_tasks: 4
  liaison_tasks: 3
  extra_tasks: 3
  barred_pairs: 9
  incompatible_pairs: 0
  edges: 55
n_workers: 5
n_tasks: 32
n_skills: 0
seed: 0
deadline_factor: 1.25
reference_makespan: 680
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
  0c7807f43f76f289706d33c63247548cf268864b2424f0a206efcbcea9c8b7ad:
    family: pert
    a: 5.01912829150923
    b: 8.36521381918205
    c: 30.265776566543693
  107dc244259c12187a2049a77fde19bd17b4b3abd08495591295fd5e50482774:
    family: pert
    a: 5.124251816427905
    b: 8.54041969404651
    c: 44.98906335966741
  7c7f917ccc335e7fbf224bbff4dd594c4e45d8ac801fcc54139b75b400118612:
    family: pert
    a: 4.252947167508286
    b: 7.088245279180477
    c: 40.6773291692965
  f2cfad035feacff26f898bbab13e387dc33ec6bf17f0c1faaa65605f55a9813f:
    family: pert
    a: 12.483955369284114
    b: 15.604944211605142
    c: 18.309866751631798
  14def0320452519e9cdd9d83b5c923614bf2c4c7829c418bb60a8d59e4a7750c:
    family: pert
    a: 7.488632929867632
    b: 9.36079116233454
    c: 24.251270377463012
  aaf5c1a82645e72590723c82356e58043440857dbf4dbb1c6d12413df41deeae:
    family: pert
    a: 10.479572815404424
    b: 13.09946601925553
    c: 19.00788745643814
  8f5c11c131aa1d3949715cbb79e5f2bfdbe2ec9be51ea03ebe3ed65182a2752c:
    family: pert
    a: 11.271724072209137
    b: 14.08965509026142
    c: 23.444014737604466
  325df1a73b40a85f47cac1bad0d6c87d042baeeb6951a1c28104fcc49a839d82:
    family: pert
    a: 11.893559401722422
    b: 14.866949252153027
    c: 19.204091159357915
  94daf6b6c6e16203902a29da4aad6d1697de7f84fc47b8657b20a51669414ff2:
    family: pert
    a: 8.50641442593349
    b: 10.633018032416862
    c: 22.703929755542383
  2b78b822920c05931adf06d5e0db470bd4dd5fdf1a322b343c4b9e8e4560a61f:
    family: pert
    a: 24.64291085460607
    b: 30.803638568257583
    c: 65.30959126947235
  0ccfcdb27472177f49681cbe7cebe605c6823e9679364d7dff15f6e0bf34318f:
    family: pert
    a: 41.8947636591666
    b: 52.368454573958246
    c: 77.91700857424438
  b1bcec6c8182db866957e8eb6ce6c8f89bee83709acd48fec67048dbc280a81a:
    family: pert
    a: 23.79550593022119
    b: 29.744382412776485
    c: 48.437257330398296
  f7e17863a30da52af6b6c065736b462043e33714e70a45351434441fe501bd52:
    family: pert
    a: 36.99445755283164
    b: 46.243071941039545
    c: 70.22423130452208
  ac27c356e5f80ceedc54d2bac88b2477aaff6500fd35db7fba7a076bb6d95c05:
    family: pert
    a: 36.76936774287733
    b: 45.96170967859666
    c: 63.50037406414166
  e1e97286acf8a6c105791bfa4154ced0df50ff1de2637d458d6fa8142a7e8555:
    family: pert
    a: 33.16169458473589
    b: 41.45211823091986
    c: 63.55096754629832
  368aeee0c29b6d8ba9dc09325895e85daf4a012e934dfb74c9cca831546a4979:
    family: pert
    a: 30.345572767460126
    b: 37.931965959325154
    c: 61.554659412501785
  3bdb7febf5bd9b6917645c1049edce2d622ff69cba37a2d372bd8e37c2f1aec1:
    family: pert
    a: 29.268469968101513
    b: 36.58558746012689
    c: 78.99483152718713
  136ea18bbd385de8407700bcc35a5a313c1c9af1d2a25589cc9ea42f88a0fc4a:
    family: pert
    a: 45.409427916486706
    b: 56.76178489560838
    c: 74.73158979724455
  eb45ff28f0cea3900e3adb1a197a089c1b071b61f8d9582bf50a08b589eca762:
    family: pert
    a: 18.614757030275364
    b: 26.59251004325052
    c: 51.458154572574
  b55b8f0212599056f353c63af6146c0bcd4760233b72c66de79ca4e5fbf96238:
    family: pert
    a: 19.302792285456658
    b: 27.57541755065237
    c: 83.67262986259853
  de902cc5da857a8bd7dbb183484b187eacbfc4225fc840d7fb52be020d6ab3d8:
    family: pert
    a: 18.16271980457496
    b: 25.946742577964226
    c: 61.78475663585373
  a8dd8eeab7ebc6248458d0bd712e0aff4a127c133bc37f344e5c80ea6152494e:
    family: pert
    a: 26.678492933118857
    b: 38.11213276159837
    c: 84.40684104159432
  48037b19ec14ebc90613d3ab6762674ca1657495336172d13f2d2245bdda0786:
    family: pert
    a: 14.608926979749445
    b: 20.86989568535635
    c: 64.56748765341311
  9f64a501f2cb94faf509e99a143bf0acc412749dbb023a90d649e96df2269bcc:
    family: pert
    a: 19.812750330452452
    b: 28.303929043503505
    c: 70.12094648107674
  3b69b3a3e651d9e5154db4ac064a00049f3fb7426c8a120560e252e845ed1824:
    family: pert
    a: 23.249310350384018
    b: 33.2133005005486
    c: 83.05354834292154
  a09097f085e02347034f7fc5e1573f0bab942d7434c6041a09eb5c76dafcd5b5:
    family: pert
    a: 22.367078387175297
    b: 31.952969124536143
    c: 53.15534403085451
  0b0031e11174a52b975a7bf17cf4608a8dfa2ad67ff144a4270b60f26b3bb0c5:
    family: pert
    a: 18.44917229737467
    b: 26.35596042482096
    c: 41.85757412341033
  013b10a3af2b913ec3c216ba78520a29cd8bb3d2dd884ff960b3ccbb8e4208c0:
    family: pert
    a: 37.20247812119074
    b: 53.146397315986775
    c: 72.28376887010333
  1a3d997f1a8761b6edc553fe92538038893e8e593f766e737cea0b08b4ae1bcb:
    family: pert
    a: 19.024616438371485
    b: 27.17802348338784
    c: 49.50523768609451
  43ef11672830344074075ab61c9aa92a316b2d1cdbbeac181443c1e7db1e9f9a:
    family: pert
    a: 27.247569067975164
    b: 38.92509866853595
    c: 60.89220034579005
  876b40fe944f92562b2df0a9f8f46d8f357ef22804f6d2dbbd6b26126967710a:
    family: pert
    a: 34.96307088056028
    b: 43.70383860070035
    c: 84.20804816243755
  c0c987b05234642c232b56e99b8a9f84b905cabb5dc3ce662fff9c39d7dc3a15:
    family: pert
    a: 37.57573084776461
    b: 46.96966355970576
    c: 78.1238594590795
  c2f217e65f78890e90554357763ecc1dcc3a30d8cae964aa06015830b0ecdde9:
    family: pert
    a: 30.302896714315768
    b: 37.87862089289471
    c: 69.2231685468429
  90b962792c70b69c9d54f342ae2b79ae8078f572d848090ea97d1b3ce4128459:
    family: pert
    a: 41.87159582512342
    b: 52.33949478140427
    c: 76.94918785518426
  964ea48e1243568feee4065b9c63e9d27a3f145a08bdb80ea9e23c47195795ae:
    family: pert
    a: 57.00719107970786
    b: 71.25898884963482
    c: 86.72387554036268
  e84c5d142d453541653352a25097fab745d5e21c25ddad04bb78be6ea8f5c4d3:
    family: pert
    a: 34.760906222681264
    b: 43.45113277835158
    c: 90.32072674400352
  dcbbdae5fa2310d0c06973814c41900b4789ecba016f1f7d0337567c76fc4fcc:
    family: pert
    a: 40.62460457950697
    b: 50.78075572438371
    c: 117.52906505753516
  e575d098984c5d71972b936fb794238df1d88cb6013e49fd2f222e89a1f0f8b8:
    family: pert
    a: 54.093329519644705
    b: 67.61666189955588
    c: 83.80453168716477
  b98282953e51a9573f571d1d115951701108904b53aa1ddf84bd5cbdc0a734d0:
    family: pert
    a: 32.69174699958457
    b: 40.86468374948071
    c: 78.5175309564487
  2a382fc1f887212a4a585a1da3a0889f9cc6660405b91d90154678a20250b158:
    family: pert
    a: 37.57127560477937
    b: 46.96409450597422
    c: 63.290599028184744
  95016bb29c9806691916c85ad1c0ddc83d0039d72b71b12f45b1a49187fe6364:
    family: pert
    a: 33.81370136705984
    b: 42.267126708824804
    c: 75.93476379604958
  648ed9e72cf949b6dbfb0f3957809a97b3a6869915c1944a752c7545ceef728b:
    family: pert
    a: 45.578333176961166
    b: 56.97291647120146
    c: 133.347410546727
  4f9368cdb00439d77d9f520536f9c9528d73abebeed444a15d09ac58f6d0cd72:
    family: pert
    a: 23.466184568980115
    b: 33.523120812828736
    c: 60.02373798738542
  c2663a8d0814a05824791c4fef2343c7f02ffae9fd2725315a52e70021cc8789:
    family: pert
    a: 28.016704805032944
    b: 40.02386400718992
    c: 62.29085586856719
  6059353d2bfe39cdd147e68f105a205ac63341a445245be0e1c72f297a44d8e1:
    family: pert
    a: 21.728139390371112
    b: 27.16017423796389
    c: 34.955642319733386
  fa6b8267f8990b475897cedc3e7366ba89c9666f9f1936d3e320d6ea30f8f4ac:
    family: pert
    a: 28.08363518807168
    b: 40.1194788401024
    c: 102.1284443906432
  b1b5e161a37b70854197660dfc23a4051e9b6f79ef1b443dedaba752fa7c7cd6:
    family: pert
    a: 20.91842866146839
    b: 29.883469516383418
    c: 119.22200666923457
  e00a323fc016a3d420adcf42629be1fccec33487276e3164ad9fcbd6a9fe26e8:
    family: pert
    a: 31.13494216210931
    b: 44.478488803013306
    c: 76.55454481304497
  af56c07894e112a6ea7dff3352b23078eb7b6aec2e083baf0e759a16311d9ab4:
    family: pert
    a: 12.332820876753287
    b: 20.55470146125548
    c: 62.17918077531197
  38933b11716d6151f616a9dd4a7ad7b87a06dd1393fe6eec6cbb6f0c874b774b:
    family: pert
    a: 14.198845730147177
    b: 23.66474288357863
    c: 106.9158310907573
  3229961f8edfef24a05e85a9e0943fb9a27af26718c4511e23a3a4671fd5f2dc:
    family: pert
    a: 11.263128004078801
    b: 18.771880006798003
    c: 103.94100454633266
  92023b587231e80fbb7bfab617334e25de68a5fb511407d26ed29517af4ad9a3:
    family: pert
    a: 23.421142185244797
    b: 39.035236975408
    c: 71.00893184828115
  97cd0c6816b2bad4cda30f636e81b4236db065b30c7ddfac9d98baf1fa18df80:
    family: pert
    a: 22.277641534117077
    b: 37.1294025568618
    c: 105.61830098519039
  6c29583483ae97419c29bb477ddfd1b7abc7dec5846dd173f7728b3d38c20980:
    family: pert
    a: 12.578072657372916
    b: 20.96345442895486
    c: 69.37680090226482
  e6803a7f71ca8aed356df262979d3e7e6ad7edcddfaecacbb3ec8477aef29ec3:
    family: pert
    a: 12.56616884430734
    b: 20.943614740512235
    c: 83.70733928189087
  078c3bead97f9128407e3af3df25a603bf1349bacb7c3908e232f50f1c4e617e:
    family: pert
    a: 18.829807218708257
    b: 31.38301203118043
    c: 99.50100199553636
  2be6ca09bd2a57858785f83fb4274e42c53bff0464336f7e66ced2bdcf102577:
    family: pert
    a: 8.448389498282127
    b: 14.080649163803546
    c: 87.23972859258359
  b4945ddf3393cecfd058a341b7323a9b6fa991e7fb7d4a085b72e053231d022c:
    family: pert
    a: 16.163997743986346
    b: 26.939996239977244
    c: 104.53455145967548
  6546dd2a19792e7a8d93e569c8dac9fdf1296b54c9d544be999795487b47be31:
    family: pert
    a: 26.58443276253491
    b: 37.97776108933559
    c: 66.4685208236693
  14b2d9cf51841b004f617665bd25b77dfe75b4c89bc3ef9fd195921f59af322a:
    family: pert
    a: 23.689775836285392
    b: 33.842536908979135
    c: 61.0862983046785
  fb27862ae1383b8f1695f4acc833b8dbd13c6e2209c76981ad61e27a58472a83:
    family: pert
    a: 31.27149992403163
    b: 44.67357132004519
    c: 86.16070541192484
  4c74d68fa3200c7fa19ef1f7e39c285a12beb4fb492ce453c19241b1e3e4007f:
    family: pert
    a: 28.765463391121813
    b: 41.09351913017402
    c: 82.5502169995352
  2b4e8ad7421eebf1acd1070081f3412829d1e3407fa53f338d28759eab4b087d:
    family: pert
    a: 29.329962833766455
    b: 41.89994690538065
    c: 90.33818899651045
  f67b96b416681f2403276aeade91e4c3db04e02feff76e37aa1eb3ee106c4175:
    family: pert
    a: 86.68796493046864
    b: 108.3599561630858
    c: 179.57955670623164
  11115e498ce92a7a2c505e7885986cce34e2d07a47fabeb9ce4c7158919dcb93:
    family: pert
    a: 51.11699201110377
    b: 63.896240013879705
    c: 94.44149704982017
  01f17cd3e9ca055332daafe77192b83c70ec96746a7e91095730ee42f99d753e:
    family: pert
    a: 19.74731638022436
    b: 28.210451971749087
    c: 68.04909625537361
  c2c32e99881b77c5ea7ecc77b5b968a1103f904ce0c104e1323d87e575df987b:
    family: pert
    a: 17.01844853057997
    b: 24.312069329399957
    c: 42.193433867043225
  63cf0f65f850525c47dbcfca5af916fdca04f0906e089deed0067274c046decf:
    family: pert
    a: 17.831128817550116
    b: 25.473041167928738
    c: 55.2113187818633
  ee754c57149f2d11008a648ce9389f8642d451bee2079a6331a40aef563d2255:
    family: pert
    a: 15.855440499760144
    b: 22.650629285371636
    c: 63.158840218596914
  da52dc6053d68443a1e76e346e2b3ca7385dde23f8848fc1147ad125adc0cbb4:
    family: pert
    a: 26.792344392490534
    b: 38.27477770355791
    c: 77.91228620820534
  79446fe7e0199a969eec28d886affcea75964664afbc39e725eada99c85b9e78:
    family: pert
    a: 20.549221755350835
    b: 29.356031079072626
    c: 94.34166947552659
  8765cd502fa06af8549e4ab7924bf76687d6e9f444c87cf5f6711c029eea8e6c:
    family: pert
    a: 18.10636976003952
    b: 25.866242514342172
    c: 58.95616115655656
  494b805cd9b858d7de78a1ef8f9e3820f8985a04eb30c8538f8342f07fa9a2bf:
    family: pert
    a: 19.1959108325283
    b: 27.422729760754713
    c: 82.83004213184229
  b1ae9ee66fa33d72ab27b5dc433d0b6cdccc177dc74e0acef0e31b5d3920e989:
    family: pert
    a: 21.75183794566369
    b: 31.074054208090992
    c: 63.133734741661364
  70c1e8e50349437e1373f6bd4b413095869c62c38e9cbc22da7a136a7e2f7c29:
    family: pert
    a: 16.174425704231975
    b: 20.21803213028997
    c: 33.508376987509074
  70325813ed941cb91881d3531515dd1cb5bcb1ee9774254bc038b8a0a441a72c:
    family: pert
    a: 25.50171840997617
    b: 31.87714801247021
    c: 43.08829048295122
  13848a08c254217dc009467c7040a4f35e6e7ead2ccf4c3eaabcfc8a051c5199:
    family: pert
    a: 24.714688837350717
    b: 30.893361046688394
    c: 47.964558689126314
  0d08b27ea46eae37021fc2a274813359bda61bc60c36218e10b52b7f30ac7957:
    family: pert
    a: 24.92943340677664
    b: 31.161791758470798
    c: 46.37313871947044
  d3b5fb6b882bae69aa9c6dd396da70aab7e70ef00616c90e66914266a8c0aba7:
    family: pert
    a: 20.522973429703804
    b: 25.653716787129753
    c: 38.495336866805395
  22a0ff7ec88dbff0a9b104f8cfe22344cb3b299cc052b2346b022ecb48dc9a6d:
    family: pert
    a: 23.556347387638663
    b: 29.445434234548326
    c: 38.065197642953024
  e3c4a0b9d6bc8b75ea319d87bf303a97cb84654dda2a2aa7381d5b33a47e2ae8:
    family: pert
    a: 13.701729827112983
    b: 17.127162283891227
    c: 35.308082278829175
  9787f6186ad10f681e0c1dd345c5f9d23231478fd61ac6ef3034e3fadd4c9b4d:
    family: pert
    a: 26.4093301004539
    b: 33.011662625567375
    c: 45.947088914197046
  741e278c85d083e64be12bf36de12d235d80b83b7792d4bbc2ca39a1eecfe736:
    family: pert
    a: 13.91776930413027
    b: 17.397211630162836
    c: 38.75357303548358
  763b469dd42c7831f9b60249f0040311d0c0f940dbd1872601a32ca533914c43:
    family: pert
    a: 17.725611635738954
    b: 22.15701454467369
    c: 36.38370888103228
  69a43559f15a041376292d4d56e45fd875b0180fd79bf74bfcd13b99f3a1caa3:
    family: pert
    a: 16.545534028476926
    b: 20.681917535596156
    c: 34.122475724698006
  e0b4034a22e7adf54695708ddb673e0ad85c7e2e4bfe73ce054488dbe78b78a9:
    family: pert
    a: 12.623921294085118
    b: 15.779901617606397
    c: 26.39186591843879
  4d0adf0ec0c73e65624a2a89a7471efa80fb677576742ffad80028fb89d3daa0:
    family: pert
    a: 6.0892922975286625
    b: 7.611615371910828
    c: 13.554832600692523
  0c46537a9348d1567116b184235cea1eaffcd3199b24de6b37524bb276f17020:
    family: pert
    a: 25.978988367291556
    b: 32.473735459114444
    c: 162.3686772955722
  9ba2e0c8f6d05a38df0562d3a6d9b63d43995236fc56dd5eda003619830c1fcd:
    family: pert
    a: 27.103070369275443
    b: 33.8788379615943
    c: 169.3941898079715
  5715443121c994e1865919bb960b78d7b91ac4cdfea6296ee949816cde69d4d5:
    family: pert
    a: 26.61316623429592
    b: 33.2664577928699
    c: 166.33228896434952
  0a5d7de210f4792b4feb256116df3d8eb07d87cef657209eb5c5eae340727f50:
    family: pert
    a: 28.35074730382905
    b: 35.43843412978631
    c: 177.19217064893155
  0e35ccfd7d0f905125661e924b74e5c712ecec798093d56c1e8a7fd1d1ccf501:
    family: pert
    a: 30.32358150869414
    b: 37.90447688586767
    c: 189.52238442933836
  bc26c64780d5ceee9088451e226913a93fd1f8282c5a1ba25c6ae5a26606d009:
    family: pert
    a: 26.15784114031758
    b: 32.69730142539697
    c: 163.48650712698486
  eecfb7decbb28c2fc41d3ecab3cb35e84e04d687e280928fc355b67ceabc6ee0:
    family: pert
    a: 28.807477639891886
    b: 36.00934704986486
    c: 180.04673524932429
  a8dd5261b45bf667328a356969fe4d06aa64b408762d9105496953ea1422253a:
    family: pert
    a: 12.820185989247097
    b: 16.02523248655887
    c: 27.60980395700101
  4d3a6738ac5f0bda27157ffed37900afc7ae80917577be67495cf168d8d5091a:
    family: pert
    a: 14.210986329459699
    b: 17.763732911824622
    c: 28.270612269764293
  e12f83fb0604198ce6367060b0f586689828693a2c7aa29053e2dc02df8b5104:
    family: pert
    a: 13.347715042975125
    b: 16.684643803718906
    c: 31.75820408510869
  c986bd268c9372d4310917b6a3799b31eac5ba8fdfd0b39cc949862753433f26:
    family: pert
    a: 2.852838233834005
    b: 3.566047792292506
    c: 6.825169996441938
  5faf560b9ac87f6548bf235ca0b8afbbdf5a229a102855e70c561d5c8b1ae10e:
    family: pert
    a: 27.58624723930935
    b: 39.40892462758479
    c: 197.04462313792394
  2916cabb960e053ce6ca1a84eb54156f89b48bd0cd3d42b1f91250c97157036e:
    family: pert
    a: 28.63578754725431
    b: 40.90826792464902
    c: 204.54133962324508
  70d0eda2ea09f477cb03bfed3e22864db73b77c0445f697951b6ad172857d0a6:
    family: pert
    a: 26.475095842403395
    b: 37.82156548914771
    c: 189.10782744573854
  9636be815bc884514b5f0e7d3cd5616cfd52325f8ada3bccd3b11edd8ebebf3f:
    family: pert
    a: 5.148850171284864
    b: 8.58141695214144
    c: 44.854925874965545
  10ea70a153a375fb5e1593e0add2a41fbc4519664837201c4378650988994bc6:
    family: pert
    a: 6.5374150708278576
    b: 10.895691784713096
    c: 31.460672185683336
  f6c6d4e8dac85d5ef8fbc0917985d749e21ce280909ac857f64f6e7c3c6686a2:
    family: pert
    a: 10.846613516722524
    b: 18.07768919453754
    c: 35.9672734240483
  2dc140b0837f4e71ee542502cadfb2a347a3705ce7ab96883a65d92d414805d3:
    family: pert
    a: 7.030583316619013
    b: 11.717638861031688
    c: 49.94143257341133
  19672bd00c2fcd61096b6d48bdfa735d2bae66a48d54690ddd608e58572e8cf0:
    family: pert
    a: 8.034169857174286
    b: 13.390283095290478
    c: 37.29775475201685
  70c0a6a8252006d193f3011bb2a094555d8b2d67e2fcabc2b68530bed3e06dd7:
    family: pert
    a: 9.8557947522873
    b: 16.4263245871455
    c: 45.59250304463375
  bd18182cf3d92640486aa5a0958eb34d8b95d9fb36351e4584dc8a5409417229:
    family: pert
    a: 11.58229659163199
    b: 19.303827652719985
    c: 65.9481986938394
  7bd6dd67cf46015372955d085dfcd04f204ddee7f49558d8a0a1568f0dad47c5:
    family: pert
    a: 9.459201941478995
    b: 15.765336569131659
    c: 48.699999926302524
  64dfc09af01081931135c65775f9796c59eede7ac70288b9ddddf763e4143bf9:
    family: pert
    a: 7.16951004083312
    b: 11.949183401388533
    c: 70.27439597865975
  309e4d61bf08457dbde8a45918a0d6fbd31236e7f56738780555be8dfd3b8453:
    family: pert
    a: 8.79665079791177
    b: 14.661084663186285
    c: 34.82541030308675
  e9b5000ea552ab8c80fc24cf96e6184224ea2249b3622ffede43702ba8863f65:
    family: pert
    a: 6.640209304064434
    b: 11.067015506774057
    c: 37.0180758748841
  f4c34149b0ce5e37fc2e0416957cf393f75122acf1493943b7b855c5dae038c8:
    family: pert
    a: 7.538568998171172
    b: 12.56428166361862
    c: 45.98310370802314
  7fc5b2b11fc04cc092936475d320d8dcec638f5263b9b317546c5c67785dd8d6:
    family: pert
    a: 10.471495864715365
    b: 17.452493107858942
    c: 56.657524318068624
  3f73f18008f33028b67669337039a65412e7bb7a0e77041c33c997e455690f72:
    family: pert
    a: 8.339111025749343
    b: 13.898518376248907
    c: 37.63918597055091
  ec06704a37fb2d603ad841ca22814c5bcd71d27c1e902c007a154954e0f9fb4e:
    family: pert
    a: 5.911311529496115
    b: 9.852185882493526
    c: 67.68923883665383
  c3d8d14e7c0c3c6bca30936e9f678b3e160490a12f53a856dc7d1228aa8d944c:
    family: pert
    a: 2.2906644612487224
    b: 3.2723778017838896
    c: 10.348757757395
  8bca3bce577dcfdc039ab2bff16c13e53e4c34eca492aa16ba4a808092b341e1:
    family: pert
    a: 3.317284603179615
    b: 4.738978004542307
    c: 14.245443014131018
  a922ab813f1b3c1ea9ef3c5ebcb94a05f44601e65d94d12256d082cf462f854b:
    family: pert
    a: 3.83929596244065
    b: 5.484708517772358
    c: 7.91540316529347
  27bae9d7539a541ed2956eddb0cb3a62136122dde16fb4437b0312e9cfbf4423:
    family: pert
    a: 5.494043047231084
    b: 7.848632924615836
    c: 15.819731912601348
  ae2830ebb499fb2816bd360b44fdf497088b7ce4a01525669af152a875cd14d2:
    family: pert
    a: 2.8486343675244257
    b: 4.069477667892037
    c: 10.292596541109763
  f012ae5bd3dafc6fd8652f6cb7d0c58219f0a83d2ba1034527f58fb283ef72e2:
    family: pert
    a: 4.740471690159922
    b: 6.772102414514175
    c: 12.54690134871436
  5cc31f38cbe5591361be25d94000115a2240a89aa2fbfcfc93ed1588554c52f4:
    family: pert
    a: 2.6516330406859776
    b: 3.7880472009799684
    c: 6.7671067933585585
  eb2ba59f9e9f74960236696611faaf0edd4390ac32a9d62fb69e54ff2d082b9b:
    family: pert
    a: 18.978964160383978
    b: 23.723705200479973
    c: 39.20415520876093
  cb299b8cbd010752d2154a09a121373d32494737daebeb68e59b9cc37ee457e9:
    family: pert
    a: 19.442946725780956
    b: 24.303683407226192
    c: 35.199404250496556
  8108718cfe61e9ee0b9e0a0a99b2e0fb8c24d2e203ee4ab7378a5529b7283b06:
    family: pert
    a: 16.793562086351105
    b: 20.99195260793888
    c: 30.298307937081397
  7889d65bcd0ebda3aaf7f81f65e6e23b97b4ce5aa7065d63879703dbb4d6ba2d:
    family: pert
    a: 13.363649237967905
    b: 16.704561547459882
    c: 27.133769435700103
  fabcc7f597e09e599f8661db159b44b2bdae4c6fb14b7f09e854a0c2ca10a8b5:
    family: pert
    a: 18.23137156702276
    b: 22.789214458778446
    c: 36.933565175833394
  117734d08d6600d7167a0c1d11280d4d1e7ef10c6d2d089c389e05275e097cc8:
    family: pert
    a: 15.113049578438392
    b: 18.89131197304799
    c: 31.52338819716444
  087084346972a5a3b4a7a797cb3280b7a9a02aa744ca5c0821fe0147c1912709:
    family: pert
    a: 15.07177912173086
    b: 18.839723902163573
    c: 40.237359390667685
  1fa9830f27f93484ca8c14032d2eeffe2cd0dae069ab853d84bbe4ec7758fccd:
    family: pert
    a: 25.29534575320972
    b: 31.61918219151215
    c: 44.17988052373394
  022fe421fbc8b6723f4215b67cadd613e28b1ca71def4eab5f63c94e2d077983:
    family: pert
    a: 21.71910343399468
    b: 27.148879292493348
    c: 34.71153811305069
  3c27afb8146c267d9df2689c9beb68585a457d51a12280686ba046ecb05dc7f1:
    family: pert
    a: 14.061520334787112
    b: 17.576900418483888
    c: 31.8688838950497
  7bc0a7e82b1c40f5e55cd2774a858e564266b60500a12036b63ad077ec0555ca:
    family: pert
    a: 15.664853457934441
    b: 19.58106682241805
    c: 29.53768122892022
  5d3764130c59a92462654e0d03e8d848a51344e1a4f95a0d5a0f667c6b968e87:
    family: pert
    a: 22.492861333415828
    b: 28.116076666769782
    c: 36.69236913337615
  5d89213dda79ab2f4b3f5192fe4f6bf45925742eb1b01c70e8732baef34a9639:
    family: pert
    a: 18.788659722395995
    b: 31.314432870659992
    c: 148.69839207217314
  b5ec4b6d2c4ea3d2eea48401d28b03025ef5e205b07204a5fcee039b5e393e75:
    family: pert
    a: 27.226992724045406
    b: 45.37832120674234
    c: 185.5547497815139
  afa3784131100badd6cb0dfbe6aaf9646cc6c619c091d65c218d1c68e6d5b2e4:
    family: pert
    a: 11.291173356637747
    b: 18.818622261062913
    c: 95.57154069979212
  17b8c2febb1646523ef7c4b5d76ad0a38eae2a68ae07fcccd927ae256be302f0:
    family: pert
    a: 19.85152939136653
    b: 33.085882318944215
    c: 123.80377636038209
  2c22acf17d289e00791dc774cf6973de42df4b84a98cb4ebab669766fa9ada56:
    family: pert
    a: 21.896393144100607
    b: 36.493988573501014
    c: 155.03037521018777
  d4dd8768fa188e40921c4c4c2d9038ead87a44f07b2077a03bc1323431a50e68:
    family: pert
    a: 23.316933927422223
    b: 38.861556545703706
    c: 131.7369586244212
  5243267f2e48d8fe4504301634d09213c7af550bb3931025a84b8126adf88292:
    family: pert
    a: 16.1566639095487
    b: 26.92777318258117
    c: 72.15521243169809
  b4ed6883f41668501f21974dba6e5bc4699b3f72f4c6525b8c3af407282aed6c:
    family: pert
    a: 24.91011709750741
    b: 31.137646371884262
    c: 43.575115042327624
  1e336c68fea2fa731f68113bf1760a5dbe8dae1569e02c610dddc721304cdd6d:
    family: pert
    a: 20.203366644243175
    b: 25.254208305303965
    c: 36.31168137531338
  0cd923317d115a551da37d7a099110824e5095020211b850f8bbd37d729dc31a:
    family: pert
    a: 22.500782534510567
    b: 28.125978168138207
    c: 36.548911635814
  3688f6661980136f9dbbf80e697cd80d673a46a014f8e9daf84a39a16c0de3c1:
    family: pert
    a: 30.457539290162114
    b: 38.07192411270264
    c: 59.30894970425874
  e26c99fcd26acb4185ba5aaa4d22e7cdab1bcc8721b0945402034ffbaac51102:
    family: pert
    a: 25.399503009771365
    b: 31.749378762214203
    c: 57.16539512943898
  44bb311f6802e6f662920eb2885df9c9ef729ce686e51d4f79964db4b6e086a4:
    family: pert
    a: 24.65207534193425
    b: 30.815094177417812
    c: 57.0895642398634
  c3295e8e8e38c70de59325c2dfdd49c585564157101840f30ff0111f7010e700:
    family: pert
    a: 28.24380217954377
    b: 40.348288827919674
    c: 80.46001787722206
  b0689ac8aaccad799fd03e810e90acc7c814b9ab30bf97dedf493882d491d7e3:
    family: pert
    a: 46.09432548887098
    b: 57.61790686108872
    c: 100.79646945739748
  c4848fc9b87882f06616c46a68a7e67b0b374b5acfc0af1c69ce532d06bb167b:
    family: pert
    a: 90.4190252017792
    b: 113.023781502224
    c: 177.64557770864218
  af8bb69366382d60c3f9c9c324c0bef7f84c596ea8b258d94010e3fc61ba9fc8:
    family: pert
    a: 40.824926489250494
    b: 51.031158111563116
    c: 101.07609010363312
  91910cfdfa358aa1c42762980e4b72403250317e6623d62ebfc55ca44d7e5f82:
    family: pert
    a: 68.445726281675
    b: 85.55715785209374
    c: 193.8277124864035
  39a36961f8f1dd11075bd393be8b1bd09bbd33c5eb62d0eba8d85c6fb0994b9a:
    family: pert
    a: 28.95782937096682
    b: 48.26304895161137
    c: 241.31524475805685
  747a9bf18f656cd99526331adac01a13f19991cc9a9663cceabcb34647d61ee9:
    family: pert
    a: 30.038515794642592
    b: 50.06419299107099
    c: 250.32096495535495
  90fe4030f170af7625e4617263b93c675df54eea5abc590781201b9e0a7e6d7c:
    family: pert
    a: 20.96642557010752
    b: 34.94404261684587
    c: 228.66560885373613
  5ed94d004456925c697f43eeee46123872beb08c33382dcfd72b4eba2807ca06:
    family: pert
    a: 18.069622962668387
    b: 22.58702870333548
    c: 39.433286065863776
  60bee884ea8c9f6f7d2438d14043593f3afe71711b6f91e91c7ee015553ae570:
    family: pert
    a: 18.266559342818482
    b: 22.833199178523103
    c: 34.35349439748873
  2aea6a0411e3baa8be7ad5d0672a980b817f430c86ea8355d996818b6b49c9e7:
    family: pert
    a: 22.60014379679412
    b: 28.25017974599265
    c: 41.33595979390682
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
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 0c7807f43f76f289706d33c63247548cf268864b2424f0a206efcbcea9c8b7ad
  - id: 2
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 107dc244259c12187a2049a77fde19bd17b4b3abd08495591295fd5e50482774
  - id: 3
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 7c7f917ccc335e7fbf224bbff4dd594c4e45d8ac801fcc54139b75b400118612
- id: task_3
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: f2cfad035feacff26f898bbab13e387dc33ec6bf17f0c1faaa65605f55a9813f
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: 14def0320452519e9cdd9d83b5c923614bf2c4c7829c418bb60a8d59e4a7750c
  - id: 3
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: aaf5c1a82645e72590723c82356e58043440857dbf4dbb1c6d12413df41deeae
  - id: 4
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 8f5c11c131aa1d3949715cbb79e5f2bfdbe2ec9be51ea03ebe3ed65182a2752c
  - id: 5
    dedication:
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 325df1a73b40a85f47cac1bad0d6c87d042baeeb6951a1c28104fcc49a839d82
  - id: 6
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 94daf6b6c6e16203902a29da4aad6d1697de7f84fc47b8657b20a51669414ff2
- id: task_4
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
    distribution_hash: 2b78b822920c05931adf06d5e0db470bd4dd5fdf1a322b343c4b9e8e4560a61f
  - id: 2
    dedication:
      worker_3: 1.0
    distribution_hash: 0ccfcdb27472177f49681cbe7cebe605c6823e9679364d7dff15f6e0bf34318f
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: b1bcec6c8182db866957e8eb6ce6c8f89bee83709acd48fec67048dbc280a81a
- id: task_5
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: f7e17863a30da52af6b6c065736b462043e33714e70a45351434441fe501bd52
  - id: 2
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: ac27c356e5f80ceedc54d2bac88b2477aaff6500fd35db7fba7a076bb6d95c05
  - id: 3
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: e1e97286acf8a6c105791bfa4154ced0df50ff1de2637d458d6fa8142a7e8555
  - id: 4
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 368aeee0c29b6d8ba9dc09325895e85daf4a012e934dfb74c9cca831546a4979
  - id: 5
    dedication:
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 3bdb7febf5bd9b6917645c1049edce2d622ff69cba37a2d372bd8e37c2f1aec1
  - id: 6
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 136ea18bbd385de8407700bcc35a5a313c1c9af1d2a25589cc9ea42f88a0fc4a
- id: task_6
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_3: 0.75
      worker_4: 0.75
    distribution_hash: eb45ff28f0cea3900e3adb1a197a089c1b071b61f8d9582bf50a08b589eca762
  - id: 2
    dedication:
      worker_2: 0.5
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: b55b8f0212599056f353c63af6146c0bcd4760233b72c66de79ca4e5fbf96238
  - id: 3
    dedication:
      worker_2: 1.0
      worker_3: 0.5
      worker_4: 0.75
    distribution_hash: de902cc5da857a8bd7dbb183484b187eacbfc4225fc840d7fb52be020d6ab3d8
  - id: 4
    dedication:
      worker_4: 0.5
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: a8dd8eeab7ebc6248458d0bd712e0aff4a127c133bc37f344e5c80ea6152494e
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: 48037b19ec14ebc90613d3ab6762674ca1657495336172d13f2d2245bdda0786
  - id: 6
    dedication:
      worker_4: 1.0
      worker_3: 0.5
      worker_1: 0.75
    distribution_hash: 9f64a501f2cb94faf509e99a143bf0acc412749dbb023a90d649e96df2269bcc
  - id: 7
    dedication:
      worker_4: 0.5
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 3b69b3a3e651d9e5154db4ac064a00049f3fb7426c8a120560e252e845ed1824
  - id: 8
    dedication:
      worker_4: 0.75
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: a09097f085e02347034f7fc5e1573f0bab942d7434c6041a09eb5c76dafcd5b5
  - id: 9
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 0b0031e11174a52b975a7bf17cf4608a8dfa2ad67ff144a4270b60f26b3bb0c5
  - id: 10
    dedication:
      worker_2: 0.5
      worker_1: 1.0
      worker_3: 0.75
    distribution_hash: 013b10a3af2b913ec3c216ba78520a29cd8bb3d2dd884ff960b3ccbb8e4208c0
  - id: 11
    dedication:
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 1a3d997f1a8761b6edc553fe92538038893e8e593f766e737cea0b08b4ae1bcb
  - id: 12
    dedication:
      worker_2: 0.75
      worker_1: 0.75
      worker_3: 0.75
    distribution_hash: 43ef11672830344074075ab61c9aa92a316b2d1cdbbeac181443c1e7db1e9f9a
- id: task_7
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 0.75
    distribution_hash: 876b40fe944f92562b2df0a9f8f46d8f357ef22804f6d2dbbd6b26126967710a
  - id: 2
    dedication:
      worker_2: 1.0
      worker_3: 0.5
      worker_1: 1.0
    distribution_hash: c0c987b05234642c232b56e99b8a9f84b905cabb5dc3ce662fff9c39d7dc3a15
  - id: 3
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: c2f217e65f78890e90554357763ecc1dcc3a30d8cae964aa06015830b0ecdde9
  - id: 4
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: 90b962792c70b69c9d54f342ae2b79ae8078f572d848090ea97d1b3ce4128459
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_1: 0.75
    distribution_hash: 964ea48e1243568feee4065b9c63e9d27a3f145a08bdb80ea9e23c47195795ae
  - id: 6
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: e84c5d142d453541653352a25097fab745d5e21c25ddad04bb78be6ea8f5c4d3
  - id: 7
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 0.5
    distribution_hash: dcbbdae5fa2310d0c06973814c41900b4789ecba016f1f7d0337567c76fc4fcc
  - id: 8
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: e575d098984c5d71972b936fb794238df1d88cb6013e49fd2f222e89a1f0f8b8
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: b98282953e51a9573f571d1d115951701108904b53aa1ddf84bd5cbdc0a734d0
  - id: 10
    dedication:
      worker_2: 0.75
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 2a382fc1f887212a4a585a1da3a0889f9cc6660405b91d90154678a20250b158
  - id: 11
    dedication:
      worker_2: 0.75
      worker_4: 0.75
      worker_3: 1.0
    distribution_hash: 95016bb29c9806691916c85ad1c0ddc83d0039d72b71b12f45b1a49187fe6364
  - id: 12
    dedication:
      worker_2: 0.5
      worker_4: 0.5
      worker_3: 0.75
    distribution_hash: 648ed9e72cf949b6dbfb0f3957809a97b3a6869915c1944a752c7545ceef728b
- id: task_8
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
      worker_4: 1.0
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 4f9368cdb00439d77d9f520536f9c9528d73abebeed444a15d09ac58f6d0cd72
  - id: 2
    dedication:
      worker_3: 0.75
      worker_4: 0.5
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: c2663a8d0814a05824791c4fef2343c7f02ffae9fd2725315a52e70021cc8789
- id: task_9
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 6059353d2bfe39cdd147e68f105a205ac63341a445245be0e1c72f297a44d8e1
- id: task_10
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_4: 1.0
    distribution_hash: fa6b8267f8990b475897cedc3e7366ba89c9666f9f1936d3e320d6ea30f8f4ac
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: b1b5e161a37b70854197660dfc23a4051e9b6f79ef1b443dedaba752fa7c7cd6
  - id: 3
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: e00a323fc016a3d420adcf42629be1fccec33487276e3164ad9fcbd6a9fe26e8
- id: task_11
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_4: 1.0
    distribution_hash: af56c07894e112a6ea7dff3352b23078eb7b6aec2e083baf0e759a16311d9ab4
  - id: 2
    dedication:
      worker_2: 0.5
      worker_3: 0.75
      worker_4: 1.0
    distribution_hash: 38933b11716d6151f616a9dd4a7ad7b87a06dd1393fe6eec6cbb6f0c874b774b
  - id: 3
    dedication:
      worker_3: 1.0
      worker_2: 0.75
      worker_1: 1.0
    distribution_hash: 3229961f8edfef24a05e85a9e0943fb9a27af26718c4511e23a3a4671fd5f2dc
  - id: 4
    dedication:
      worker_3: 0.75
      worker_2: 0.5
      worker_1: 0.75
    distribution_hash: 92023b587231e80fbb7bfab617334e25de68a5fb511407d26ed29517af4ad9a3
  - id: 5
    dedication:
      worker_3: 0.5
      worker_2: 0.75
      worker_1: 0.5
    distribution_hash: 97cd0c6816b2bad4cda30f636e81b4236db065b30c7ddfac9d98baf1fa18df80
  - id: 6
    dedication:
      worker_4: 0.75
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 6c29583483ae97419c29bb477ddfd1b7abc7dec5846dd173f7728b3d38c20980
  - id: 7
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_3: 0.5
    distribution_hash: e6803a7f71ca8aed356df262979d3e7e6ad7edcddfaecacbb3ec8477aef29ec3
  - id: 8
    dedication:
      worker_1: 1.0
      worker_4: 0.5
      worker_2: 0.5
    distribution_hash: 078c3bead97f9128407e3af3df25a603bf1349bacb7c3908e232f50f1c4e617e
  - id: 9
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 2be6ca09bd2a57858785f83fb4274e42c53bff0464336f7e66ced2bdcf102577
  - id: 10
    dedication:
      worker_1: 1.0
      worker_4: 0.75
      worker_2: 0.5
    distribution_hash: b4945ddf3393cecfd058a341b7323a9b6fa991e7fb7d4a085b72e053231d022c
- id: task_12
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: 6546dd2a19792e7a8d93e569c8dac9fdf1296b54c9d544be999795487b47be31
  - id: 2
    dedication:
      worker_4: 1.0
      worker_1: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 14b2d9cf51841b004f617665bd25b77dfe75b4c89bc3ef9fd195921f59af322a
  - id: 3
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
    distribution_hash: fb27862ae1383b8f1695f4acc833b8dbd13c6e2209c76981ad61e27a58472a83
  - id: 4
    dedication:
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 4c74d68fa3200c7fa19ef1f7e39c285a12beb4fb492ce453c19241b1e3e4007f
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: 2b4e8ad7421eebf1acd1070081f3412829d1e3407fa53f338d28759eab4b087d
- id: task_13
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: f67b96b416681f2403276aeade91e4c3db04e02feff76e37aa1eb3ee106c4175
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 11115e498ce92a7a2c505e7885986cce34e2d07a47fabeb9ce4c7158919dcb93
- id: task_14
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.5
      worker_4: 1.0
    distribution_hash: 01f17cd3e9ca055332daafe77192b83c70ec96746a7e91095730ee42f99d753e
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
    distribution_hash: c2c32e99881b77c5ea7ecc77b5b968a1103f904ce0c104e1323d87e575df987b
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 0.75
    distribution_hash: 63cf0f65f850525c47dbcfca5af916fdca04f0906e089deed0067274c046decf
  - id: 4
    dedication:
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: ee754c57149f2d11008a648ce9389f8642d451bee2079a6331a40aef563d2255
  - id: 5
    dedication:
      worker_1: 1.0
      worker_2: 0.5
    distribution_hash: da52dc6053d68443a1e76e346e2b3ca7385dde23f8848fc1147ad125adc0cbb4
  - id: 6
    dedication:
      worker_1: 1.0
      worker_2: 0.75
    distribution_hash: 79446fe7e0199a969eec28d886affcea75964664afbc39e725eada99c85b9e78
  - id: 7
    dedication:
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 8765cd502fa06af8549e4ab7924bf76687d6e9f444c87cf5f6711c029eea8e6c
  - id: 8
    dedication:
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: 494b805cd9b858d7de78a1ef8f9e3820f8985a04eb30c8538f8342f07fa9a2bf
  - id: 9
    dedication:
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: b1ae9ee66fa33d72ab27b5dc433d0b6cdccc177dc74e0acef0e31b5d3920e989
- id: task_15
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 0.75
    distribution_hash: 70c1e8e50349437e1373f6bd4b413095869c62c38e9cbc22da7a136a7e2f7c29
  - id: 2
    dedication:
      worker_1: 1.0
      worker_3: 0.5
      worker_4: 0.75
    distribution_hash: 70325813ed941cb91881d3531515dd1cb5bcb1ee9774254bc038b8a0a441a72c
  - id: 3
    dedication:
      worker_1: 0.5
      worker_3: 0.75
      worker_4: 0.75
    distribution_hash: 13848a08c254217dc009467c7040a4f35e6e7ead2ccf4c3eaabcfc8a051c5199
  - id: 4
    dedication:
      worker_4: 0.5
      worker_1: 0.75
      worker_2: 1.0
    distribution_hash: 0d08b27ea46eae37021fc2a274813359bda61bc60c36218e10b52b7f30ac7957
  - id: 5
    dedication:
      worker_4: 0.5
      worker_1: 1.0
      worker_2: 1.0
    distribution_hash: d3b5fb6b882bae69aa9c6dd396da70aab7e70ef00616c90e66914266a8c0aba7
  - id: 6
    dedication:
      worker_4: 0.75
      worker_1: 0.75
      worker_2: 0.75
    distribution_hash: 22a0ff7ec88dbff0a9b104f8cfe22344cb3b299cc052b2346b022ecb48dc9a6d
  - id: 7
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: e3c4a0b9d6bc8b75ea319d87bf303a97cb84654dda2a2aa7381d5b33a47e2ae8
  - id: 8
    dedication:
      worker_1: 0.5
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 9787f6186ad10f681e0c1dd345c5f9d23231478fd61ac6ef3034e3fadd4c9b4d
  - id: 9
    dedication:
      worker_4: 1.0
      worker_3: 0.5
      worker_2: 0.75
    distribution_hash: 741e278c85d083e64be12bf36de12d235d80b83b7792d4bbc2ca39a1eecfe736
  - id: 10
    dedication:
      worker_4: 0.75
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: 763b469dd42c7831f9b60249f0040311d0c0f940dbd1872601a32ca533914c43
  - id: 11
    dedication:
      worker_4: 1.0
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: 69a43559f15a041376292d4d56e45fd875b0180fd79bf74bfcd13b99f3a1caa3
- id: task_16
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.25
    distribution_hash: e0b4034a22e7adf54695708ddb673e0ad85c7e2e4bfe73ce054488dbe78b78a9
  - id: 2
    dedication:
      worker_3: 0.5
    distribution_hash: 4d0adf0ec0c73e65624a2a89a7471efa80fb677576742ffad80028fb89d3daa0
- id: task_17
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: 0c46537a9348d1567116b184235cea1eaffcd3199b24de6b37524bb276f17020
  - id: 2
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
      worker_5: 0.5
    distribution_hash: 9ba2e0c8f6d05a38df0562d3a6d9b63d43995236fc56dd5eda003619830c1fcd
  - id: 3
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_4: 1.0
      worker_5: 0.5
    distribution_hash: 5715443121c994e1865919bb960b78d7b91ac4cdfea6296ee949816cde69d4d5
  - id: 4
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
      worker_5: 0.5
    distribution_hash: 0a5d7de210f4792b4feb256116df3d8eb07d87cef657209eb5c5eae340727f50
  - id: 5
    dedication:
      worker_4: 1.0
      worker_3: 1.0
      worker_2: 1.0
      worker_5: 0.25
    distribution_hash: 0e35ccfd7d0f905125661e924b74e5c712ecec798093d56c1e8a7fd1d1ccf501
  - id: 6
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
      worker_5: 0.5
    distribution_hash: bc26c64780d5ceee9088451e226913a93fd1f8282c5a1ba25c6ae5a26606d009
  - id: 7
    dedication:
      worker_2: 1.0
      worker_3: 1.0
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: eecfb7decbb28c2fc41d3ecab3cb35e84e04d687e280928fc355b67ceabc6ee0
- id: task_18
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 0.75
      worker_4: 1.0
    distribution_hash: a8dd5261b45bf667328a356969fe4d06aa64b408762d9105496953ea1422253a
  - id: 2
    dedication:
      worker_3: 1.0
      worker_2: 1.0
      worker_1: 0.5
      worker_4: 0.75
    distribution_hash: 4d3a6738ac5f0bda27157ffed37900afc7ae80917577be67495cf168d8d5091a
  - id: 3
    dedication:
      worker_3: 0.75
      worker_2: 1.0
      worker_1: 1.0
      worker_4: 0.75
    distribution_hash: e12f83fb0604198ce6367060b0f586689828693a2c7aa29053e2dc02df8b5104
- id: task_19
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 1.0
      worker_2: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: c986bd268c9372d4310917b6a3799b31eac5ba8fdfd0b39cc949862753433f26
- id: task_20
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_2: 1.0
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: 5faf560b9ac87f6548bf235ca0b8afbbdf5a229a102855e70c561d5c8b1ae10e
  - id: 2
    dedication:
      worker_4: 0.75
      worker_3: 0.5
      worker_2: 0.75
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: 2916cabb960e053ce6ca1a84eb54156f89b48bd0cd3d42b1f91250c97157036e
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_2: 0.5
      worker_1: 0.5
      worker_5: 0.5
    distribution_hash: 70d0eda2ea09f477cb03bfed3e22864db73b77c0445f697951b6ad172857d0a6
- id: task_21
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 1.0
    distribution_hash: 9636be815bc884514b5f0e7d3cd5616cfd52325f8ada3bccd3b11edd8ebebf3f
  - id: 2
    dedication:
      worker_4: 0.75
      worker_2: 1.0
    distribution_hash: 10ea70a153a375fb5e1593e0add2a41fbc4519664837201c4378650988994bc6
  - id: 3
    dedication:
      worker_1: 0.5
      worker_4: 1.0
    distribution_hash: f6c6d4e8dac85d5ef8fbc0917985d749e21ce280909ac857f64f6e7c3c6686a2
  - id: 4
    dedication:
      worker_1: 1.0
      worker_4: 0.75
    distribution_hash: 2dc140b0837f4e71ee542502cadfb2a347a3705ce7ab96883a65d92d414805d3
  - id: 5
    dedication:
      worker_3: 0.75
      worker_4: 0.75
    distribution_hash: 19672bd00c2fcd61096b6d48bdfa735d2bae66a48d54690ddd608e58572e8cf0
  - id: 6
    dedication:
      worker_3: 0.5
      worker_4: 0.75
    distribution_hash: 70c0a6a8252006d193f3011bb2a094555d8b2d67e2fcabc2b68530bed3e06dd7
  - id: 7
    dedication:
      worker_3: 0.75
      worker_1: 0.5
    distribution_hash: bd18182cf3d92640486aa5a0958eb34d8b95d9fb36351e4584dc8a5409417229
  - id: 8
    dedication:
      worker_3: 1.0
      worker_1: 0.5
    distribution_hash: 7bd6dd67cf46015372955d085dfcd04f204ddee7f49558d8a0a1568f0dad47c5
  - id: 9
    dedication:
      worker_3: 0.75
      worker_1: 1.0
    distribution_hash: 64dfc09af01081931135c65775f9796c59eede7ac70288b9ddddf763e4143bf9
  - id: 10
    dedication:
      worker_3: 1.0
      worker_2: 0.5
    distribution_hash: 309e4d61bf08457dbde8a45918a0d6fbd31236e7f56738780555be8dfd3b8453
  - id: 11
    dedication:
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: e9b5000ea552ab8c80fc24cf96e6184224ea2249b3622ffede43702ba8863f65
  - id: 12
    dedication:
      worker_3: 0.5
      worker_2: 1.0
    distribution_hash: f4c34149b0ce5e37fc2e0416957cf393f75122acf1493943b7b855c5dae038c8
  - id: 13
    dedication:
      worker_2: 0.5
      worker_1: 1.0
    distribution_hash: 7fc5b2b11fc04cc092936475d320d8dcec638f5263b9b317546c5c67785dd8d6
  - id: 14
    dedication:
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: 3f73f18008f33028b67669337039a65412e7bb7a0e77041c33c997e455690f72
  - id: 15
    dedication:
      worker_2: 1.0
      worker_1: 0.75
    distribution_hash: ec06704a37fb2d603ad841ca22814c5bcd71d27c1e902c007a154954e0f9fb4e
- id: task_22
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
    distribution_hash: c3d8d14e7c0c3c6bca30936e9f678b3e160490a12f53a856dc7d1228aa8d944c
  - id: 2
    dedication:
      worker_4: 0.75
    distribution_hash: 8bca3bce577dcfdc039ab2bff16c13e53e4c34eca492aa16ba4a808092b341e1
  - id: 3
    dedication:
      worker_2: 1.0
    distribution_hash: a922ab813f1b3c1ea9ef3c5ebcb94a05f44601e65d94d12256d082cf462f854b
  - id: 4
    dedication:
      worker_2: 0.5
    distribution_hash: 27bae9d7539a541ed2956eddb0cb3a62136122dde16fb4437b0312e9cfbf4423
  - id: 5
    dedication:
      worker_3: 0.75
    distribution_hash: ae2830ebb499fb2816bd360b44fdf497088b7ce4a01525669af152a875cd14d2
  - id: 6
    dedication:
      worker_3: 0.5
    distribution_hash: f012ae5bd3dafc6fd8652f6cb7d0c58219f0a83d2ba1034527f58fb283ef72e2
  - id: 7
    dedication:
      worker_3: 1.0
    distribution_hash: 5cc31f38cbe5591361be25d94000115a2240a89aa2fbfcfc93ed1588554c52f4
- id: task_23
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.75
      worker_4: 1.0
      worker_1: 0.5
    distribution_hash: eb2ba59f9e9f74960236696611faaf0edd4390ac32a9d62fb69e54ff2d082b9b
  - id: 2
    dedication:
      worker_3: 1.0
      worker_4: 0.5
      worker_1: 1.0
    distribution_hash: cb299b8cbd010752d2154a09a121373d32494737daebeb68e59b9cc37ee457e9
  - id: 3
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 8108718cfe61e9ee0b9e0a0a99b2e0fb8c24d2e203ee4ab7378a5529b7283b06
  - id: 4
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 7889d65bcd0ebda3aaf7f81f65e6e23b97b4ce5aa7065d63879703dbb4d6ba2d
  - id: 5
    dedication:
      worker_4: 0.75
      worker_2: 0.5
      worker_3: 0.75
    distribution_hash: fabcc7f597e09e599f8661db159b44b2bdae4c6fb14b7f09e854a0c2ca10a8b5
  - id: 6
    dedication:
      worker_4: 0.75
      worker_2: 0.75
      worker_3: 0.75
    distribution_hash: 117734d08d6600d7167a0c1d11280d4d1e7ef10c6d2d089c389e05275e097cc8
  - id: 7
    dedication:
      worker_1: 1.0
      worker_3: 0.5
      worker_2: 0.75
    distribution_hash: 087084346972a5a3b4a7a797cb3280b7a9a02aa744ca5c0821fe0147c1912709
  - id: 8
    dedication:
      worker_1: 0.75
      worker_3: 0.5
      worker_2: 0.75
    distribution_hash: 1fa9830f27f93484ca8c14032d2eeffe2cd0dae069ab853d84bbe4ec7758fccd
  - id: 9
    dedication:
      worker_1: 1.0
      worker_3: 1.0
      worker_2: 0.75
    distribution_hash: 022fe421fbc8b6723f4215b67cadd613e28b1ca71def4eab5f63c94e2d077983
  - id: 10
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 3c27afb8146c267d9df2689c9beb68585a457d51a12280686ba046ecb05dc7f1
  - id: 11
    dedication:
      worker_2: 1.0
      worker_4: 1.0
      worker_1: 1.0
    distribution_hash: 7bc0a7e82b1c40f5e55cd2774a858e564266b60500a12036b63ad077ec0555ca
  - id: 12
    dedication:
      worker_2: 0.5
      worker_4: 1.0
      worker_1: 0.75
    distribution_hash: 5d3764130c59a92462654e0d03e8d848a51344e1a4f95a0d5a0f667c6b968e87
- id: task_24
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_1: 0.75
      worker_4: 0.5
    distribution_hash: 5d89213dda79ab2f4b3f5192fe4f6bf45925742eb1b01c70e8732baef34a9639
  - id: 2
    dedication:
      worker_1: 0.5
      worker_4: 0.5
    distribution_hash: b5ec4b6d2c4ea3d2eea48401d28b03025ef5e205b07204a5fcee039b5e393e75
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: afa3784131100badd6cb0dfbe6aaf9646cc6c619c091d65c218d1c68e6d5b2e4
  - id: 4
    dedication:
      worker_4: 0.75
      worker_3: 0.5
    distribution_hash: 17b8c2febb1646523ef7c4b5d76ad0a38eae2a68ae07fcccd927ae256be302f0
  - id: 5
    dedication:
      worker_4: 0.5
      worker_3: 0.5
    distribution_hash: 2c22acf17d289e00791dc774cf6973de42df4b84a98cb4ebab669766fa9ada56
  - id: 6
    dedication:
      worker_1: 0.75
      worker_3: 0.5
    distribution_hash: d4dd8768fa188e40921c4c4c2d9038ead87a44f07b2077a03bc1323431a50e68
  - id: 7
    dedication:
      worker_1: 1.0
      worker_3: 1.0
    distribution_hash: 5243267f2e48d8fe4504301634d09213c7af550bb3931025a84b8126adf88292
- id: task_25
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_1: 0.75
      worker_4: 0.75
      worker_3: 0.75
    distribution_hash: b4ed6883f41668501f21974dba6e5bc4699b3f72f4c6525b8c3af407282aed6c
  - id: 2
    dedication:
      worker_2: 0.75
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 1e336c68fea2fa731f68113bf1760a5dbe8dae1569e02c610dddc721304cdd6d
  - id: 3
    dedication:
      worker_2: 0.5
      worker_1: 1.0
      worker_4: 1.0
      worker_3: 1.0
    distribution_hash: 0cd923317d115a551da37d7a099110824e5095020211b850f8bbd37d729dc31a
- id: task_26
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_2: 1.0
    distribution_hash: 3688f6661980136f9dbbf80e697cd80d673a46a014f8e9daf84a39a16c0de3c1
  - id: 2
    dedication:
      worker_4: 0.75
      worker_3: 1.0
      worker_2: 1.0
    distribution_hash: e26c99fcd26acb4185ba5aaa4d22e7cdab1bcc8721b0945402034ffbaac51102
  - id: 3
    dedication:
      worker_4: 1.0
      worker_3: 0.75
      worker_2: 0.75
    distribution_hash: 44bb311f6802e6f662920eb2885df9c9ef729ce686e51d4f79964db4b6e086a4
- id: task_27
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 1.0
      worker_4: 1.0
      worker_2: 1.0
      worker_1: 1.0
    distribution_hash: c3295e8e8e38c70de59325c2dfdd49c585564157101840f30ff0111f7010e700
- id: task_28
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: b0689ac8aaccad799fd03e810e90acc7c814b9ab30bf97dedf493882d491d7e3
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: c4848fc9b87882f06616c46a68a7e67b0b374b5acfc0af1c69ce532d06bb167b
- id: task_29
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_3: 0.5
    distribution_hash: af8bb69366382d60c3f9c9c324c0bef7f84c596ea8b258d94010e3fc61ba9fc8
  - id: 2
    dedication:
      worker_3: 0.25
    distribution_hash: 91910cfdfa358aa1c42762980e4b72403250317e6623d62ebfc55ca44d7e5f82
- id: task_30
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_2: 0.75
      worker_4: 0.5
      worker_3: 0.75
      worker_1: 1.0
      worker_5: 0.25
    distribution_hash: 39a36961f8f1dd11075bd393be8b1bd09bbd33c5eb62d0eba8d85c6fb0994b9a
  - id: 2
    dedication:
      worker_2: 0.75
      worker_4: 0.75
      worker_3: 1.0
      worker_1: 0.75
      worker_5: 0.5
    distribution_hash: 747a9bf18f656cd99526331adac01a13f19991cc9a9663cceabcb34647d61ee9
  - id: 3
    dedication:
      worker_2: 1.0
      worker_4: 0.75
      worker_3: 1.0
      worker_1: 0.75
      worker_5: 0.5
    distribution_hash: 90fe4030f170af7625e4617263b93c675df54eea5abc590781201b9e0a7e6d7c
- id: task_31
  milestone: false
  modes:
  - id: 1
    dedication:
      worker_4: 1.0
      worker_2: 0.5
      worker_3: 1.0
    distribution_hash: 5ed94d004456925c697f43eeee46123872beb08c33382dcfd72b4eba2807ca06
  - id: 2
    dedication:
      worker_4: 1.0
      worker_2: 1.0
      worker_3: 1.0
    distribution_hash: 60bee884ea8c9f6f7d2438d14043593f3afe71711b6f91e91c7ee015553ae570
  - id: 3
    dedication:
      worker_4: 0.5
      worker_2: 1.0
      worker_3: 0.75
    distribution_hash: 2aea6a0411e3baa8be7ad5d0672a980b817f430c86ea8355d996818b6b49c9e7
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
  - task_15
- - task_2
  - task_16
- - task_2
  - task_18
- - task_3
  - task_17
- - task_4
  - task_5
- - task_5
  - task_12
- - task_7
  - task_16
- - task_8
  - task_15
- - task_9
  - task_14
- - task_10
  - task_13
- - task_4
  - task_26
- - task_25
  - task_14
- - task_9
  - task_15
- - task_26
  - task_13
- - task_6
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
  delta: 850
validation:
  project_key: 7b65c329aad775d830711d1997023d00cde5bb58e77939875a50915ebac49d34
  is_correct: true
  is_trivial: false
  classification: unclassified
  errors: []
  reasons:
  - 'Shortest critical path: 101 days; worst-case serial bound: 1922 days'
  - Neither deadline bounds nor structural checks decide triviality
  structural_flags: []
  validation_version: 6
```
